import tkinter as tk
from tkinter import messagebox, simpledialog
import functions
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MoneyTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Money Tracker")
        self.root.geometry("500x600")
        
        # Load data from JSON file
        data = functions.load_data()
        self.money = data["money"]
        self.spent = data["spent"]
        
        # Title
        title = tk.Label(root, text="Money Tracker", font=("Arial", 24, "bold"))
        title.pack(pady=10)
        
        # Money display
        self.money_label = tk.Label(root, text=f"Current Money: ${self.money}", font=("Arial", 14))
        self.money_label.pack(pady=10)
        
        # Buttons frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=20, padx=10, fill=tk.BOTH, expand=True)
        
        # Button configurations
        buttons = [
            ("Add Entry", self.add_entry),
            ("View Total", self.view_total),
            ("View Chart", self.view_chart),
            ("View All", self.view_all),
            ("Category Total", self.category_total),
            ("Highest Spending", self.highest_spent),
            ("Highest Income", self.highest_income),
            ("Average Spending", self.average_spending),
            ("Category Average", self.category_average),
            ("Delete Entry", self.delete_entry_gui),
            ("Set Money", self.set_money_gui),
            ("Clear All", self.clear_all),
            ("Exit", self.exit_app),
        ]
        
        # Create buttons
        for text, command in buttons:
            btn = tk.Button(button_frame, text=text, command=command, font=("Arial", 11), 
                           width=20, pady=10)
            btn.pack(pady=5)
    
    def update_money_display(self):
        self.money_label.config(text=f"Current Money: ${self.money}")

    def _modal_single_input(self, title, prompt):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.transient(self.root)
        win.grab_set()

        tk.Label(win, text=prompt).pack(padx=10, pady=8)
        entry = tk.Entry(win)
        entry.pack(padx=10, pady=6)

        result = {"value": None}

        def on_ok():
            result["value"] = entry.get()
            win.destroy()

        def on_cancel():
            win.destroy()

        btn_frame = tk.Frame(win)
        btn_frame.pack(pady=8)
        tk.Button(btn_frame, text="OK", width=10, command=on_ok).pack(side=tk.LEFT, padx=6)
        tk.Button(btn_frame, text="Cancel", width=10, command=on_cancel).pack(side=tk.LEFT, padx=6)

        entry.focus_set()
        self.root.wait_window(win)
        return result["value"]

    def _modal_add_entry(self):
        win = tk.Toplevel(self.root)
        win.title("Add Entry")
        win.transient(self.root)
        win.grab_set()

        tk.Label(win, text="Type:").grid(row=0, column=0, sticky="w", padx=10, pady=6)
        entry_type_var = tk.StringVar(value="spending")
        tk.Radiobutton(win, text="Spending", variable=entry_type_var, value="spending").grid(row=0, column=1, sticky="w")
        tk.Radiobutton(win, text="Income", variable=entry_type_var, value="income").grid(row=0, column=2, sticky="w")

        tk.Label(win, text="Amount:").grid(row=1, column=0, sticky="w", padx=10, pady=6)
        amount_entry = tk.Entry(win)
        amount_entry.grid(row=1, column=1, columnspan=2, sticky="we", padx=10)

        tk.Label(win, text="Category:").grid(row=2, column=0, sticky="w", padx=10, pady=6)
        category_entry = tk.Entry(win)
        category_entry.grid(row=2, column=1, columnspan=2, sticky="we", padx=10)

        tk.Label(win, text="Description:").grid(row=3, column=0, sticky="w", padx=10, pady=6)
        desc_entry = tk.Entry(win)
        desc_entry.grid(row=3, column=1, columnspan=2, sticky="we", padx=10)

        result = {"value": None}

        def on_ok():
            try:
                amt = int(amount_entry.get())
            except Exception:
                messagebox.showerror("Error", "Please enter a valid integer amount.")
                return
            result["value"] = {
                "type": entry_type_var.get(),
                "amount": amt,
                "category": category_entry.get(),
                "text": desc_entry.get()
            }
            win.destroy()

        def on_cancel():
            win.destroy()

        btn_frame = tk.Frame(win)
        btn_frame.grid(row=4, column=0, columnspan=3, pady=10)
        tk.Button(btn_frame, text="OK", width=10, command=on_ok).pack(side=tk.LEFT, padx=6)
        tk.Button(btn_frame, text="Cancel", width=10, command=on_cancel).pack(side=tk.LEFT, padx=6)

        amount_entry.focus_set()
        self.root.wait_window(win)
        return result["value"]
    
    def add_entry(self):
        data = self._modal_add_entry()
        if not data:
            return
        self.spent.append(data)
        if data["type"] == "spending":
            self.money -= data["amount"]
        else:
            self.money += data["amount"]
        functions.save_data(self.money, self.spent)
        self.update_money_display()
        messagebox.showinfo("Success", f"Entry added: {data.get('text')}")
    
    def view_total(self):
        money_spent = 0
        money_earned = 0
        
        for entry in self.spent:
            if entry["type"] == "spending":
                money_spent += entry["amount"]
            elif entry["type"] == "income":
                money_earned += entry["amount"]
        
        message = f"You have earned: ${money_earned}\nYou have spent: ${money_spent}\nYou have left: ${self.money}"
        messagebox.showinfo("Total Money", message)
    
    def view_chart(self):
        money_spent = 0
        money_earned = 0
        
        for entry in self.spent:
            if entry["type"] == "spending":
                money_spent += entry["amount"]
            elif entry["type"] == "income":
                money_earned += entry["amount"]
        
        # Create a new window for the chart
        chart_window = tk.Toplevel(self.root)
        chart_window.title("Income vs Spending Chart")
        chart_window.geometry("600x400")
        
        # Create figure
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))
        
        # Bar chart
        categories = ['Income', 'Spending']
        amounts = [money_earned, money_spent]
        colors = ['green', 'red']
        ax1.bar(categories, amounts, color=colors)
        ax1.set_ylabel('Amount ($)')
        ax1.set_title('Income vs Spending')
        ax1.set_ylim(0, max(money_earned, money_spent) * 1.2 if max(money_earned, money_spent) > 0 else 100)
        
        # Add value labels on bars
        for i, (cat, amt) in enumerate(zip(categories, amounts)):
            ax1.text(i, amt, f'${amt}', ha='center', va='bottom', fontweight='bold')
        
        # Pie chart
        if money_earned > 0 or money_spent > 0:
            sizes = [money_earned, money_spent]
            labels = [f'Income\n${money_earned}', f'Spending\n${money_spent}']
            ax2.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
            ax2.set_title('Distribution')
        else:
            ax2.text(0.5, 0.5, 'No data available', ha='center', va='center', transform=ax2.transAxes)
            ax2.set_title('Distribution')
        
        # Embed chart in tkinter
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def view_all(self):
        report = functions.view_all_entries(self.spent)
        win = tk.Toplevel(self.root)
        win.title("All Entries")
        win.geometry("600x400")

        txt_frame = tk.Frame(win)
        txt_frame.pack(fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(txt_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        text_widget = tk.Text(txt_frame, wrap=tk.NONE, yscrollcommand=scrollbar.set)
        text_widget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=text_widget.yview)

        text_widget.insert("1.0", report)
        text_widget.config(state=tk.DISABLED)
    
    def category_total(self):
        category = self._modal_single_input("Category", "For which category are you looking?")
        if category is None:
            return
        
        cat_money = 0
        entries_list = []
        
        for entry in self.spent:
            if category == entry["category"]:
                cat_money += entry["amount"]
                entries_list.append(str(entry))
        
        message = "\n".join(entries_list) + f"\n\nTotal: ${cat_money}"
        messagebox.showinfo(f"Category: {category}", message)
    
    def highest_spent(self):
        spending_entries = [entry for entry in self.spent if entry.get("type") == "spending"]
        
        if not spending_entries:
            messagebox.showinfo("Highest Spending", "No spending entries available.")
            return
        
        highest_entry = max(spending_entries, key=lambda x: x["amount"])
        messagebox.showinfo("Highest Spending", str(highest_entry))
    
    def highest_income(self):
        income_entries = [entry for entry in self.spent if entry.get("type") == "income"]
        
        if not income_entries:
            messagebox.showinfo("Highest Income", "No income entries available.")
            return
        
        highest_entry = max(income_entries, key=lambda x: x["amount"])
        messagebox.showinfo("Highest Income", str(highest_entry))
    
    def average_spending(self):
        if not self.spent:
            messagebox.showinfo("Average", "No entries available.")
            return
        
        total = sum(entry["amount"] for entry in self.spent)
        average = total / len(self.spent)
        messagebox.showinfo("Average Spending", f"Your average spending is: ${average:.2f}")
    
    def category_average(self):
        category = self._modal_single_input("Category", "For which category are you looking?")
        if category is None:
            return
        
        cat_entries = [entry for entry in self.spent if entry["category"] == category]
        
        if not cat_entries:
            messagebox.showinfo("Category Average", f"No entries found for category '{category}'")
            return
        
        total = sum(entry["amount"] for entry in cat_entries)
        average = total / len(cat_entries)
        messagebox.showinfo("Category Average", f"The average spending in category '{category}' is: ${average:.2f}")
    
    def delete_entry_gui(self):
        if not self.spent:
            messagebox.showinfo("Delete Entry", "No entries to delete.")
            return
        
        entries_display = "\n".join([f"{i}: {entry}" for i, entry in enumerate(self.spent)])
        messagebox.showinfo("Current Entries", entries_display)
        
        index_str = self._modal_single_input("Delete Entry", "Enter the index of the entry you want to delete:")
        if index_str is None:
            return
        try:
            index = int(index_str)
            if 0 <= index < len(self.spent):
                deleted_entry = self.spent.pop(index)
                self.money += deleted_entry["amount"]
                functions.save_data(self.money, self.spent)
                self.update_money_display()
                messagebox.showinfo("Success", f"Deleted entry: {deleted_entry}")
            else:
                messagebox.showerror("Error", "Invalid index.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
    
    def set_money_gui(self):
        amount_str = self._modal_single_input("Set Money", "Set your total money amount:")
        if amount_str is None:
            return
        try:
            self.money = int(amount_str)
            functions.save_data(self.money, self.spent)
            self.update_money_display()
            messagebox.showinfo("Success", f"Money set to ${self.money}")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")
    
    def clear_all(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all entries and reset money to $1000?"):
            self.spent.clear()
            self.money = 1000
            functions.save_data(self.money, self.spent)
            self.update_money_display()
            messagebox.showinfo("Success", "All entries cleared and money reset to $1000")
    
    def exit_app(self):
        if messagebox.askyesno("Exit", "Do you want to exit?"):
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MoneyTrackerApp(root)
    root.mainloop()
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

import tkinter as tk
from tkinter import messagebox, simpledialog
from src import functions
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class MoneyTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Money Tracker")
        self.root.geometry("800x700")
        self.root.configure(bg="#f0f0f0")
        
        # Load data from JSON file
        data = functions.load_data()
        self.money = data["money"]
        self.spent = data["spent"]
        
        # === HEADER ===
        header_frame = tk.Frame(root, bg="#2c3e50", height=100)
        header_frame.pack(fill=tk.X, padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        title = tk.Label(header_frame, text="💰 Money Tracker", font=("Arial", 28, "bold"), 
                        bg="#2c3e50", fg="white")
        title.pack(pady=10)
        
        # Money display - prominent card style
        money_frame = tk.Frame(header_frame, bg="#27ae60", relief=tk.RAISED, bd=2)
        money_frame.pack(pady=8, padx=20, fill=tk.X)
        
        self.money_label = tk.Label(money_frame, text=f"${self.money}", font=("Arial", 36, "bold"),
                                   bg="#27ae60", fg="white")
        self.money_label.pack(side=tk.LEFT, padx=20, pady=10)
        
        money_text = tk.Label(money_frame, text="Current Balance", font=("Arial", 12),
                            bg="#27ae60", fg="white")
        money_text.pack(side=tk.LEFT, padx=0, pady=10)
        
        # === MAIN CONTENT ===
        main_frame = tk.Frame(root, bg="#f0f0f0")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        # === SECTION 1: ADD & QUICK VIEW ===
        section1_title = tk.Label(main_frame, text="Quick Actions", font=("Arial", 12, "bold"),
                                 bg="#f0f0f0", fg="#2c3e50")
        section1_title.grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 8))
        
        quick_buttons = [
            ("➕ Add Entry", self.add_entry, "#3498db"),
            ("📊 View Total", self.view_total, "#3498db"),
            ("📈 Chart", self.view_chart, "#3498db"),
        ]
        
        for i, (text, command, color) in enumerate(quick_buttons):
            btn = self._create_button(main_frame, text, command, color, width=20)
            btn.grid(row=1, column=i, padx=5, pady=5)
        
        # === SECTION 2: ANALYTICS ===
        section2_title = tk.Label(main_frame, text="Analytics", font=("Arial", 12, "bold"),
                                 bg="#f0f0f0", fg="#2c3e50")
        section2_title.grid(row=2, column=0, columnspan=3, sticky="w", pady=(15, 8))
        
        analytics_buttons = [
            ("⏱️ Timeline", self.view_money_timeline, "#9b59b6"),
            ("📋 View All", self.view_all, "#9b59b6"),
            ("🏷️ Category Total", self.category_total, "#9b59b6"),
        ]
        
        for i, (text, command, color) in enumerate(analytics_buttons):
            btn = self._create_button(main_frame, text, command, color, width=20)
            btn.grid(row=3, column=i, padx=5, pady=5)
        
        # === SECTION 3: STATISTICS ===
        section3_title = tk.Label(main_frame, text="Statistics", font=("Arial", 12, "bold"),
                                 bg="#f0f0f0", fg="#2c3e50")
        section3_title.grid(row=4, column=0, columnspan=3, sticky="w", pady=(15, 8))
        
        stats_buttons = [
            ("💸 Highest Spend", self.highest_spent, "#e74c3c"),
            ("💰 Highest Income", self.highest_income, "#e74c3c"),
            ("📐 Avg Spending", self.average_spending, "#e74c3c"),
        ]
        
        for i, (text, command, color) in enumerate(stats_buttons):
            btn = self._create_button(main_frame, text, command, color, width=20)
            btn.grid(row=5, column=i, padx=5, pady=5)
        
        # === SECTION 4: SETTINGS ===
        section4_title = tk.Label(main_frame, text="Settings & Management", font=("Arial", 12, "bold"),
                                 bg="#f0f0f0", fg="#2c3e50")
        section4_title.grid(row=6, column=0, columnspan=3, sticky="w", pady=(15, 8))
        
        settings_buttons = [
            ("📊 Category Avg", self.category_average, "#16a085"),
            ("🗑️ Delete Entry", self.delete_entry_gui, "#c0392b"),
            ("💵 Set Balance", self.set_money_gui, "#16a085"),
        ]
        
        for i, (text, command, color) in enumerate(settings_buttons):
            btn = self._create_button(main_frame, text, command, color, width=20)
            btn.grid(row=7, column=i, padx=5, pady=5)
        
        # === SECTION 5: DANGER ZONE ===
        danger_frame = tk.Frame(main_frame, bg="#f0f0f0")
        danger_frame.grid(row=8, column=0, columnspan=3, sticky="ew", pady=(15, 0))
        
        clear_btn = self._create_button(danger_frame, "⚠️ Clear All Data", self.clear_all, "#e67e22", width=35)
        clear_btn.pack(side=tk.LEFT, padx=5, pady=5)
        
        exit_btn = self._create_button(danger_frame, "❌ Exit", self.exit_app, "#c0392b", width=35)
        exit_btn.pack(side=tk.LEFT, padx=5, pady=5)
    
    def _create_button(self, parent, text, command, color, width=20):
        """Create a styled button with consistent appearance"""
        btn = tk.Button(parent, text=text, command=command, 
                       font=("Arial", 10, "bold"), width=width, pady=12,
                       bg=color, fg="white", relief=tk.RAISED, bd=1,
                       cursor="hand2", activebackground=self._lighten_color(color),
                       activeforeground="white")
        return btn
    
    def _lighten_color(self, color_hex):
        """Lighten a hex color by a percentage"""
        color_map = {
            "#3498db": "#5dade2",
            "#9b59b6": "#af7ac5",
            "#e74c3c": "#ec7063",
            "#16a085": "#48c9b0",
            "#c0392b": "#e74c3c",
            "#e67e22": "#f39c12",
        }
        return color_map.get(color_hex, color_hex)
    
    def update_money_display(self):
        self.money_label.config(text=f"${self.money}")

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
        totals = functions.get_totals(self.spent, self.money)
        message = f"You have earned: ${totals['earned']}\nYou have spent: ${totals['spent']}\nYou have left: ${totals['balance']}"
        messagebox.showinfo("Total Money", message)
    
    def view_chart(self):
        chart_data = functions.get_chart_data(self.spent)
        money_earned = chart_data["earned"]
        money_spent = chart_data["spent"]
        
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

    def view_money_timeline(self):
        """Display money balance over time as a line graph."""
        if not self.spent:
            messagebox.showinfo("Money Over Time", "No entries to display.")
            return
        
        # Calculate starting money by working backwards from current money
        net_change = 0
        for entry in self.spent:
            if entry["type"] == "spending":
                net_change -= entry["amount"]
            else:  # income
                net_change += entry["amount"]
        
        starting_money = self.money - net_change
        timeline = functions.get_timeline_data(self.spent, starting_money)
        
        # Create a new window for the chart
        chart_window = tk.Toplevel(self.root)
        chart_window.title("Money Over Time")
        chart_window.geometry("800x500")
        
        # Create figure and plot
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Extract values and labels
        money_amounts = [item[0] for item in timeline]
        x_values = list(range(len(money_amounts)))
        
        # Plot line graph
        ax.plot(x_values, money_amounts, marker='o', linestyle='-', linewidth=2, 
                markersize=6, color='blue', label='Money Balance')
        
        ax.set_xlabel('Entry Number', fontsize=12)
        ax.set_ylabel('Money Amount ($)', fontsize=12)
        ax.set_title('Money Balance Over Time', fontsize=14, fontweight='bold')
        ax.grid(True, alpha=0.3)
        ax.legend()
        
        # Format y-axis as currency
        ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${x:.0f}'))
        
        # Embed chart in tkinter
        canvas = FigureCanvasTkAgg(fig, master=chart_window)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def view_all(self):
        report = functions.format_all_entries(self.spent)
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
        
        cat_money = functions.calculate_category_total(self.spent, category)
        entries_list = functions.get_entries_by_category(self.spent, category)
        
        if not entries_list:
            messagebox.showinfo(f"Category: {category}", f"No entries found for this category.\n\nTotal: $0")
            return
        
        message = "\n".join(str(entry) for entry in entries_list) + f"\n\nTotal: ${cat_money}"
        messagebox.showinfo(f"Category: {category}", message)
    
    def highest_spent(self):
        highest_entry = functions.get_highest_spending_entry(self.spent)
        
        if not highest_entry:
            messagebox.showinfo("Highest Spending", "No spending entries available.")
            return
        
        messagebox.showinfo("Highest Spending", str(highest_entry))
    
    def highest_income(self):
        highest_entry = functions.get_highest_income_entry(self.spent)
        
        if not highest_entry:
            messagebox.showinfo("Highest Income", "No income entries available.")
            return
        
        messagebox.showinfo("Highest Income", str(highest_entry))
    
    def average_spending(self):
        if not self.spent:
            messagebox.showinfo("Average", "No entries available.")
            return
        
        average = functions.calculate_average_spending(self.spent)
        messagebox.showinfo("Average Spending", f"Your average spending is: ${average:.2f}")
    
    def category_average(self):
        category = self._modal_single_input("Category", "For which category are you looking?")
        if category is None:
            return
        
        cat_entries = functions.get_entries_by_category(self.spent, category)
        
        if not cat_entries:
            messagebox.showinfo("Category Average", f"No entries found for category '{category}'")
            return
        
        average = functions.calculate_category_average(self.spent, category)
        messagebox.showinfo("Category Average", f"The average spending in category '{category}' is: ${average:.2f}")
    
    def delete_entry_gui(self):
        if not self.spent:
            messagebox.showinfo("Delete Entry", "No entries to delete.")
            return
        
        entries_display = functions.format_entries_for_display(self.spent)
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


def run():
    """Entry point for the Money Tracker application."""
    root = tk.Tk()
    app = MoneyTrackerApp(root)
    root.mainloop()


if __name__ == "__main__":
    run()
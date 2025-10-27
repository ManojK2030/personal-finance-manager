from rich.prompt import Prompt
from rich.console import Console
import sqlite3
from datetime import datetime

console = Console()

def add_transaction(user_id, t_type):
    category = Prompt.ask("Category (e.g., Food, Rent, Salary)")
    amount = float(Prompt.ask("Amount"))
    date = Prompt.ask("Date (YYYY-MM-DD)", default=datetime.today().strftime('%Y-%m-%d'))

    with sqlite3.connect("finance.db") as conn:
        c = conn.cursor()
        c.execute("INSERT INTO transactions (user_id, type, category, amount, date) VALUES (?, ?, ?, ?, ?)",
                  (user_id, t_type, category, amount, date))
        conn.commit()
        console.print(f"[green]{t_type.capitalize()} added successfully![/green]")

def delete_transaction(user_id):
    tid = Prompt.ask("Enter transaction ID to delete")
    with sqlite3.connect("finance.db") as conn:
        c = conn.cursor()
        c.execute("DELETE FROM transactions WHERE id = ? AND user_id = ?", (tid, user_id))
        conn.commit()
        console.print("[yellow]Transaction deleted.[/yellow]")

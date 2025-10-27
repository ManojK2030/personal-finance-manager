from rich.prompt import Prompt
from rich.console import Console
import sqlite3

console = Console()

def set_budget(user_id):
    category = Prompt.ask("Category")
    amount = float(Prompt.ask("Monthly Budget Amount"))
    with sqlite3.connect("finance.db") as conn:
        c = conn.cursor()
        c.execute("REPLACE INTO budgets (user_id, category, amount) VALUES (?, ?, ?)",
                  (user_id, category, amount))
        conn.commit()
        console.print("[green]Budget set successfully.[/green]")

def check_budget(user_id):
    with sqlite3.connect("finance.db") as conn:
        c = conn.cursor()
        c.execute("""
        SELECT b.category, b.amount, IFNULL(SUM(t.amount), 0)
        FROM budgets b
        LEFT JOIN transactions t ON b.category = t.category AND t.user_id = b.user_id AND t.type = 'expense'
        AND strftime('%Y-%m', t.date) = strftime('%Y-%m', 'now')
        WHERE b.user_id = ?
        GROUP BY b.category
        """, (user_id,))
        rows = c.fetchall()

    for category, limit, spent in rows:
        if spent > limit:
            console.print(f"[red]Budget exceeded for {category}! Spent ₹{spent:.2f} / ₹{limit:.2f}[/red]")
        else:
            console.print(f"[green]{category}: ₹{spent:.2f} / ₹{limit:.2f}[/green]")

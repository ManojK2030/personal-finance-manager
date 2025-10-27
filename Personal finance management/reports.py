import sqlite3
from rich.console import Console
from rich.table import Table

console = Console()

def generate_report(user_id, period="monthly"):
    query = """
    SELECT type, category, SUM(amount) FROM transactions
    WHERE user_id = ? AND strftime('%Y-%m', date) = strftime('%Y-%m', 'now')
    GROUP BY type, category
    """ if period == "monthly" else """
    SELECT type, category, SUM(amount) FROM transactions
    WHERE user_id = ? AND strftime('%Y', date) = strftime('%Y', 'now')
    GROUP BY type, category
    """

    with sqlite3.connect("finance.db") as conn:
        c = conn.cursor()
        c.execute(query, (user_id,))
        rows = c.fetchall()

    table = Table(title=f"{period.capitalize()} Financial Report")
    table.add_column("Type")
    table.add_column("Category")
    table.add_column("Amount", justify="right")

    total_income = total_expense = 0
    for t_type, category, amount in rows:
        table.add_row(t_type, category, f"{amount:.2f}")
        if t_type == "income":
            total_income += amount
        else:
            total_expense += amount

    console.print(table)
    console.print(f"[bold green]Total Income:[/bold green] ₹{total_income:.2f}")
    console.print(f"[bold red]Total Expenses:[/bold red] ₹{total_expense:.2f}")
    console.print(f"[bold cyan]Savings:[/bold cyan] ₹{total_income - total_expense:.2f}")

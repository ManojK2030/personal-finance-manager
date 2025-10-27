import sqlite3
import bcrypt
from rich.prompt import Prompt
from rich.console import Console

console = Console()

def register_user():
    username = Prompt.ask("Enter a new username")
    password = Prompt.ask("Enter a password", password=True)
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

    with sqlite3.connect("finance.db") as conn:
        c = conn.cursor()
        try:
            c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed))
            conn.commit()
            console.print("[green]Registration successful![/green]")
        except sqlite3.IntegrityError:
            console.print("[red]Username already exists.[/red]")

def login_user():
    username = Prompt.ask("Username")
    password = Prompt.ask("Password", password=True)

    with sqlite3.connect("finance.db") as conn:
        c = conn.cursor()
        c.execute("SELECT id, password FROM users WHERE username = ?", (username,))
        result = c.fetchone()
        if result and bcrypt.checkpw(password.encode(), result[1]):
            console.print(f"[green]Welcome back, {username}![/green]")
            return result[0]
        else:
            console.print("[red]Invalid credentials.[/red]")
            return None

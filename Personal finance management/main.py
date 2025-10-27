from rich.console import Console
from rich.prompt import Prompt
from auth import register_user, login_user
from db import init_db
from finance import add_transaction, delete_transaction
from reports import generate_report
from budget import set_budget, check_budget

console = Console()

def main():
    init_db()
    console.print("[bold cyan]Welcome to Personal Finance Manager[/bold cyan]\n")
    while True:
        console.print("[yellow]Please choose an option:[/yellow]")
        console.print("1. Register")
        console.print("2. Login")
        console.print("3. Exit")

        choice = Prompt.ask("Enter your choice (1/2/3)")
        if choice == "1":
            register_user()
        elif choice == "2":
            user_id = login_user()
            if user_id:
                dashboard(user_id)
        elif choice == "3":
            console.print("[bold red]Goodbye![/bold red]")
            break
        else:
            console.print("[red]Invalid choice. Please enter 1, 2, or 3.[/red]")

def dashboard(user_id):
    while True:
        console.print("\n[bold magenta]Dashboard Options:[/bold magenta]")
        console.print("1. Add Income")
        console.print("2. Add Expense")
        console.print("3. Delete Transaction")
        console.print("4. View Report")
        console.print("5. Set Budget")
        console.print("6. Check Budget")
        console.print("7. Logout")

        action = Prompt.ask("Enter your choice (1-7)")
        if action == "1":
            add_transaction(user_id, "income")
        elif action == "2":
            add_transaction(user_id, "expense")
        elif action == "3":
            delete_transaction(user_id)
        elif action == "4":
            generate_report(user_id)
        elif action == "5":
            set_budget(user_id)
        elif action == "6":
            check_budget(user_id)
        elif action == "7":
            console.print("[bold red]Logging out...[/bold red]")
            break
        else:
            console.print("[red]Invalid option. Please choose between 1 and 7.[/red]")

if __name__ == "__main__":
    main()


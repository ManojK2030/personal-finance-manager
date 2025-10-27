import shutil

def backup():
    shutil.copy("finance.db", "finance_backup.db")

def restore():
    shutil.copy("finance_backup.db", "finance.db")

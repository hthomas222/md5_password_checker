import hashlib
from rich.console import Console
from rich.table import Table
from rich import print
import sys

def pass_checker():
    enter_pass = input("Please enter a plaintext password: ")

    encoded_text = enter_pass.encode('utf-8')
    md5_hash = hashlib.md5(encoded_text).hexdigest()


    with open("test.txt") as file:
        file = file.readlines()
    li = []
    for i in file: 
        i = i.strip()
        if i == md5_hash:
            li.append(md5_hash)
    if li != []:
        print(enter_pass, "was in the top password list under hashes.")
        print("The hash is:", li)
    else: 
        print(enter_pass, "was not in the top password list under hashes.")


def check(test):
    if test == "2":
        return test
    if test == "1":
        sys.exit()
    sel = ["1", "2"]
    while test not in sel:
            console.log("Please enter either 1 or 2")
            test = console.input("[bold red]Select 1 to exit |""[bold green]| Select 2 to continue: ")
    return test


# Main
test = ""
while test != "1":
    print()
    table = Table(title="Password Checker Command")
    table.add_column("NUM", style="green")
    table.add_column("TASK", style="red")
    table.add_column("Description", style="blue")
    table.add_row("1", "pass_checker", "This will take a plaintext password and md5 hash it and check it against the top 100 hashes used.")
    console = Console()
    console.print(table)
    print()
    selection = input("enter a number to execute the command: ")
    if selection == "1":
        pass_checker()
    else:
        console.log("[bold red]Please enter a valid choice!")
    print()
    test = console.input("[bold red]Select 1 to exit |""[bold green]| Select 2 to continue: ")
    if test != "1":
        x = check(test)
        if x == "1":
            sys.exit()

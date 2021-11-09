try:
    import colorama
    from colorama import Fore
except ImportError:
    print("colorama was unable to be imported")
    exit(1)

colorama.init(autoreset=True)

print(Fore.CYAN + "This is some cyan text")
print(Fore.RED + "This is some red text")
print("This is some normal text")
print(Fore.GREEN + "This is some green text")
print(Fore.YELLOW + "This is some yellow text")
import sys
from calcscore import calc_score
from colorama import init, Fore, Style

init()

def on_death(time_started, asteroids_hit):
    score_str, time_str = calc_score(time_started, asteroids_hit)
    print("")
    print(Fore.RED + "=====================================")
    print(Fore.LIGHTRED_EX + "             Game over!             ")
    print(f"{score_str}\n{time_str}")
    print(Fore.RED + "=====================================" + Style.RESET_ALL)
    print("")
    sys.exit(0)

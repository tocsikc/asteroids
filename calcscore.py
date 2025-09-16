import time
from colorama import init, Fore, Style

init()

def calc_score(time_started, asteroids_hit):
    time_end = int(time.time())
    secs_alive = time_end - time_started
    score = secs_alive + asteroids_hit

    score_str, time_str = get_high_score(score, secs_alive)

    return score_str, time_str

def get_high_score(score, secs): # check if a new high score has been set
    with open("data/highscore.txt", "r") as f:
        lines = f.readlines()
        data = lines[1].strip().split("-")

        high_score = int(data[0])
        best_time = int(data[1])

        score_str = Fore.RESET + "Your Score: " + Fore.LIGHTGREEN_EX + f"{score}" + Fore.RESET + " High Score: "+ Fore.YELLOW + f"{high_score}"
        time_str = Fore.RESET + "Time Lived: " + Fore.LIGHTGREEN_EX + f"{format_time(secs)}" + Fore.RESET + " Best Time: "+ Fore.YELLOW + f"{format_time(best_time)}"
        
        if score > high_score: # New high score
            set_high_score(score, best_time)
            score_str = Fore.LIGHTYELLOW_EX + "HIGH SCORE! " + Fore.LIGHTMAGENTA_EX + f"{score}" + Fore.RESET + " (Previous best: " +  f"{high_score})" 
            high_score = score

        if secs > best_time: # New best time
            set_high_score(high_score, secs)
            time_str = Fore.LIGHTYELLOW_EX + f"NEW BEST TIME! " + Fore.LIGHTMAGENTA_EX + f"{format_time(secs)}" + Fore.RESET + " (Previous best: " + f"{format_time(best_time)})" + Style.RESET_ALL

    return score_str, time_str

def set_high_score(score, secs): # write new high score data to file
    with open("data/highscore.txt", "w") as f:
        f.write(f"score-seconds\n{str(score)}-{str(secs)}")

def format_time(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    if seconds < 60:
        return "%ds" % (sec)
    elif seconds < 3600:
        return "%dm, %ds" % (min, sec)
    else:
        return "%dh, %dm, %ds" % (hour, min, sec)

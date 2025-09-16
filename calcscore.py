import pygame
import time

def calc_score(time_started, asteroids_hit):
    time_end = int(time.time())
    secs_alive = time_end - time_started
    time_alive = format_time(secs_alive)
    score = secs_alive + asteroids_hit
    return score, time_alive

def format_time(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    if seconds < 60:
        return "%ds" % (sec)
    elif seconds < 3600:
        return "%dm, %ds" % (min, sec)
    else:
        return "%dh, %dm, %ds" % (hour, min, sec)

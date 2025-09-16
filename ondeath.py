import sys
from calcscore import calc_score

def on_death(time_started, asteroids_hit):
    score, time_alive = calc_score(time_started, asteroids_hit)
    print("Game over!")
    print(f"Score: {score}\nSurvived {time_alive}")
    sys.exit(0)

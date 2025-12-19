# 02_while_loops.py

"""
Demonstrates the use of while loop with a counter
Use case: Countdown timer
"""
import time

countdown = 5
while countdown > 0:
    print("Timer:", countdown)
    time.sleep(1)
    countdown -= 1
print("Timer ended!")

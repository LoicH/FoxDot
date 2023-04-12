"""2023-04-12"""

Clock.sleep_time = 0.0001

Clock.bpm = 138

# Basic drumset
k1 >> play("|x2| ") # Kickdrum 1
h1 >> play(" -  ", amp=1) # Hihat 1
cl >> play("  * ", amp=.7) # Clap 1

# Groove add:
k2 >> play(" v ( [( v)v])", amp=.1) # 2nd kickdrum
h2 >> play("   :", delay=0, amp=.5) # 2nd hi-hat
c2 >> play("  |*2| ", amp=.2, delay=PWhite(-.2,.3)) # 2nd clap


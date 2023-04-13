"""2023-04-13
Late night session
Listen to the recording here: https://soundcloud.com/rokil-1/ambient
"""


Clock.bpm = 90
Scale.default = "minor"

# First the pads
pa >> pads(
    P[4, 4, 2, 0] + (0, 2, 4), dur=4, oct=4, lpf=expvar([200, 1000], 16), tremolo=0
)

# Some wonderful space sounds
sp >> space(P[0, 6, 4, 2], dur=4)

# Then some bass
db >> dbass(
    P[0, 0, 0, 0, 4, 4, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2],
    oct=(4, 5),
    amp=linvar([0.2, 0.6], 16),
)

# A little marimba melody
ma >> marimba(
    P[0, 6, 4, 2].arp([0, 4, 2]),
    dur=PDur(3, 8),
    amp=3,  # To fade out: linvar([3,0],16),
    oct=(5, 6),
    fmod=linvar([-5, 5], 4),
)

# Some keyboard reinforcement:
p2 >> keys(P[4, 4, 2, 0] + (2, 4), dur=4, amp=linvar([2, 0], 16), oct=(5, 6), fmod=2)

# At the end stop the instruments
db.stop()
ma.stop()
pa.stop()

"""2021-06-13
My cover of M.O.O.N. - 'Hydrogen' (Hotline Miami Soundtrack)
Listen my recording here: https://soundcloud.com/rokil-1/oxygen
"""

Clock.bpm = 127
Scale.default = "minor"

# Percus
# var.lpf = expvar([10, 1e4], 32)
lpf = 100
b1 >> dbass(dur=PDur(3, 8), lpf=lpf)
# b2 >> dub(dur=PDur(3,8))
d1 >> play("x o x o ", sample=(0, -1), amp=0.6).every(4, "stutter", cycle=16, dur=1 / 2)
d2 >> play("V ", sample=-1, lpf=lpf)
d3 >> play(":", sample=(0, -1), dur=1 / 4, amp=[1, 0.5, 0.5, 1], lpf=lpf).every(
    3, "stutter", cycle=8
)
d4 >> play(" H", dur=1 / 2)


# Mélodie
var.sustain = var([1 / 4, 1 / 2, 1 / 4, 3 / 4], [12, 4, 12, 4])
patt = P[0].stutter(15) | P[2]
print(len(patt))
p2 >> pasha(
    patt,
    oct=6,
    dur=1 / 4,
    slide=0,
    glide=0,  # [0]*15 + [5],
    #    slidedelay=0,
    sus=var.sustain,
    amp=0,
    fmod=linvar(-5, 5, 16),
    hpf=linvar(10, 1e5, 16),
)


# Partie B
a = 0.0
p3 >> orient(
    P[0].arp([-1, -2, -1, -3, -1]),
    dur=PDur(5, 8),
    oct=4,
    amp=a,
    sus=8 / 9 - var.sustain,
)
var.c = Pvar([4, 5, 4, 3], 8)
c1 >> bell(var.c, amp=a, delay=1, dur=PDur(5, 16), sus=1 / 2) + (0)


print(SynthDefs)

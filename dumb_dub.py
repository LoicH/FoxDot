"""2021-05-28"""

var.v = Pvar([4, 7, 2, 0])
var.c = var([2, 5, 2, 7])

b1 >> karp(c, dur=PDur(2, 4), oct=4, lpf=1000).every(4, "stutter")
p1 >> pluck(v, dur=PDur(3, 8), amp=0.5) + (0, 2, 6)
# p1.stop()
p2 >> karp(v, dur=PDur(3, 8), oct=6, amp=0.5).every(4, "stutter") + (0, 8)
d1 >> play("x       x     o-", sample=1)
d2 >> play("x       x       ", amp=0.7, sample=3, lpf=1000)
p2.stop()


b1 >> dirt(var.v, dur=P[2, 2, 2 / 3, 2 / 3, 2 / 3, 2], amp=0.8)
p1 >> pluck(var.c, dur=2, delay=1, fmod=linvar([-5, 5], 8), echo=0.25, room=0.8) + (
    0,
    2,
)

v1 >> viola(
    P[2, 5, 2, 6],
    dur=4,
    oct=5,
    fmod=0,
    slide=linvar([-0.2, 0.2], 8),
    slidedelay=12 / 16,
)
v1.stop()
p2 >> pluck(P[0, 2, 4, 6].arp([0, 2]).arp([0, 7]), dur=PDur(2, 8))
p2.stop()

var.p = Pvar([0, 7, 2, 5])
p3 >> pasha(var.p.arp([0, 2, 4]), dur=PDur(1, 8), sus=1 / 3, amp=0.8).every(
    8, "reverse"
).every(4, "stutter")


Scale.default = "major"

b2 >> bell(var.c, dur=4, sus=2, delay=3)
b2.stop()

b3 >> blip(var.v.arp([0, -2, -4, 1]), dur=PDur(3, 8))

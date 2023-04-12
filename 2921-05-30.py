Clock.bpm = 130

var.c = Pvar([5,4,3,6])
var.t = Pvar([0,1,5,1])
b1 >> dirt(var.c)
b1.stop()
d1 >> play("x o x o ").every(8, "stutter")
d1.stop()
d2 >> play("x  -x  -", sample=-2)
d2.stop()
p1 >> pluck(P[2, 2], oct=6, dur=[1/4, (3+12)/4], lpf=400)
p1.stop()
p2 >> blip(P[8,5, 4, 2], delay=2, dur=1)
p2.stop()
v1 >> viola(var.t, dur=4, oct=6, fmod=linvar([-3,3], 8))
v1.stop()



p2 >> play("(x-)(-x)o(- h[---])", sample=(1,9)).every(16, "stutter", 4)
p3 >> play("sss(sss )", sample=(9,8), amp=.8)

p2.stop()
p3.stop()

print(Samples.loops)


p1 >> play("V", sample=list(range(0,9)), dur=PDur(3,8), amp=0)
d2 >> play("(x-)(-x)  o   ", amp=0)

p2 >> pluck(var([0, -3, -2, -4], 4), dur=1/2, amp=1.2) + (0, 2, const(4))


b1 >> blip(Pvar([0, -1, 2, 4]).arp([0,7]), oct=6, dur=PDur(5,4), amp=1)
b1.stop()

b2 >> dirt(Pvar([0, -1, -2, -4]), 
    dur=PDur(3,8), 
    amp=.2)

g3 >>pluck(var([0, -3, -2, -4], 4), amp=.4, dur=2, delay=1, oct=(5,6), echo=.2, room=1, fmod=linvar([-5, 5], 8)) + (const(4), 2)

v1 >> viola(Pvar([5, 2, 0, 0]).arp([0, 2]), dur=[1, 1/2, 1/2, 3/4, 1/2, 3/4], amp=.4).every(12, "stutter")


# Techno :
# V PDur(3,8)

# v appuie le "poum"

# 1 coup de 'w' pour de la dubstep


print(SynthDefs)
d3 >> play("( -)(- )  ", sample=(1,2))
d5 >> play("(x )( x)o ", sample=-1)
d5.stop()

d4 >> play("ssss")
var.c = Pvar([5,var([3,-1])], 4)
aa >> dbass(var.c, dur=PDur(3,8), sus=1)
aa.stop()
bb >> pasha(var.c, delay=1, dur=2, echo=.2)
bb.stop()


var.d = var([0, 1, [3, -2], [3, var([5,3], 1)]], [4, 4, 2, 2])
pp >> pluck(var.d + (0,2), dur=2, delay=.5)
aa >> blip(var.d + [4,2,4,5], dur=1/2)
bb >> dbass(var.d+[0,7], dur=PDur(2,8))
kk >> orient(var.d+[[0, [2,3]], 2,[3,  [4,6]],4,[5, [6,7]]], dur=PDur(4,8), amp=1.2).every(4, "reverse")

p1 >> pluck([0, 1, 2, Pvar([[4, 5, 6, 7], [11, 9]], 8)], dur=1, sus=1)
p1.stop()


Clock.bpm = 60

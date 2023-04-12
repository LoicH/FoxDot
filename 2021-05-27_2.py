p = P[0,3,0,4].stutter(4)+P[0,0,0,1]

print(p)

v = var([0,3,0,4], 8)

print(v)

d1 >> play("x  -o --", sample=0)
p1 >> pluck(v, dur=PDur(3,8), 
        oct=5, 
        delay=[0,0,.5,0], 
        sus=var([0.5, 1.5]), 
        blur=1, 
        fmod=linvar([-10,10],8),
        slide=0   
        ) + (0,8)

p1.stop()

k1 >> karp(v, dur=PDur(3,8), sus=2, chop=4, pitch=[0,0,0,0,.1],
    room=.6, mix=0, echo=.2)

s = linvar([0.5, 1.2], 8)
print(s)

b1 >> bass(v, dur=PDur(3,4), oct=5, sus=s, lpf=140) 

Scale.default = "major"
Clock.bpm = 130


p1 >> pluck([0,1,2,3])#.every(3, "stutter")


p1.stop()

d1 >> play("x-o-", dur=1/2).every(3, "stutter", 4, cycle=4, dur=3)

d1.stop()

d2 >> play("H Hn")




# Write your code here :-)
from microbit import *
display.off()

while True:
    i1 = pin6.read_digital * 2
    i2 = pin7.read_digital * -10
    i3 = pin8.read_digital * 2
    i4 = pin9.read_digital * 2
    weighted_sum = i1 + i2 + i3 + i4
    if weighted_sum > 5:
        pin0.write_digital(1)
        pin1.write_digital(1)
    else:
        pin0.write_digital(0)
        pin1.write_digital(0)

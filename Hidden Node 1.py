## NEURON H1 ##

from microbit import *
display.off()

weighted_sum = 0

while True:
    i1 = pin6.read_digital()
    i2 = pin7.read_digital()
    i3 = pin8.read_digital()
    i4 = pin9.read_digital()

    if i1 == 1:
        weighted_sum += 0

    if i2 == 1:
        weighted_sum += 0

    if i3 == 1:
        weighted_sum += 10

    if i4 == 1:
        weighted_sum += 10

    if weighted_sum > 15:
        pin0.write_digital(1)
        pin1.write_digital(1)
    else:
        pin0.write_digital(0)
        pin1.write_digital(0)

    weighted_sum = 0

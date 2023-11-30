# Write your code here :-)
from microbit import *
display.off()

while True:
    h1 = pin4.read_digital() * 10
    h2 = pin6.read_digital() * 10
    h3 = pin7.read_digital() * 10
    h4 = pin8.read_digital() * -30
    h5 = pin9.read_digital() * -30
    weighted_sum = h1 + h2 + h3 + h4 + h5
    if weighted_sum > 5:
        pin0.write_digital(1)
        pin1.write_digital(1)
    else:
        pin0.write_digital(0)
        pin1.write_digital(0)

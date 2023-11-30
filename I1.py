
from microbit import *
display.off()

while True:
    x = pin0.read_analog()
    if x < 700:
        pin4.write_digital(1)
        pin6.write_digital(1)
        pin7.write_digital(1)
        pin8.write_digital(1)
        pin9.write_digital(1)
    else:
        pin4.write_digital(0)
        pin6.write_digital(0)
        pin7.write_digital(0)
        pin8.write_digital(0)
        pin9.write_digital(0)






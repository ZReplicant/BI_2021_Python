# This program converts from RCF or g to RPM and vice versa.
# RCF (Relative Centrifugal Force) is the amount of acceleration to be applied to the sample due to the force generated from the spinning of rotor and gravitational force. RCF is synonymous to g-force (g).
# RPM (Revolutions Per Minute) is the measurement of how fast the centrifuge rotor does a full rotation in one minute. It is basically a speed of the centrifuge.

# Choose converter mode
while 1:
    mode = str(input('Please, choose converter mode. 1 for RCF or g to RPM. 2 for RPM to RCF or g. 0 for explanation of the terms. Type q to quit.'))
# Set conditions
    if mode == '0':
        print('This program converts from RCF or g to RPM and vice versa.\nRCF (Relative Centrifugal Force) is the amount of acceleration to be applied to the sample due to the force generated from the spinning of rotor and gravitational force. RCF is synonymous to g-force (g).\nRPM (Revolutions Per Minute) is the measurement of how fast the centrifuge rotor does a full rotation in one minute. It is basically a speed of the centrifuge.')
    elif mode == '1' or mode == '2':
        val = float(input('Nice. What is the value?'))
        rot = float(input('Would you please type the diameter of the centrifuge rotor (mm)?'))
        if mode == '1':
            print(round(((val / (1.118 * rot)) ** 0.5) * 1000, 3))
        if mode == '2':
            print(round(1.118 * rot * (val / 1000) ** 2, 3))
    elif mode == 'q':
        break
    else:
        print('Something is wrong with controls, could you type the command again?')
    print('Hello again!')


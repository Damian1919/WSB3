student = 0
finalNumberOfStudent = 0

def studentCounter(meter, floor, desinf):
    student = round(meter/7.5)
    finalNumberOfStudent = student * floor
    if desinf != 0:
        percent = finalNumberOfStudent * 0.1
        finalNumberOfStudent += percent

    return finalNumberOfStudent






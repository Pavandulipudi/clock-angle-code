Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def findAngle(hh, mm):
    # handle 24-hour notation
    hh = hh % 12

    # find the position of the hour's hand
    h = (hh * 360) // 12 + (mm * 360) // (12 * 60)

    # find the position of the minute's hand
    m = (mm * 360) // (60)
    # calculate the angle difference
    angle = abs(h - m)

    # consider the shorter angle and return it
    if angle > 180:
        angle = 360 - angle
    return angle


# Clock Angle Problem
if __name__ == '__main__':
    hh = int(input("enter the hours time"))
    mm = int(input("enter the minutes time"))
    print(findAngle(hh, mm))
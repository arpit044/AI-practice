import math
import os
import random
import re
import sys


if __name__ == '__main__':
    timeCharged = float(input().strip())
    if timeCharged >= 4.00:
        print (8.00)
    else:
        print (round(2*timeCharged, 2))

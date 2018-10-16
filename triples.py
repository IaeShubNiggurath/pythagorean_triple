#!/usr/bin/env python3

##   
#
###  kurz.andi@gmx.ch
#
##   


def main():
    for hypothenuse in range(1, 110):
        for x in range(1, hypothenuse):
            for y in range(1, x):
                if(x*x + y*y == hypothenuse*hypothenuse):
                    print("{:3}² + {:3}² = {:3}²".format(y, x, hypothenuse))
                    break
                continue
            continue
        continue


if __name__ == '__main__':
    main()

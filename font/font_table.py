import cv2
import matplotlib.pyplot as plt

img = cv2.imread("./font/misaki_gothic.png")


def font(x_offset,y_offset):
    font_bin = list()
    for y in range(8):
        line = 0b00000000
        for x in range(8):
            line = line<<1
            x_address = y + x_offset*8
            y_address = x + y_offset*8
            if img[x_address,y_address][0] == 0:
                print("#",end="")
                line |= 0b1
            else:
                print(" ",end="")
        print("|",format(line,'08b'))
        font_bin.append(line.to_bytes(1,"little"))
    print("--------")
    return font_bin

if __name__ == "__main__":
    count = 0
    bin_data = list()
    #1列目
    for num in range(16):
        print("",format(count,'04x'))
        bin_data += font(0,0)
        count += 1
    #2列目
    for num in range(11):
        print("",format(count,'04x'))
        bin_data += font(7,num)
        count += 1

    for num in range(16-11):
        print("",format(count,'04x'))
        bin_data += font(1,2)
        count += 1
    second_fonts = [
        [0,0],#
        [0,9],#!
        [0,76],#"
        [0,83],##
        [0,79],#$
        [0,82],#%
        [0,84],#&
        [0,75],#'
        [0,41],#(
        [0,42],#)
        [0,85],#*
        [0,59],#+
        [0,3],#,
        [0,29],#-
        [0,4],#.
        [0,30],#/
    ]
    #3列目
    for num in range(16):
        print("",format(count,'04x'))
        bin_data += font(second_fonts[num][0],second_fonts[num][1])
        count += 1

    #4列目
    #数字
    for num in range(10):
        bin_data += font(2,num+15)
        count += 1

    second_fonts = [
        [0,6],#:
        [0,7],#;
        [0,49],#<
        [0,64],#=
        [0,50],#>
        [0,8],#?
    ]
    #3列目
    for num in range(6):
        print("",format(count,'04x'))
        bin_data += font(second_fonts[num][0],second_fonts[num][1])
        count += 1
    
    print("",format(count,'04x'))
    bin_data += font(0,86)#@
    count += 1

    for num in range(26):
        bin_data += font(2,num+32)
        count += 1
    
    second_fonts = [
        [0,45],#[
        [0,31],#\
        [0,46],#]
        [0,15],#^
        [0,17],#_
    ]
    #3列目
    for num in range(5):
        print("",format(count,'04x'))
        bin_data += font(second_fonts[num][0],second_fonts[num][1])
        count += 1
    
    print("",format(count,'04x'))
    bin_data += font(0,13)#`
    count += 1

    for num in range(26):
        print("",format(count,'04x'))
        bin_data += font(2,num+64)
        count += 1
    
    second_fonts = [
        [0,47],#{
        [0,34],#|
        [0,48],#}
        [0,32],#~
        [1,2],#12
    ]
    #3列目
    for num in range(5):
        print("",format(count,'04x'))
        bin_data += font(second_fonts[num][0],second_fonts[num][1])
        count += 1



    print("================================")
    print("binary size =>", len(bin_data),"Byte")
    print("================================")

    with open("./font.bin",mode='wb') as f:
        f.writelines(bin_data)

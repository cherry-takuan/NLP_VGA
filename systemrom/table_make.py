import pprint

def pattern(H_count, V_count):
    #result = 0b00011100
    result = 0b00111100
    if V_count == 49:
        #VRS
        result |= 0b00000001
    if V_count == 49 and H_count == 524:
        #HRS
        result |= 0b00000010
    if V_count == 49 and H_count != 524:
        #HCLK
        result &= 0b11111011
    if 42 <= V_count and V_count <= 47:
        result &= 0b11110111
    if 490 <= H_count and H_count <= 491:
        result &= 0b11101111
    if H_count < 480 and 1 <= V_count and V_count <= 40:
        result |= 0b00100000
        result &= 0b11011111
    return result

def pattern2(H_count, V_count):
    #result = 0b00011100
    result = 0b00111100
    if V_count == 49:
        #VRS
        result |= 0b00000001
    if V_count == 49 and H_count == 524:
        #HRS
        result |= 0b00000010
    if V_count == 49 and H_count != 524:
        #HCLK
        result &= 0b11111011
    if 42 <= V_count and V_count <= 47:
        result &= 0b11110111
    if (490 == H_count and 1 <= V_count) or H_count == 491 or (H_count == 492 and 0 == V_count) :
        result &= 0b11101111
    if H_count < 480 and 1 <= V_count and V_count <= 40:
        #result |= 0b00100000
        result &= 0b11011111
    return result

bin = list()

for H_count in range(526):
#for H_count in range(0b1):
    for V_count in range(0b1000000):
        bin.append(pattern(H_count,V_count).to_bytes(1,"little"))
        #bin.append(pattern(H_count,V_count).to_bytes(1,"little"))
        print(H_count,"\t",V_count,"\t",format(pattern(H_count,V_count),'08b'))



print("================================")
print("binary size =>", len(bin),"Byte")
print("================================")

#with open("./VGA.bin",mode='wb') as f:
#    f.writelines(bin)
#with open("./VGA_v2.bin",mode='wb') as f:
#    f.writelines(bin)
#with open("./VGA_v1.bin",mode='wb') as f:
#    f.writelines(bin)
with open("./VGA_v3.bin",mode='wb') as f:
    f.writelines(bin)
#with open("./VGA_v1_A.bin",mode='wb') as f:
#    f.writelines(bin)




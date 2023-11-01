import random

def monobit_test(bit_str):
    num_of_ones = bit_str.count('1')
    if 9654 <= num_of_ones <= 10346: return True

def runs_test(bit_str):
    max_seq = 1
    seq = 1
    for i in range(0, len(bit_str)-1):
        if bit_str[i] == bit_str[i+1]:
            seq += 1
        else:
            seq = 1
        if seq > max_seq:
            max_seq = seq
   
    if max_seq > 36: return False
    else: return True

def poker_test(bit_str):
    m = 4 
    k = len(bit_str) // m
    block_map = {}

    for i in range(0, len(bit_str), m):
        block = bit_str[i : i+m]
        if block in block_map:
            block_map[block] += 1
        else: block_map[block] = 1

    chi_3 = ((2 ** m) / k) * sum([n ** 2 for n in block_map.values()]) - k
    if 1.03 <= chi_3 <= 57.4: return True
    else: return False

def runs_lengths_test(bit_str):
    ones_map = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6+" : 0}
    ones_len = 1
    zeros_map = {"1" : 0, "2" : 0, "3" : 0, "4" : 0, "5" : 0, "6+" : 0}
    zeros_len = 1

    for i in range(0, len(bit_str)-1):
        if bit_str[i] == '1':
            if bit_str[i] == bit_str[i+1]:
                ones_len += 1
                if i+1 ==  len(bit_str)-1:
                    matching_lenghts(ones_map, ones_len) 
                    break
            else:
                matching_lenghts(ones_map, ones_len) 
                ones_len = 1
                if i+1 ==  len(bit_str)-1:
                    matching_lenghts(zeros_map, zeros_len) 
        elif bit_str[i] == '0':
            if bit_str[i] == bit_str[i+1]:
                zeros_len += 1
                if i+1 ==  len(bit_str)-1:
                    matching_lenghts(zeros_map, zeros_len) 
                    break
                     
            else: 
                matching_lenghts(zeros_map, zeros_len) 
                zeros_len = 1
                if i+1 ==  len(bit_str)-1:
                    matching_lenghts(ones_map, ones_len) 
    zero_test = True
    one_test = True
    intervals = ((2267,2733), (1079, 1421), (502,748), (223,402), (90,223), (90,223))
    for i, j in zip(zeros_map.values(), intervals):
        zero_test = zero_test and (i in range(j[0], j[1]+1))

    for i, j in zip(ones_map.values(), intervals):
        one_test = one_test and (i in range(j[0], j[1]+1))

    return zero_test and one_test

def matching_lenghts(bit_map, lenght):
    match lenght:
        case 1: bit_map["1"] += 1
        case 2: bit_map["2"] += 1
        case 3: bit_map["3"] += 1
        case 4: bit_map["4"] += 1
        case 5: bit_map["5"] += 1
        case _ if lenght >= 6: bit_map["6+"] += 1


if __name__ == '__main__':
    bit_string = bin(random.getrandbits(20000)).lstrip("0b")
    print("Monobit test result:", monobit_test(bit_string))
    print("Maximum series length test result:", runs_test(bit_string))
    print("Poker test result", poker_test(bit_string))
    print("Series test result:", runs_lengths_test(bit_string))

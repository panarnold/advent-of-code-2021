with open('day3.txt') as f:
    data = [x for x in f.read().split()]

gamma = ''
epsilon = ''

for b in range(0, len(data[0])):
    one = 0
    zero = 0
    for c in range(0, len(data)):
        if data[c][b] == '0':
            zero +=1
        else:
            one += 1
    
    if zero > one:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

g = int(gamma, 2)
e = int(epsilon, 2)
print('part 1: ', g * e)

data2 = data[:]
index = 0
while len(data) > 1:
    one = 0
    zero = 0
    ones = []
    zeroes = []
    for c in range(0, len(data)):
        if data[c][index] == '0':
            zero += 1
            zeroes.append(data[c])
        else:
            one += 1
            ones.append(data[c])

    if zero > one:
        data = zeroes
    else:
        data = ones
    index += 1

oxygen = int(data[0], 2)

data = data2
index = 0
while len(data) > 1:
    one = 0
    zero = 0
    ones = []
    zeroes = []
    for c in range(0, len(data)):
        if data[c][index] == '0':
            zero += 1
            zeroes.append(data[c])
        else:
            one += 1
            ones.append(data[c])
    if one < zero:
        data = ones
    else:
        data = zeroes
    index += 1

co2 = int(data[0], 2)

print('part2:', oxygen * co2)



# def string_to_bin_to_int(element):
#     return int(element, 2)

# def fulfill_binary_chunk(filename):
#     bites_chunk = []
#     with open(filename) as f:
#         arr = f.readlines()
#     for el in arr:
#         el = list(el.strip())
#         bites_chunk.append(el)
#     return bites_chunk

# def binary_diagnostics_gases_oxygen(filename):
#     bites_chunk = fulfill_binary_chunk(filename)
#     oxygen_chunk = bites_chunk[:]
   
    
#     temp = []
#     # for i, items in bites_chunk:

#     # while len(oxygen_chunk) > 1:
#     for i, items in enumerate(zip(*bites_chunk)):
        
        
#         if items.count('1') >= items.count('0'):
#             oxygen_chunk = list(filter(lambda a: a[i] == '1', oxygen_chunk))
#                 # co2_chunk = list(filter(lambda a: a[i] == '0', co2_chunk))
#         else:
#             oxygen_chunk = list(filter(lambda a: a[i] == '0', oxygen_chunk))
#                 # co2_chunk = list(filter(lambda a: a[i] == '1', co2_chunk))
        
        

#     print('oxygenchunk', oxygen_chunk)
    
#     # ones_count = 0
#     # zeroes_count = 0
#     # for item in oxygen_chunk:
#     #     if item[len(item) - 1] == '0':
#     #         zeroes_count +=1
#     #     else:
#     #         ones_count +=1

#     # print('ones', ones_count)
#     # print('zeroes', zeroes_count)
    
#     # if ones_count >= 1:
#     #     oxygen_chunk = [x for x in oxygen_chunk if x[len(x) - 1] == '1']
#     # else:
#     #     oxygen_chunk = [x for x in oxygen_chunk if x[len(x) - 1] == '0']
            
#             # co2_chunk = list(filter(lambda a: a[i] == '0', co2_chunk))

#     # print(oxygen_chunk)
#     # oxygen_chunk = sum(oxygen_chunk, [])
    
#     # oxygen_chunk = ''.join(oxygen_chunk)
#     # print('oxy', oxygen_chunk)
#     # return oxygen_chunk
   


# def binary_diagnostics_gases_co2(filename):
#     bites_chunk = fulfill_binary_chunk(filename)
#     co2_chunk = bites_chunk[:]

#     for i, items in enumerate(zip(*co2_chunk)):
#         if len(co2_chunk) > 2:
#             if items.count('1') >= items.count('0'):
#                 # oxygen_chunk = list(filter(lambda a: a[i] == '1', oxygen_chunk))
#                 co2_chunk = list(filter(lambda a: a[i] == '0', co2_chunk))
#             else:
#                 co2_chunk = list(filter(lambda a: a[i] == '1', co2_chunk))
#         else:
#             break
        
#     ones_count = 0
#     zeroes_count = 0
#     for item in co2_chunk:
#         if item[len(item) - 1] == '0':
#             zeroes_count +=1
#         else:
#             ones_count +=1

#     # print(ones_count)
#     # print(zeroes_count)
    
#     if zeroes_count > 1:
#         co2_chunk = [x for x in co2_chunk if x[len(x) - 1] == '1']
#     else:
#         co2_chunk = [x for x in co2_chunk if x[len(x) - 1] == '0']
    

#     co2_chunk = sum(co2_chunk, [])
#     co2_chunk = ''.join(co2_chunk)
#     print('co2 ', co2_chunk)
#     return co2_chunk




        




# def binary_diagnostics_gamma_epsilon(filename):
#     bites_chunk = fulfill_binary_chunk(filename)
#     gamma, epsilon = '', ''

#     # oxygen_chunk, co2_chunk = bites_chunk[:], bites_chunk[:]


#     for items in zip(*bites_chunk):
#         if items.count('1') >= items.count('0'):
#             gamma += '1'
#             epsilon += '0'
#             # oxygen_chunk = list(filter(lambda a: a[i] == '1', oxygen_chunk))
            
#         else:
#             gamma += '0'
#             epsilon += '1'
#             # oxygen_chunk = list(filter(lambda a: a[i] == '0', oxygen_chunk))
        
    
#     gamma = string_to_bin_to_int(gamma)
#     epsilon = string_to_bin_to_int(epsilon)
#     print(gamma*epsilon)
   


# binary_diagnostics_gamma_epsilon('example3.txt')
# # oxygen = binary_diagnostics_gases_oxygen('day3.txt')
# # co2 = binary_diagnostics_gases_co2('day3.txt')
# oxygen = binary_diagnostics_gases_oxygen('day3.txt')

# # print(string_to_bin_to_int(oxygen))
# # print(string_to_bin_to_int(co2))
# # print(string_to_bin_to_int(oxygen) * string_to_bin_to_int(co2))


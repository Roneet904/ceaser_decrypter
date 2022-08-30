import string



def assignNumbers(a_dict,count):
    for letter in alphabet:
        a_dict[letter] = count
        count +=1

def solve_shift (shift_num,alpha_dict,string):
    new_string = ''
    letter_num_list = list(alpha_dict.keys())
   
    for letter in string:
        shift = (alpha_dict.get(letter)) + shift_num
        if shift >= 26:
            shift -= 26
        new_string += letter_num_list[shift - 1]

    return new_string

if __name__ =='__main__':
    alphabet = list(string.ascii_lowercase)
    a_dict = {}
    count = 1
    shift_num = 11
    cipher = 'xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadds'

    assignNumbers(a_dict, count)

    decrypted_message = solve_shift(shift_num, a_dict,cipher)
    
    print (decrypted_message)

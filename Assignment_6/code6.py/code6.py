import string


def main():
    print('MAIN MENU:\n', '1) Encode a string =1 \n', '2) Decode a string =2 \n', '3) QUIT = q')

    def encode():
        message = str.upper(input("Enter text to encrypt:"))
        shift = int(input("Enter the number to shift letters by:"))
        stringValue = [ord(message) - 96 for message in message]
        encode_msg_val = []
        [encode_msg_val.append(int(stringValue[i])+shift) for i in range(len(stringValue))]
        encode_msg_array = []
        for i in range(len(encode_msg_val)):
            encode_val = encode_msg_val[i] + 96
            encode_msg_array.append(chr(encode_val))
            encode_msg = ''.join(encode_msg_array)
        print(encode_msg)
        return main()

    def decode():
        decode_msg = str.upper(input("Enter text to encrypt:"))
        shift = int(input("Enter the number to shift letters by:"))

        decode_msg_val = [ord(decode_msg) - 96 for decode_msg in decode_msg]

        decode_val = []
        [decode_val.append(decode_msg_val[i] - shift) for i in range(len(decode_msg_val))]

        decode_msg_array = []
        [decode_msg_array.append(decode_val[i] + 96) for i in range(len(decode_val))]

        decode_msg_list = []
        [decode_msg_list.append(chr(decode_msg_array[i])) for i in range(len(decode_msg_array))]

        decode_msg = ''.join(decode_msg_list)
        print(decode_msg)
        return main()

    choice = input('Enter your selection:==>')
    if choice == '1':
        encode()
    elif choice == '2':
        decode()
    elif choice == 'q' or choice == 'Q':
        print('Have a nice day.')
    else:
        print('Error. Please try again')
        return main()


main()
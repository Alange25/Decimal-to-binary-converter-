"""-DecimalToBinaryConverterProgram-
   -Alexander Lange-"""


def math_computation():
    """returning user input"""
    print("==========The Decimal To Binary Converter Program===========")
    print("------------------------------------------------------------")
    print()
    return input("Enter a Binary value to be converted to decimal/integer? ")


def convert_to_decimal(mess):
    """a function to convert binary to decimal"""
    result = 0
    length = len(mess)
    for i in range(0, length):
        if mess[i] == '1':
            result += 2**(len(mess)-i-1)
    return result


def convert_to_binary(mess):
    """a function to convert decimal to binary"""
    result = ""
    num = int(mess)
    # Repeat the loop till n becomes negative
    while num > 0:
        # Finding the reminder
        rem = num % 2
        # Appending reminder to the result
        result += str(rem)
        # Making num to its half
        num //= 2
    # Reverse the value of result
    result = result[::-1]
    return result


def main():
    """the main function"""
    a = math_computation()
    ans1 = convert_to_decimal(a)
    print("Your Decimal value is : " + str(ans1))

    b = int(input("Enter an integer value to be converted to binary? "))
    ans2 = convert_to_binary(b)
    print("Your Binary value is : " + str(ans2))


main()

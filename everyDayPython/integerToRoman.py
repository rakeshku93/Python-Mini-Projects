import os
import sys

def integer_to_roman(integer):
    """
    This function converts a integer number to its roman form

    Args:
        integer (int): Any random interger value provided by command line

    Returns:
        roman value: Roman form of input 
    """
    integer_roman = {
            1000: "M", 900: "CM", 500: "D", 400: "CD", 
            100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X",  
            9: "IX", 5: "V", 4: "IV", 1: "I" 
            }

    roman_literal = ""
    for value, numeral in integer_roman.items():
        while integer >= value:
            roman_literal += numeral
            integer -= value
            
    return roman_literal

if __name__ == "__main__":

    try:
        if sys.argv[1:]:
            integer = int(" ".join(sys.argv[1:]))
            roman_number = integer_to_roman(integer)
            
        print(f"The Roman conversion of number {integer} is : {roman_number}")
    
    except Exception as e:
        print(e)
        
    
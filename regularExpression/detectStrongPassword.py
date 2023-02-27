import os
import re
import sys

def detect_password_stregth(passwrd="Regex@09!"):
    """This function detects whether a given password is strong or not."""
    
    print("\nTesting for password:", passwrd)
    
    if len(passwrd) >= 8:
        digitRegex = re.compile(r"\d+")
        digitMatchObject = digitRegex.search(passwrd)
        
        upperCaseRegex = re.compile(r"[A-Z]+")
        upperCaseObject = upperCaseRegex.search(passwrd)
        
        lowerCaseRegex = re.compile(r"[a-z]+")
        lowerCaseObject = lowerCaseRegex.search(passwrd)
        
        if digitMatchObject is not None:
            if upperCaseObject is not None:
                if lowerCaseObject is not None:
                    
                    print(f">>digitMatchObject: {digitMatchObject.group()}")
                    print(f">>upperCaseObject: {upperCaseObject.group()}")
                    print(f">>lowerCaseObject: {lowerCaseObject.group()}")
                    
                    return "Strong Password"
                
                else:
                    return "Password is weak. It should contain both uppercase & lowercase characters"
            else:
                return "Password is weak. It should contain atleast 1 uppercase characters"     
        else:
            return "Password is weak. It should contain atleast 1 digit"
    else:
        return "Password is weak. It should contain atleast 8 characters"
    

if __name__ == "__main__":
    print(f"Password Status: {detect_password_stregth()}")
        
    argv_password = " ".join(sys.argv[1:])
    if argv_password:
        print(f"Password Status: {detect_password_stregth(argv_password)}")
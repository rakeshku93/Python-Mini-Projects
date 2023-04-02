"""Launches a map in the browser using `multiple addresses` from the command line using **webbrowser**"""
import webbrowser
import time
import sys
    
# sys.argv variable stores a list of the program's filename and command line arguments.
# sys.argv[0] is name of python scripts
# sys.arg[1:] contains command line arguments 
if len(sys.argv) > 1:
    # iterate over each args 
    for argv in sys.argv[1:]:
        print(f"arg: {argv} and type of argv: {type(argv)}")
        address_string = "".join(argv)
        print(f"{address_string = }")
        webbrowser.open(f"https://www.google.com/maps/place/{address_string}")
        time.sleep(1)

else:
    print("No address is passed...")
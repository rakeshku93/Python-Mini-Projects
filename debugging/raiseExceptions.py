
def boxPrint(symbol, width, height):
    """In this code we're raising our own exceptions uisng raise keyword"""
    print("--")
    print(f"Creating Pattern with: {symbol=} {width=} {height=}")
    
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string.")
    
    if width <= 2:
        raise Exception("Width must be greater than 2")
    
    if height <= 2:
        raise Exception("Height must be greater than 2")
    
    
    print(symbol*width)
    for i in range(height-2):
        print(symbol + (" " *(width-2)) + symbol)
    print(symbol*width)
    

if __name__ == "__main__":
    
    for sym, w, h in (('*', 4, 4), ('x', 1, 3), ('O', 20, 5), ('ZZ', 3, 3)):
        try:
            boxPrint(sym, w, h)
            
        except Exception as e:
            print("An Error occured: ", str(e))
    
    
# Note: try and except handles errors gracefully. 
# Even when code fails for one set of (symbol, w, h); it raises error and runs for other parameters. 
# But, this is not the case with `assert` keyword. If `assert` fails, it crash the program.
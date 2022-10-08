import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
# once debugging is done, we don't need to remove from each line  we can disable it using this below syntax
# logging.disable(level = logging.CRITICAL) 

logging.debug("Start of the program.")
def factorial(num):
    logging.debug(f"Start of the factorial calculation for: {num=}")
    total = 1
    if num <= 1:
        return total
    else:
        for i in range(1, num+1):
            total *= i
            logging.debug(f"i is {i} and total is {total}")
        
        logging.debug(f"End of factorial calculation for: {num=}")
        return total

if __name__ == "__main__":
    # num = int(input("Enter the number: "))
    num = 6
    print(f"Factorial of {num}! = {factorial(num)}")
    logging.debug(f"End of the program.")
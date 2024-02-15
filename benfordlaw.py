from typing import List
import json

def check(size: int,tab: List[int]) -> bool:
    hashMap={
            1 : 30.1,
            2 : 17.6,
            3 : 12.5,
            4 : 9.7, 
            5 : 7.9, 
            6 : 6.7, 
            7 : 5.8, 
            8 : 5.1, 
            9 : 4.6
            }
    #For each digit
    for i in range(9):
        taux=tab[i]*100/size
        if taux < hashMap[i+1] - 10 or taux > hashMap[i+1] + 10:
            return True 
    return False

def main(json_file: str):
    # Load the JSON
    with open(json_file) as file:
        data = json.load(file)

    # Define variables
    tab = [0] * 9
    size = len(data["data"])

    for i in range(size):
        for j in str(data["data"][i]):
            # iterate over each character
            if j.isnumeric() and j != '0':
                tab[int(j) - 1] += 1
                break

    if check(size, tab):
        print("Respect Benford’s law")
    else:
        print("Do not respect Benford's law")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage : python3 benfordlaw.py <json_file>")
        sys.exit(1)
    main(sys.argv[1])
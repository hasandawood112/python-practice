def newString(str):
    if len(str) >= 2 and str[:2] == "Is":
        return str
    return "Is " + str

string = input("Enter any string : ")

print("New string is : ", newString(string))

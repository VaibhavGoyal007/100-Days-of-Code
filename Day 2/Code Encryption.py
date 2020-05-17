string = input()
key = int(input())
output = ""
if string == ""  or string == " ":
    print("No Code to Encrypt")
elif key < 0 or key > 1000:
    print("Invalid key is passed")
else:
    for char in string:
        if 97 <= ord(char) <= 122:
            if ord(char)+key > 122:
                output = output + chr(ord(char)+key-97)
            else:
                output = output + chr(ord(char)+key)
        elif 65 <= ord(char) <= 90:
            if ord(char)+key > 90:
                output = output + chr(ord(char)+key-65)
            else:
                output = output + chr(ord(char)+key)
        elif 48 <= ord(char) <= 57:
            if ord(char)+key > 57:
                output = output + chr(ord(char)+key-48)
            else:
                output = output + chr(ord(char)+key)
        else:
            output = output + char
print(output)

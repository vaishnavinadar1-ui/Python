def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text

def main():
    user = input("Input: ")
    print(convert(user))

main()

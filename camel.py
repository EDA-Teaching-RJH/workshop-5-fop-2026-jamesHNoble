def main():
    name1 = input("what is your name?")
    nameAdd = " "
    for chr in name1:
        if chr.isupper():
            nameAdd += "_" + chr.lower()
        else:
            nameAdd += chr

    print(nameAdd)

main()


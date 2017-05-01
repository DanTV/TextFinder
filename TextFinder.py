def main():
    text= input("Text: ")
    if len(text) < 1:
        print("A len of text must be bigges 1 character!")
        from time import sleep
        sleep(2)
        main()

    find = input("What Find: ")
    if len(find) < 1:
        print("A len of word must be bigges 1 character!")
        from time import sleep
        sleep(2)
        main()
    curid = 0
    progress = 0
    curidd = []
    for i in range(0, len(text)):
        if text[i] == find[curid]:
            curid += 1

	# if ID of word = len of word
        if curid == len(find):
            curid=0
            progress += 1
            curidd.append(i- len(find)+1)
    result1 = text
    for c in range(0,len(curidd)):
        result = result1[:curidd[c]] + "\033[91m" + find + "\033[0m"+ result1[curidd[c]+len(find):]
        result1 = result

        for v in range(0, len(curidd)):
            curidd[v] = curidd[v]+9
    print("RESULT(founded words will be pink):\n"+result)
main()

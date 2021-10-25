print("Welcome to your personalized tool!")
command = input("> ")
while True:
    if command[:4] == "file":
        file = open(command.split(" ")[1], "r")
    elif command[:4] == "exit":
        exit(0)
    elif command[:3] == "sum":
        nums = [int(x) for x in command[4:].split(" ")]
        print(f"{sum(nums)}")
    elif command[:3] == "avg":
        nums = [int(x) for x in command[4:].split(" ")]
        print(f"{sum(nums)/len(nums)}")
    elif command[:4] == "help":
        print("The available commands are: file, info, dictionary, search, sum, avg, help, exit.")
    elif command[:10] == "dictionary":
        if "file" in globals().keys():
            try:
                file_dict = dict([[line.split(",")[0], int(line.split(",")[1].replace("\n", ""))] for line in file.readlines()])
            except:
                print("Invalid dictionary file.")
            file.seek(0)
        else:
            print("Please load a file.")
    elif command[:6] == "search":
        if "file_dict" in globals().keys():
            word = command.split(" ")[1]
            if word in file_dict.keys():
                print(f"{word} is in the dictionnary")
            else:
                print(f"{word} is not in the dictionnary")
        else:
            print("Please make dictionary before searching.")
    elif command[:4] == "info":
        if "file" in globals().keys():
            print(f"{len(file.readlines())} lines")
            file.seek(0)
            print(f"{len(file.read())} caracters")
            file.seek(0)
        else:
            print("Please load a file.")
    else:
        print("Unknown command!")
    command = input("> ")
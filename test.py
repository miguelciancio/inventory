try:
    with open("inventory.txt", "r", encoding="utf-8") as rfile:
        lines = rfile.readlines()
        # iterate the lines of the file ignoring the first line which is useless for us at the moment.
        for index, line in enumerate(lines):
            if index == 0:
                pass
            else:
                print(line, end="")
except Exception as error:
    print("Error:", error)

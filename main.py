VERSION = 0.1
MEMORY = {}
CURSOR_LINE = ""

def save_to_memory(address, value):
    MEMORY[address] = value

def tokenize(text_input):
    return text_input.split()

def setup():
    pass

def loop():
    while True:
        CURSOR_LINE = input(">> ")
        if(len(CURSOR_LINE) > 1):
            tokens = tokenize(CURSOR_LINE)
            if(tokens[0] == "bye" or tokens[0] == "exit"):
                exit()
        else:
            print("Wrong input")
        CURSOR_LINE = ""

def main():
    print(f"PyBasic Version {VERSION}")
    setup()
    loop()

if __name__ == "__main__":
    main()

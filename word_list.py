
#String that includes all words separated by a space.
file_path = "words.txt"
try:
    with open(file_path, "r") as file:
        dictionary = file.read().splitlines()
except FileNotFoundError:
    dictionary = ["test1", "test2", "test3", "test4", "test5"]

#`dictionary` stores all words in a list.

#main function to test if `dictionary` is formatted correctly
def main():
    print(dictionary)

if __name__ == '__main__':
    main()
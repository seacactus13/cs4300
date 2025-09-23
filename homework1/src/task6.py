def count_words_in_file(filename):
    with open(filename, "r") as f:
        text = f.read()
    words = text.split()
    return len(words)

def main():
    filename = "task6_read_me.txt"
    total_words = count_words_in_file(filename)
    print(f"Total words in {filename}: {total_words}")

if __name__ == "__main__":
    main()

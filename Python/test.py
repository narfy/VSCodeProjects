def main():
    f = open("Python\words.txt", 'r')
    print(f.read())
    for i in range(5):
        print(i)

if __name__ == "__main__":
    main()
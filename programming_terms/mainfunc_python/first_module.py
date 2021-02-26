# this set up gives you the option to run (or not run) a chunk of code when imported from another python file

print(f"First Module name: {__name__}")


def main():
    print(f"First Module Main Method name: {__name__}")


if __name__ == '__main__':
    main()
    print("Run Directly")
else:
    print("Run from Import")

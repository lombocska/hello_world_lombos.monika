import sys

#def
def main():

# if you write just your first name
    if len(sys.argv) == 2:
        name = sys.argv[1]

# if you write you first and last name
    elif len(sys.argv) > 2:
        name = sys.argv[1] + " " + sys.argv[2]

# if you don't write your name
    else:
        name = "World"
    print( "Hello ", name, "!" )

if __name__ == "__main__":
    main()

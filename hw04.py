# ------------------------------------------------------
#        Name: Frida Li
#       Peers: (add any collaborators)
#  References: (anything you checked to solve this)
# ------------------------------------------------------
import sys

secret_word = "food"

# Task 1
def check_text():
    
    """Ask the user for text until it contains the secret word or 'dog'/'Dog'."""
    # Keep asking for input until a matching word is found.
    while True:
        text = input("Enter some text:")
        if secret_word in text:
            print("You used the secret word!")
            return
        
        elif "dog" in text or "Dog" in text:
            print('You used the word "dog" or the word "Dog"!')
            return
    
        else:
            print("Try again")




# Task 2
def check_greater():
    """Compare two integers and repeat until they are different."""

    
    while True:
        a = int(input("Give me the first number:"))
        b = int(input("Give me the second number:"))
        
        if a > b:
            print("First is Greater")
            return
    
        if a < b:
            print("Second is Greater")
            return
    
        if a == b:
            print("Try again")




# Task 3
def get_special_numbers():
    """Print numbers from 1 to 40 that are odd, divisible by 3, and not divisible by 5."""
    b = False
    for i in range(1,41):
        # Check if the number meets all three conditions.
        if i % 2 ==1 and i %3 ==0 and i % 5 != 0:
            b = True
            
        else:
            b = False
        
        if b:
            print(i)
                
            



# Task 4.a
def my_for_loop():
    """Check a word's length and spaces, then classify each character as a vowel or consonant."""
    
    word = input("Give me a word:")
    # Reject words with invalid lengths or spaces.
    if 2<= len(word) <=5 and " " not in word:
        for i in range(0,len(word)):
            letter = word[i]
            if letter in "aeiouAEIOU":
                print(f"letter {letter} is a vowel")
                
            else:
                print(f"letter {letter} is a consonant")
            
                
    else:
        print("bad word")


# Task 4.b
def my_while_loop():
    """Repeat a menu until the user chooses to return or exit the program."""
    
    while True:
        menu = input("Choose a, b or c:")
        while menu == "a":
            menu = input("Choose a, b or c:")
        
        if menu == "b":
            print("Goodbye")
            return
        
        if menu == "c":
            sys.exit()
    
        if menu not in ("a", "b", "c"):
            print("try again")
        

# ---------------------------------------
# Do not modify anything below this line
# ---------------------------------------

def main():

    # Task 1 calls
    check_text()

    # Task 2 calls
    check_greater()

    # Task 3 calls
    get_special_numbers()

    # Task 4 calls
    my_for_loop()
    my_while_loop()

if __name__ == "__main__":
    main()
    print("The End")

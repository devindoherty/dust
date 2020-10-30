import time

answer_a = ["A", "a"]
answer_b = ["B", "b"]
answer_c = ["C", "c"]
answer_d = ["D", "d"]

yes = ["Y", "y", "Yes", "yes"]
no = ["N", "n", "No", "no"]

required = ("\nThat is not an option. Choose again.")

def intro():
    print ("You were born on the planet Azad in year 890 of the Third Imperium. "
           "Your father, lord of one of the great interstellar noble Houses, was:")
    time.sleep(1)
    print ("""A. Merciless and cruel \n
           B. A fool addicted to salts \n
           C. Noble, kind, and beloved by all \n
           D. Mysterious and distant \n""")
    choice = input(">>> ")
    if choice in answer_a:
        option_cruel()
    elif choice in answer_b:
        option_fool()
    elif choice in answer_c:
        option_noble()
    elif choice in answer_d:
        option_strange()
    else:
        print (required)
        intro()



def option_cruel():
    print ("Cruelty. Alas.")
    time.sleep(1)
    intro()

def option_fool():
    print ("A foolish man leads his House astray.")
    time.sleep(1)
    intro()

def option_noble():
    print ("He was a paragon of virtue. ")
    time.sleep(1)
    intro()      

def option_strange():
    print ("Years often went by without you seeing him.")
    time.sleep(1)
    intro()

intro()

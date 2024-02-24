git alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
             'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print("Wel come to Encrypt and Decrypt !!!!!")


def caeser(start_word, shift, direction):
    end_word = ""
    if direction == "decode":
        shift *= -1
    for char in start_word:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = position + shift
            end_word += alphabets[new_position]
        else:
            end_word += char
    print(f"The {direction}d word is : {end_word}")


should_continue = True
while should_continue:
    direction = input("Enter  encode or decode : ")
    word = input("Enter the word : ")
    shift = int(input("Enter the number of shifts : "))
    if shift>26:
        shift = shift % 26
    caeser(word, shift, direction)

    result = input("Type 'yes' if you wnat to continue else 'no' to exit")
    if result=="no":
        should_continue=False
        print("Good Bye")




 
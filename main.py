def count_words(string):
    words = string.split()
    return len(words)


def count_letters(string):
    dico = {}
    string = string.lower()

    for letter in string:
        if letter in dico and letter.isalpha() == True:
            dico[letter] += 1
        elif letter not in dico and letter.isalpha() == True:
            dico[letter] = 1
    
    return dico


def ordonne(string):
    return string["num"]


def sort_letters(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=ordonne)
    return sorted_list


def main():
    with open("books/frankenstein.txt") as book:
        book_contents = book.read()
        number_of_words = count_words(book_contents)
        number_of_letters = count_letters(book_contents)
        sorted_letters = sort_letters(number_of_letters)
    return number_of_words, sorted_letters


mots, lettres = main()
print(f"Il y a {mots} dans Frankenstein.")
print()
for elem in lettres:
    print (f"La lettre '{elem['char']}' est présente '{elem['num']}' fois dans le livre.")
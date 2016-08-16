"""
Write three functions:
sort1(langauges)
sort2(languages)
sort3(langauges)
Goal: Print exactly the below w/ three functions:
1:
    Arabic
    English
    Koine Greek
    Latin
    Romanian
    C++
    JavaScript
    Python
    R
2:
    R
    C++
    Latin
    Arabic
    Python
    English
    Romanian
    JavaScript
    Koine Greek
3:
    JavaScript
    R
    Latin
    Python
    Romanian
    Koine Greek
    English
    Arabic
    C++
"""
import operator

languages = {'JavaScript': 'P',
             'Arabic': 'N',
             'R': 'P',
             'Python': 'P',
             'C++': 'P',
             'Koine Greek': 'N',
             'Latin': 'N',
             'Romanian': 'N',
             'English': 'N'}

def sort1(languages):
    #languages_list = sorted(sorted(languages), key=languages.__getitem__)
    languages_tuple = sorted(sorted(languages.items()), key=operator.itemgetter(1))
    print("1:")
    for key, val in languages_tuple:
        print("\t" + key)

def sort2(languages):
    languages_list = sorted(languages, key=len)
    print("2:")
    for val in languages_list:
        print("\t" + val)

def sort3(languages):
    languages_list = sorted(languages, key=last_char, reverse=True)
    print("3:")
    for val in languages_list:
        print("\t" + val)

def last_char(word):
    return word[-1].lower()

def main():
    sort1(languages)
    sort2(languages)
    sort3(languages)

if __name__ == "__main__":
    main()

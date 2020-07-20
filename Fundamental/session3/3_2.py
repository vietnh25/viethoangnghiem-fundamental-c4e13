caudo = input('enter your quizz: ')

def split_line(text):

    # split the text
    words = list(text)
    # print(words) 
    # for each word in the line:
    # for word in words:
    #     words.append(word)
    #     # print the word
    #     print(words) 
    for i in range(len(words)):
        print(words[i], end='')

split_line(caudo)  
answer = input('answer your: ')
if answer == caudo:
    print("Bingo!")
else:
    print(":(")    
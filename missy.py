original_lyric = input('Please enter a lyric: ')
punctuation = ['!', '.', ',', "'", '"', '?', ':', ';']

def missyElliot(lyric):
    if not lyric.isdigit():
        reversed_lyric = []
        lyric_list = lyric.split()

        for index, word in enumerate(lyric_list):
            for mark in punctuation:
                if mark in word:
                    new_word = word.replace(mark, '')
                    lyric_list.remove(word)
                    lyric_list.insert(index, new_word)
                else:
                    continue

        for word in lyric_list:
            new_word = word[::-1]
            reversed_lyric.append(new_word)

        print(reversed_lyric)

        new_lyric_list = reversed(reversed_lyric)
        final_lyric = ' '.join(new_lyric_list)
    else:
        return "This really only works with words."

    return final_lyric

newline = missyElliot(original_lyric)
print(newline)

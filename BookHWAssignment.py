from urllib.request import urlopen

url = "https://www.gutenberg.org/files/1342/1342-0.txt"
local_name = "prideandprejudice.txt"

url_2 = "https://www.gutenberg.org/files/11/11-0.txt"
local_name_2 = "aliceinwonderland.txt"

import certifi
import ssl

def save_locally():
    """
    Save the book locally, so we can use it faster and no need to load every time
    :return: None
    """
    with open(local_name, "w") as local_fp:
        with urlopen(url, context=ssl.create_default_context(cafile=certifi.where())) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp.write(line)

    with open(local_name_2, "w") as local_fp:
        with urlopen(url_2, context=ssl.create_default_context(cafile=certifi.where())) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp.write(line)

punctuation = ",;!.?-()"

def get_unique_words():
    """
    Get the dictionary of unique words and their frequency
    :return: dict
    """
    unique_words = {}

    with open(local_name_2) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            # get the words:
            for word in line.split():
                unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words

def get_unique_words_2():
    """
    Get the dictionary of unique words and their frequency
    :return: dict
    """
    unique_words_2 = {}

    with open(local_name) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            # get the words:
            for word in line.split():
                unique_words_2[word] = unique_words_2.get(word, 0) + 1

    return unique_words_2



save_locally()
unique_words_number = len(get_unique_words())
unique_words_number2 = len(get_unique_words_2())

print(f"Pride and Prejudice has {unique_words_number} unique words.")
print(f"Alice in Wonderland has {unique_words_number2} unique words.")



file = open(local_name, 'r')
data = file.read()
totalword = data.split()
pptotalword = len(totalword)

file_2 = open(local_name_2, 'r')
data_2 = file_2.read()
totalword_2 = data_2.split()
awtotalword = len(totalword)

print(f"By dividing the total words of Pride and Prejudice and dividing by unique words we get:{int(pptotalword / unique_words_number)}")

print(f"By dividing the total words of Alice in Wonderland and dividing by unique words we get:{int(awtotalword / unique_words_number2)}")

print(f" Therefore the author of Alice in Wonderland has a wider vocabulary than the author of Pride and Prejudice")

            

unique_words7 = []
unique_words7_2 = []

for word in get_unique_words:
    if len(word) >= 7:
        unique_words7.append(word)


for word in get_unique_words_2:
    if len(word) >= 7:
        unique_words7_2.append(word)


print(f"Pride and Prejudice has {unique_words7} unique words longer than 7 characters")
print(f"Alice in Wonderland has {unique_words7_2} unique words longer than 7 characters")

#was not able to find a way to do the 7 character question since the function is not iterable.
        





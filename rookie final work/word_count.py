
def word_count(file):
    counts = dict()
    words = file.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    print('This text contains ' ,len(counts) ,'words. Below you can see frequency of each word in the file: ')
    print(counts)

# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# input
sentence = input ("Enter a sentence: " + underline.start)
print (underline.end, end = '')

# process
sentence = sentence.rstrip ('.')


# output
print ("First word: " + sentence.split (' ')[0])
print ("Last word: " + sentence.split (' ')[-1])


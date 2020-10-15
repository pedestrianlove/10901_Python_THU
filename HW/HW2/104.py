# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# input
name = input ("Enter a 3-part name: " + underline.start)
print (underline.end, end = '')


# output
print ("Middle name: " + name.split (' ')[1])

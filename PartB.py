from sys import argv
import re


# tokenize each line
# Runtime Complexity: O(N)
def tokenLine(line):
    line = line.lower().strip()                     #O(1)
    line_regex = re.sub('[^a-zA-Z0-9]', ' ', line)  #O(N)
    tokens = re.split('\s+', line_regex)            #O(N)
    tk = []
    for i in range(len(tokens)):                    #O(N)
        tokens[i] = tokens[i].strip()               #O(1)
        if len(tokens[i]) > 0:                      #O(1)
            tk.append(tokens[i])                    #O(1)
    return tk
                                                    #O(1)+O(N)+O(N)+O(N)+O(1)+O(1)+O(1) = O(N)
# updates the dictionary
# key: word
# value: number of appearances
# Runtime Complexity:   O(N)
def updateDictCount(tkLine, dict_count):
    for word in tkLine:             #O(N)
        if dict_count.get(word):    #O(1)
            dict_count[word] += 1   #O(1)
        else:                       #O(1)
            dict_count[word] = 1    #O(1)
    return dict_count
                                    # O(N)+O(1)+O(1)+O(1)+O(1)=O(N)

#processing the line(tokenizing and updating frequencies)
#Runtime Complexity: O(N)
def processLine(line, dict_counts, open_file):
    while line:                                 #O(N)
        tks = tokenLine(line)                   #O(N)
        updateDictCount(tks, dict_counts)       #O(N)
        line = open_file.readline()             #O(N)
                                                #O(N)+O(N)+O(N)+O(N)=O(N)

# finds the common words between the two dictionaries
# Runtime Complexity: #O(N)
def findCommonWords(dict_counts, dict_counts2, common_words):
    for word in dict_counts:                #O(N)
        if dict_counts2.get(word):          #O(1)
            common_words.append(word)       #O(1)
                                            #O(N)+O(1) +O(1)= O(N)

#main function of the program
#Runtime Complexity: O(N)
#It runs in linear time relative to the size of the input
def main():
    try:
        script, filename, filename2 = argv                          #O(1)
        open_file = open(filename, encoding='utf8')                 #O(1)
        open_file2 = open(filename2, encoding='utf8')               #O(1)

        line = open_file.readline()                                 #O(N)
        dict_counts = {}                                            #O(1)
        processLine(line, dict_counts, open_file)                   #O(N)


        line2 = open_file2.readline()                               #O(N)
        dict_counts2 = {}                                           #O(1)
        processLine(line2, dict_counts2, open_file2)                #O(N)

        common_words = []                                           #O(1)
        findCommonWords(dict_counts, dict_counts2, common_words)    #O(N)
        print(len(common_words), end = "")                          #O(1)
    except ValueError:
        print("Wrong number of files entered!")                                                             #O(1)
    except FileNotFoundError:
        print("Please enter a file in the current directory!")                                              #O(1)

if __name__ == "__main__":
    main()
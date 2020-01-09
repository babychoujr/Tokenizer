from sys import argv
import sys
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
                                                    #Sum: O(N)
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
                                    #O(N)+O(1)+O(1)+O(1)+O(1)=O(N)
# prints the sortedDict
# Runtime Complexity: O(N)
def printSortedDict(sorted_dictFile):
    count = 0                                       #O(1)
    for key, value in sorted_dictFile:              #O(N)
        if count != 0:                              #O(1)
            print()                                 #O(1)
        print(key + '\t' + value)                   #O(1)
        count += 1
                                            #O(1) + O(N) + O(1) +O(1)+O(1) = O(N)

#main function of the program
# Runtime Complexity: O(NLogN)
# It runs in linear time relative to the size of the input
def main():
    try:
        script, filename = argv                                                                                 #O(1)
        open_file = ''                                                                                          #O(1)
        open_file = open(filename, encoding='utf8')                                                         #O(1)
        line = open_file.readline()                                                                         #O(N)
        dict_counts = {}                                                                                    #O(1)
        while line:                                                                                         #O(N)
            tks = tokenLine(line)                                                                           #O(N)
            updateDictCount(tks, dict_counts)                                                               #O(N)
            line = open_file.readline()                                                                     #O(N)
        sorted_dict_counts = sorted(dict_counts.items(), key = lambda k: (-k[1], k[0]))                     #O(NLogN)
        printSortedDict(sorted_dict_counts)                                                                 #O(N)
    except ValueError:
        print("Wrong number of files entered!")                                                             #O(1)
    except FileNotFoundError:
        print("Please enter a file in the current directory!")                                              #O(1)

if __name__ == "__main__":
    main()
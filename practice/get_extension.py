def get_extension(filename):
    file_list = list(filename)
    if "." not in file_list:
        print "null"
    else:
        for i in range(len(file_list)):
            if "." == file_list[i]:
                print "".join(file_list[i+1:])

get_extension(raw_input())


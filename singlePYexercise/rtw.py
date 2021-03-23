import sys
if __name__ == "__main__":
    max_entries = 8
    input_stuff = ["E:\\as\tdb\\asdg\ddf\\fff.c 12903","E:\\asdb\\asdg\ddff\\f.c 12903","E:\\sdb\Asdg\dd\Efff.c 12903", \
                   "19451049  123"]
    record = ' '.join(''.join("E:\\as\tdb\\asdg\ddf\\fff.c 12903".split('\\')[-1]).split())
    print(record)

    result = {}
    for line in input_stuff:
        file_name = (r''+line.split(" ")[0]).split("\\")[-1]
        line_number = (r''+line.split(" ")[-1]).split('\n')[0]
        if len(file_name) > 16:
            file_name = file_name[-16:]
        if (file_name,line_number) not in result:
            result[(file_name,line_number)] = 1
            max_entries = max_entries - 1
        else:
            result[(file_name, line_number)] += 1


    for key in result.keys():
        print(key[0],key[1],result[key])


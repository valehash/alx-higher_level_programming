#!/usr/bin/python3

if __name__ == "__main__":
    import sys,json

    save_file = __import__('5-save_to_json_file').save_to_json_file
    load_file = __import__('6-load_from_json_file').load_from_json_file
    
    args =  sys.argv[1:]
    file_name = 'add_item.json'
    my_list =[]
    
    for i in len(args):
        my_list.append(argv[i])
        i +=1
        
    save_file(my_list, file_name) 

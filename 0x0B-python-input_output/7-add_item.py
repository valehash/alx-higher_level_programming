#!/usr/bin/python3

if __name__ == "__main__":
    import sys,json

    save_file = __import__('5-save_to_json_file').save_to_json_file
    load_file = __import__('6-load_from_json_file').load_from_json_file
    
    args =  sys.argv[1:]
    file_name = 'add_item.json'
    my_list =[]
    
    for i in args:
        my_list.append(i)
        break
    save_file(my_list,file_name)
    
    new_list = load_file(file_name)

    new_list = new_list + my_list

    save_file(new_list,file_name)

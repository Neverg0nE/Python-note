def print_file_info(file_name):
    """
    read file by giving path
    :param file_name: the path of file
    :return: None
    """
    f=None
    try:
        f=open(file_name,'r',encoding='UTF-8')
        print(f.read())
    except Exception as e:
        print(f'error appear!!!{e}')
    finally:
        if f:                #if f=None,representing an error;if there is any content in f,meaning true
            f.close()

def append_to_file(file_name,data):
    """
    append
    :param file_name: the path of file
    :param data: the appended content
    :return: None
    """
    f = open(file_name, 'a', encoding='UTF-8')
    f.write(data)
    f.write('\n')
    f.close()

if __name__ == '__main__':
    print_file_info('D:/临时安装包/4399.txt')      #D:/临时安装包/4399.txt
    # append_to_file()
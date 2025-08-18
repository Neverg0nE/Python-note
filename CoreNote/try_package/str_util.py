def str_reverse(s):
    """
    this function is aim to reverse the string
    :param s: the string that will be reversed
    :return: the direction changing string
    """
    return s[::-1]
def substr(s,x,y):
    """
    this func slices the string based on x and y
    :param s: the string that will be sliced
    :param x: the start index in slice
    :param y: the end index in slice
    :return:  the sliced string
    """
    return s[x:y]

if __name__ == '__main__':
   print(substr('woada',1,4))
   print(str_reverse('aslkdjlawkdjla'))

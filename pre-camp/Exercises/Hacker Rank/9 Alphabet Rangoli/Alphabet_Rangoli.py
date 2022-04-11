import string
def print_rangoli(size):
    if size == 1:
        print("a")
        return
    alphabet = list(string.ascii_lowercase)
    rev_al = list(string.ascii_lowercase)
    rev_al.reverse()
    middle = "-".join(rev_al[-size:])+"-"+"-".join(alphabet[1:size])
    s = len(middle)
    widdle = middle
    for i in range(size-1, 0, -1):
        if i == size-1:
            print((2*i)*"-"+ middle[:size*2-(i*2)]+ middle[(size*2)+(i*2):] + (2*i-1)*"-")
            continue
        print((2*i)*"-"+ middle[:size*2-(i*2)]+ middle[(size*2)+(i*2):] + (2*i)*"-")
    print(middle)
    for i in range(1, size):
        if i == size-1:
            print((2*i)*"-" + widdle[:size*2-(i*2)] + widdle[(size*2)+(i*2):] +((2*i)-1)*"-")
            break
        print((2*i)*"-" + widdle[:size*2-(i*2)] + widdle[(size*2)+(i*2):] +(2*i)*"-")
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

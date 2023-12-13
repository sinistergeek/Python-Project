one_digit_words = {
        '0':["zero"],
        '1':["one"],
        '2':["two","twen"],
        '3':["three","thir"],
        '4':["four","for"],
        '5':["five","fif"],
        '6':["six"],
        '7':["seven"],
        '8':["eight"],
        '9':["nine"]
        }

two_digit_words = ["ten","eleven","twelve"]
hundred = "hundred"
large_sum_words = ["thousand","million","billion","trillion","quadrillion","quintillion","sextillion","septillion","octillion","nonillion"]


def converter(n):
    word = []
    if n.startswith('-'):
        word.append("(negative)")
        n = n[1:]

    if len(n) % 3 != 0 and len(n) > 3:
        n = n.zfill(3*(((len(n)-1)//3)+1))


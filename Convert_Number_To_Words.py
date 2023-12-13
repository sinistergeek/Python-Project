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
        sum_list =[n[i:i + 3] for i in range(0,len(n),3)]
        skip = False

        for i,num in enumerate(sum_list):
            if num != '000':skip=False
            for _ in range(len(num)):
                if(len(sum_list) > 1 or (len(sum_list) == 1 and len(sum_list[0])==3)) and i == len(sum_list) -1 and (word[-1] in large_sum_words or hundred in large_sum_words or hundred in word[-1]):
                    word.append("and")
                word.append(one_digit_words[num][0])
                num = num[1:]
                break
            if len(num) == 2:
                if nump[0] != '0':
                    if(len(sum_list) > 1 or (len(sum_list) ==1 and len(sum_list[0]) == 3)) and i == len(sum_list) - 1:
                        word.append("and")
                    if num.startswith('1'):
                        if int(num[1]) in range(3):
                            word.append(two_digit_words[int(num[1])])
                        else:
                            number = one_digit_words[num[1][1 if int(num[1]) in range(3,6,2) else 0]]
                            word.append(number +("teen" if not number[-1] == "t" else "een"))

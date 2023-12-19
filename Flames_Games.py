from tkinter import *
def clear_all():
    Player1_field.delete(0,END)
    Player2_field.delete(0,END)
    Status_field.delete(0,END)
    Player1_field.focus_set()

def tell_status():
    p1 = Player1_field.get()
    p2 = Player2_field.get()
    p1 = p1.replace("","")
    p2 = p2.replace("","")
    p1 = list(p1)
    p1 = list(p2)
    Status.field.insert(10,result_flame(p1,p2))

def result_flame(x,y):
    for i in x[:]:
        if i in y:
            x.remove(i)
            y.remove(i)
    count = len(x) + len(y)
    result = ["Friends","Love","Affection","Marriage","Enemy","Siblings"]
    while len(result) > 1:
        split_index = (count % len(result) - 1)
        if(split_index >= 0):
            right = result[split_index + 1:]
            left =result[:split_index]
            result = right + left
        else:
            result = result[:len(result) -1]

    return result

if __name__ == "__main__":


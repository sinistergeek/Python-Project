import tabula
import os
print("[-+-] striing pdf_csv.py..")
print("[-+-] import a pdf and convert it to a csv")

print("[-+-] importing required packages for pdf_csv.py..")
print("[-+-] pdf_csv.py package imported \n")

def pdf_csv():
    print("[-+-] default filenames: ")
    filename = "sample1"
    pdf = filename + ".pdf"
    csv = filename + ".csv"
    print(pdf)
    print(csv + "\n")

    print("[-+-] default directory:")
    print("[-+-] (based on current working direcotry of python file)")
    defaultdir = os.getcwd()
    print(defaultdir +"\n")

    print("[-+-] default file paths.")
    pdf_path = os.path.join(defaultdir,pdf)
    csv_path = os.path.join(defaultdir,csv)
    print(pdf_path)
    print(csv_path + "\n")
    if os.path.exists(pdf_path) == True:
        print("[-+-] pdf found: " + pdf + "\n")
        pdf_flag = True
    else:
        print("[-+-] looking for another pdf...")


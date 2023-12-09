import ezgmail
def attachmentdownload(resultthreads):
    countofresults = len(resulthreads)
    try:
        for i in range(countofresults):
            if len(resulthreads[i].messages) > 1:
                for j in range(countofresults):
                    resulthreads[i].messages[j].downloadAllAttachments()

            else:
                resulthreads[i].messages[0].downloadAllAttachments()
        print("Download compelete.Please check your root directory.")


    except:
        raise Exception("Error occured while downloading attachment(s).")

if __name__ == '__main__':
    query = input("Enter search query: ")
    newquery = query + "+ has:attachment"
    resulthreads = ezgmail.search(newquery)
    if len(resulthreads) == 0:
        print("Result has no attachments:")
    else:
        print("Result(s) with attachments:")
        for threads in resulthreads:
            print(f"Email Subject: {threads.messages[0].subject}")
        try:
            ask = input("Do you want to download attachments(s) in result(s) (Yes/No)?")
            if ask == "Yes":
                attachmentdownload(resulthreads)
            else:
                print("Program exited")

        except:
            print("Something went wrong")



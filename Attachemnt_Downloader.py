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


import threading
import sys
import queue
class FileOperations:
    def fileLinesWordsCount(self,filename):
        try:
            with open(filename,"r") as f:
                linecount=0   
                wordcount = 0
                #reading each line
                for line in f:
                    #spliting the current line into list of words
                    words  = line.split()
                    linecount += 1
                    wordcount += len(words)
            #adding the result into the queue
            q.put([filename,linecount,wordcount])
        except IOError:
            print ("%s doesn't exist or error while processing the file\n"%filename)

if __name__ == "__main__":
    try:
        #Queue to store the result
        q = queue.Queue()
        #list to store the threads 
        list1=[]
        #creating object of class FileOperation to access fileLinesWordsCount method
        obj1 = FileOperations()
        #creating thread and appending to list
        for filename in sys.argv[1:]:
            list1.append(threading.Thread(target=obj1.fileLinesWordsCount, args=(filename,)))
        #starting the thread
        for t in list1:
            t.start()
        #invoking join method
        for t in list1:
             t.join()
        #reading queue and printing the result
        while not q.empty():
            for i in q.get():
                print (i, "\t",end=" "),
            print ("\n")
    except Exception as e:
        print (e)

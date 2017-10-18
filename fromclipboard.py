import messagebox
import meaning
def getcontent():
    ''' filed=open('dictionary.txt',"a")
    #print(filed)
    counting=open('count.txt',"r")
    print(counting)
    s=counting.read()
    counting.close()
    count=int(s)
    print(count)
    print('----------')'''
    import tkinter as tk
    root = tk.Tk()
    root.withdraw()
    prev='@'
    while(True):
      c = root.clipboard_get()
      if c !=prev:
        #count+=1
        #counting=open('count.txt',"w")
        #counting.write(str(count))
        prev=c
        print(c)
        text=meaning.func(c)
        print(text)
        #if(text!="Sorry"):
         #filed.write(text)
         #filed.write('\n#\n')
        messagebox.display(text)
if __name__== "__main__":
    getcontent()

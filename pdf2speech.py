import slate,subprocess,pyttsx
loc=raw_input('Enter location of pdf:')
with open(loc) as f:
        doc=slate.PDF(f)
choice=input("Speak(0)/Save(1):")
if choice==1:
        page=input('Enter number of to save in 1 file(0 for all):')
        if page==0:
                page=len(doc)
        i=0
        while i<len(doc):
                t=""
                for j in range(i,i+page):
                        if i+j>=len(doc):
                                break
                        t=t+doc[j-1]
                name=(str)(i)+" to "+(str)(i+page)
                i=i+page
                subprocess.call(["espeak", "-w"+name+".mp3", t])
else:
        page=input("Enter page number to speak:")
        t=doc[page-1]
        engine=pyttsx.init()
        engine.say(doc[page-1])
        engine.runAndWait()

import slate,subprocess
loc=raw_input('Enter location of pdf:')
with open(loc) as f:
    doc=slate.PDF(f)
page=input('Enter page number to save(in 1 file):')
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

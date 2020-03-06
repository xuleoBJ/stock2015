f = open('123\\123.txt')
fwrite=open('123\\É¾³ýÖØ¸´ÐÐ.txt','w')
fwrite.write('\n'.join(set([line.strip() for line in f])))
fwrite.close()

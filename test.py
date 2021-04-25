'''import glob
import os
os.chdir( "D:/DigLab/media/sujit/" )
for files in glob.glob( "*" ):
    f = open( files, 'rb' )
    print ( files )
    for line in f:
        if b"python" in line:
            print( f , line )
'''
import PyPDF2
import glob
import os
os.chdir( "D:/DigLab/media/" )


for ofile in glob.glob('*'):
    print ( ofile )
    os.chdir( "D:/DigLab/media/" + ofile + '/' )
    for file in glob.glob('*'):
        print ( file )
        print ('DEBUG: file=>{0}<'.format(file) )
        if '.pdf' in file : 
            pdfFileObj = open( file, 'rb')

            pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
            search_word = "matlab"
            search_word_count = 0
            for pageNum in range(1, pdfReader.numPages):
                pageObj = pdfReader.getPage(pageNum)
                text = pageObj.extractText().encode('utf-8')
                search_text = text.lower().split()
                for word in search_text:
                    if search_word in word.decode("utf-8"):
                        search_word_count += 1
                    
            print("The word {} was found {} times in {}".format(search_word, search_word_count, "D:/DigLab/media/" + ofile + '/' + file ))

        else:
            with open(file,'r') as f:
                contents = f.read()
                # print ( contents )
            if 'google' . lower ()  in contents . lower () :
                print("The word {} was found {} times in {} ".format('google', contents . count ('google'),"D:/DigLab/media/" + ofile + '/' + file ))



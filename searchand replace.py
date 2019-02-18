import os

texttosearch = 'VSPG200_redis'
texttoreplace = 'VSPG200'

sourcepath = os.listdir('/usr/local/megha/conf/probe/')

for file in sourcepath:
    inputfile = '/usr/local/megha/conf/probe/' + file
    print ('conversion is going on for file:'  +inputfile)
    with open (inputfile , 'r') as inputfile:
        filedata = inputfile.read()
        freq = 0
        freq = filedata.count(texttosearch)
    destinationpath = '/usr/local/megha/conf/probe/' + file
    filedata = filedata.replace(texttosearch,texttoreplace)
    with open (destinationpath, 'w') as file:
        file.write(filedata)
    print ('Total words replaced %d'  % freq)

~

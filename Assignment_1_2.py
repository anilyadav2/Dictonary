

encryption_key = { 'a':'!', 'b':'@', 'c':'#', 'd':'$', 'e':'%', 'f':'^', 'g':'&', 'h':'*', 'i':'(', 'j':')', 'k':'<', 
'l':'>', 'm':'?', 'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 
'w':'j', 'x':'k', 'y':'l', 'z':'m', 'A':'n', 'B':'o', 'C':'p', 'D':'q', 'E':'r', 'F':'s', 'G':'t', 
'H':'u', 'I':'v', 'J':'w', 'K':'x', 'L':'y', 'M':'z', 'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E',
 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M', '1':'N', '2':'O', '3':'P',
  '4':'Q', '5':'R', '6':'S', '7':'T', '8':'U', '9':'V', '0':'W'                 
                 }


f1 = open("encripted_file.txt", "w")

f = open("info_security.txt", "r")
for line in f:
    encrypted_txt=''
    for ch in line:
        if ch in encryption_key:
            encrypted_txt += str(encryption_key[ch])
        else:
            encrypted_txt += ch
    f1.write(encrypted_txt+'\n')

f1.close()
f.close()

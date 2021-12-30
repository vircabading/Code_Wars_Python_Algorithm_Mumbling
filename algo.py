#####################################################
#   Code Wars: MUMBLING
#####################################################

def accum(s):
    output = ""
    for letterIdx in range( len(s) ) :
        for idx in range( letterIdx+1 ) :
            ltr = s[letterIdx]
            if idx == 0 :
                output += ltr.upper();
            else:
                output += ltr.lower();
        if letterIdx != (len(s)-1) :
            output += "-"
    return output

print ("abcd:", accum("abcd"));
print ("RqaEzty:", accum("RqaEzty"));
print ("cwAt:", accum("cwAt"));
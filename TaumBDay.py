def taumBday(b, w, bc, wc, z):
    # Write your code here
    if(abs(bc-wc)>z):
        if(bc<wc):
            return b*bc+z*w+w*bc
        else:
            return w*wc+z*b+b*wc
    else:
        return b*bc+w*wc

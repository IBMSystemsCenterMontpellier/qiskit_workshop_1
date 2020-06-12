# PM Nov 2019 
from matplotlib.pyplot import imshow
import numpy as np
from IPython.display import Image, display, Markdown, Latex
# from PIL import Image
# convert a bitsring to the related card

def convert_to_card(val):
    color = int(val[3:], 2)
    sign = int(val[::-1][2:], 2)

    colors = ["clubs", "spades", "hearts", "diamonds"]
    signs = ["8", "7", "10", "9", "Queen", "King", "Ace", "Jack"]

    return signs[sign] + " of " + colors[color]
 
def convert_to_card_image(val):
    color = int(val[3:], 2)
    sign = int(val[::-1][2:], 2)

    colors = ["C", "S", "H", "D"]
    signs = ["8", "7", "10", "9", "Q", "K", "A", "J"]

    return signs[sign]  + colors[color]


def create_express(bitstr):
    V = exprvars('v', len(bitstr))
    index=int(bitstr,2)
    t=2**(len(bitstr))*['0']
    t[index]='1'
    string=''.join(t)
    f = truthtable(V,string )
    result=str(truthtable2expr(f))
    return result

def create_express2(bitstr):
    a=0
    t=[]
    for i in reversed(bitstr):
        if i=='1':
            t.append('v'+str(a))
        elif i=='0':
            t.append('~v'+str(a))
        else:
            print('ce n\'est pas un bitstring en base 2')
            return None
        a=a+1
    string='And('+','.join(t)+')'
    return string
    
# print(Dame)
# pil_im = Image.open('cards/PNG/QH.png', 'r')
def print_image(bitstring):
    name=convert_to_card_image(bitstring)
    pil_im = Image('cards/PNG/'+name+'.png',width=100,height=100)
    display(pil_im)
    
def decimalToBinary(x):
    result=(bin(x)[2:])
    return result

def binaryToDecimal(x):    
    return int(x,2) 

def vector2latex(vector, precision=5, pretext="", display_output=True):
    out_latex = "\n$$ " + pretext
    out_latex += "\\begin{bmatrix}\n"
    for amplitude in vector:
        amplitude = np.real_if_close(amplitude)
        amp_mod = np.mod(np.real(amplitude), 1)
        if (np.isclose(amp_mod, 0) or np.isclose(amp_mod, 1)) and type(amplitude) == np.ndarray:
            out_latex += str(int(np.round(amplitude))) + " \\\\\n"
        else:
            out_latex += '{:.{}f}'.format(amplitude, precision) + " \\\\\n"
    out_latex = out_latex[:-4] # remove trailing ampersands
    out_latex += "\end{bmatrix} $$"
    if display_output:
        display(Markdown(out_latex))
    else:
        return out_latex

def unitary2latex(unitary, precision=5, pretext="", display_output=True):
    out_latex = "\n$$ " + pretext
    out_latex += "\\begin{bmatrix}\n"
    for row in unitary:
        out_latex += "\t" # This makes the latex source more readable
        for amplitude in row:
            amplitude = np.real_if_close(amplitude)
            amp_mod = np.mod(np.real(amplitude), 1)
            if (np.isclose(amp_mod, 0) or np.isclose(amp_mod, 1)) and type(amplitude) == np.ndarray:
                out_latex += str(int(np.round(amplitude))) + " & "
            else:
                out_latex += '{:.{}f}'.format(amplitude, precision) + " & "
        out_latex = out_latex[:-2] # remove trailing ampersands
        out_latex += " \\\\\n"
    out_latex += "\end{bmatrix} $$"
    if display_output:
        display(Markdown(out_latex))
    else:
        return out_latex
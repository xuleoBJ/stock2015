# my favourite XML library
from xml.etree import ElementTree as et
 
# create an SVG XML element (see the SVG specification for attribute details)
doc = et.Element('svg', width='210mm', height='297mm', version='1.1', xmlns='http://www.w3.org/2000/svg')


case=1
#5x5
cd=15 
if case==5:
    for i in range(5): 
        for j in range(0,3*6):
            if j%6 != 0:
                et.SubElement(doc, 'rect', x=str(10+cd*i)+"mm", y=str(cd*j)+'mm', width=str(cd)+'mm', height=str(cd)+'mm', style="fill:none;stroke:black;stroke-width:1;" )
                et.SubElement(doc, 'rect', x=str(210/2+cd*i)+"mm", y=str(cd*j)+'mm', width=str(cd)+'mm', height=str(cd)+'mm', style="fill:none;stroke:black;stroke-width:1;" )
#4x4
cd=15 
if case==4:
    for i in range(4): 
        for j in range(0,3*5):
            if j%5 != 0:
                et.SubElement(doc, 'rect', x=str(10+cd*i)+"mm", y=str(cd*j)+'mm', width=str(cd)+'mm', height=str(cd)+'mm', style="fill:none;stroke:black;stroke-width:1;" )
                et.SubElement(doc, 'rect', x=str(210/2+cd*i)+"mm", y=str(cd*j)+'mm', width=str(cd)+'mm', height=str(cd)+'mm', style="fill:none;stroke:black;stroke-width:1;" )

#3x3
cd=15
if case==3:
    for i in range(3): 
        for j in range(0,4*4):
            if j%4 != 0:
                et.SubElement(doc, 'rect', x=str(10+cd*i)+"mm", y=str(cd*j)+'mm', width=str(cd)+'mm', height=str(cd)+'mm', style="fill:none;stroke:black;stroke-width:1;" )
                et.SubElement(doc, 'rect', x=str(210/3+cd*i)+"mm", y=str(cd*j)+'mm', width=str(cd)+'mm', height=str(cd)+'mm', style="fill:none;stroke:black;stroke-width:1;" )
                et.SubElement(doc, 'rect', x=str(210*2/3+cd*i)+"mm", y=str(cd*j)+'mm', width=str(cd)+'mm', height=str(cd)+'mm', style="fill:none;stroke:black;stroke-width:1;" )
intervalBlank=10
if case==1:
    _width=(210-intervalBlank*4)/3
    _height=(297-intervalBlank*5)/4
    for j in range(0,4):
        et.SubElement(doc, 'rect', x=str(intervalBlank)+"mm", y=str(intervalBlank+297*j/4)+'mm', width=str(_width)+'mm', height=str(_height)+'mm', \
                style="fill:none;stroke:black;stroke-width:1;" )
        et.SubElement(doc, 'rect', x=str(intervalBlank*2+_width)+"mm", y=str(intervalBlank+297*j/4)+'mm', width=str(_width)+'mm', height=str(_height)+'mm', \
                style="fill:none;stroke:black;stroke-width:1;" )
        et.SubElement(doc, 'rect', x=str(intervalBlank*3+_width*2)+"mm", y=str(intervalBlank+297*j/4)+'mm', width=str(_width)+'mm', height=str(_height)+'mm', \
                style="fill:none;stroke:black;stroke-width:1;" )
 
# ElementTree 1.2 doesn't write the SVG file header errata, so do that manually
f = open('sample.svg', 'w')
f.write('<?xml version=\"1.0\" standalone=\"no\"?>\n')
f.write('<!DOCTYPE svg PUBLIC \"-//W3C//DTD SVG 1.1//EN\"\n')
f.write('\"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd\">\n')
f.write(et.tostring(doc))
f.close()

import sys
import json
import yaml
import xmltodict
from tkinter import *
import tkinter as tk
from tkinter.filedialog import askopenfilename

def jsonParson(v, output, outputTarget):
    with open(v) as f:
        d = json.load(f)
        if output == "xml":
            xml = xmltodict.unparse(d)
            saveFile(xml, outputTarget)
        if output == "yaml":
            file = open(outputTarget, 'w')
            yaml.dump(d, file)
            file.close()
        if output == "yml":
            file = open(outputTarget, 'w')
            yaml.dump(d, file)
            file.close()

def yamlParson(v, output, outputTarget):
    with open(v) as stream:
        yml = yaml.safe_load(stream)
        if output == "json":
            file = open(outputTarget, 'w')
            json.dump(yml, file)
            file.close()
        if output == "xml":
            xml = xmltodict.unparse(yml)
            saveFile(xml, outputTarget) 

def xmlParson(v, output, outputTarget):
    with open(v) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        if output == "json":
            file = open(outputTarget, 'w')
            json.dump(data_dict, file)
            file.close()
        if output == "yaml":
            file = open(outputTarget, 'w')
            yaml.dump(data_dict, file)
            file.close()
        if output == "yml":
            file = open(outputTarget, 'w')
            yaml.dump(data_dict, file)
            file.close()
        
def saveFile(output, outputTarget):         
    file = open(outputTarget, 'w')
    file.write(output)
    file.close()
    
def validateParamse():
    args= sys.argv
    print(args[1])
    input = paramType(args[1])
    output = paramType(args[2])
    if input == "json":
        return jsonParson(args[1], output, args[2])
    if input == "xml":
        return xmlParson(args[1], output, args[2])
    if input == "yaml":
        return yamlParson(args[1], output, args[2])
    if input == "yml":
        return yamlParson(args[1], output, args[2])

def paramType(v):
    if "json" in v: 
        return "json"
    if "xml" in v: 
        return "xml"
    if "yaml" in v: 
        return "yaml"
    if "yml" in v: 
        return "yml"


# validateParamse()
 
root = Tk()
root.title(" file chooser")
root.geometry('350x200')
lbl = Label(root)
lbl.grid()
 
def clicked():
    Tk().withdraw()
    filename = askopenfilename()
    print(filename)
    btn.pack()

 
btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)

btn.grid(column=2, row=0)
name_var=tk.StringVar()
name_label = tk.Label(root, text = 'file name', font=('calibre',10, 'bold'))
name_label.grid(row=1,column=0)

name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
name_entry.grid(row=0,column=1)



root.mainloop()
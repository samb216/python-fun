import xml.etree.cElementTree as ET 
import numpy as np
import pandas as pd 
import datetime

headers= [['PAY','CHI','ELE'],['Call','Duration'],['HoldDate']]

data = [[1000,150,56.42],['Inbound',10],['23/11/2023']]

template_ID = [[3,1],[2,2],[1,1]]

actions = [['IandE',],['INC','OUT'],['ONH']]

# actions = ['IandE','INC','ONH']



Activity = ET.Element("Activity")
Info = ET.SubElement(Activity,"Information")
ET.SubElement(Info, "Date", name="DTS").text = str(datetime.datetime.now().strftime("%Y-%m-%d"))
ET.SubElement(Info,"Time", name = "TS").text = str(datetime.datetime.now().strftime("%H:%M:%S"))
ET.SubElement(Info,"DCA",name="DCA").text = 'BWLegal'

message = ET.SubElement(Activity, "Action")

for i,account in enumerate(actions):

    acct = ET.SubElement(message,"Acct")
    temp = template_ID[i]
    print(temp)
    for fields in range(0,temp[1]):
        print(fields)
        dummy = ET.SubElement(acct,account[fields])
        for amount in range(0,temp[0]):
            print(amount,"ammount")
            print(dummy)
            ET.SubElement(dummy,"test",name="test").text = "tester"
            # ET.SubElement(dummy, x, name=str(x)).text = str(data[i][j])



    # dummy = ET.SubElement(Activity, account)

    # for j,x in enumerate(headers[i]):
                
    #     ET.SubElement(dummy, x, name=str(x)).text = str(data[i][j])
        

tree = ET.ElementTree(Activity)
tree.write("filename.xml",encoding='utf-8',xml_declaration=True)
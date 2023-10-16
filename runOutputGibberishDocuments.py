import os
import sys
import pathlib
import random
from docx import Document
import datetime
import uuid

import pandas as pd
import numpy as np

#Reportlab to prepare the PDFs
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

#fake intellisense
from commonSeedDataTypes import commonSeedDataTypes as cSDY
from commonSeedDataTypes import commonCityDictValues as cCityFields

# our code
import libFakeData as fd

#make a semi unique batch name so there shouldn't be collisions 
#if we make multiple uploads of gibberish data.
batchName = str(uuid.uuid4())[:8]

def loadSeedData():
    global sdFirstNames
    global sdLastNames 
    global sdLastNames 
    global sdStreetNames 
    global sdCourseNames 
    global sdCompanyNames 
    global sdTextParts 
    global sdApplicationTypes
    global sdPurchaseObjects 
    global sdContractServices 
    global sdCityDictList 
    global sdCreditCards 
    
    sdFirstNames = fd.getSeedDataFromFile(cSDY.FirstNames)
    sdLastNames = fd.getSeedDataFromFile(cSDY.LastNames)
    sdLastNames = fd.getSeedDataFromFile(cSDY.LastNames)
    sdStreetNames = fd.getSeedDataFromFile(cSDY.StreetNames)
    sdCourseNames = fd.getSeedDataFromFile(cSDY.CourseNames)
    sdCompanyNames = fd.getSeedDataFromFile(cSDY.CompanyNames)
    sdTextParts = fd.getSeedDataFromFile(cSDY.TextParts)
    sdApplicationTypes = fd.getSeedDataFromFile(cSDY.ApplicationTypes)
    sdPurchaseObjects = fd.getSeedDataFromFile(cSDY.PurchaseObjects)
    sdContractServices = fd.getSeedDataFromFile(cSDY.ContractServices)
    sdCreditCards = fd.getSeedDataFromFile(cSDY.CreditCards)
    sdCityDictList = fd.getSeedDataCityList()
    

currentPath = os.path.dirname(os.path.abspath(__file__))
outPutPath = os.path.join(currentPath,"OutPut") 

if not os.path.exists(outPutPath):
    print("Output path does NOT exists ", outPutPath)
    os.mkdir(outPutPath)
else:
    print("Output path exists ", outPutPath)

def outputContracts(numberToPrint = 1):
    for sequence in range (0,numberToPrint):
        date = datetime.datetime.now()+datetime.timedelta(weeks= -1*random.choice(range(1,300,1)))
        year =  date.strftime("%Y")
        month = date.strftime("%b")
        batch = date.strftime("")
        documentName = f"C{year}-{month}.{sequence}B{batchName}.docx"
        #Contract 
        msDoc = Document()
        msDoc.add_heading(f"Contract {year}-{month}.{sequence}")
        company = fd.getRandomItemFromList(sdCompanyNames)
        paragraph = msDoc.add_paragraph(f"This is a contract between us and {company} for {fd.getRandomItemFromList(sdTextParts)}.")
        tableRowCount = 5
        table = msDoc.add_table(rows=tableRowCount, cols=4)
        #header row
        row_cells = table.rows[0].cells
        row_cells[0].text = "item"
        row_cells[1].text = "quantity"
        row_cells[2].text = "price"
        row_cells[3].text = "" 
        total = 0.00

        for i in range(1,tableRowCount-1):
            #add row
            row_cells = table.rows[i].cells
            row_cells[0].text = fd.getRandomItemFromList(sdPurchaseObjects)
            quantity = random.choice([2,10,12,42])
            row_cells[1].text = str(quantity)
            unitPrice = random.choice([1.00,3.00,7.00,4.20])
            row_cells[2].text = str(unitPrice) 
            rowPrice = unitPrice*quantity
            row_cells[3].text = str("{:.2f}".format(unitPrice*quantity))
            total = total + rowPrice

        table.rows[tableRowCount-1].cells[3].text = str("{:.2f}".format(total))

        for i in range(1,4):
            msDoc.add_paragraph(f"{fd.getRandomItemFromList(sdTextParts)}.")
        fileNameAndPath = os.path.join(outPutPath,documentName)
        msDoc.save(fileNameAndPath)
        #change the create and modify date 
        os.utime(fileNameAndPath, (date.timestamp(), date.timestamp()))

def outputApprovalLetter(sequence=0, applicationDate = datetime.datetime.now(), applicationType="", firstName="",lastName = ""):
    
    date = applicationDate+datetime.timedelta(days=random.choice(range(2,42,1)))
    year =  date.strftime("%Y")
    month = date.strftime("%b")
    batch = date.strftime("")
    documentName = f"LApproval{year}-{month}.{sequence}B{batchName}.docx"
    
    msDoc = Document()
    
    msDoc.add_paragraph(f"{firstName} {lastName}")
    city = fd.getRandomItemFromList(sdCityDictList)
    msDoc.add_paragraph(f"{random.choice(range(2000,3000,10))}, {fd.getRandomItemFromList(sdStreetNames)}")
    msDoc.add_paragraph(f"{city[cCityFields.CityName]}, {city[cCityFields.Province]}")
    msDoc.add_paragraph(f"{city[cCityFields.PostalCode]}")
    msDoc.add_paragraph(f"")
    msDoc.add_paragraph(f"Re: Approval {applicationType} application")
    msDoc.add_paragraph(f"")
    msDoc.add_paragraph(f"")
    tableRowCount = 5
    table = msDoc.add_table(rows=tableRowCount, cols=4)
    #header row
    row_cells = table.rows[0].cells
    row_cells[0].text = "item"
    row_cells[1].text = "quantity"
    row_cells[2].text = "price"
    row_cells[3].text = "" 
    total = 0.00

    for i in range(1,4):
        randomParagraph = ""
        for x in range(2,random.choice(range(3,6))):
            randomParagraph = randomParagraph + f"{fd.getRandomItemFromList(sdTextParts)}. "
        msDoc.add_paragraph(f"{randomParagraph}.")

    paragraph = msDoc.add_paragraph(f"")
    paragraph = msDoc.add_paragraph(f"")
    paragraph = msDoc.add_paragraph(f"Sincerely")
    paragraph = msDoc.add_paragraph(f"")
    paragraph = msDoc.add_paragraph(f"")
    paragraph = msDoc.add_paragraph(f"Admin Clerk {fd.getRandomAtoZ()}")
    paragraph = msDoc.add_paragraph(f"")
    
    fileNameAndPath = os.path.join(outPutPath,documentName)
    msDoc.save(fileNameAndPath)
    #change the create and modify date 
    os.utime(fileNameAndPath, (date.timestamp(), date.timestamp()))

def outputApplications(numberOfApplications = 1):

    for sequence in range(0,numberOfApplications):
        reportElements = []
        date = datetime.datetime.now()+datetime.timedelta(weeks= -1*random.choice(range(1,300,1)))
        year =  date.strftime("%Y")
        month = date.strftime("%b")
        reportName = f"A{year}-{month}.{sequence}B{batchName}.pdf"
        
        applicationType = fd.getRandomItemFromList(sdApplicationTypes)

        report = SimpleDocTemplate(os.path.join(outPutPath,f"{reportName}"))
        styles = getSampleStyleSheet()

        #title
        reportElements.append(Paragraph(f"Application: {applicationType}",styles["h1"]))
        #intro paragraph
        reportElements.append(Paragraph(f"{fd.getRandomItemFromList(sdTextParts)}.{fd.getRandomItemFromList(sdTextParts)}.{fd.getRandomItemFromList(sdTextParts)}.{fd.getRandomItemFromList(sdTextParts)}."))

        firstName = fd.getRandomItemFromList(sdFirstNames)
        lastName = fd.getRandomItemFromList(sdLastNames)
        table_data = [["First Name:",firstName]]
        table_data.append(["Last Name:",lastName])
        dob = datetime.datetime.now()+datetime.timedelta(days= -1*random.choice(range(365*18,365*99)))
        table_data.append(["Date of Birth:",dob.strftime("%Y %b %d")])

        #add a report image
        # attachment_path = "./images/sampleIcon.jpg"
        # attachment_filename = os.path.basename(attachment_path)
        # report_image = Image(attachment_path, width=1*inch,height=1*inch)
        # report_image.hAlign = "CENTER"
        
        report_table = Table (data=table_data)

        reportElements.append(Paragraph(f"Application Details",styles["h2"]))
        reportElements.append(report_table)

        if applicationType not in ["Housing",
                                "Learning Grant",
                                "Employment",
                                "Daycare Supplement",
                                "Rental Assistance"]:
            reportElements.append(Paragraph("Fee Collection",styles["h2"]))
            reportElements.append(Paragraph(f"Credit card: {fd.getRandomItemFromList(sdCreditCards)}"))
            reportElements.append(Paragraph(f"CVC: 12{fd.getRandom0to9Str}"))
            reportElements.append(Paragraph(f"Credit card: {fd.getRandomItemFromList(sdCreditCards)}"))
            reportElements.append(Paragraph(f"Amount: {str(random.choice(range(100,900,10)))}"))  
        
        else:
            reportElements.append(Paragraph("Conditions",styles["h2"])) 
            #build approval letter
        
        #report conclusion
        reportElements.append(Paragraph(f""))
        reportElements.append(Paragraph(f"{fd.getRandomItemFromList(sdTextParts)}.{fd.getRandomItemFromList(sdTextParts)}.{fd.getRandomItemFromList(sdTextParts)}.{fd.getRandomItemFromList(sdTextParts)}."))
        
        report.build(reportElements)
        os.utime(os.path.join(outPutPath,f"{reportName}"), (date.timestamp(), date.timestamp()))

        outputApprovalLetter(sequence=sequence,applicationDate=date, 
                                    applicationType=applicationType,firstName=firstName, lastName=lastName)
            
def outputReports():
    
    for application in sdApplicationTypes:
        reportName = f"rpt{application}B{batchName}.pdf"
        df = pd.DataFrame(columns = ["Year","Application Count"])
        for year in range (2000,datetime.datetime.now().year):
            df.loc[df.shape[0]] = [year,random.choice(range (200, 2000))]
        
        outputPathAndFileName = os.path.join(outPutPath,f"{reportName}.xls")
        df.to_excel(outputPathAndFileName,sheet_name=application, index=False)
        
if __name__ == '__main__':
    for file in os.listdir(outPutPath):
        fileAndPath = os.path.join(outPutPath,file)
        if os.path.isfile(fileAndPath):
            os.remove(fileAndPath)
    
    loadSeedData()
    outputContracts(20)
    outputApplications(20)
    outputReports()

    print("done")   
    
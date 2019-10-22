from cv2 import cv2
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import date
import pandas as pd

# Google Drive dependencies
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from subprocess import call
import os, sys, re, click


# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

# Modify the below variables according to your preference
# Enter valid paths from your own file system
# The input file contains names as a line seperated list
# Make sure this output directory already exists or else candidateficates won't actually be generated

input_txt_file = '/home/shub/devel/personal/version-beta/certificate_gen_script/requirements.txt'
template_file_path = '/home/shub/devel/personal/version-beta/images/certificate_template.jpg'
output_directory_path = '/home/shub/devel/personal/version-beta/certificate_gen_script/output/'

font_size = 3.8
font_color = (51,51,51)

# Test with different values for your particular Template
# This variables determine the exact position where your text will overlay on the template

# Y adjustment determines the px to position above the horizontal center of the template (may be positive or negative)
coordinate_y_adjustment = 4

# X adjustment determiens the px to position to the right of verticial center of the template (may be positive or negative)
coordinate_x_adjustment = 7

# w adjustment determiens the px to position to the right of verticial center of the template (may be positive or negative)
coordinate_w_adjustment = 361

# z adjustment determiens the px to position to the right of verticial center of the template (may be positive or negative) 
coordinate_z_adjustment = 1064

current_date = date.today

# The Brains
print('[Progress].....')

with open(input_txt_file) as input_list:
    
    content = input_list.read().splitlines()

    for line in content:

        candidate_name = line

        img = cv2.imread(template_file_path)

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = candidate_name

        textsize = cv2.getTextSize(text, font, font_size, 10)[0]
        text_x = (img.shape[1] - textsize[0]) / 2 + coordinate_x_adjustment
        text_y = (img.shape[0] + textsize[1]) / 2 - coordinate_y_adjustment
        text_x = int(text_x)
        text_y = int(text_y)
		
        cv2.putText(img, text, (text_x, text_y), font, font_size, font_color, 10)
        # cv2.putText(img, text, (text_w, text_z), font, font_size, font_color, 10)        
        candidate_path = output_directory_path + candidate_name + '.png'
        cv2.imwrite(candidate_path,img)

    cv2.destroyAllWindows()

# Introduction to google-sheets API
"""
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/shub/devel/personal/version-beta/certificate_gen_script/macro-dogfish-238009-6417513b1b38.json', scope)
sheet = gspread.authorize(credentials)
wks = sheet.open("Certificate_Registration (Responses)").sheet1

current_date = date.today()
name_of_org = wks.col_values(2)
email = wks.col_values(3)
name_of_person = wks.col_values(4)
gender = wks.col_values(5)
certification = wks.col_values(6)

# conversion from xlsx to csv
xlsx = pd.read_excel('', sheetname=0, index=0)
'''make necessary changes in the dataframe'''
with open('','w') as outfile:
    pd.to_string(outfile)
"""

# Google drive upload
print ("[ Making a google drive upload of output folder ]")
if click.confirm('Do you want to continue?', default=True):
    os.system("gdrive upload -r /home/shub/devel/personal/version-beta/certificate_gen_script/output")
else:
    pass

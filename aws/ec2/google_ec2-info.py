#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-

from oauth2client.service_account import ServiceAccountCredentials
import gspread

#scope = [‘https://spreadsheets.google.com/feeds’, ‘https://www.googleapis.com/auth/drive’]
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

# 'googlekey.json 자리에 다운받은 json 파일을 경로와 함께 적어주도록 한다.'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    '/Users/moontaekwon/access-key/moon-devops-2bfe856d7274.json', scope)

gc = gspread.authorize(credentials)
   	
# "TEST" 부분 대신 사용할 스프레드시트의 이름을 적어주도록 한다.
wks = gc.open("ec2-info").sheet1
# A1 칸에 "TEST" 라는 내용을 적는 코드
wks.update_acell('A1', "TEST")
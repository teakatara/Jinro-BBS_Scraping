import csv
from bs4 import BeautifulSoup

#filePath = "C:\Users\syouk\Desktop\高専授業用フォルダ\5年\プログラム設計法\werewolfBBS\"
filePath = "C:\\Users\\syouk\\Desktop\\高専授業用フォルダ\\5年\\プログラム設計法\\werewolfBBS\\100\\1day.csv"
saveFilePath = "C:\\Users\\syouk\\Desktop\\高専授業用フォルダ\\5年\\プログラム設計法\\1day_edited.csv"
complex = []

def talkTypeJudgment(soup):
    if(soup.find("div",class_="mes_say_body1") is not None):
        return "発言"
    if(soup.find("div",class_="mes_whisper_body1") is not None):
        return "人狼"
    if(soup.find("div",class_="mes_think_body1") is not None):
        return "呟き"
    if(soup.find("div",class_="mes_groan_body1") is not None):
        return "墓場"
    return "アナウンス"

with open(filePath, encoding="utf-8") as f:
    firstReadFlag = True
    complex = []
    for a in csv.reader(f):
        if(firstReadFlag):
            firstReadFlag = False
            a.extend(["type","content"])
        else:
            soup = BeautifulSoup(a[3],"html.parser")
            #会話内容
            print(soup.text)
            #会話の種類
            talkType = talkTypeJudgment(soup)
            print(talkType)
            a.extend([talkType,soup.text])

        #ここからCSVに保存するコードを書く
        complex.append(a)

print(*complex,sep="\n")

with open(saveFilePath,'w',encoding="utf-8") as file:
        writer = csv.writer(file,lineterminator="\n")
        writer.writerows(complex)

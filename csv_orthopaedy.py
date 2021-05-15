import csv
import glob
from bs4 import BeautifulSoup

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

#filePath = "C:\Users\syouk\Desktop\高専授業用フォルダ\5年\プログラム設計法\werewolfBBS\"
#filePath = "C:\\Users\\syouk\\Desktop\\高専授業用フォルダ\\5年\\プログラム設計法\\werewolfBBS\\100\\1day.csv"
#saveFilePath = "C:\\Users\\syouk\\Desktop\\高専授業用フォルダ\\5年\\プログラム設計法\\1day_edited.csv"

inputDirectoryPath = input()
#print(*inputFilePath,sep="\n")
filePaths = glob.glob(inputDirectoryPath + "\\**\\*")
#print(*filePaths,sep="\n")

for path in filePaths:
    complex = []
    with open(path, encoding="utf-8") as f:
        firstReadFlag = True
        for a in csv.reader(f):
            if(firstReadFlag):
                firstReadFlag = False
                a.extend(["type","content"])
            else:
                soup = BeautifulSoup(a[3],"html.parser")
                #会話内容
                #print(soup.text)
                #会話の種類
                talkType = talkTypeJudgment(soup)
                #print(talkType)
                a.extend([talkType,soup.text])

            complex.append(a)

    #print(*complex,sep="\n")

    #ここからCSVに保存するコードを書く
    with open(path,'w',encoding="utf-8") as file:
            writer = csv.writer(file,lineterminator="\n")
            writer.writerows(complex)

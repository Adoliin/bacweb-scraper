import os
import requests
import bs4
import sys
arguments = sys.argv

# -- GLOBAL VARIABLES --
optionList = [
    'Allemand',
    'Espagnol',
    'Russe',
    'chinois',
    'Turque',
    'Italien',
    'Ã\x89ducation Musicale',
    'Arts & Plastiques',
    'ThÃ©Ã¢tre'
    ]

def main():
    global projectDir
    projectDir = initDir()
    mainPageSource = requests.get('http://www.bacweb.tn/section.htm')
    soup = bs4.BeautifulSoup(mainPageSource.text, 'lxml')
    subjectList = soup.find_all('tbody')[0].find_all('tr')
    sectionNum = menu()
    if sectionNum == 8:
        for i in range(7):
            getSection(subjectList, i+1)
    else:
        getSection(subjectList, sectionNum)

def menu():
    print('Chose section(s) to download:')
    print('[1] Math')
    print('[2] Science')
    print('[3] Economie')
    print('[4] Technique')
    print('[5] Lettres')
    print('[6] Sport')
    print('[7] Info')
    print('[8] ALL')
    while True:
        ans = input('--> ')
        if ans in ['1', '2', '3', '4', '5', '6', '7', '8']:
            return int(ans)
        else:
            print('You must pick a number from the menu!')
            continue


def initDir():
    #create bac folder if it dosent exist and chdir into it
    if os.path.exists('bac') == False :
        os.makedirs('bac')
    projectDir = os.path.join(os.getcwd(), 'bac')
    os.chdir(projectDir)
    return projectDir + '/'

def getSection(subjectList, sectionNum):
    for subject in subjectList:
        sectionList = subject.find_all('td')
        try:
            subjectName = sectionList[0].text
        except:
            pass
        else:
            sectionSubject = sectionList[sectionNum].select('a')
            if len(sectionSubject) != 0:
                linkToSubject = 'http://www.bacweb.tn/'+sectionSubject[0]['href']
                if subjectName in optionList:
                    # print('OPTION : '+subjectName)
                    pass
                else:
                    getSubject(linkToSubject, subjectName)

def getSubject(linkToSubject, subjectName):
    print(subjectName)
    subjectPageSource = requests.get(linkToSubject)
    soup = bs4.BeautifulSoup(subjectPageSource.text, 'lxml')
    yearsList = soup.find_all('tr')
    for year in yearsList:
        subjectsByYear = year.find_all('td')
        try:
            yearNumber = int(subjectsByYear[0].text)
        except:
            pass
        else:
            getYear(yearNumber, subjectsByYear)

def getYear(yearNumber, subjectsByYear):
    yearNumberDir = str(yearNumber) + '/'
    if os.path.exists(projectDir+yearNumberDir) == False :
        os.makedirs(projectDir+yearNumberDir)

    os.chdir(projectDir+yearNumberDir)
    if os.path.exists(projectDir+yearNumberDir+'principale') == False :
        os.makedirs(projectDir+yearNumberDir+'principale')
    if os.path.exists(projectDir+yearNumberDir+'controle') == False :
        os.makedirs(projectDir+yearNumberDir+'controle')

    principale_sujet  = subjectsByYear[1].find_all('a')
    getSujet(principale_sujet, yearNumberDir, 'principale')

    principale_corrige = subjectsByYear[2].find_all('a')
    getSujet(principale_corrige, yearNumberDir, 'principale')

    controle_sujet = subjectsByYear[3].find_all('a')
    getSujet(controle_sujet, yearNumberDir, 'controle')

    controle_corrige = subjectsByYear[4].find_all('a')
    getSujet(controle_corrige, yearNumberDir, 'controle')

    os.chdir(projectDir)

def getSujet(sujet, yearNumberDir, promotion):
    if len(sujet) != 0:
        sujetLink = 'http://www.bacweb.tn/'+sujet[0]['href']
        p = sujetLink.rindex('/')
        sujetName = sujetLink[p+1:]
        os.chdir(projectDir+yearNumberDir+promotion)
        currentDir = os.getcwd()+'/'
        if os.path.exists(currentDir+sujetName) == False:
            os.system(f'wget -O "{sujetLink}" &> /dev/null')
        os.chdir(projectDir)

if __name__ == '__main__':
    main()

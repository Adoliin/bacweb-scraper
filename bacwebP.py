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
sections_g = [
    'math',
    'science',
    'economie',
    'technique',
    'lettres',
    'sport',
    'info',
]
bacDir = os.path.join(os.getcwd(),'bac')

def main():
    sectionNum = menu()
    subjectList = getSubjectList()
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

def getSubjectList():
    mainPageSource = requests.get('http://www.bacweb.tn/section.htm')
    soup = bs4.BeautifulSoup(mainPageSource.text, 'lxml')
    return soup.find_all('tbody')[0].find_all('tr')

def getProjectDir(section):
    #create bac folder if it dosent exist and chdir into it
    projectDir = os.path.join(bacDir, f'bac-{section}')
    if os.path.exists(projectDir) == False :
        os.makedirs(projectDir)
    os.chdir(projectDir)
    return projectDir

def getSection(subjectList, sectionNum):
    sectionName = sections_g[sectionNum-1]
    global projectDir
    projectDir = getProjectDir(sectionName)
    print(f'\n~~~Downloading "{sectionName}" section:~~~')
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
    print(f'Downloading all of "{subjectName}" exams of current section.')
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
    yearNumberDir = os.path.join(projectDir, str(yearNumber))
    if os.path.exists(yearNumberDir) == False :
        os.makedirs(yearNumberDir)
    os.chdir(yearNumberDir)

    sessionDir_P = os.path.join(yearNumberDir, 'principale')
    if os.path.exists(sessionDir_P) == False :
        os.makedirs(sessionDir_P)

    sessionDir_C = os.path.join(yearNumberDir, 'controle')
    if os.path.exists(sessionDir_C) == False :
        os.makedirs(sessionDir_C)

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
        promotionDir = os.path.join(yearNumberDir, promotion)
        os.chdir(promotionDir)
        sujetDir = os.path.join(promotionDir, sujetName)
        if os.path.exists(sujetDir) == False:
            os.system(f'wget "{sujetLink}" &> /dev/null')
        os.chdir(projectDir)

if __name__ == '__main__':
    main()

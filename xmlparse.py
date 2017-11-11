import xml.etree.ElementTree as ET
import sqlite3 as DB

tree = ET.parse('one_basicold.xml')

root = tree.getroot()

class Book(object):
    def __init__(self,id,name):
        self.id = id
        self.name = name

class Verse(object):
    def __init__(self,book_id,chapter,verse,text):
        self.book_id = book_id
        self.chapter = chapter
        self.verse = verse
        self.text = text

conn = DB.connect('bibledb.sqlite')
c = conn.cursor()

i = 0
for book in root.iter('book'):
    i = i+1
    name = book.get('name')
    b = Book(i,name)
    #print(b.id,b.name)
    print('Insertando libro: ' + b.name)
    

    for chapter in book.iter('chapter'):
        #rank = item.find('rank').text
        chnumber = chapter.get('number')
        #print('Capitulo: ' + chnumber)
        for v in chapter.iter('verse'):
            verse = Verse(b.id,chnumber,v.get('number'),v.text)
            sql = "INSERT INTO Versos (BookId,ChapterNo,VerseNo,Texto) VALUES (" + str(verse.book_id) + "," + str(verse.chapter) + ","+ str(verse.verse) +",'"+ verse.text.replace("'","") +"')"
            #print(sql)
            c.execute(sql)
            #conn.commit()
            
            #print(verse.verse,verse.text)
    sql = "INSERT INTO Books (Nombre,CantCapitulos) VALUES ('" + b.name + "',"+ str(chnumber) +")"
    c.execute(sql)
    #print(sql)
    conn.commit()

conn.close()

from ast import ExtSlice
from sqlite3.dbapi2 import Cursor, connect
import sys
from PyQt5.QtCore import QDateTime 
from PyQt5.QtWidgets import * 
from tab_wigdet_python import * 
import sqlite3

app = QApplication(sys.argv)
pen_ana = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pen_ana)

pen_ana.show()


#------------------------ Sayfa Aktifleştirme----------------------#



ui.tabWidget.setTabEnabled(3,False)
ui.tabWidget.setTabEnabled(2,False)
ui.tabWidget.setTabEnabled(1,False)
ui.tabWidget.setCurrentIndex(0)

sys_kullanıcı ="benferhat_clk"
sys_parola  ="Miranbahoz"


def sayfa_aktifleştir ():
    if (ui.lne_giris.text().lower()== sys_kullanıcı) and (ui.lne_parola.text()== sys_parola): 
            ui.tabWidget.setTabEnabled(1,True)
            ui.tabWidget.setTabEnabled(2,True)
            ui.tabWidget.setTabEnabled(3,True)
            ui.tabWidget.setTabEnabled(0,False)
            
            
    else:
        QMessageBox.critical(pen_ana,"Dikat Giriş Başarısız!","Kullanıncı Adı veya Parola Hatalı")






#---------------------------Veri Tabanı Bağlantısı-----------------$
con = sqlite3.connect("database.db")
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Kitap(ID INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT,\
                kitap_adı TEXT NOT NULL UNIQUE, \
                yazar TEXT NOT NULL, \
                yazın_evi TEXT,\
                sayfa_sayısı TEXT,\
                raf TEXT )")
con.commit()

#-----------------------Kitaplar Menüsne Git-----------#
def pbt_kitaplara_git ():
        ui.tabWidget.setCurrentIndex(1)

#------------------------------Kitap Ekle--------------------#

def kitap_ekle ():
        if ui.lne_kitap_adi.text() == "":
                ui.statusbar.showMessage("Lütfen kitap adını giriniz.")
        elif ui.lne_yazar.text() == "":
                ui.statusbar.showMessage("Lütfen Yazarı Girniz")
        

        else:
                _lne_kitap_adi =ui.lne_kitap_adi.text().upper()
                _lne_yazar=ui.lne_yazar.text().upper()
                _lne_yayin_evi=ui.lne_yayin_evi.text().upper() 
                _spb_kitap_sayfasi=ui.spb_kitap_sayfasi.value()
                _lne_raf = ui.lne_raf.text()

                cursor.execute("INSERT INTO kitap\
                        (kitap_adı,yazar,yazın_evi,sayfa_sayısı,raf)\
                        VALUES(?,?,?,?,?)",\
                        (_lne_kitap_adi,_lne_yazar,_lne_yayin_evi,_spb_kitap_sayfasi,_lne_raf))
                con.commit()
                


                QMessageBox.information(pen_ana,"KAYIT EDİLDİ. ","ITKayıt Başarıyla Gerçekleşti")
                listele()
                pbt_kitaplara_git()
#----------------------------Listele-------------------------#
def listele ():
        ui.tablw_Kitap_listesi.setHorizontalHeaderLabels((
        "NO","KİTAP ADI","YAZAR","YAYIN EVİ","SAYFA SAYISI","RAF"))

        ui.tablw_Kitap_listesi.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        cursor.execute("SELECT * FROM kitap")
        for satırIndeks, satırVeri in enumerate(cursor):
                for SutunIndex, StunVeri in enumerate(satırVeri):
                        ui.tablw_Kitap_listesi.setItem(satırIndeks,SutunIndex,QTableWidgetItem(str(StunVeri)))
        ui.lne_kitap_adi.clear()
        ui.lne_yazar.clear()
        ui.lne_kitap_adi.clear
        ui.lne_yayin_evi.clear()
        ui.spb_kitap_sayfasi.setValue(150)
        ui.lne_raf.clear()



#--------------------------------------------ARANA--------------------#
def arama_kitap ():
        arama1 = ui.lne_kitap.text().upper()
        arama2 = ui.lne_yazar_.text().upper()
        cursor.execute("SELECT * FROM kitap WHERE kitap_adı =? OR yazar=? OR (kitap_adı=? AND yazar=?) ",\
                        (arama1,arama2,arama1,arama2))
        con.commit()
        ui.tablw_Kitap_listesi.clear()
        for satırIndex, satırVeri in enumerate(cursor):
                for sutunIndex, sutunVeri in enumerate(satırVeri):
                        ui.tablw_Kitap_listesi.setItem(satırIndex,sutunIndex,QTableWidgetItem(str(sutunVeri)))

#------------------------Veri Tabanı Bağlantısı(Kullanıc)----------------#
con_kullanici  =sqlite3.connect("database_kullanici.db")
cursor_kullanici = con_kullanici.cursor()
cursor_kullanici.execute("CREATE TABLE IF NOT EXISTS kullanici(Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ad TEXT NOT NULL,\
                        soyad TEXT NOT NULL,\
                        sinif TEXT,\
                        gsm_no TEXT NOT NULL,\
                        kitap_adi TEXT,\
                        yazar TEXT,\
                        tarih TEXT,\
                        teslim TEXT)")
con_kullanici.commit()

#----------------------------------------Kullancı Ekle----------------#



def Kullanici_ekle ():
        if ui.lne_ad.text() =="":
                ui.statusbar.showMessage("Lütfen Ad Giriniz!",10000)
                ui.statusbar.setStyleSheet("color: rgb(255, 0, 0);")
        elif ui.lnek_soyad.text() =="":
                ui.statusbar.showMessage("Lütfen Soyadı Giriniz!",10000)
                ui.statusbar.setStyleSheet("color: rgb(255, 0, 0);")
        elif ui.lnek_gsm_no.text() =="":
                ui.statusbar.showMessage("Lütfen GSM NO Giriniz!",10000)
                ui.statusbar.setStyleSheet("color: rgb(255, 0, 0);")

        
        else:

                _lne_ad = ui.lne_ad.text().capitalize()
                _lne_soyad=ui.lnek_soyad.text().capitalize()
                _lne_sinif=ui.lnek_sinif.text().capitalize()
                _lne_gsm_no=ui.lnek_gsm_no.text().capitalize()
                _lne_k_kitap_adi=ui.lnek_kitap_ad.text().capitalize()
                _lne_kullanici_yazar=ui.lne_kullanci_yazar.text().capitalize()
                _calanderw =ui.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
                _cmb_teslim=ui.cmb_teslim.currentText()
                cursor_kullanici.execute("INSERT INTO kullanici( ad,soyad,sinif,gsm_no,kitap_adi,yazar,tarih,teslim)VALUES(?,?,?,?,?,?,?,?)",\
                                        (_lne_ad,_lne_soyad,_lne_sinif,_lne_gsm_no,_lne_k_kitap_adi,_lne_kullanici_yazar,_calanderw,_cmb_teslim))

                con_kullanici.commit()
                listele2()


        listele3()
        
#-----------------------------Kullacı Kitap Listele----------------#

def listele2 ():
        ui.tablw_Kitap_listesi_2.setHorizontalHeaderLabels((
        "KİTAP ADI ","YAZAR",))

        ui.tablw_Kitap_listesi_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        cursor.execute("SELECT  kitap_adı,yazar FROM kitap")
        for satırIndeks, satırVeri in enumerate(cursor):
                for SutunIndex, StunVeri in enumerate(satırVeri):
                        ui.tablw_Kitap_listesi_2.setItem(satırIndeks,SutunIndex,QTableWidgetItem(str(StunVeri)))

        ui.lne_ad.clear()
        ui.lnek_soyad.clear()
        ui.lnek_sinif.clear()
        ui.lnek_gsm_no.clear()
        ui.lnek_kitap_ad.clear()
        ui.lne_kullanci_yazar.clear()

#--------------------------Kullanıcı Listele-------------#

def listele3 ():
        ui.tablw_kullanicilar.setHorizontalHeaderLabels((
        "Sıra","AD","SOYAD","SINIF","GSM NO","ALDIĞI KİTAP","KİTABIN YAZARI","SON TESLİM TARİHİ","TESLİM DURUMU"))
        
        ui.tablw_kullanicilar.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        


        cursor_kullanici.execute("SELECT * FROM kullanici")
        for satırIndeks, satırVeri in enumerate(cursor_kullanici):
                for SutunIndex, StunVeri in enumerate(satırVeri):
                        ui.tablw_kullanicilar.setItem(satırIndeks,SutunIndex,QTableWidgetItem(str(StunVeri)))
        


#----------------------------Doldur-------------------------#
def doldur ():
        try:

                secili=ui.tablw_Kitap_listesi_2.selectedItems()
                ui.lnek_kitap_ad.setText(secili[0].text())
                ui.lne_kullanci_yazar.setText(secili[1].text())
        except Exception as hata :
                ui.statusbar.showMessage("")


#--------------------------Doldur 2 ------------------------#
def doldur2():
        try:
        
       
                secili = ui.tablw_kullanicilar.selectedItems()
                ui.lne_ad.setText(secili[1].text())
                ui.lnek_soyad.setText(secili[2].text())
                ui.lnek_sinif.setText(secili[3].text())
                ui.lnek_gsm_no.setText(secili [4].text())
                ui.lnek_kitap_ad.setText(secili[5].text())
                ui.lne_kullanci_yazar.setText(secili[6].text())
            
                yil=int(secili[7].text()[0:4])
                ay=int(secili[7].text()[5:7])
                gun=int(secili[7].text()[8:10])
                ui.calendarWidget.setSelectedDate(QtCore.QDate(yil,ay,gun))
                ui.cmb_teslim.setCurrentText(secili[7].text())
        except Exception as hata:
                ui.statusbar.showMessage("")
        
       
#-----------------Kulancı Bilgilerini Güncele-----------------#
def guncele ():  
        secili = ui.tablw_kullanicilar.selectedItems()
        _ıd =int(secili[0].text())        
        _lne_ad = ui.lne_ad.text()
        _lne_soyad=ui.lnek_soyad.text()
        _lne_sinif=ui.lnek_sinif.text()
        _lne_gsm_no=ui.lnek_gsm_no.text()
        _lne_k_kitap_adi=ui.lnek_kitap_ad.text()
        _lne_kullanici_yazar=ui.lne_kullanci_yazar.text()
        _calanderw =ui.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        _cmb_teslim=ui.cmb_teslim.currentText()
        cursor_kullanici.execute("UPDATE kullanici SET ad=?,\
                        soyad=?,sinif=?,gsm_no=?,kitap_adi=?,yazar=?,tarih=?,teslim=? WHERE ID=?",\
                        (_lne_ad,_lne_soyad,_lne_sinif,_lne_gsm_no,_lne_k_kitap_adi,_lne_kullanici_yazar,_calanderw,_cmb_teslim,_ıd))
        
        con_kullanici.commit()
        listele3()

#-----------------------------ARAMA-----------------------#
def arama ():
        arama1 =ui.lne_ad.text().capitalize()
        arama2 =ui.lnek_soyad.text().capitalize()
        arama3 =ui.calendarWidget.selectedDate().toString(QtCore.Qt.ISODate)
        cursor_kullanici.execute("SELECT * FROM kullanici WHERE ad=? OR soyad=? OR tarih=? OR (ad=? AND soyad=?)",\
                        (arama1,arama2,arama3,arama1,arama2))
        con_kullanici.commit()
        ui.tablw_kullanicilar.clear()
        for satırIndeks, satırVeri in enumerate(cursor_kullanici):
                for SutunIndex, StunVeri in enumerate(satırVeri):
                        ui.tablw_kullanicilar.setItem(satırIndeks,SutunIndex,QTableWidgetItem(str(StunVeri)))
        listele2()


listele()
listele2()
listele3()

        



#-----------------------------Sinyal Slot--------------------#

ui.pbt_giris.clicked.connect(sayfa_aktifleştir)
ui.pbt_kaydet.clicked.connect(kitap_ekle)
ui.pbt_kitaplara_git.clicked.connect(pbt_kitaplara_git)
ui.pbt_kul_kaydet.clicked.connect(Kullanici_ekle)
ui.tablw_Kitap_listesi_2.itemSelectionChanged.connect(doldur)
ui.tablw_kullanicilar.itemSelectionChanged.connect(doldur2)
ui.pbt_guncele.clicked.connect(guncele)
ui.pbt_ara.clicked.connect(arama)
ui.pbt_kitap_ara.clicked.connect(arama_kitap)
ui.pbt_listele.clicked.connect(listele)

sys.exit(app.exec_())
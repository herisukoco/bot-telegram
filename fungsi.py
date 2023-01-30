import datetime
import json
import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
from telegram import update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
from koneksi import *

#def pesantext(update, context):
#    a = update.message.text
#    print(a)


def menu(update: update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Set lokasi", callback_data='10')],
        [InlineKeyboardButton("Pasien", callback_data=f'2')],
        [InlineKeyboardButton("Obat", callback_data=f'5'), InlineKeyboardButton("Rumah Sakit", callback_data=f'6', )],
        [InlineKeyboardButton("Oksigen", callback_data=f'7'), InlineKeyboardButton("Ambulance", callback_data=f'8')],
        [InlineKeyboardButton("Tempat Vaksin", callback_data=f'vaksin')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.send_message(chat_id=update.effective_chat.id ,text="Silahkan pilih :", reply_markup=reply_markup)


def pasien(update: update, context: CallbackContext) -> None:
    data = context.bot.getChat(chat_id=update.effective_chat.id)
    id = data.id
    mycursor.execute(f"SELECT `kode_kab` FROM `user_db` WHERE `user_id`={id}")
    result = mycursor.fetchall()
    kode_kab = result.__str__().replace("(", "").replace(")", "").replace(",", "") \
        .replace("[", "").replace("'", "").replace("]", "")

    if kode_kab == '0':
        query = update.callback_query
        keyboard = [
            [InlineKeyboardButton("Set lokasi", callback_data='10')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text('anda belum menentukan lokasi, tentukan lokasi terlebih dahulu',
                                reply_markup=reply_markup)
    else :
        kode_prov = kode_kab[:2]
        sql = f" SELECT `provinsi` From `prov_db` where `kode_prov`={kode_prov}"
        mycursor.execute(sql)
        prov = mycursor.fetchall()
        prov = prov.__str__().upper().replace("(", "").replace(")", "").replace(",", "") \
            .replace("[", "").replace("'", "").replace("]", "")
        if (prov == 'DI YOGYAKARTA'):
            prov = 'DAERAH ISTIMEWA YOGYAKARTA'
            print(prov)

        base_url = 'https://data.covid19.go.id/public/api/prov.json'
        response = requests.get(base_url).json()
        list = response['list_data']
#        print(list)
#        with open('pasien.json') as file:
#            data = json.load(file)
#            list = data['list_data']
        for i in list:
            provinsi = i['key']
            if (prov == provinsi):
                jml_kasus = i['jumlah_kasus']
                jml_sembuh = i['jumlah_sembuh']
                jml_meninggal = i['jumlah_meninggal']
                jml_dirawat = i['jumlah_dirawat']
                jk = i['jenis_kelamin']
                kel_umur = i['kelompok_umur']
                for j in jk:
                    kel = j['key']
                    if (kel == "LAKI-LAKI"):
                        laki = j['doc_count']
                    else:
                        perempuan = j['doc_count']
                for j in kel_umur:
                    umur = j['key']
                    if (umur == "0-5"):
                        usia1 = j['doc_count']
                    elif (umur == "6-18"):
                        usia2 = j['doc_count']
                    elif (umur == "19-30"):
                        usia3 = j['doc_count']
                    elif (umur == "31-45"):
                        usia4 = j['doc_count']
                    elif (umur == "46-59"):
                        usia5 = j['doc_count']
                    else :
                        usia6 = j['doc_count']

        caption = (f"Provinsi {prov}, \n"
                   f"Jumlah kasus = {jml_kasus} \n "
                   f"jumlah pasien sembuh = {jml_sembuh} \n "
                   f"jumlah pasien meninggal = {jml_meninggal} \n "
                   f"jumlah pasien dirawat = {jml_dirawat}")

        he = [jml_kasus, jml_sembuh, jml_meninggal, jml_dirawat]
        ba = ('Kasus', 'Sembuh', 'meninggal', 'dirawat')
        plt.bar(ba, he)
        folder = 'picture/'
        plt.savefig(folder + f'{prov}.png')
        plt.figure()
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(f'picture/{prov}.png', 'rb'),
                               caption=caption)

        caption_1 = (f"Berdasarkan Jenis Kelamin \n"
                     f"Perempuan = {perempuan}\n"
                     f"Laki Laki = {laki} \n")

        he1 = [perempuan, laki]
        ba1 = ('perempuan', 'laki laki')
        plt.bar(ba1, he1)
        folder = 'picture/'
        plt.savefig(folder + f'jk_{prov}.png')
        plt.figure()
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(f'picture/jk_{prov}.png', 'rb'),
                               caption=caption_1)

        caption_2 = (f"Berdasarkan Rentang Usia \n"
                     f"0 - 5   = {usia1}\n"
                     f"6 - 18  = {usia2}\n"
                     f"19 - 30 = {usia3}\n"
                     f"31 - 45 = {usia4}\n"
                     f"46 - 59 = {usia5}\n"
                     f"≥ 60    = {usia6}")

        he2 = [usia1, usia2, usia3, usia4, usia5, usia6]
        ba2 = ('0-5', '6-18', '19-30', '31-45', '46-59', '≥ 60')
        plt.bar(ba2, he2)
        folder = 'picture/'
        plt.savefig(folder + f'usia_{prov}.png')
        plt.figure()
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(f'picture/usia_{prov}.png', 'rb'),
                               caption=caption_2)
        context.bot.send_message(chat_id=update.effective_chat.id, text="sumber : kementrian kesehatan\nhttps://covid19.go.id ")
    menu(update, context)



def rs(update: update, context: CallbackContext) -> None:
    data = context.bot.getChat(chat_id=update.effective_chat.id)
    id = data.id
    print(id)
    mycursor.execute(f"SELECT `kode_kab` FROM `user_db` WHERE `user_id`={id}")
    result = mycursor.fetchall()
    kode_kab = result.__str__().replace("(", "").replace(")", "").replace(",", "") \
        .replace("[", "").replace("'", "").replace("]", "")
    if kode_kab == '0':
        query = update.callback_query
        keyboard = [
            [InlineKeyboardButton("Set lokasi", callback_data='10')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text('anda belum menentukan lokasi, tentukan lokasi terlebih dahulu',
                                reply_markup=reply_markup)

    else:
        kode_prov = kode_kab[:2]
        print(kode_prov)
        url = f"https://yankes.kemkes.go.id/app/siranap/rumah_sakit?jenis=1&propinsi={kode_prov}prop&kabkota={kode_kab}"
        print(url)
        req0 = requests.get(url)
        btfsoup = BeautifulSoup(req0.text, 'html.parser')
        card = btfsoup.find_all('div', attrs={'class': 'card'})
        x = 0
        for i in card:
            x = x+1
            nama_rs = ''.join(i.find('h5', 'mb-0').text.strip().split('\n'))
            ket0 = ''.join(i.find_all('p', 'mb-0')[0].text.strip().split('\n'))
            ket1 = ''.join(i.find_all('p', 'mb-0')[1].text.strip().split('\n'))
            telp = ''.join(i.find('span').text.strip().split('\n'))
            link = i.find('a')
            link = link.get('href')
            if ket1 != "Bed IGD Penuh!":
                ket3 = ''.join(i.find('b').text.strip().split('\n'))
                base_url = f"{link}"
                req = requests.get(base_url)
                soup = BeautifulSoup(req.text, 'html.parser')
                isi = soup.__str__()
                text = ' tidak tersedia'
                if "card" in isi:
                    items = soup.find_all('div', {'class': 'card-body'})
                    text = ''
                    for j in items:
                        name = ''.join(
                            j.find('p', 'mb-0').text.strip().replace('Update', '').replace('1', '').replace('2',
                                                                                                            '').replace(
                                '3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace(
                                '8', '').replace('9', '').replace('0', '').replace('-', '').replace(':', '').split(
                                '\n'))
                        s = ' '.join(j.find('div', {'class': 'row pt-2 pt-md-0'}).text.strip().split('\n'))
                        p = s.lower()
                        if "tempat tidur 0" in p and "kosong 0" in p:
                            name = ''
                            s = ''
                        else:
                            name = name
                            s = s
                        text = f'{text}\n{name}\n{s}\n'
                        text = text.strip('\n')
                context.bot.send_message(chat_id=update.effective_chat.id, text=f"{nama_rs}\n"
                                                                                f"{ket0}\n"
                                                                                f"Tersedia {ket3} Bed Kosong Tanpa Antrian"
                                                                                f" Pasien\n"
                                                                                f"{telp}\n"
                                                                                f"\n"
                                                                                f"Detail Ruang\n"
                                                                                f"{text}")
        v = 0
        if x == 0:
            mycursor.execute(f"SELECT * from rs_db WHERE kode_kab={kode_kab}")
            data = mycursor.fetchall()

            for k in data:
                nama_rs = k[1]
                alamat = k[2]
                kode_rs = k[0].__str__().replace("(", "").replace(")", "").replace(",", "") \
                            .replace("[", "").replace("'", "").replace("]", "")
                base_url = f"https://yankes.kemkes.go.id/app/siranap/tempat_tidur?kode_rs={kode_rs}&jenis=1"
                req2 = requests.get(base_url)
                soup = BeautifulSoup(req2.text, 'html.parser')
                items = soup.find_all('div', {'class': 'card-body'})
                telp = soup.find('i', {'class': 'fa fa-phone'}).__str__().replace("</i>", "").replace("<i aria-hidden=","").\
                    replace("true", "").replace("class","").replace("fa fa-phone","").replace(">","").replace("=","").\
                    replace('"', '')

                text = ''
                for j in items:
                    name = ''.join(
                    j.find('p', 'mb-0').text.strip().replace('Update', '').replace('1', '').replace('2',
                                                                                                '').replace(
                    '3', '').replace('4', '').replace('5', '').replace('6', '').replace('7', '').replace(
                    '8', '').replace('9', '').replace('0', '').replace('-', '').replace(':', '').split(
                    '\n'))
                    s = ' '.join(j.find('div', {'class': 'row pt-2 pt-md-0'}).text.strip().split('\n'))
                    p = s.lower()
                    if "tempat tidur 0" in p and "kosong 0" in p:
                        name = ''
                        s = ''
                    else:
                        name = name
                        s = s
                        text = f'{text}\n{name}\n{s}\n'
                        text = text.strip('\n')
                context.bot.send_message(chat_id=update.effective_chat.id, text=f"{nama_rs}\n"
                                                                                f"{alamat}\n"
                                                                                f"{telp}\n"
                                                                                f"\n"
                                                                                f"Detail Ruang\n"
                                                                                f"{text}")
                v = v+1
        if v == 0:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Rumah Sakit Covid Di lokasi anda tidak tersedia")
        menu(update, context)

def oksigen(update: update, context: CallbackContext) -> None:
    data = context.bot.getChat(chat_id=update.effective_chat.id)
    id = data.id
    print("1")
    mycursor.execute(f"SELECT `kode_kab` FROM `user_db` WHERE `user_id`={id}")
    result = mycursor.fetchall()
    str = result.__str__().replace("(", "").replace(")", "").replace(",", "") \
        .replace("[", "").replace("'", "").replace("]", "")
    if str == '0':
        query = update.callback_query
        keyboard = [
            [InlineKeyboardButton("Set lokasi", callback_data='10')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text('anda belum menentukan lokasi, tentukan lokasi terlebih dahulu',
                                reply_markup=reply_markup)

    else:
        mycursor.execute(f"SELECT `kabupaten` FROM `kab_db` WHERE `kode_kab`={str}")
        kabupaten = mycursor.fetchone()
        kabupaten = kabupaten.__str__().replace("(", "").replace(")", "").replace(",", "") \
        .replace("[", "").replace("'", "").replace("]", "")
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Daftar tempat Oksigen Di {kabupaten}")
        mycursor.execute(f"SELECT * FROM `oksigen_db` WHERE `kode_kab`={str}")
        result = mycursor.fetchall()
        j = 0
        for i in result:
            j = j+1
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"{i[1]}\n"
                                                                            f"{i[2]}\n"
                                                                            f"{i[3]}\n"
                                                                            f"{i[4]}\n"
                                                                            f"{i[5]}\n")
        if j == 0:
            context.bot.send_message(chat_id=update.effective_chat.id, text="Tidak tersedia")
        menu(update, context)

def obat(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("Azithromycin", callback_data=f'AZITHROMYCIN')],
        [InlineKeyboardButton("Favipiravir", callback_data=f'FAVIPIRAVIR')],
        [InlineKeyboardButton("Ivermectin", callback_data=f'IVERMECTIN')],
        [InlineKeyboardButton("Multivitamin", callback_data=f'MULTIVITAMIN')],
        [InlineKeyboardButton("Oseltamivir", callback_data=f'OSELTAMIVIR')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text('Obat yang bisa anda pilih', reply_markup=reply_markup)


def obat1(update: update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    key = query.data
    print(key)
    data = context.bot.getChat(chat_id=update.effective_chat.id)
    id = data.id
    print(id)
    mycursor.execute(f"SELECT `kode_kab` FROM `user_db` WHERE `user_id`={id}")
    result = mycursor.fetchall()
    str = result.__str__().replace("(", "").replace(")", "").replace(",", "")\
        .replace("[", "").replace("'","").replace("]","")
    print(str)
    if str == '0':
        query = update.callback_query
        keyboard = [
            [InlineKeyboardButton("Set lokasi", callback_data='10')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text('anda belum menentukan lokasi, tentukan lokasi terlebih dahulu', reply_markup=reply_markup)
    else:
        with open('obat.json') as file:
            data = json.load(file)
            jum = 0
            for i in data:
                kode = i['kode']
                kabkota = i['kabkota']
                prov = i['Prov']
                prov = prov.replace(" ", "%20")
                kabkota1 = kabkota.replace(" ", "%20")
                kabkota0 = kabkota.title()
                kabkota2 = kabkota0.replace(" ","%20")
                if kode == str:
                    query.edit_message_text(text=f"{key} DI {kabkota}")
                    key = key.title()
                    print(key)
                    date = datetime.datetime.now().strftime("%Y-%m-%d")
                    base_url = (f"https://farmaplus-api.kemkes.go.id/mastermasters?"
                                f"_where%5B_or%5D%5B0%5D%5B0%5D%5Bobat_contains%5D%5B0%5D={key}"
                                f"&_where%5B_or%5D%5B0%5D%5B1%5D%5Bprovinsi%5D%5B0%5D={prov}"
                                f"&_where%5B_or%5D%5B0%5D%5B2%5D%5Bkabkota%5D%5B0%5D={kabkota1}"
                                f"&_where%5B_or%5D%5B0%5D%5B2%5D%5Bkabkota%5D%5B1%5D={kabkota2}"
                                f"&_q=&_start=0&_limit=10&_sort=jumlah:DESC")
                    print(base_url)
                    req = requests.get(base_url).json()
                    for j in req:
                        obt = (j['obat'])
                        obt_det = (j['obatDetail'])
                        stok = (j['status'])
                        jumlah = (j['jumlah'])
                        nama = (j['nama'])
                        alamat = (j['alamat'])
                        wa = (j['wa'])
                        telp = (j['msisdn'])
                        if stok == "tersedia":
                            jum = jum + 1
                            context.bot.send_message(chat_id=update.effective_chat.id, text=f"{nama}\n"
                                                                                            f"{obt}, {obt_det}\n"
                                                                                            f"tersedia sebanyak {jumlah}\n"
                                                                                            f"{alamat}\n"
                                                                                            f"No WA {wa} , No Telp {telp}")
            if jum == 0:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=f"tidak tersedia")
            menu(update, context)


def vaksin(update: update, context: CallbackContext) -> None:
    data = context.bot.getChat(chat_id=update.effective_chat.id)
    id = data.id
    mycursor.execute(f"SELECT `kode_kab` FROM `user_db` WHERE `user_id`={id}")
    result = mycursor.fetchall()
    str = result.__str__().replace("(", "").replace(")", "").replace(",", "") \
        .replace("[", "").replace("'", "").replace("]", "")
    if str == '0':
        query = update.callback_query
        keyboard = [
            [InlineKeyboardButton("Set lokasi", callback_data='10')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text('anda belum menentukan lokasi, tentukan lokasi terlebih dahulu',
                                reply_markup=reply_markup)
    else:
        mycursor.execute(f"SELECT `kabupaten` FROM `kab_db` WHERE `kode_kab`={str}")
        kabupaten = mycursor.fetchone()
        kabupaten = kabupaten.__str__().replace("(", "").replace(")", "").replace(",", "") \
        .replace("[", "").replace("'", "").replace("]", "")
        mycursor.execute(f"SELECT * FROM `vaksin_db` WHERE `kode_kab`={str}")
        result = mycursor.fetchall()
        j = 0
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Daftar tempat Vaksin Di {kabupaten}")
        for i in result:
            j = j + 1
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"{i[1]}\n"
                                                                            f"{i[2]}\n"
                                                                            f"{i[3]}\n"
                                                                            f"{i[5]}\n"
                                                                            f"{i[6]}\n")


        if j == 0:
            context.bot.send_message(chat_id=update.effective_chat.id, text=f"Data Vaksin Di {kabupaten} belum tersedia")
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=f"Sumber = https://covid19.go.id/faskesvaksin")

        menu(update, context)

def ambulan(update: update, context: CallbackContext)->None:
    data = context.bot.getChat(chat_id=update.effective_chat.id)
    id = data.id
    mycursor.execute(f"SELECT `kode_kab` FROM `user_db` WHERE `user_id`={id}")
    result = mycursor.fetchall()
    str = result.__str__().replace("(", "").replace(")", "").replace(",", "") \
        .replace("[", "").replace("'", "").replace("]", "")
    if str == '0':
        query = update.callback_query
        keyboard = [
            [InlineKeyboardButton("Set lokasi", callback_data='10')],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        query.edit_message_text('anda belum menentukan lokasi, tentukan lokasi terlebih dahulu',
                                reply_markup=reply_markup)
    else:
        sql = f"Select * From ambulan_db where kode_kab={str}"
        mycursor.execute(sql)
        i = 0
        hasil = mycursor.fetchall()
        for j in hasil:
            i = i + 1
        if i == 0:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Data Ambulance di tempat anda tidak tersedia"
                                          "\nsilahkan hubungi salah satu nomer dibawah ini "
                                          "\nAmbulan 118"
                                          "\nKemenkes/Hotline Covid 119")
        else:
            for j in hasil:
                penyedia = j[1]
                keterangan = j[2]
                alamat = j[3]
                hp = j[4]
                context.bot.send_message(chat_id=update.effective_chat.id, text=f"{penyedia}\n"
                                                                                f"{keterangan}\n"
                                                                                f"\n{alamat}\n"
                                                                                f"no Telepon = {hp}")

        menu(update, context)
from itertools import count

from fungsi import *
import fungsi as f
import provinsi as p
from koneksi import *
import time

def answer(update: update, context: CallbackContext):
    data = context.bot.getChat(chat_id=update.effective_chat.id)
    id_user = data.id

    keyboard = [
        [InlineKeyboardButton('Back', callback_data='9')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query
    query.answer()
    key = query.data
    if key == 'vaksin':
        f.vaksin(update, context)
    elif key == '1':
        f.menu(update, context)
    elif key == '2':
        f.pasien(update, context)
    elif key == '5':
        f.obat(update, context)
    elif key == '6':
        f.rs(update, context)
    elif key == '7':
        f.oksigen(update, context)
    elif key == '8':
        f.ambulan(update,context)
    elif key == '9':
        f.menu(update, context)
    elif key == '10':
        p.prov(update, context)
    elif key == '11':
        p.aceh(update, context)
    elif key == '12':
        p.sumut(update, context)
    elif key == '13':
        p.sumbar(update, context)
    elif key == '14':
        p.riau(update, context)
    elif key == '15':
        p.jambi(update, context)
    elif key == '16':
        p.sumsel(update, context)
    elif key == '17':
        p.bengkulu(update, context)
    elif key == '18':
        p.lampung(update, context)
    elif key == '19':
        p.babel(update, context)
    elif key == '20':
        p.kepri(update, context)
    elif key == '31':
        p.jakarta(update, context)
    elif key == '32':
        p.jabar(update, context)
    elif key == '33':
        p.jateng(update, context)
    elif key == '34':
        p.yogya(update, context)
    elif key == '35':
        p.jatim(update, context)
    elif key == '36':
        p.banten(update, context)
    elif key == '51':
        p.bali(update, context)
    elif key == '52':
        p.ntb(update, context)
    elif key == '53':
        p.ntt(update, context)
    elif key == '61':
        p.kalbar(update, context)
    elif key == '62':
        p.kalteng(update, context)
    elif key == '63':
        p.kalsel(update, context)
    elif key == '64':
        p.kaltim(update, context)
    elif key == '65':
        p.kaltara(update, context)
    elif key == '71':
        p.sulut(update, context)
    elif key == '72':
        p.sulteng(update, context)
    elif key == '73':
        p.sulsel(update, context)
    elif key == '74':
        p.sultra(update, context)
    elif key == '75':
        p.gorontalo(update, context)
    elif key == '76':
        p.sulbar(update, context)
    elif key == '81':
        p.maluku(update, context)
    elif key == '82':
        p.maltara(update, context)
    elif key == '91':
        p.papua(update, context)
    elif key == '92':
        p.papuabarat(update, context)
    elif key == '1101':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1101', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1102':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1102', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1103':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1103', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1104':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1104', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1105':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1105', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1106':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1106', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1107':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1107', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1108':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1108', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1109':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1109', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1110':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1110', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1111':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1111', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1112':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1112', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1113':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1113', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1114':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1114', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1115':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1115', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1116':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1116', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1117':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1117', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1118':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1118', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1171':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1171', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1172':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1172', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1173':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1173', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1174':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1174', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1175':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1175', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1201':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1201', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1202':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1202', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1203':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1203', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1204':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1204', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1205':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1205', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1206':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1206', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1207':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1207', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1208':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1208', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1209':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1209', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1210':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1210', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1211':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1211', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1212':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1212', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1213':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1213', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1214':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1214', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1215':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1215', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1216':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1216', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1217':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1217', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1218':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1218', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1219':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1219', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1220':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1220', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1221':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1221', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1222':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1222', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1223':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1223', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1271':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1271', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1272':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1272', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1273':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1273', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1274':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1274', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1275':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1275', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1276':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1276', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1277':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1277', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1278':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1278', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1301':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1301', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1302':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1302', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1303':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1303', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1304':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1304', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1305':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1305', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1306':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1306', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1307':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1307', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1308':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1308', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1309':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1309', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1310':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1310', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1311':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1311', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1312':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1312', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1371':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1371', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1372':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1372', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1373':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1373', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1374':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1374', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1375':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1375', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1376':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1376', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1377':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1377', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1401':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1401', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1402':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1402', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1403':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1403', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1404':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1404', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1406':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1406', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1407':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1407', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1408':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1408', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1409':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1409', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1410':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1410', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1471':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1471', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1473':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1473', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1501':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1501', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1502':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1502', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1503':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1503', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1504':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1504', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1505':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1505', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1506':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1506', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1507':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1507', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1508':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1508', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1509':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1509', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1571':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1571', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1601':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1601', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1602':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1602', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1603':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1603', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1604':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1604', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1605':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1605', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1606':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1606', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1607':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1607', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1608':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1608', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1609':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1609', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1610':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1610', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1611':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1611', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1671':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1671', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1672':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1672', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1673':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1673', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1674':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1674', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1701':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1701', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1702':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1702', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1703':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1703', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1704':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1704', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1705':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1705', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1706':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1706', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1707':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1707', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1708':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1708', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1709':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1709', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1771':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1771', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1801':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1801', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1802':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1802', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1803':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1803', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1804':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1804', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1805':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1805', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1806':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1806', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1807':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1807', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1808':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1808', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1809':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1809', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1810':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1810', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1871':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1871', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1872':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1872', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1901':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1901', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1902':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1902', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1903':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1903', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1904':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1904', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1905':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1905', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1906':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1906', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '1971':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'1971', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '2001':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'2001', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '2002':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'2002', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '2003':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'2003', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '2004':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'2004', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '2005':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'2005', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '2071':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'2071', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '2072':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'2072', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3101':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3101', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3171':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3171', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3172':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3172', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3173':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3173', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3174':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3174', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3175':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3175', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3201':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3201', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3202':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3202', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3203':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3203', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3204':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3204', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3205':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3205', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3206':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3206', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3207':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3207', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3208':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3208', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3209':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3209', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3210':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3210', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3211':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3211', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3212':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3212', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3213':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3213', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3214':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3214', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3215':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3215', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3216':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3216', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3217':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3217', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3271':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3271', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3272':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3272', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3273':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3273', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3274':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3274', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3275':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3275', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3276':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3276', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3277':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3277', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3278':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3278', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3279':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3279', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3301':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3301', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3302':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3302', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3303':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3303', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3304':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3304', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3305':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3305', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3306':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3306', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3307':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3307', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3308':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3308', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3309':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3309', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3310':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3310', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3311':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3311', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3312':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3312', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3313':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3313', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3314':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3314', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3315':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3315', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3316':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3316', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3317':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3317', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3318':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3318', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3319':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3319', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3320':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3320', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3321':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3321', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3322':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3322', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3323':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3323', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3324':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3324', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3325':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3325', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3326':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3326', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3327':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3327', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3328':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3328', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3329':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3329', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3371':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3371', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3372':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3372', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3373':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3373', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3374':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3374', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3375':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3375', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3376':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3376', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3401':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3401', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3402':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3402', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3403':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3403', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3404':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3404', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3471':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3471', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3501':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3501', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3502':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3502', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3503':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3503', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3504':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3504', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3505':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3505', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3506':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3506', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3507':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3507', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3508':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3508', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3509':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3509', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3510':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3510', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3511':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3511', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3512':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3512', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3513':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3513', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3514':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3514', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3515':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3515', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3516':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3516', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3517':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3517', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3518':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3518', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3519':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3519', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3520':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3520', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3521':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3521', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3522':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3522', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3523':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3523', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3524':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3524', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3525':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3525', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3526':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3526', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3527':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3527', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3528':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3528', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3529':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3529', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3571':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3571', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3572':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3572', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3573':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3573', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3574':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3574', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3575':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3575', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3576':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3576', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3577':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3577', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3578':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3578', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3579':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3579', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3601':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3601', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3602':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3602', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3603':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3603', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3604':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3604', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3671':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3671', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3672':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3672', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3673':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3673', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '3674':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'3674', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5101':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5101', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5102':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5102', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5103':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5103', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5104':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5104', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5105':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5105', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5106':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5106', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5107':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5107', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5108':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5108', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5130':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5130', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5171':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5171', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5201':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5201', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5202':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5202', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5203':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5203', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5204':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5204', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5205':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5205', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5206':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5206', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5207':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5207', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5208':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5208', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5271':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5271', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5272':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5272', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5301':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5301', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5302':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5302', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5303':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5303', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5304':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5304', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5305':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5305', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5306':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5306', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5307':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5307', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5308':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5308', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5309':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5309', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5310':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5310', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5311':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5311', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5312':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5312', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5313':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5313', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5314':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5314', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5316':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5316', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5320':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5320', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '5371':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'5371', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6101':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6101', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6102':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6102', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6103':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6103', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6104':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6104', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6105':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6105', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6106':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6106', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6107':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6107', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6108':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6108', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6109':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6109', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6110':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6110', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6112':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6112', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6171':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6171', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6172':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6172', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6201':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6201', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6202':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6202', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6203':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6203', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6204':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6204', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6205':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6205', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6206':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6206', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6207':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6207', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6208':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6208', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6209':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6209', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6210':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6210', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6211':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6211', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6212':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6212', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6213':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6213', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6271':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6271', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6301':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6301', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6302':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6302', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6303':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6303', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6304':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6304', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6305':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6305', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6306':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6306', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6307':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6307', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6308':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6308', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6309':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6309', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6310':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6310', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6311':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6311', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6371':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6371', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6372':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6372', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6402':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6402', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6403':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6403', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6404':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6404', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6405':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6405', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6409':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6409', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6471':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6471', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6472':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6472', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6474':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6474', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6501':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6501', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6502':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6502', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6504':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6504', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '6571':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'6571', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7101':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7101', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7102':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7102', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7103':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7103', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7104':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7104', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7105':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7105', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7106':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7106', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7107':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7107', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7109':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7109', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7110':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7110', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7171':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7171', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7172':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7172', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7173':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7173', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7174':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7174', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7202':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7202', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7203':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7203', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7204':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7204', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7205':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7205', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7206':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7206', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7207':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7207', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7208':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7208', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7209':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7209', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7271':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7271', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7301':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7301', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7302':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7302', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7303':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7303', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7304':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7304', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7305':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7305', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7306':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7306', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7307':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7307', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7308':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7308', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7309':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7309', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7310':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7310', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7311':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7311', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7312':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7312', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7313':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7313', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7314':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7314', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7315':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7315', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7316':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7316', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7317':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7317', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7318':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7318', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7322':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7322', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7325':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7325', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7326':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7326', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7371':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7371', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7372':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7372', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7373':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7373', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7401':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7401', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7402':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7402', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7403':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7403', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7404':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7404', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7405':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7405', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7406':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7406', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7407':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7407', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7408':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7408', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7409':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7409', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7410':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7410', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7471':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7471', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7472':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7472', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7501':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7501', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7502':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7502', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7503':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7503', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7504':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7504', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7505':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7505', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7571':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7571', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7601':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7601', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7602':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7602', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7603':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7603', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7604':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7604', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '7605':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'7605', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8101':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8101', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8102':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8102', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8103':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8103', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8104':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8104', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8105':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8105', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8106':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8106', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8107':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8107', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8108':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8108', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8109':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8109', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8171':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8171', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8172':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8172', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8201':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8201', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8202':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8202', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8204':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8204', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8205':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8205', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8206':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8206', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8207':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8207', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8271':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8271', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '8272':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'8272', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9101':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9101', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9102':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9102', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9103':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9103', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9104':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9104', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9105':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9105', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9106':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9106', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9107':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9107', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9108':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9108', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9171':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9171', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9201':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9201', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9202':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9202', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9203':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9203', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9204':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9204', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9205':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9205', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9208':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9208', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9210':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9210', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9211':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9211', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9212':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9212', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9213':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9213', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9214':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9214', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9215':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9215', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9216':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9216', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9217':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9217', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9220':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9220', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9227':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9227', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9228':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9228', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9230':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9230', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)
    elif key == '9271':
        sql = f"UPDATE user_db SET kode_kab = %s WHERE user_db.user_id = %s"
        val = (f'9271', f'{id_user}')
        mycursor.execute(sql, val)
        mydb.commit()
        query.edit_message_text("Lokasi anda berhasil ditambahkan")
        time.sleep(3)
        f.menu(update, context)

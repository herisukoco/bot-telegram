from fungsi import *

def prov(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("Aceh", callback_data=f"11"),
         InlineKeyboardButton("Sumatera Utara", callback_data=f"12")],
        [InlineKeyboardButton("Sumatera Barat", callback_data=f"13"),
         InlineKeyboardButton("Riau", callback_data=f"14")],
        [InlineKeyboardButton("Jambi", callback_data=f"15"),
         InlineKeyboardButton("Sumatera Selatan", callback_data=f"16")],
        [InlineKeyboardButton("Bengkulu", callback_data=f"17"),
         InlineKeyboardButton("Lampung", callback_data=f"18")],
        [InlineKeyboardButton("Bangka Belitung", callback_data=f"19"),
         InlineKeyboardButton("Kepulauan Riau", callback_data=f"20")],
        [InlineKeyboardButton("Dki Jakarta", callback_data=f"31"),
         InlineKeyboardButton("Jawa Barat", callback_data=f"32")],
        [InlineKeyboardButton("Jawa Tengah", callback_data=f"33"),
         InlineKeyboardButton("Di Yogyakarta", callback_data=f"34")],
        [InlineKeyboardButton("Jawa Timur", callback_data=f"35"),
         InlineKeyboardButton("Banten", callback_data=f"36")],
        [InlineKeyboardButton("Bali", callback_data=f"51"),
         InlineKeyboardButton("Nusa Tenggara Barat", callback_data=f"52")],
        [InlineKeyboardButton("Nusa Tenggara Timur", callback_data=f"53"),
         InlineKeyboardButton("Kalimantan Barat", callback_data=f"61")],
        [InlineKeyboardButton("Kalimantan Tengah", callback_data=f"62"),
         InlineKeyboardButton("Kalimantan Selatan", callback_data=f"63")],
        [InlineKeyboardButton("Kalimantan Timur", callback_data=f"64"),
         InlineKeyboardButton("Kalimantan Utara", callback_data=f"65")],
        [InlineKeyboardButton("Sulawesi Utara", callback_data=f"71"),
         InlineKeyboardButton("Sulawesi Tengah", callback_data=f"72")],
        [InlineKeyboardButton("Sulawesi Selatan", callback_data=f"73"),
         InlineKeyboardButton("Sulawesi Tenggara", callback_data=f"74")],
        [InlineKeyboardButton("Gorontalo", callback_data=f"75"),
         InlineKeyboardButton("Sulawesi Barat", callback_data=f"76")],
        [InlineKeyboardButton("Maluku", callback_data=f"81"),
         InlineKeyboardButton("Maluku Utara", callback_data=f"82")],
        [InlineKeyboardButton("Papua Barat", callback_data=f"91"),
         InlineKeyboardButton("Papua", callback_data=f"92")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Provinsi:", reply_markup=reply_markup)

def aceh(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("SIMEULUE", callback_data=f"1101"),
         InlineKeyboardButton("ACEH SINGKIL", callback_data=f"1102")],
        [InlineKeyboardButton("ACEH SELATAN", callback_data=f"1103"),
         InlineKeyboardButton("ACEH TENGGARA", callback_data=f"1104")],
        [InlineKeyboardButton("ACEH TIMUR", callback_data=f"1105"),
         InlineKeyboardButton("ACEH TENGAH", callback_data=f"1106")],
        [InlineKeyboardButton("ACEH BARAT", callback_data=f"1107"),
         InlineKeyboardButton("ACEH BESAR", callback_data=f"1108")],
        [InlineKeyboardButton("PIDIE", callback_data=f"1109"),
         InlineKeyboardButton("BIREUEN", callback_data=f"1110")],
        [InlineKeyboardButton("ACEH UTARA", callback_data=f"1111"),
         InlineKeyboardButton("ACEH BARAT DAYA", callback_data=f"1112")],
        [InlineKeyboardButton("GAYO LUES", callback_data=f"1113"),
         InlineKeyboardButton("ACEH TAMIANG", callback_data=f"1114")],
        [InlineKeyboardButton("NAGAN RAYA", callback_data=f"1115"),
         InlineKeyboardButton("ACEH JAYA", callback_data=f"1116")],
        [InlineKeyboardButton("BENER MERIAH", callback_data=f"1117"),
         InlineKeyboardButton("PIDIE JAYA", callback_data=f"1118")],
        [InlineKeyboardButton("KOTA BANDA ACEH", callback_data=f"1171"),
         InlineKeyboardButton("KOTA SABANG", callback_data=f"1172")],
        [InlineKeyboardButton("KOTA LANGSA", callback_data=f"1173"),
         InlineKeyboardButton("KOTA LHOKSEUMAWE", callback_data=f"1174")],
        [InlineKeyboardButton("KOTA SUBULUSSALAM", callback_data=f"1175")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def sumut(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("NIAS", callback_data=f"1201"),
         InlineKeyboardButton("MANDAILING NATAL", callback_data=f"1202")],
        [InlineKeyboardButton("TAPANULI SELATAN", callback_data=f"1203"),
         InlineKeyboardButton("TAPANULI TENGAH", callback_data=f"1204")],
        [InlineKeyboardButton("TAPANULI UTARA", callback_data=f"1205"),
         InlineKeyboardButton("TOBA SAMOSIR", callback_data=f"1206")],
        [InlineKeyboardButton("LABUHAN BATU", callback_data=f"1207"),
         InlineKeyboardButton("ASAHAN", callback_data=f"1208")],
        [InlineKeyboardButton("SIMALUNGUN", callback_data=f"1209"),
         InlineKeyboardButton("DAIRI", callback_data=f"1210")],
        [InlineKeyboardButton("KARO", callback_data=f"1211"),
         InlineKeyboardButton("DELI SERDANG", callback_data=f"1212")],
        [InlineKeyboardButton("LANGKAT", callback_data=f"1213"),
         InlineKeyboardButton("NIAS SELATAN", callback_data=f"1214")],
        [InlineKeyboardButton("HUMBANG HASUNDUTAN", callback_data=f"1215"),
         InlineKeyboardButton("PAKPAK BHARAT", callback_data=f"1216")],
        [InlineKeyboardButton("SAMOSIR", callback_data=f"1217"),
         InlineKeyboardButton("SERDANG BEDAGAI", callback_data=f"1218")],
        [InlineKeyboardButton("BATU BARA", callback_data=f"1219"),
         InlineKeyboardButton("PADANG LAWAS UTARA", callback_data=f"1220")],
        [InlineKeyboardButton("PADANG LAWAS", callback_data=f"1221"),
         InlineKeyboardButton("LABUHAN BATU SELATAN", callback_data=f"1222")],
        [InlineKeyboardButton("LABUHAN BATU UTARA", callback_data=f"1223"),
         InlineKeyboardButton("KOTA SIBOLGA", callback_data=f"1271")],
        [InlineKeyboardButton("KOTA TANJUNG BALAI", callback_data=f"1272"),
         InlineKeyboardButton("KOTA PEMATANG SIANTAR", callback_data=f"1273")],
        [InlineKeyboardButton("KOTA TEBING TINGGI", callback_data=f"1274"),
         InlineKeyboardButton("KOTA MEDAN", callback_data=f"1275")],
        [InlineKeyboardButton("KOTA BINJAI", callback_data=f"1276"),
         InlineKeyboardButton("KOTA PADANG SIDEMPUAN", callback_data=f"1277")],
        [InlineKeyboardButton("KOTA GUNUNG SITOLI", callback_data=f"1278")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def sumbar(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("KEPULAUAN MENTAWAI", callback_data=f"1301"),
         InlineKeyboardButton("PESISIR SELATAN", callback_data=f"1302")],
        [InlineKeyboardButton("KAB. SOLOK", callback_data=f"1303"),
         InlineKeyboardButton("SIJUNJUNG", callback_data=f"1304")],
        [InlineKeyboardButton("TANAH DATAR", callback_data=f"1305"),
         InlineKeyboardButton("PADANG PARIAMAN", callback_data=f"1306")],
        [InlineKeyboardButton("AGAM", callback_data=f"1307"),
         InlineKeyboardButton("LIMA PULUH KOTA", callback_data=f"1308")],
        [InlineKeyboardButton("PASAMAN", callback_data=f"1309"),
         InlineKeyboardButton("SOLOK SELATAN", callback_data=f"1310")],
        [InlineKeyboardButton("DHARMASRAYA", callback_data=f"1311"),
         InlineKeyboardButton("PASAMAN BARAT", callback_data=f"1312")],
        [InlineKeyboardButton("KOTA PADANG", callback_data=f"1371"),
         InlineKeyboardButton("KOTA SOLOK", callback_data=f"1372")],
        [InlineKeyboardButton("KOTA SAWAH LUNTO", callback_data=f"1373"),
         InlineKeyboardButton("KOTA PADANG PANJANG", callback_data=f"1374")],
        [InlineKeyboardButton("KOTA BUKITTINGGI", callback_data=f"1375"),
         InlineKeyboardButton("KOTA PAYAKUMBUH", callback_data=f"1376")],
        [InlineKeyboardButton("KOTA PARIAMAN", callback_data=f"1377")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def riau(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("KUANTAN SENGINGI", callback_data=f"1401"),
         InlineKeyboardButton("INDRAGIRI HULU", callback_data=f"1402")],
        [InlineKeyboardButton("INDRAGIRI HILIR", callback_data=f"1403"),
         InlineKeyboardButton("PELALAWAN", callback_data=f"1404")],
        [InlineKeyboardButton("KAMPAR", callback_data=f"1406"),
         InlineKeyboardButton("ROKAN HULU", callback_data=f"1407")],
        [InlineKeyboardButton("BENGKALIS", callback_data=f"1408"),
         InlineKeyboardButton("ROKAN HILIR", callback_data=f"1409")],
        [InlineKeyboardButton("MERANTI", callback_data=f"1410"),
         InlineKeyboardButton("KOTA PEKAN BARU", callback_data=f"1471")],
        [InlineKeyboardButton("KOTA DUMAI", callback_data=f"1473")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def jambi(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("KERINCI", callback_data=f"1501"),
         InlineKeyboardButton("MERANGIN", callback_data=f"1502")],
        [InlineKeyboardButton("SAROLANGUN", callback_data=f"1503"),
         InlineKeyboardButton("BATANG HARI", callback_data=f"1504")],
        [InlineKeyboardButton("MUARO JAMBI", callback_data=f"1505"),
         InlineKeyboardButton("TANJUNG JABUNG TIMUR", callback_data=f"1506")],
        [InlineKeyboardButton("TANJUNG JABUNG BARAT", callback_data=f"1507"),
         InlineKeyboardButton("TEBO", callback_data=f"1508")],
        [InlineKeyboardButton("BUNGO", callback_data=f"1509"),
         InlineKeyboardButton("KOTA JAMBI", callback_data=f"1571")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)


def sumsel(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("KOTA JAMBI", callback_data=f"1571"),
         InlineKeyboardButton("OGAN KOMERING ULU", callback_data=f"1601")],
        [InlineKeyboardButton("OGAN KOMERING ILIR", callback_data=f"1602"),
         InlineKeyboardButton("MUARA ENIM", callback_data=f"1603")],
        [InlineKeyboardButton("LAHAT", callback_data=f"1604"),
         InlineKeyboardButton("MUSI RAWAS", callback_data=f"1605")],
        [InlineKeyboardButton("MUSI BANYU ASIN", callback_data=f"1606"),
         InlineKeyboardButton("BANYUASIN", callback_data=f"1607")],
        [InlineKeyboardButton("OGAN KOMERING ULU SELATAN", callback_data=f"1608"),
         InlineKeyboardButton("OGAN KOMERING ULU TIMUR", callback_data=f"1609")],
        [InlineKeyboardButton("OGAN ILIR", callback_data=f"1610"),
         InlineKeyboardButton("EMPAT LAWANG", callback_data=f"1611")],
        [InlineKeyboardButton("KOTA PALEMBANG", callback_data=f"1671"),
         InlineKeyboardButton("KOTA PRABUMULIH", callback_data=f"1672")],
        [InlineKeyboardButton("KOTA PAGAR ALAM", callback_data=f"1673"),
         InlineKeyboardButton("KOTA LUBUK LINGGAU", callback_data=f"1674")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def bengkulu(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("BENGKULU SELATAN", callback_data=f"1701"),
         InlineKeyboardButton("REJANG LEBONG", callback_data=f"1702")],
        [InlineKeyboardButton("BENGKULU UTARA", callback_data=f"1703"),
         InlineKeyboardButton("KAUR", callback_data=f"1704")],
        [InlineKeyboardButton("SELUMA", callback_data=f"1705"),
         InlineKeyboardButton("MUKOMUKO", callback_data=f"1706")],
        [InlineKeyboardButton("LEBONG", callback_data=f"1707"),
         InlineKeyboardButton("KEPAHIANG", callback_data=f"1708")],
        [InlineKeyboardButton("BENGKULU TENGAH", callback_data=f"1709"),
         InlineKeyboardButton("KOTA BENGKULU", callback_data=f"1771")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def lampung(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("LAMPUNG BARAT", callback_data=f"1801"),
         InlineKeyboardButton("TANGGAMUS", callback_data=f"1802")],
        [InlineKeyboardButton("LAMPUNG SELATAN", callback_data=f"1803"),
         InlineKeyboardButton("LAMPUNG TIMUR", callback_data=f"1804")],
        [InlineKeyboardButton("LAMPUNG TENGAH", callback_data=f"1805"),
         InlineKeyboardButton("LAMPUNG UTARA", callback_data=f"1806")],
        [InlineKeyboardButton("WAY KANAN", callback_data=f"1807"),
         InlineKeyboardButton("TULANGBAWANG", callback_data=f"1808")],
        [InlineKeyboardButton("PESAWARAN", callback_data=f"1809"),
         InlineKeyboardButton("PRINGSEWU", callback_data=f"1810")],
        [InlineKeyboardButton("KOTA BANDAR LAMPUNG", callback_data=f"1871"),
         InlineKeyboardButton("KOTA METRO", callback_data=f"1872")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)


def babel(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("BANGKA", callback_data=f"1901"),
         InlineKeyboardButton("BELITUNG", callback_data=f"1902")],
        [InlineKeyboardButton("BANGKA BARAT", callback_data=f"1903"),
         InlineKeyboardButton("BANGKA TENGAH", callback_data=f"1904")],
        [InlineKeyboardButton("BANGKA SELATAN", callback_data=f"1905"),
         InlineKeyboardButton("BELITUNG TIMUR", callback_data=f"1906")],
        [InlineKeyboardButton("KOTA PANGKAL PINANG", callback_data=f"1971")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def kepri(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("KARIMUN", callback_data=f"2001"),
         InlineKeyboardButton("BINTAN", callback_data=f"2002")],
        [InlineKeyboardButton("NATUNA", callback_data=f"2003"),
         InlineKeyboardButton("LINGGA", callback_data=f"2004")],
        [InlineKeyboardButton("KEPULAUAN ANAMBAS", callback_data=f"2005"),
         InlineKeyboardButton("KOTA BATAM", callback_data=f"2071")],
        [InlineKeyboardButton("KOTA TANJUNG PINANG", callback_data=f"2072")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def jakarta(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("ADM. KEPULAUAN SERIBU", callback_data=f"3101"),
         InlineKeyboardButton("KOTA JAKARTA SELATAN", callback_data=f"3171")],
        [InlineKeyboardButton("KOTA JAKARTA TIMUR", callback_data=f"3172"),
         InlineKeyboardButton("KOTA JAKARTA PUSAT", callback_data=f"3173")],
        [InlineKeyboardButton("KOTA JAKARTA BARAT", callback_data=f"3174"),
         InlineKeyboardButton("KOTA JAKARTA UTARA", callback_data=f"3175")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)


def jabar(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("BOGOR", callback_data=f"3201"),
         InlineKeyboardButton("SUKABUMI", callback_data=f"3202")],
        [InlineKeyboardButton("CIANJUR", callback_data=f"3203"),
         InlineKeyboardButton("BANDUNG", callback_data=f"3204")],
        [InlineKeyboardButton("GARUT", callback_data=f"3205"),
         InlineKeyboardButton("TASIKMALAYA", callback_data=f"3206")],
        [InlineKeyboardButton("CIAMIS", callback_data=f"3207"),
         InlineKeyboardButton("KUNINGAN", callback_data=f"3208")],
        [InlineKeyboardButton("CIREBON", callback_data=f"3209"),
         InlineKeyboardButton("MAJALENGKA", callback_data=f"3210")],
        [InlineKeyboardButton("SUMEDANG", callback_data=f"3211"),
         InlineKeyboardButton("INDRAMAYU", callback_data=f"3212")],
        [InlineKeyboardButton("SUBANG", callback_data=f"3213"),
         InlineKeyboardButton("PURWAKARTA", callback_data=f"3214")],
        [InlineKeyboardButton("KARAWANG", callback_data=f"3215"),
         InlineKeyboardButton("BEKASI", callback_data=f"3216")],
        [InlineKeyboardButton("BANDUNG BARAT", callback_data=f"3217"),
         InlineKeyboardButton("KOTA BOGOR", callback_data=f"3271")],
        [InlineKeyboardButton("KOTA SUKABUMI", callback_data=f"3272"),
         InlineKeyboardButton("KOTA BANDUNG", callback_data=f"3273")],
        [InlineKeyboardButton("KOTA CIREBON", callback_data=f"3274"),
         InlineKeyboardButton("KOTA BEKASI", callback_data=f"3275")],
        [InlineKeyboardButton("KOTA DEPOK", callback_data=f"3276"),
         InlineKeyboardButton("KOTA CIMAHI", callback_data=f"3277")],
        [InlineKeyboardButton("KOTA TASIKMALAYA", callback_data=f"3278"),
         InlineKeyboardButton("KOTA BANJAR", callback_data=f"3279")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)


def jateng(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("CILACAP", callback_data=f"3301"),
         InlineKeyboardButton("BANYUMAS", callback_data=f"3302")],
        [InlineKeyboardButton("PURBALINGGA", callback_data=f"3303"),
         InlineKeyboardButton("BANJARNEGARA", callback_data=f"3304")],
        [InlineKeyboardButton("KEBUMEN", callback_data=f"3305"),
         InlineKeyboardButton("PURWOREJO", callback_data=f"3306")],
        [InlineKeyboardButton("WONOSOBO", callback_data=f"3307"),
         InlineKeyboardButton("MAGELANG", callback_data=f"3308")],
        [InlineKeyboardButton("BOYOLALI", callback_data=f"3309"),
         InlineKeyboardButton("KLATEN", callback_data=f"3310")],
        [InlineKeyboardButton("SUKOHARJO", callback_data=f"3311"),
         InlineKeyboardButton("WONOGIRI", callback_data=f"3312")],
        [InlineKeyboardButton("KARANGANYAR", callback_data=f"3313"),
         InlineKeyboardButton("SRAGEN", callback_data=f"3314")],
        [InlineKeyboardButton("GROBOGAN", callback_data=f"3315"),
         InlineKeyboardButton("BLORA", callback_data=f"3316")],
        [InlineKeyboardButton("REMBANG", callback_data=f"3317"),
         InlineKeyboardButton("PATI", callback_data=f"3318")],
        [InlineKeyboardButton("KUDUS", callback_data=f"3319"),
         InlineKeyboardButton("JEPARA", callback_data=f"3320")],
        [InlineKeyboardButton("DEMAK", callback_data=f"3321"),
         InlineKeyboardButton("SEMARANG", callback_data=f"3322")],
        [InlineKeyboardButton("TEMANGGUNG", callback_data=f"3323"),
         InlineKeyboardButton("KENDAL", callback_data=f"3324")],
        [InlineKeyboardButton("BATANG", callback_data=f"3325"),
         InlineKeyboardButton("PEKALONGAN", callback_data=f"3326")],
        [InlineKeyboardButton("PEMALANG", callback_data=f"3327"),
         InlineKeyboardButton("TEGAL", callback_data=f"3328")],
        [InlineKeyboardButton("BREBES", callback_data=f"3329"),
         InlineKeyboardButton("KOTA MAGELANG", callback_data=f"3371")],
        [InlineKeyboardButton("KOTA SURAKARTA", callback_data=f"3372"),
         InlineKeyboardButton("KOTA SALATIGA", callback_data=f"3373")],
        [InlineKeyboardButton("KOTA SEMARANG", callback_data=f"3374"),
         InlineKeyboardButton("KOTA PEKALONGAN", callback_data=f"3375")],
        [InlineKeyboardButton("KOTA TEGAL", callback_data=f"3376")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def yogya(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("KULON PROGO", callback_data=f"3401"),
         InlineKeyboardButton("BANTUL", callback_data=f"3402")],
        [InlineKeyboardButton("GUNUNG KIDUL", callback_data=f"3403"),
         InlineKeyboardButton("SLEMAN", callback_data=f"3404")],
        [InlineKeyboardButton("KOTA YOGYAKARTA", callback_data=f"3471")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def jatim(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("PACITAN", callback_data=f"3501"),
         InlineKeyboardButton("PONOROGO", callback_data=f"3502")],
        [InlineKeyboardButton("TRENGGALEK", callback_data=f"3503"),
         InlineKeyboardButton("TULUNGAGUNG", callback_data=f"3504")],
        [InlineKeyboardButton("BLITAR", callback_data=f"3505"),
         InlineKeyboardButton("KEDIRI", callback_data=f"3506")],
        [InlineKeyboardButton("MALANG", callback_data=f"3507"),
         InlineKeyboardButton("LUMAJANG", callback_data=f"3508")],
        [InlineKeyboardButton("JEMBER", callback_data=f"3509"),
         InlineKeyboardButton("BANYUWANGI", callback_data=f"3510")],
        [InlineKeyboardButton("BONDOWOSO", callback_data=f"3511"),
         InlineKeyboardButton("SITUBONDO", callback_data=f"3512")],
        [InlineKeyboardButton("PROBOLINGGO", callback_data=f"3513"),
         InlineKeyboardButton("PASURUAN", callback_data=f"3514")],
        [InlineKeyboardButton("SIDOARJO", callback_data=f"3515"),
         InlineKeyboardButton("MOJOKERTO", callback_data=f"3516")],
        [InlineKeyboardButton("JOMBANG", callback_data=f"3517"),
         InlineKeyboardButton("NGANJUK", callback_data=f"3518")],
        [InlineKeyboardButton("MADIUN", callback_data=f"3519"),
         InlineKeyboardButton("MAGETAN", callback_data=f"3520")],
        [InlineKeyboardButton("NGAWI", callback_data=f"3521"),
         InlineKeyboardButton("BOJONEGORO", callback_data=f"3522")],
        [InlineKeyboardButton("TUBAN", callback_data=f"3523"),
         InlineKeyboardButton("LAMONGAN", callback_data=f"3524")],
        [InlineKeyboardButton("GRESIK", callback_data=f"3525"),
         InlineKeyboardButton("BANGKALAN", callback_data=f"3526")],
        [InlineKeyboardButton("SAMPANG", callback_data=f"3527"),
         InlineKeyboardButton("PAMEKASAN", callback_data=f"3528")],
        [InlineKeyboardButton("SUMENEP", callback_data=f"3529"),
         InlineKeyboardButton("KOTA KEDIRI", callback_data=f"3571")],
        [InlineKeyboardButton("KOTA BLITAR", callback_data=f"3572"),
         InlineKeyboardButton("KOTA MALANG", callback_data=f"3573")],
        [InlineKeyboardButton("KOTA PROBOLINGGO", callback_data=f"3574"),
         InlineKeyboardButton("KOTA PASURUAN", callback_data=f"3575")],
        [InlineKeyboardButton("KOTA MOJOKERTO", callback_data=f"3576"),
         InlineKeyboardButton("KOTA MADIUN", callback_data=f"3577")],
        [InlineKeyboardButton("KOTA SURABAYA", callback_data=f"3578"),
         InlineKeyboardButton("KOTA BATU", callback_data=f"3579")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def banten(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("PANDEGLANG", callback_data=f"3601"),
         InlineKeyboardButton("LEBAK", callback_data=f"3602")],
        [InlineKeyboardButton("TANGERANG", callback_data=f"3603"),
         InlineKeyboardButton("SERANG", callback_data=f"3604")],
        [InlineKeyboardButton("KOTA TANGERANG", callback_data=f"3671"),
         InlineKeyboardButton("KOTA CILEGON", callback_data=f"3672")],
        [InlineKeyboardButton("KOTA SERANG", callback_data=f"3673"),
         InlineKeyboardButton("KOTA TANGERANG SELATAN", callback_data=f"3674")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)


def bali(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("JEMBRANA", callback_data=f"5101"),
         InlineKeyboardButton("TABANAN", callback_data=f"5102")],
        [InlineKeyboardButton("BADUNG", callback_data=f"5103"),
         InlineKeyboardButton("GIANYAR", callback_data=f"5104")],
        [InlineKeyboardButton("KLUNGKUNG", callback_data=f"5105"),
         InlineKeyboardButton("BANGLI", callback_data=f"5106")],
        [InlineKeyboardButton("Karangasem", callback_data=f"5107"),
         InlineKeyboardButton("BULELENG", callback_data=f"5108")],
        [InlineKeyboardButton("BADUNG", callback_data=f"5130"),
         InlineKeyboardButton("KOTA DENPASAR", callback_data=f"5171")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def ntb(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("LOMBOK BARAT", callback_data=f"5201"),
         InlineKeyboardButton("LOMBOK TENGAH", callback_data=f"5202")],
        [InlineKeyboardButton("LOMBOK TIMUR", callback_data=f"5203"),
         InlineKeyboardButton("SUMBAWA", callback_data=f"5204")],
        [InlineKeyboardButton("DOMPU", callback_data=f"5205"),
         InlineKeyboardButton("BIMA", callback_data=f"5206")],
        [InlineKeyboardButton("SUMBAWA BARAT", callback_data=f"5207"),
         InlineKeyboardButton("LOMBOK UTARA", callback_data=f"5208")],
        [InlineKeyboardButton("KOTA MATARAM", callback_data=f"5271"),
         InlineKeyboardButton("KOTA BIMA", callback_data=f"5272")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)


def ntt(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("SUMBA BARAT", callback_data=f"5301"),
         InlineKeyboardButton("SUMBA TIMUR", callback_data=f"5302")],
        [InlineKeyboardButton("KUPANG", callback_data=f"5303"),
         InlineKeyboardButton("TIMOR TENGAH SELATAN", callback_data=f"5304")],
        [InlineKeyboardButton("TIMOR TENGAH UTARA", callback_data=f"5305"),
         InlineKeyboardButton("BELU", callback_data=f"5306")],
        [InlineKeyboardButton("ALOR", callback_data=f"5307"),
         InlineKeyboardButton("LEMBATA", callback_data=f"5308")],
        [InlineKeyboardButton("FLORES TIMUR", callback_data=f"5309"),
         InlineKeyboardButton("SIKKA", callback_data=f"5310")],
        [InlineKeyboardButton("ENDE", callback_data=f"5311"),
         InlineKeyboardButton("NGADA", callback_data=f"5312")],
        [InlineKeyboardButton("MANGGARAI", callback_data=f"5313"),
         InlineKeyboardButton("ROTE NDAO", callback_data=f"5314")],
        [InlineKeyboardButton("SUMBA TENGAH", callback_data=f"5316"),
         InlineKeyboardButton("SABU RAIJUA", callback_data=f"5320")],
        [InlineKeyboardButton("KOTA KUPANG", callback_data=f"5371")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def kalbar(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("SAMBAS", callback_data=f"6101"),
         InlineKeyboardButton("BENGKAYANG", callback_data=f"6102")],
        [InlineKeyboardButton("LANDAK", callback_data=f"6103"),
         InlineKeyboardButton("PONTIANAK", callback_data=f"6104")],
        [InlineKeyboardButton("SANGGAU", callback_data=f"6105"),
         InlineKeyboardButton("KETAPANG", callback_data=f"6106")],
        [InlineKeyboardButton("SINTANG", callback_data=f"6107"),
         InlineKeyboardButton("KAPUAS HULU", callback_data=f"6108")],
        [InlineKeyboardButton("SEKADAU", callback_data=f"6109"),
         InlineKeyboardButton("MELAWI", callback_data=f"6110")],
        [InlineKeyboardButton("KUBU RAYA", callback_data=f"6112"),
         InlineKeyboardButton("KOTA PONTIANAK", callback_data=f"6171")],
        [InlineKeyboardButton("KOTA SINGKAWANG", callback_data=f"6172")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def kalteng(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("KOTAWARINGIN BARAT", callback_data=f"6201"),
         InlineKeyboardButton("KOTAWARINGIN TIMUR", callback_data=f"6202")],
        [InlineKeyboardButton("KAPUAS", callback_data=f"6203"),
         InlineKeyboardButton("BARITO SELATAN", callback_data=f"6204")],
        [InlineKeyboardButton("BARITO UTARA", callback_data=f"6205"),
         InlineKeyboardButton("SUKAMARA", callback_data=f"6206")],
        [InlineKeyboardButton("LAMANDAU", callback_data=f"6207"),
         InlineKeyboardButton("SERUYAN", callback_data=f"6208")],
        [InlineKeyboardButton("KATINGAN", callback_data=f"6209"),
         InlineKeyboardButton("PULANG PISAU", callback_data=f"6210")],
        [InlineKeyboardButton("GUNUNG MAS", callback_data=f"6211"),
         InlineKeyboardButton("BARITO TIMUR", callback_data=f"6212")],
        [InlineKeyboardButton("MURUNG RAYA", callback_data=f"6213"),
         InlineKeyboardButton("KOTA PALANGKA RAYA", callback_data=f"6271")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def kalsel(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("TANAH LAUT", callback_data=f"6301"),
         InlineKeyboardButton("KOTA BARU", callback_data=f"6302")],
        [InlineKeyboardButton("BANJAR", callback_data=f"6303"),
         InlineKeyboardButton("BARITO KUALA", callback_data=f"6304")],
        [InlineKeyboardButton("TAPIN", callback_data=f"6305"),
         InlineKeyboardButton("HULU SUNGAI SELATAN", callback_data=f"6306")],
        [InlineKeyboardButton("HULU SUNGAI TENGAH", callback_data=f"6307"),
         InlineKeyboardButton("HULU SUNGAI UTARA", callback_data=f"6308")],
        [InlineKeyboardButton("TABALONG", callback_data=f"6309"),
         InlineKeyboardButton("TANAH BUMBU", callback_data=f"6310")],
        [InlineKeyboardButton("BALANGAN", callback_data=f"6311"),
         InlineKeyboardButton("KOTA BANJARMASIN", callback_data=f"6371")],
        [InlineKeyboardButton("KOTA BANJAR BARU", callback_data=f"6372")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def kaltim(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("KUTAI BARAT", callback_data=f"6402"),
         InlineKeyboardButton("KUTAI KARTANEGARA", callback_data=f"6403")],
        [InlineKeyboardButton("KUTAI TIMUR", callback_data=f"6404"),
         InlineKeyboardButton("BERAU", callback_data=f"6405")],
        [InlineKeyboardButton("PENAJAM PASER UTARA", callback_data=f"6409"),
         InlineKeyboardButton("KOTA BALIKPAPAN", callback_data=f"6471")],
        [InlineKeyboardButton("KOTA SAMARINDA", callback_data=f"6472"),
         InlineKeyboardButton("KOTA BONTANG", callback_data=f"6474")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def kaltara(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("MALINAU", callback_data=f"6501"),
         InlineKeyboardButton("BULUNGAN", callback_data=f"6502")],
        [InlineKeyboardButton("NUNUKAN", callback_data=f"6504"),
         InlineKeyboardButton("KOTA TARAKAN", callback_data=f"6571")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def sulut(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("BOLAANG MENGONDOW", callback_data=f"7101"),
         InlineKeyboardButton("MINAHASA", callback_data=f"7102")],
        [InlineKeyboardButton("KEPULAUAN SANGIHE", callback_data=f"7103"),
         InlineKeyboardButton("KEPULAUAN TALAUD", callback_data=f"7104")],
        [InlineKeyboardButton("MINAHASA SELATAN", callback_data=f"7105"),
         InlineKeyboardButton("MINAHASA UTARA", callback_data=f"7106")],
        [InlineKeyboardButton("BOLAANG MONGONDOW UTARA", callback_data=f"7107"),
         InlineKeyboardButton("MINAHASA TENGGARA", callback_data=f"7109")],
        [InlineKeyboardButton("BOLAANG MONGONDOW SELATAN", callback_data=f"7110"),
         InlineKeyboardButton("KOTA MANADO", callback_data=f"7171")],
        [InlineKeyboardButton("KOTA BITUNG", callback_data=f"7172"),
         InlineKeyboardButton("KOTA TOMOHON", callback_data=f"7173")],
        [InlineKeyboardButton("KOTA KOTAMOBAGU", callback_data=f"7174")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)


def sulteng(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("BANGGAI", callback_data=f"7202"),
         InlineKeyboardButton("MOROWALI", callback_data=f"7203")],
        [InlineKeyboardButton("POSO", callback_data=f"7204"),
         InlineKeyboardButton("DONGGALA", callback_data=f"7205")],
        [InlineKeyboardButton("TOLI-TOLI", callback_data=f"7206"),
         InlineKeyboardButton("BUOL", callback_data=f"7207")],
        [InlineKeyboardButton("PARIGI MOUTONG", callback_data=f"7208"),
         InlineKeyboardButton("TOJO UNA-UNA", callback_data=f"7209")],
        [InlineKeyboardButton("KOTA PALU", callback_data=f"7271")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)


def sulsel(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("Kepulauan Selayar", callback_data=f"7301"),
         InlineKeyboardButton("BULUKUMBA", callback_data=f"7302")],
        [InlineKeyboardButton("BANTAENG", callback_data=f"7303"),
         InlineKeyboardButton("JENEPONTO", callback_data=f"7304")],
        [InlineKeyboardButton("TAKALAR", callback_data=f"7305"),
         InlineKeyboardButton("GOWA", callback_data=f"7306")],
        [InlineKeyboardButton("SINJAI", callback_data=f"7307"),
         InlineKeyboardButton("BONE", callback_data=f"7308")],
        [InlineKeyboardButton("MAROS", callback_data=f"7309"),
         InlineKeyboardButton("PANGKAJENE KEPULAUAN", callback_data=f"7310")],
        [InlineKeyboardButton("BARRU", callback_data=f"7311"),
         InlineKeyboardButton("SOPPENG", callback_data=f"7312")],
        [InlineKeyboardButton("WAJO", callback_data=f"7313"),
         InlineKeyboardButton("SIDENRENG RAPPANG", callback_data=f"7314")],
        [InlineKeyboardButton("PINRANG", callback_data=f"7315"),
         InlineKeyboardButton("ENREKANG", callback_data=f"7316")],
        [InlineKeyboardButton("LUWU", callback_data=f"7317"),
         InlineKeyboardButton("TANA TORAJA", callback_data=f"7318")],
        [InlineKeyboardButton("LUWU UTARA", callback_data=f"7322"),
         InlineKeyboardButton("LUWU TIMUR", callback_data=f"7325")],
        [InlineKeyboardButton("TORAJA UTARA", callback_data=f"7326"),
         InlineKeyboardButton("KOTA MAKASSAR", callback_data=f"7371")],
        [InlineKeyboardButton("PARE-PARE", callback_data=f"7372"),
         InlineKeyboardButton("KOTA PALOPO", callback_data=f"7373")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)


def sultra(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("BUTON", callback_data=f"7401"),
         InlineKeyboardButton("MUNA", callback_data=f"7402")],
        [InlineKeyboardButton("KONAWE", callback_data=f"7403"),
         InlineKeyboardButton("KOLAKA", callback_data=f"7404")],
        [InlineKeyboardButton("KONAWE SELATAN", callback_data=f"7405"),
         InlineKeyboardButton("BOMBANA", callback_data=f"7406")],
        [InlineKeyboardButton("WAKATOBI", callback_data=f"7407"),
         InlineKeyboardButton("KOLAKA UTARA", callback_data=f"7408")],
        [InlineKeyboardButton("BUTON UTARA", callback_data=f"7409"),
         InlineKeyboardButton("KONAWE UTARA", callback_data=f"7410")],
        [InlineKeyboardButton("KOTA KENDARI", callback_data=f"7471"),
         InlineKeyboardButton("KOTA BAU-BAU", callback_data=f"7472")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def gorontalo(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("BOALEMO", callback_data=f"7501"),
         InlineKeyboardButton("GORONTALO", callback_data=f"7502")],
        [InlineKeyboardButton("POHUWATO", callback_data=f"7503"),
         InlineKeyboardButton("BONE BOLANGO", callback_data=f"7504")],
        [InlineKeyboardButton("GORONTALO UTARA", callback_data=f"7505"),
         InlineKeyboardButton("KOTA GORONTALO", callback_data=f"7571")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def sulbar(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("MAJENE SULBAR", callback_data=f"7601"),
         InlineKeyboardButton("POLEWALI MANDAR", callback_data=f"7602")],
        [InlineKeyboardButton("MAMASA SULBAR", callback_data=f"7603"),
         InlineKeyboardButton("MAMUJU SULBAR", callback_data=f"7604")],
        [InlineKeyboardButton("MAMUJU UTARA SULBAR", callback_data=f"7605")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def maluku(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("MALUKU TENGGARA BARAT", callback_data=f"8101"),
         InlineKeyboardButton("MALUKU TENGGARA", callback_data=f"8102")],
        [InlineKeyboardButton("MALUKU TENGAH", callback_data=f"8103"),
         InlineKeyboardButton("BURU", callback_data=f"8104")],
        [InlineKeyboardButton("KEP. ARU", callback_data=f"8105"),
         InlineKeyboardButton("SERAM BAGIAN BARAT", callback_data=f"8106")],
        [InlineKeyboardButton("SERAM BAGIAN TIMUR", callback_data=f"8107"),
         InlineKeyboardButton("MALUKU BARAT DAYA", callback_data=f"8108")],
        [InlineKeyboardButton("BURU SELATAN", callback_data=f"8109"),
         InlineKeyboardButton("KOTA AMBON", callback_data=f"8171")],
        [InlineKeyboardButton("KOTA TUAL", callback_data=f"8172")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def maltara(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("HALMAHERA BARAT", callback_data=f"8201"),
         InlineKeyboardButton("HALMAHERA TENGAH", callback_data=f"8202")],
        [InlineKeyboardButton("HALMAHERA SELATAN", callback_data=f"8204"),
         InlineKeyboardButton("HALMAHERA UTARA", callback_data=f"8205")],
        [InlineKeyboardButton("HALMAHERA TIMUR", callback_data=f"8206"),
         InlineKeyboardButton("MOROTAI", callback_data=f"8207")],
        [InlineKeyboardButton("KOTA TERNATE", callback_data=f"8271"),
         InlineKeyboardButton("Kepulauan Tidore", callback_data=f"8272")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def papua(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("FAK-FAK", callback_data=f"9101"),
         InlineKeyboardButton("KAIMANA", callback_data=f"9102")],
        [InlineKeyboardButton("TELUK WONDAMA", callback_data=f"9103"),
         InlineKeyboardButton("TELUK BINTUNI", callback_data=f"9104")],
        [InlineKeyboardButton("MANOKWARI", callback_data=f"9105"),
         InlineKeyboardButton("SORONG SELATAN", callback_data=f"9106")],
        [InlineKeyboardButton("SORONG", callback_data=f"9107"),
         InlineKeyboardButton("RAJA AMPAT", callback_data=f"9108")],
        [InlineKeyboardButton("KOTA SORONG", callback_data=f"9171")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

def papuabarat(update: update, context: CallbackContext) -> None:
    query = update.callback_query
    keyboard = [
        [InlineKeyboardButton("MERAUKE", callback_data=f"9201"),
         InlineKeyboardButton("JAYAWIJAYA", callback_data=f"9202")],
        [InlineKeyboardButton("JAYAPURA", callback_data=f"9203"),
         InlineKeyboardButton("NABIRE", callback_data=f"9204")],
        [InlineKeyboardButton("BIAK NUMFOR", callback_data=f"9205"),
         InlineKeyboardButton("KEPULAUAN YAPEN", callback_data=f"9208")],
        [InlineKeyboardButton("ADM. PANIAI", callback_data=f"9210"),
         InlineKeyboardButton("PUNCAK JAYA", callback_data=f"9211")],
        [InlineKeyboardButton("MIMIKA", callback_data=f"9212"),
         InlineKeyboardButton("BOVEN DIGOEL", callback_data=f"9213")],
        [InlineKeyboardButton("MAPPI", callback_data=f"9214"),
         InlineKeyboardButton("ASMAT", callback_data=f"9215")],
        [InlineKeyboardButton("YAHUKIMO", callback_data=f"9216"),
         InlineKeyboardButton("PEGUNUNGAN BINTANG", callback_data=f"9217")],
        [InlineKeyboardButton("KEEROM", callback_data=f"9220"),
         InlineKeyboardButton("SUPIORI", callback_data=f"9227")],
        [InlineKeyboardButton("MAMBERAMO RAYA", callback_data=f"9228"),
         InlineKeyboardButton("LANNY JAYA", callback_data=f"9230")],
        [InlineKeyboardButton("KOTA JAYAPURA", callback_data=f"9271")],
        [InlineKeyboardButton("Kembali", callback_data="10")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    context.bot.edit_message_text(chat_id=query.message.chat_id, message_id=query.message.message_id, text="Silahkan pilih Kota/Kabupaten:", reply_markup=reply_markup)

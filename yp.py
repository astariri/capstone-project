listYP=[
    {'number': '6', 'index': 'f', 'nama_depan': 'Benjamin', 'nama_belakang': 'Williams', 'telepon': '291857463012'},
    {'number': '20', 'index': 't', 'nama_depan': 'Charlotte', 'nama_belakang': 'Jhoynes', 'telepon': '504198327615'},
    {'number': '4', 'index': 'd', 'nama_depan': 'Daniel', 'nama_belakang': 'Browny', 'telepon': '136970845281'},
    {'number': '5', 'index': 'e5', 'nama_depan': 'Emilys', 'nama_belakang': 'Miller', 'telepon': '927345610854'},
    {'number': '2', 'index': 'b', 'nama_depan': 'Finnss', 'nama_belakang': 'Davish', 'telepon': '465812397064'},
    {'number': '7', 'index': 'g', 'nama_depan': 'Gracey', 'nama_belakang': 'García', 'telepon': '839710254618'},
    {'number': '8', 'index': 'h', 'nama_depan': 'Henriy', 'nama_belakang': 'Rodriguez', 'telepon': '571408239176'},
    {'number': '26', 'index': 'z', 'nama_depan': 'Isabella', 'nama_belakang': 'Martinez', 'telepon': '620497318554'},
    {'number': '10', 'index': 'j', 'nama_depan': 'Jackson', 'nama_belakang': 'Martinez', 'telepon': '193856472108'},
    {'number': '15', 'index': 'o', 'nama_depan': 'Katherine', 'nama_belakang': 'Williams', 'telepon': '345218790643'},
    {'number': '12', 'index': 'l', 'nama_depan': 'Lhiamz', 'nama_belakang': 'Rodriguez', 'telepon': '978603124586'},
    {'number': '19', 'index': 's', 'nama_depan': 'Madison', 'nama_belakang': 'Johnson', 'telepon': '612430875194'},
    {'number': '14', 'index': 'n', 'nama_depan': 'Nooaah', 'nama_belakang': 'Davish', 'telepon': '874695312080'},
    {'number': '11', 'index': 'k', 'nama_depan': 'Olivia', 'nama_belakang': 'García', 'telepon': '305217896341'},
    {'number': '24', 'index': 'x', 'nama_depan': 'Parker', 'nama_belakang': 'Rodriguez', 'telepon': '687943120854'},
    {'number': '17', 'index': 'q', 'nama_depan': 'Quinns', 'nama_belakang': 'Martinez', 'telepon': '519278634040'},
    {'number': '18', 'index': 'r', 'nama_depan': 'Riyaan', 'nama_belakang': 'Jonesh', 'telepon': '874031529618'},
    {'number': '13', 'index': 'm', 'nama_depan': 'Sophia', 'nama_belakang': 'Martinez', 'telepon': '152397486095'},
    {'number': '25', 'index': 'y', 'nama_depan': 'Ummmaa', 'nama_belakang': 'Jonesh', 'telepon': '431087965284'},
    {'number': '22', 'index': 'v', 'nama_depan': 'Victor', 'nama_belakang': 'Martinez', 'telepon': '825314907463'},
    {'number': '3', 'index': 'c', 'nama_depan': 'Theodore', 'nama_belakang': 'García', 'telepon': '678245931420'},
    {'number': '23', 'index': 'w', 'nama_depan': 'Willow', 'nama_belakang': 'Rodriguez', 'telepon': '364512890734'},
    {'number': '16', 'index': 'p', 'nama_depan': 'Xander', 'nama_belakang': 'Williams', 'telepon': '790643185274'},
    {'number': '21', 'index': 'u', 'nama_depan': 'Yharaa', 'nama_belakang': 'García', 'telepon': '514907632081'},
    {'number': '1', 'index': 'a', 'nama_depan': 'Abigail', 'nama_belakang': 'Johnson', 'telepon': '702648319518'},
    {'number': '9', 'index': 'i', 'nama_depan': 'Zanney', 'nama_belakang': 'Johnson', 'telepon': '630185274194'},
]

def read_list() :
    print('List Yellow Pages\n')
    print('No\t| Index\t| Nama Depan\t| Nama Belakang\t| No.Telepon')
    for i in range(len(listYP)) :
        print('{}\t| {}\t| {}\t| {}\t| {}\t'.format(listYP[i]['number'],listYP[i]['index'],listYP[i]['nama_depan'],listYP[i]['nama_belakang'],listYP[i]['telepon']))

def add_list() :
    no = int(input('Masukkan Nomor Urut : '))
    index = input('Masukkan huruf pertama (index) : ')
    nd = input('masukkan Nama depan : ')
    nb = input('Masukkan Nama Belakang : ')
    telp = input('Masukkan Nomor Telepon : ')
    listYP.append({
        'number': no,
        'index': index,
        'nama_depan': nd,
        'nama_belakang' : nb,
        'telepon' : telp
    })
    read_list()

def delete_list() :
    read_list()
    no = int(input('Masukkan nomor list yang ingin dihapus : '))
    index_to_delete = None
    for i, item in enumerate(listYP):
        if(int(item['number']) == no) :
            index_to_delete = i
            break
    if index_to_delete is not None:
        del listYP[index_to_delete]
        print(f'data dengan nomor {no} telah dihapus.')
    else:
        print(f'data dengan nomor {no} tidak ditemukan.')
   
def edit_list() :
    read_list()
    no = int(input('Masukkan nomor list yang ingin diedit : '))
    telp = int(input('Masukkan nomor telepon terbaru : '))

    index_to_edit = None
    for i, item in enumerate(listYP):
        if(int(item['number']) == no) :
            index_to_edit = i
            break
    if index_to_edit is not None:
        listYP[i]['telepon']=telp
        print(f'data dengan nomor {no} telah diedit.')
    else:
        print(f'data dengan nomor {no} tidak ditemukan.')


def sort_list() :
    listYP.sort(key=lambda x: x['index'])
    read_list()


while True :
    menuUtama = input('''
        Halo, ada yang bisa Yellow Pages bantu?

        List Menu :
        1. Menampilkan List
        2. Menambah List
        3. Menghapus List
        4. Merubah Data List
        5. Urutankan Dari List A-Z
        6. Keluar dari Yellow Pages

        Masukkan angka Menu yang ingin dijalankan : ''')
    
    if(menuUtama == '1') :
        menuChild = input('''
            List Menu :
            1. Menampilkan List
            2. Keluar dari Menu Ini
            Masukkan Huruf Menu yang ingin dijalankan : ''')

        if(menuChild == '1') :
            read_list()

    elif(menuUtama == '2') :
        menuChild = input('''
            List Menu :
            1. Menambahkan List
            2. Keluar dari Menu Ini
            Masukkan Huruf Menu yang ingin dijalankan : ''')

        if(menuChild == '1') :
            add_list()

    elif(menuUtama == '3') :
        menuChild = input('''
            List Menu :
            1. Menghapus List
            2. Keluar dari Menu Ini
            Masukkan Huruf Menu yang ingin dijalankan : ''')

        if(menuChild == '1') :
            delete_list()

    elif(menuUtama == '4') :
        menuChild = input('''
            List Menu :
            1. Merubah Data List
            2. Keluar dari Menu Ini
            Masukkan Huruf Menu yang ingin dijalankan : ''')

        if(menuChild == '1') :
            edit_list()
    
    elif(menuUtama == '5') :
        menuChild = input('''
            List Menu :
            1. Urutkan Data List
            2. Keluar dari Menu Ini
            Masukkan Huruf Menu yang ingin dijalankan : ''')

        if(menuChild == '1') :
            sort_list()

    elif(menuUtama == '6') :
        break

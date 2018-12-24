import fut

session = fut.core.Core('edoardodenigris2@gmail.com', 'Alicante2018', 'Latina', platform='ps4')
# my_team = session._usermassinfo['squad']['players']
# session._usermassinfo['squad']['manager']
club = session.club(ctype='staff')

#find asset id staff management
for items in club:
    if items['itemType'] != 'manager':
        if items['rareflag'] == 1:
            if items['untradeable'] == False:
                print(items)
                print(items['assetId'])

auction_players = session.searchAuctions('staff', max_buy=200)
rare_pl = []
cnt = 1
nations_number = 200
max_n_pages = 10
#asset_id = 100188

list_of_managers= [1001880, 1000452, 1002137, 1000074, 1000076, 1000320, 1000128, 1001135, 1000121, 1000274, 1000044,
                    1000174, 1000353, 1000248, 1001046, 1001247, 1001379, 1001557, 1002109, 1000247, 1000448, 1000524,
                    1000528, 1000530, 1000532, 1000957, 1001920, 1000693, 1001045, 1000543, 1000506, 1000538, 1000367,
                    1002064, 1000517, 1000450, 1000520, 1000546, 1000417, 1000961, 1000523, 1000861, 1000264, 1000507,
                    1000067, 1000113, 1000156, 1000256, 1001042, 1000068, 1000097, 1002197, 1000009, 2000236, 3000303,
                    4000358, 4000357, 2000128,2000339, 2000264, 2000266, 4000357,2000287, 2000256, 2000064, 2000252,
                    2000248, 2000260, 2000315, 2000326, 2000310, 2000228, 2000224, 2000328, 2000314, 2000232, 2000232,
                    9000173, 9000258, 9000221, 9000117, 9000237, 9000323, 9000257, 9000245, 9000308,9000025, 9000324,
                    9000157, 9000169]




while len(rare_pl)== 0:
    print('trial ' + str(cnt))
    cnt += 1
    for ids in list_of_managers:
        sess = session.searchAuctions('staff', max_buy=200, assetId=ids)
        if len(sess) > 0:
            for item in sess:
                if item['rareflag'] == 1:
                    print('FOUND...')
                    trade_id = item['tradeId']
                    session.bid(trade_id, 200)
                    print('SELL...')
                    session.quickSell(item['id'])

quit()
# 21452

##########################

"""

while len(rare_pl)== 0:
    for j in range(nations_number):
       print('nationality number: ' + str(j))
       for k in range(max_n_pages):
           print('     page n: ' + str(k))
           sess = session.searchAuctions('staff', max_buy=200, level='gold', nationality=j, start=k)
           for i in sess:
                if len(sess) > 0:
                    print('          trial ' + str(cnt))
                    cnt +=1
                    if i['rareflag'] == 1 and i['itemType'] == 'manager':
                        rare_pl.append(i)

                else:
                    print('          next')

for i in rare_pl:
    item = rare_pl[0]
    trade_id = item['tradeId']
    session.bid(trade_id, 200)
    quit()
"""
# list of managers= [1001880, 1000452, 1002137, 1000074, 1000076, 1000320, 1000128, 1001135, 1000121, 1000274, 1000044,
#                    1000174, 1000353, 1000248, 1001046, 1001247, 1001379, 1001557, 1002109, 1000247, 1000448, 1000524,
#                    1000528, 1000530, 1000532, 1000957, 1001920, 1000693, 1001045, 1000543, 1000506, 1000538, 1000367,
#                    1002064, 1000517, 1000450, 1000520, 1000546, 1000417, 1000961, 1000523, 1000861, 1000264, 1000507,
#                    1000067, 1000113, 1000156, 1000256, 1001042, 1000068, 1000097, 1002197, 1000009,
# Abel,Gasperini, Gerrard, Rui Vitoria, S.Concecao, Marco Silva, Nuno, Josè Peseiro, Mourinho, Semin, Hodgson,
# Dyche, Howe, Pioli, Ballardini, Inzaghi, Gattuso, Carrera, D'Anna, Allegri, Sarri, Marcelino, Bordalas, Abelardo
# Garitano, Mendilibar, Calleja, Lopetegui, Eusebio, Machin, Valverde, Rubi, Jokanovic,, Paco Lopez, Gracia, Benitez
# Emery, Setièn, Guardiola, Holan, Berizzo, Pellegrino, Mohamed, Simeone,, Pochettino, Terim, Avci, Gunes, Wagner,
# Hughes, Cocu, Khatsevic, Pellegrini,

# staffmanagement= [Quian, Lopes, Serpescu, Schiopiu, Jaramillo, Gazzola, Reeder, Adamescu, Schmidt, Shaikh, Lockhart,
#                   Yuen, Walz, Murray, Humber, Burghelea, Vascencu, Spatarenco, Rivera, Mueller, Hoo, Tudor, Stanescu
# stafflist= [2000236, 3000303, 4000358, 4000357],2000128,2000339, 2000264,2000266, 4000357,2000287, 2000256, 2000064,
#             2000252, 2000248, 2000260, 2000315, 2000326, 2000310, 2000228, 2000224, 2000328, 2000314, 2000232]

#GKstaff= [2000232, 9000173, 9000258, 9000221, 9000117, 9000237, 9000323, 9000257, 9000245, 9000308,9000025, 9000324,
#          9000157, 9000169]
#GKstafflist = [Kuhn, Marks, Jones, Harrison, MacKay, Mynt,Beaudoin, York, Enrique, Lindstrom, Alecu, Doonan, Herbstreit,
#                Bowerman

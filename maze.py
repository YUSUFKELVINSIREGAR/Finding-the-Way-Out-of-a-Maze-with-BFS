labirin = [
    "############################ E ############################",
    "#                    #             #                      #",
    "#                    #             #                      #",
    "#                                                         #",
    "#                    #             #                      #",
    "####   #########   #################                      #",
    "#         #                    #                          #",
    "#         #                    #                          #",
    "#                                                         #",
    "#         #                    #                          #",
    "#         #                    #                          #",
    "#         ###   #########   ####################       ####",
    "#         #         #          #            #             #",
    "#         #         #          #            #             #",
    "#         #         #                       #             #",
    "#         #         #          #            #             #",
    "#         #         #          #            #             #",
    "###############   ########  ####            #             #",
    "#         #                    #            #             #",
    "#         #                    #            #             #",
    "#                              #            #             #",
    "#         #                    #            #             #",
    "#         #                                               #",
    "##################### S ###################################"
]

# Cari indeks 'S' dan 'E'
start_index = labirin.index("##################### S ###################################")
end_index = labirin.index("############################ E ############################")

# Ubah labirin sesuai dengan jalur yang diinginkan
for i in range(start_index + 1, end_index):
    row_list = list(labirin[i])
    if i != end_index - 1:
        row_list = row_list[:25] + '+' + row_list[26:]
    labirin[i] = ''.join(row_list)

# Cetak hasil labirin yang telah diubah
for row_list in labirin:
    print(row_list)

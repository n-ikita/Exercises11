from solution import Track, Album

track1 = Track('Parasite Eve', 'Bring Me The Horizon', '2:44', 2017, 'parasiteeve.mp3')
track2 = Track('Шахерезада', 'Натали', '3:18', 2000, 'Шахерезада-Натали.mp3')
track3 = Track('Faded', 'Crypto', '2:20', 2020, 'Faded-Crypto.mp3')

playlist = Album('Случайные треки', 2024)
playlist.add_track(track1)
playlist.add_track(track2)
playlist.add_track(track3)


exiting = False
while not exiting:
    print('\n'*100)
    playlist.print_info()

    operation = int(input('Выберите опцию: \n'
                          '1: Играть \n'
                          '2: Пауза \n'
                          '3: Стоп \n'
                          '4: Следующий трек\n'
                          '5: Выход \n'))
    if operation == 1:
        playlist.play()
    elif operation == 2:
        playlist.pause()
    elif operation == 3:
        playlist.stop()
    elif operation == 4:
        playlist.next_track()
    elif operation == 5:
        exiting = True

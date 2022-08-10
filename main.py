# what i want to do is to create a library for anime and manga first, then be able to add anime and manga to the library


lib = ['One Piece Anime', 'Gintama', 'SBR', 'One Piece Manga', 'Vinland Saga Manga', 'Berserk', 'CSM']
completed = ['AOT', 'Monster', 'Vagabond', 'Homunculus', 'Jojo Anime', 'Kotaro lives alone', 'Ajin', 'Bleach Anime', 'Fire force Anime'
, 'Vinland Saga Anime', 'That time I got reincarnated as a slime S1', 'Akame Ga Kill', 'AOT Junior High', 'JJK Anime', 'OPM Anime S1', 
'Tokyo Revengers Anime S1', 'Akira Movie', 'Blue Exorcist', 'Demon Slayer Mugen Train', 'Demon Slayer Anime S1', 'Bunny Girl Senpai S1',
'Your Name', 'All of Dragon Ball', 'MHA Anime S1, S2, S3 , S4', 'Saiki K'
]

question = input('Would you like to add another animanga? (Y,N) ').upper()
if question == 'Y':
    y = input('Which animanga would you like to add? ')
    lib.append(y)
    print(f'You have now added {y} to your library! Make sure you put it in your text editor.')
    lib_question = input('Would you like to see your library? (Y,N) ').upper()
    if lib_question == 'Y':
        print(f'Here is your library')
        print(lib)
    else:
        print('Goodbye!')
else:
    comp_y = input('Would you like to add an animanga to completed? (Y,N)')
    if comp_y == 'Y':
        comp_branch = input('Which animanga would you like to be set as completed? ')
        completed.append(comp_branch)
        lib.remove(comp_branch)
    else:
        print('Goodbye!')
        

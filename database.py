#PCD (Pokemon Card Database) 0.7

import time
import pickle  #Built-in module which is used for save and load programs (Not like a pickle)

cards = []
message = ''
input_user = ''

print('Welcome to the PCD Command Prompt, or the Pokemon Card Database')
print('type commands or help to get more information')

while input_user != 'logout':
    input_user = input('')
    if input_user == 'add':
        message = input('<Add Pokemon card to database>')
        cards.append(message)
        print('[ADDING]')
        time.sleep(2)
        print('[ADDED] Your Card has been added to database.')
        message = ''
        input_user = ''
        print('')
    if input_user == 'showcards':
        for pokemon in cards:
            print(pokemon)
        print('')
        input_user = ''
    if input_user == 'commands':
        print('Ok, here are some of the commands, more will be added')
        print('')
        print('add - Adds Pokemon Card to the database')
        print('showcards - Shows the cards that you have added to the database')
        print('save - Saves your cards to a data file in the disk')
        print('load - Loads your cards from the disk to the command prompt')
        print('searchcard - Searches for a card that you have added')
        print('logout - Terminates the database')
        print('removecard - removes your card from the database')
        print('')
        input_user = ''
    if input_user == 'save':
        pickle.dump(cards, open("cards.dat", "wb"))
        print('SAVED')
    if input_user == 'load':
        cards = pickle.load(open("cards.dat", "rb"))
        print('LOADED')
    if input_user == 'help':
        print('The PCD Command Prompt is a application where you can store all of your Pokemon Cards.')
        print('You can search, add, and show the cards you have uploaded')
        print('Your data is stored in a file, which would come in handy for save and load commands.')
        print('')
    if input_user == 'searchcard':
        card = input('Type the card you want to search for on the database')
        print('Searching...')
        time.sleep(1)
        if card in cards:
            print(f'Your card: {card} is in the database.')
            print('')
        else:
            print('Your card is not available in the database. Perhaps you didnt add it?')
            print('')
    if input_user == 'removecard':
        card_remove = input('Type the card you want to remove from the database')
        if card_remove in cards:
            cards.remove(card_remove)
            print('Your card has been removed from Database')
        else:
            print('Cannot remove card because the card isnt in the database, please write the correct name.')

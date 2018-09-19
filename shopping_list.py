#make a list to hold onto our items
#print out instructions on how to use the app
#ask for new items
#add new items to our list
#be able to quit the app
#print out he list

shopp_list = [None]
while shopp_list [-1] != 'EXIT':

    if None in shopp_list:
        shopp_list.remove (None)

    shopp_list.append (input ('Enter the item: '))

    if shopp_list[-1] =='HELP':
        print ('Instructions how to use the app')


del shopp_list[-1]

for item in shopp_list:
    print (item)
#def loopy(items):
#    for item in items:
#        if item [0] != 'a':
#            print (item)
#            continue

#loopy (l_one)

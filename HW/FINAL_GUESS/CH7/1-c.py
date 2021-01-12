import pickle

# input
infile = open ("nationsDict.dat", 'rb')
nation_obj_dict = pickle.load (infile)
infile.close ()


# process
continent = input ("Enter a continent: ")
continent_nation_list = []
for nation in nation_obj_dict:
	if (nation_obj_dict[nation]._continent == continent):
		continent_nation_list.append (nation_obj_dict[nation])

## sort
continent_nation_list.sort (key = lambda x: x.popDensity (), reverse = True)


# output
for i in range (5):
	print ("  " + continent_nation_list[i]._nation)

import pickle

# input
infile = open ("nationsDict.dat", 'rb')
nation_obj_dict = pickle.load (infile)
infile.close ()


# output
nation = input ("Enter a country: ")
print ("Continent:", nation_obj_dict[nation]._continent)
print ("Population: {:,d}".format(int (nation_obj_dict[nation]._population * 1000000)))
print ("Area: {:,.2f} square miles".format (nation_obj_dict[nation]._area))

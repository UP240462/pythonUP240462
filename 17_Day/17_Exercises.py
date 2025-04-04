#1 names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia'].
#  Unpack the first five countries and store them in a variable nordic_countries,
#  store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
nordicCountries = names[:5]

# Storing Estonia and Russia in separate variables
es, ru = names[5], names[6]

# Display the results
print("Nordic countries:", nordicCountries)
print("Estonia:", es)
print("Russia:", ru)


# Making and Reading from Dictionaries Assignment
# Create a dictionary containing some information about yourself. The keys
# should include name, age, country of birth, and favorite language. Print out
# the result as in the example.

SELFDICT = {
    'name' : 'Nicki',
    'age' : '10',
    'country of birth' : 'Mongolia',
    'favorite langugage' : 'French'
}

def readOut(dictionary):
    for key, data in SELFDICT.iteritems():
        print 'My ' + key + ' is ' + data

readOut(SELFDICT)

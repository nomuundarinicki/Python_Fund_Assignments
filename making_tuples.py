MY_DICT = {
    "Speros": "(555) 555-5555",
    "Michael": "(999) 999-9999",
    "Jay": "(777) 777-7777"
}

# function
def dict_in_tuples_out(dictionary):
    tuple_list = []
    for key, data in dictionary.iteritems():
        tuple_list.append((key, data))
    print tuple_list

dict_in_tuples_out(MY_DICT)

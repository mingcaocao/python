shopping = {'apple': {'sss', 'hhh'}, 'pear': {'jjj', 'hhh'}, 'orange': 7}

def get_value(dict, Key, msg='Name'):
    Value = dict.get(Key, msg)
    return Value

def check_dict_contain(dict, Key):
    return Key in dict

def get_Keys(dict):
    return dict.Keys()

def get_values(dict):
    return dict.values()

def loop_over_dictionary(d):
    for element in d: #element is Key
        print element
        print d.get(element)

def add_or_edit_element(d, Key, Value):
    if Key not in d:
        d[Key] = Value # For edit:  if d.get("Key") == None:
                       #                d[Key] = d.get(Key) + Value
    return d

def delete_element(d, Key):
    del d[Key]
    return d

new_sh = {"apple": 7, "cookies": 6, "orange": 1}

print shopping.values()

print len(shopping)

shopping.get('apple').add('movie')
    

print shopping['apple']

print shopping

set.

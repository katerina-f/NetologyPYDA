documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def delete_doc_from_all(, dict1):
    user_input2 = input(‘введите номер документа‘)
    for list_ in list1:
        if user_input2 in list_.values():
            s = (list1.index(list_))
            del(list1[s])
        else:
            print(‘данного документа нет‘)
    for value in dict1.values():
        if user_input2 in value:
            d = value.index(user_input2)
            del(value[d])
        else:
            print(‘данного документа нет’)
    print(documents)
    print(directories)

delete_doc_from_all(documents, directories)

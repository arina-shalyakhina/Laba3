# TODO Напишите функцию для поиска индекса товара
def find_index(items_list, find_item):
    b=[]
    for e in items_list:
        if e==find_item and not e in b:
            b.append(e)
            c=items_list.index(e)
            return c
    if b==[]:
        return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

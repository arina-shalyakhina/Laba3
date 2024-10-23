def find_common_participants(participants_first_group, participants_second_group, s=','):
    a=participants_first_group.split(s)
    b=participants_second_group.split(s)
    c=[]
    for e in a:
        if e in b:
            c.append(e)
    e=sorted(c)
    return e

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, s='|'))

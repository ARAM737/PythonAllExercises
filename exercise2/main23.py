def f23(arr):
    for i in range(len(arr)):
        if arr[i][1] == None:
            del arr[i][1]

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][0] == "Выполнено":
                arr[i][0] = "true"
            if arr[i][0] == "Не выполнено":
                arr[i][0] = "false"

    for line in arr:
        eMail = line[2]
        eMail = eMail[line[2].index(']')+1:]
        line[2] = eMail
        name = line[1]
        name = ' '.join(name.split('.')[::-1])
        name = name[1:-2]
        line[1] = name


    for i in range(len(arr)):
            if arr[i][3]:
                num = arr[i][3]
                n = num[0] + num[1] + "/" + num[3] + num[4] + "/" + num[8] + num[9]
                arr[i][3] = n

    def sorting(sub_li):
        sub_li.sort(key=lambda x: x[1])
        return sub_li

    return sorting(arr)


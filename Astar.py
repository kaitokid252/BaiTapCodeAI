graph = {
        'A': {'C': 9,'D':7, 'E':13, 'F':20},
        'C': {'H':10},
        'D': {'E':4,'H':8},
        'E': {'K':4,'I':3},
        'K': {'B': 6},
        'H': {'K':5},
        'I': {'K':9,'B':5},
        'F': {'I':6,'G':4}
        }
heuristic = {
        'A': 14,
        'B': 0,
        'C': 15,
        'D': 6,
        'E': 8,
        'F': 7,
        'G': 12,
        'H': 10,
        'K': 2,
        'I': 4,
            }
def Astar(graph_to_seach, start, end):
    dict_f = {}                 #tạo ra dict lưu lại dữ liệu f(v) của từng điểm
    array=[]                       #tạo mảng lưu đường đi và g(u)
    array.append([[start],0])
    print("Thu tu duyet: ")       
    while(array):
        path=array.pop(0)           #lấy mảng đầu tiên
        node=path[0][-1]            #lấy vị trí cuối cùng
        print(node,end=' ')
        if node==end:
            print('\nDuong di la:',end=' ')
            return path[0]
        for adjacent in graph_to_seach.get(node,{}):
            new_path=list(path[0])
            check_round=path[1] + graph_to_seach[node][adjacent]                #tìm g(v)
            new_path.append(adjacent)
            save_path=[]
            save_path.append(new_path)                  #chèn đường đi
            save_path.append(check_round)               #chèn g(v)
            array.append(save_path)
        check_round_fail=[]
        for i in array:
            node_check=i[0][-1]
            if node_check not in dict_f:                #nếu chưa có f(v) thì lưu f(v) vào dict
                total_f = i[1] + heuristic[node_check]
                dict_f[node_check]=total_f
            else:
                total_f = i[1] + heuristic[node_check]          #kiểm tra xem f(v) có tốt hơn f(v) đang có không
                if(total_f < dict_f[node_check]):
                    dict_f[node_check]=total_f
                    for j in array:                             #nếu f(v) tốt hơn cái đang có thì xoá cái cũ và lưu lai f(v) tối ưu hơn
                        if (j[0][-1] == node_check and i!= j):
                            check_round_fail.append(j)
                elif(total_f > dict_f[node_check]):
                    array.remove(i)
        for j in check_round_fail:
            array.remove(j)
        for i in range(0,len(array)-1):                     #thực hiện sắp xếp tăng dần theo f(v)
            for j in range(i+1,len(array)):
                if(dict_f[array[i][0][-1]]> dict_f[array[j][0][-1]]):
                    a=array[i]
                    array[i]=array[j]
                    array[j]=a
                if(dict_f[array[i][0][-1]]==dict_f[array[j][0][-1]]):          #nếu f(v) bằng nhau thì xét đến g(v)
                    if(array[i][1]>array[j][1]):
                        a=array[i]
                        array[i]=array[j]
                        array[j]=a
        #print(array)
        #print(dict_f)
print(Astar(graph,'A','B'))
    


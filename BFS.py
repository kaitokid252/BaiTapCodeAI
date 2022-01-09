# graph là biểu diễn danh sách liền kề bằng dir
graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '3': ['7'],
        '5': ['7'],
        }
def bfs(graph_to_seach, start, end):
    # tạo một hàng đợi của đường đi
    queue = []
    # đưa điểm đâu tiên vào trong hàng đợi
    queue.append(start)
    visit =[]
    visit.append(start)
    print("Thu tu duyet: ")
    while queue:
        # lấy đường đi dầu tiên trong hàng đợi
        path = queue.pop(0)
        #print(path)
        # lấy vị trí cuối cùng trong đường đi
        node = path[-1]
        print(node,end=' ')
        # xuất đương đi đã tìm thấy
        if node == end:
            print("\nDuong di la: ",end=' ')
            return path
        # liệt kê các nút liền kề và tạo một đưỜng đi mới và thêm vào hàng đợi
        for adjacent in graph_to_seach.get(node,[]):
            if(adjacent not in visit):
                visit.append(adjacent)
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
print(bfs(graph, '1', '7'))
  

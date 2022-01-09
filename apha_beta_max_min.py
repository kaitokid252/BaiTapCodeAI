MAX, MIN = 1000, -1000
def minimax(depth, nodeIndex, maximizingPlayer,values, alpha, beta):
    
    if depth == 3:    #đến độ sâu giới hạn thì dừng lại và trả về giá trị của các nút đấy
        return values[nodeIndex]
    if maximizingPlayer:    #true là duyet max
        best = MIN
        #duyệt các nút 
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            # kiểm tra alpha,beta để cắt nhánh
            if beta <= alpha:
                break
        return best
    else:                       #false thì duyệt min
        best = MAX
        #duyệt các nút con
        for i in range(0, 2):
            val = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            # cắt nhánh
            if beta <= alpha:
                break
        return best
      
if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1] 
    print("The optimal value is :", minimax(0, 0, True, values, MIN, MAX))

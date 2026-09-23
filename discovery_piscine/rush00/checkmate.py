def checkmate(board_str):
    
    board = board_str.strip().split('\n')
    size = len(board)
    
    
    king_pos = None
    for r in range(size):
        for c in range(size):
            if board[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break
        
    
    if not king_pos:
        return

    kr, kc = king_pos

 
    straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    diagonal_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    # 1. ตรวจสอบแนวตรง (Rook และ Queen)
    for dr, dc in straight_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = board[r][c]
            if piece in ('R', 'Q'):
                print("Success")
                return
            elif piece != '.':
                break  
            r += dr
            c += dc

    for dr, dc in diagonal_dirs:
        r, c = kr + dr, kc + dc
        while 0 <= r < size and 0 <= c < size:
            piece = board[r][c]
            if piece in ('B', 'Q'):
                print("Success")
                return
            elif piece != '.':
                break  
            r += dr
            c += dc

    
    pawn_attack_positions = [(kr + 1, kc - 1), (kr + 1, kc + 1)]
    for r, c in pawn_attack_positions:
        if 0 <= r < size and 0 <= c < size:
            if board[r][c] == 'P':
                print("Success")
                return

    print("Fail")
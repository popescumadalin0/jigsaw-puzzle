class JigsawBoard:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.used_cells = [[False] * cols for _ in range(rows)]

    def is_cell_used(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.used_cells[row][col]
        return False

    def mark_cell_used(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.used_cells[row][col] = True

    def is_full(self):
        for row in self.used_cells:
            for cell in row:
                if not cell:
                    return False
        return True

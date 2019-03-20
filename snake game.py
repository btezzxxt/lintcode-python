from collections import deque
class SnakeGame:
    def __init__(self, width, height, foods):
        self.board = [[0 for i in range(width)] for j in range(height)]
        self.width = width
        self.height = height

        for food in foods:
            self.board[food[0]][food[1]] = 1
        
        self.snake = deque([(0, 0)])
        self.snake_body = set()
        self.snake_body.add((0,0))

        self.score = 0
        
    def move(self, direction):
        dx = [1, -1, 0, 0]
        dy = [0, 0, -1, 1]
        action = 0
        if direction == 'U':
            action = 0
        elif direction == 'D':
            action = 1
        elif direction == 'L':
            action = 2
        elif direction == 'R':
            action = 3
        else:
            return -999
        
        head = self.snake[0]
        head_next = (head[0] + dx[action], head[1] + dy[action])
        
        # out of wall
        if head_next[0] < 0 or head_next[0] >= self.height or head_next[1] < 0 or head_next[1] >= self.width:
            return -1
        
        # hit self
        if head_next in self.snake_body and head_next != self.snake[-1]:
            return -1
            
        # safe, move on 
        # no food
        if self.board[head_next[0]][head_next[1]] == 0:
            self.snake.pop()
            self.snake_body.remove(head_next)
            self.snake.appendleft(head_next)
            self.snake_body.add(head_next)
        # eat food
        else:
            self.snake.appendleft(head_next)
            self.snake_body.add(head_next)
            self.board[head_next[0]][head_next[1]] = 0
            self.score += 1
        return self.score

        
import background

tile_size = 50

class Niveau:
    def __init__(self, data):
        self.tile_list = []

        obs1 = background.load_image('samples/sol6.png', tile_size, tile_size)
        obs2 = background.load_image('samples/plateforme_2.png', tile_size, tile_size)
        obs3 = background.load_image('samples/plateforme_1.png', tile_size, tile_size)

        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1:
                    rect_x = col_count * tile_size
                    rect_y = row_count * tile_size
                    obs1_rect = background.obstacle_rect(obs1, rect_x, rect_y, tile_size, tile_size)
                    tile = (obs1, obs1_rect) 
                    self.tile_list.append(tile)
                if tile == 2:
                    rect_x = col_count * tile_size
                    rect_y = row_count * tile_size
                    obs2_rect = background.obstacle_rect(obs2, rect_x, rect_y, tile_size, tile_size)
                    tile = (obs2, obs2_rect) 
                    self.tile_list.append(tile)
                if tile == 3:
                    rect_x = col_count * tile_size
                    rect_y = row_count * tile_size
                    obs3_rect = background.obstacle_rect(obs3, rect_x, rect_y, tile_size, tile_size)
                    tile = (obs3, obs3_rect) 
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1    

    def draw(self,fenetre):
        for tile in self.tile_list:
            fenetre.blit(tile[0], tile[1])

    def list_rect(self):
        lst = []
        for tile in self.tile_list:
            lst.append(tile[1])
        return lst
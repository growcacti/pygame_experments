   def multioject(self):
         

 
         self.trows = total_rows'
        self.tcol = total_columns
        self.image = pg.image.load(filename).convert_alpha()
        self.o_rows = o_rows    #Number of rows of options in sprite total
        self.o_cols = o_cols    #Number of cols of options in sprite total
        self.rows = rows        #Number of rows for sprite chosen
        self.cols = cols        #Number of cols for sprite chosen
        self.p_rows = p_rows    #Row number of chosen sprite in sheet
        self.p_cols = p_cols    #Column number of chosen sprite in sheet
        
        self.totalCellCount = cols * rows #Total cells in the specific sprite option chosen
        
        self.option_w = self.image.get_rect().width / self.o_cols #Width of particular option in sheet
        self.option_h = self.image.get_rect().height / self.o_rows #Height of particular option in sheet
        
        self.offset_x = self.option_w * p_cols #Offset the X based on which option in the sheet
        self.offset_y = self.option_h * p_rows #Offset the Y based on which option in the sheet
        
        self.init_rect = pg.Rect(0, 0, self.option_w, self.option_h) #Form initial rectangle (before we break it up into cells)

        self.w = self.cellWidth = self.init_rect.width / cols
        self.h = self.cellHeight = self.init_rect.height / rows
        
          
        self.cells = []
        myCounter = 0
        
        for ry in range(0, rows):
            for rx in range(0,cols):
                self.cells.append(((myCounter % cols * self.w) + self.offset_x, (ry * self.h) + self.offset_y, self.w, self.h))
                myCounter += 1
                #print(self.cells)
        

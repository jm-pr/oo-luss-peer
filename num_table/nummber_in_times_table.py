class nummber_in_times_table:
    def __init__(self, x, y):
        self.location_in_table_x = x
        self.location_in_table_y = y
        self.multiplay = self.location_in_table_x * self.location_in_table_y
        self.new_line = ""


    def printeble_nummber(self):
        if self.location_in_table_y == 1:
            self.new_line = "\n"
        return(self.new_line + "|" + self.give_me_back_string_of_3_chars_from_int() + "|")

    def printeble_html_nummber(self):
        if self.location_in_table_y == 1:
            self.new_line = "<hr>"
        return(self.new_line + "|" + self.give_me_back_string_of_3_chars_from_int() + "|")

    def printeble_eqwision(self):
        return(str(self.location_in_table_x) + " X " + str(self.location_in_table_y) + " = " + str(self.multiplay))



    def give_me_back_string_of_3_chars_from_int(self):
        if self.multiplay < 10:
            return ("++"+ str(self.multiplay))
        if self.multiplay < 100:
            return ("+"+ str(self.multiplay))
        else:
            return str(self.multiplay)

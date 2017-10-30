# Created by: luca.ienzi
# Created on: oct 2017
# Created for: ICS3U
#  This program shows the circumfrance for what you imputed
import ui

def calculate_touch_up_inside(sender):
    PI = 3.14
    radius = int(view['radius_textbox'].text)
    circumfrence = 2 * PI * radius 
    view['answer_lable'].text = 'the circumfreance is:' + str(circumfrence) + "cm"
view = ui.load_view()
view.present('sheet')

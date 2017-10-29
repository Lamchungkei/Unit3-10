# Created by: Kay Lin
# Created on: 26th-Oct-2017
# Created for: ICS3U
# This program shows calculate average

import ui

answer = 0
counter = 0
average = 0

def calculate_touch_up_inside(sender):
    #input
    global answer
    global counter
    global average
    
    number = int(view['number_textfield'].text)
    
    #process
    if not (number == -1):	
        if  (0 <= number and number <= 100):
            answer = answer + number
            counter = counter + 1
            average = answer / counter
            view['current_average_label'].text = 'Your current average is: ' + str(average)
        else:
            view['answer_label'].text = 'Please input valid number.'
        
    else:
        view['answer_label'].text = 'Your final average is: ' + str(average)

view = ui.load_view()
view.present('full_sheet')

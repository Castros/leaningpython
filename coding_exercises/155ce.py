import PySimpleGUI as sg

label1 = sg.Text("Enter Feet:")
input1 = sg.Input()


label2 = sg.Text("Enter Inches:")
input2 = sg.Input()


convert_button = sg.Button("Convert")
window = sg.Window("Convertor",
                   layout=[[label1, input1],
                           [label2, input2],
                           [convert_button]
                           ])
window.read()
print("close")
window.close()
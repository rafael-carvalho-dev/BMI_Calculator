import PySimpleGUI as sg

def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI).

    Args:
        weight (float): The weight of the individual in kilograms.
        height (float): The height of the individual in meters.

    Returns:
        float: The calculated BMI.
    """
    bmi = weight / (height ** 2)
    return bmi

def evaluate_bmi_category(bmi):
    """
    Evaluate the BMI category based on the BMI value.

    Args:
        bmi (float): The Body Mass Index to categorize.

    Returns:
        str: The BMI category.
    """
    if bmi < 17:
        return 'Severe thinness'
    elif 17 <= bmi < 18.5:
        return 'Underweight'
    elif 18.5 <= bmi <= 24.9:
        return 'Normal'
    elif 25 <= bmi <= 29.9:
        return 'Overweight'
    elif 30 <= bmi <= 34.9:
        return 'Obese Class I'
    elif 35 <= bmi <= 39.9:
        return 'Obese Class II'
    else:
        return 'Obese Class III'


# Dictionary for mapping color categories
category_colors = {
    'Severe thinness': 'red',
    'Underweight': 'orange',
    'Normal': 'darkgreen',
    'Overweight': '#E2C909',
    'Obese Class I': 'orange',
    'Obese Class II': 'red',
    'Obese Class III': 'darkred'
}

# Graphic interface layout
layout = [
    [sg.Text('Weight: '), sg.InputText(key='-WEIGHT-')],
    [sg.Text('Height: '), sg.InputText(key='-HEIGHT-')],
    [sg.Button('Calculate'), sg.Button('Exit')],
    [sg.Text('Your BMI:', size=(15, 1)), 
     sg.Text('', size=(15, 1), key='-BMI-', text_color='black', background_color='#D3D3D3')],
    [sg.Text('BMI Category:', size=(15, 1)), 
     sg.Text('', size=(15, 1), key='-CATEGORY-', text_color='black', background_color='#D3D3D3')],
]

# Window creation
window = sg.Window('BMI Calculator', layout)

# Events loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == 'Calculate':
        try:
            weight = float(values['-WEIGHT-'])
            height = float(values['-HEIGHT-'])
            bmi = calculate_bmi(weight, height)
            category = evaluate_bmi_category(bmi)
            result_text_bmi = f'{bmi:.2f}'
            result_color = category_colors[category]
            result_text_category = category
        except ValueError:
            result_text_bmi = 'Invalid input'
            result_color = 'black'
            result_text_category = ''
        
        window['-BMI-'].update(result_text_bmi, text_color=result_color)
        window['-CATEGORY-'].update(result_text_category, text_color=result_color)
        
# window closure
window.close()

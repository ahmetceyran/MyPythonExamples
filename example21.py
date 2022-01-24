def get_wh():
    weight = float(input("Enter weight [pounds]: "))
    height = float(input("Enter height [inches]: "))
    return weight,height
def calc_bmi(weight,height):
    return 703 * weight / (height * height)
def show_bmi(bmi):
    print("Your body mass index is : ",bmi)

w,h=get_wh()
bmi=calc_bmi(w,h)
show_bmi(bmi)

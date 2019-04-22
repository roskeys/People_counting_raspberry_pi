from model import model
def predict(current_level,my_level,pressed_levels):
    ret = abs(current_level-my_level) * model.coef_[0] + pressed_levels * model.coef_[1] + model.intercept_
    return round(ret,2)
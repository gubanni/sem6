import re
 
 
actions = {
  "*": lambda x, y: str(float(x) * float(y)),
  "/": lambda x, y: str(float(x) / float(y)),
  "+": lambda x, y: str(float(x) + float(y)),
  "-": lambda x, y: str(float(x) - float(y))
}
 
priority_reg_exp = r"\((.+?)\)"
action_reg_exp = r"(-?\d+(?:\.\d+)?)\s*\{}\s*(-?\d+(?:\.\d+)?)"
 
 
 
def my_eval(expresion):
    while (match := re.search(priority_reg_exp, expresion)):
        expresion = expresion.replace(match.group(0), my_eval(match.group(1)))
        #print(match.group(0))
        #print(match.group(1))
    for symbol, action in actions.items():
        while (match := re.search(action_reg_exp.format(symbol), expresion)):
            expresion = expresion.replace(match.group(0), action(*match.groups()))
 
    return expresion
 
 
exp = input(f"Введите выражение которое нужно вычислить:")
print(f"Ответ: {my_eval(exp)}") 
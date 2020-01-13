def precedence(op): 
    if op == '^':
        return 3
    if op == '+' or op == '-': 
        return 1
    if op == '*' or op == '/': 
        return 2
    return 0


def applyOp(a, b, op): 
	if op == '^': return a ** b
	if op == '+': return a + b 
	if op == '-': return a - b 
	if op == '*': return a * b 
	if op == '/': return a // b 


def evaluate(tokens, x_set): 

    values = [[] for _ in range(len(x_set))]
    ops = [] 
    i = 0

    while i < len(tokens): 
 
        if tokens[i] == ' ': 
            i += 1
            continue
        
        elif tokens[i] == '(': 
            ops.append(tokens[i]) 
        
        elif tokens[i] in 'xX' :
            for index, x in enumerate(x_set):
                values[index].append(x)
                
        elif tokens[i].isdigit(): 
            val = 0
              
            while (i < len(tokens) and
                tokens[i].isdigit()): 
              
                val = (val * 10) + int(tokens[i]) 
                i += 1
            i -= 1
            for index, x in enumerate(x_set):
                values[index].append(val)
        
        elif tokens[i] == ')':
                                         
            while len(ops) != 0 and ops[-1] != '(': 
                op = ops.pop()
                for index, x in enumerate(values):
                    val2 = x.pop() 
                    val1 = x.pop() 
                    x.append(applyOp(val1, val2, op)) 

            ops.pop() 

        else: 

            while (len(ops) != 0 and
                precedence(ops[-1]) >= precedence(tokens[i])): 
                op = ops.pop() 
                for index, x in enumerate(values):
                    val2 = x.pop() 
                    val1 = x.pop() 
                    x.append(applyOp(val1, val2, op)) 
                
            ops.append(tokens[i]) 

        i += 1

    while len(ops) != 0: 
        op = ops.pop()
        for index, x in enumerate(values):
            val2 = x.pop() 
            val1 = x.pop() 
            x.append(applyOp(val1, val2, op))
    
    values = [value.pop() for value in values] 
    global one_one
    if len(list(set(values))) != len(values):
        one_one = False
    return values

set1 =[int(x) for x in input('Enter comma separated domain: ').split(',')]
set2 =[int(x) for x in input('Enter comma separated codomain: ').split(',')]
expression = input('(+,-,*,/,^) Enter expression in terms of x: ')
one_one = True
try:    
    results = evaluate(expression, set1)
    if set(results) == set(set2):
        print('ONTO')
    else:
        print('NOT ONTO')
    if one_one:
        print('ONE-ONE')
    else:
        print('NOT ONE-ONE')
except:
    print('Invalid expression')
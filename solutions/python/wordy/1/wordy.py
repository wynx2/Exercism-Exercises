def remove_non_essential(statement):
    no_question_mark = statement.rstrip('?').lower()
    no_by = no_question_mark.replace('by','')
    no_what = no_by.replace('what is','')
    return no_what

def compute_this(equation):
    if equation[1] == 'plus':
        return equation[0] + equation[2]
    if equation[1] == 'minus':
        return equation[0] - equation[2]
    if equation[1] == 'multiplied':
        return equation[0] * equation[2]
    if equation[1] == 'divided':
        return equation[0] // equation[2]

def answer(question):
    adjusted_question = remove_non_essential(question)
   
    string_holding = adjusted_question.split()
    operation_elements = []
    valid_operations = ['plus','minus','multiplied','divided']
    num_next = True
    operator_next = False

    for element_index in range(len(string_holding)):
        try:
            string_holding[element_index] = int(string_holding[element_index])
        except:
            continue
    
    for i in string_holding:
        if isinstance(i,int):
            if num_next:
                operation_elements.append(int(i))
                num_next = False
                operator_next = True
            else:
                raise ValueError('syntax error')
        elif i in valid_operations:
            if operator_next:
                operation_elements.append(i)
                operator_next = False
                num_next = True
            else:
                raise ValueError('syntax error')
        else:
            raise ValueError('unknown operation')
        

        if len(operation_elements) == 3:
            stored_result = compute_this(operation_elements)
            operation_elements.clear()
            operation_elements.append(stored_result)
            operator_next = True
            num_next = False
    if len(operation_elements) == 1:
        return operation_elements[0]
    raise ValueError('syntax error')        
            
                
            
                

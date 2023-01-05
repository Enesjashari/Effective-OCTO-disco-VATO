def arithmetic_arranger(problems, show_answers=False):
    # Check if there are too many problems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Initialize variables to store arranged problems and answers
    arranged_problems = []
    answers = []

    # Iterate through each problem
    for problem in problems:
        # Check if the problem contains a valid operator
        if problem[1] not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."

        # Split the operands and operator from the problem string
        operand1, operator, operand2 = problem.split()

        # Check if the operands contain only digits
        if not (operand1.isdigit() and operand2.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check if the operands are more than four digits in width
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the answer to the problem
        answer = str(eval(problem))

        # Store the answer to the problem
        answers.append(answer)

        # Determine the maximum width of the operands
        max_width = max(len(operand1), len(operand2))

        # Add spaces to operands to align them
        operand1 = operand1.rjust(max_width + 1)
        operand2 = operand2.rjust(max_width + 1)

        # Build the arranged problem string
        arranged_problem = operand1 + '    ' + operand2 + '\n' + operator + ' ' + '-'*max_width + '    ' + operator + ' ' + '-'*max_width + '\n'

        # Add the arranged problem to the list of arranged problems
        arranged_problems.append(arranged_problem)

    # Join the arranged problems into a single string
    arranged_problems = '\n'.join(arranged_problems)

    # If the show_answers flag is set, append the answers to the arranged problems string
    if show_answers:
        answers = [answer.rjust(max_width) for answer in answers]
        arranged_problems += '\n' + '    '.join(answers)

    return arranged_problems

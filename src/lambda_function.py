import boto3
import json
import time

from types import ModuleType

def lambda_handler(event, context):
    is_correct = False
    status_code_ok = 200

    def test_executor(executable_module, task_id):
        try:
            if task_id == "1":
                _field_value = 3
                testSquare = executable_module.Square(_field_value, _field_value, _field_value)
                assert testSquare.cell_size == _field_value, "Something is wrong with cell_size"
                assert testSquare.x_position == _field_value, "Something is wrong with x_position"
                assert testSquare.y_position == _field_value, "Something is wrong with y_position"
            elif task_id == "2":
                _cell_size = 30
                testCell = executable_module.Cell()
                assert testCell.cell_size == 30, "Your cell_size is incorrect"
                assert testCell.color == (0, 0, 0), "Your color is incorrect"
                assert testCell.display_window, "You did not create a display_window"
            elif task_id == "3":
                _length = 10
                snake = executable_module.Snake(_length)
                assert snake.getLength() == 10, "You did not properly create the getLength method"
            elif task_id == "4":
                _vector = 10
                snake = executable_module.Snake(0, _vector)
                assert snake.go_up() == "Going Up", "You did not properly check if the snake is already moving up. Be sure to return Going Up as well"
                snake2 = executable_module.Snake(_vector, -_vector)
                snake2.go_up()
                assert snake2.x_vector == 0, "Your snake is moving diagonally! Change the x_vector to 0"
                assert snake2.y_vector == 10, "Your snake is not moving up"
            elif task_id == "5":
                snake = executable_module.Snake()
                snake.add_cell()
                assert snake.length == 6, "You did not properly change the length increment of the snake"
            elif task_id == "6":
                test = executable_module.detailsOfGame()
                assert test.show_menu() == "Showing menu", "You did not properly inherit/detail the abstract method show_menu"
                assert test.start() == "Starting game!", "You did not properly inherit/detail the abstract method start"
            elif task_id == "7":
                snake = executable_module.badSnake()
                assert snake.movement() == "I do not move at all", "You did not properly inherit the Snake class"
            else:
                return False
        except AssertionError as e:
            return str(e)
        except:
            return False
        return True
        
    def execute_input(user_input):
        try:
            compiled = compile(user_input, '', 'exec')
            module = ModuleType("inputmodule")
            exec(compiled, module.__dict__)
            return module
        except:
            pass
        
    def check_correction(user_input, task_id):
        is_correct = False
        message = 'Task failed! Please try again.'
        executable_module = execute_input(user_input)
        if executable_module is not None:
            output = test_executor(executable_module, task_id)
            if isinstance(output, str):
                message = output
                is_correct = False
            elif output == True:
                is_correct = True
                message = 'Task passed!'
        return is_correct, message

    method = event.get('httpMethod',{})
    if method == 'GET':
        with open('index.html', 'r') as f:
            return {
                "statusCode": status_code_ok,
                "headers": {
                'Content-Type': 'text/html',
                },
                "body": f.read()
            }
            
    if method == 'POST': 
        postReq = json.loads(event.get('body', {}))
        try:
            editable = postReq["editable"]["0"].strip()
            userToken = postReq["userToken"].strip()
            hidden = postReq["hidden"]["0"].strip()
            shown = postReq["shown"]["0"].strip()
            
            is_correct, message = check_correction(editable, hidden)

            client = boto3.resource('dynamodb')
            table = client.Table('bt3103-solutions')
            table.put_item(
                Item={
                    'solution_id': str(round(time.time() * 1000)),
                    'input': editable,
                    'result': is_correct,
                    'message': message,
                    'user_token': userToken,
                    'task_id': hidden,
                    'time': time.ctime(),
                }
            )

        except Exception as e:
            pass
        
    return {
        'statusCode': status_code_ok,
        'headers': {
          "Access-Control-Allow-Credentials": True,
          "Access-Control-Allow-Origin": "*",
          "Content-Type": "application/json",
        },
        'body': json.dumps(
            {
                "isComplete": is_correct,
                "jsonFeedback": { "test": is_correct, "message": message },
                "htmlFeedback": "<div>Test: " + str(is_correct) + "</div><br/><div>Message: " + str(message) + "</div>",
                "textFeedback": "Test: " + str(is_correct) + "  Message: " + str(message),
            }
        )
    }

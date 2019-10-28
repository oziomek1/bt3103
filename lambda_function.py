import json
from types import ModuleType

def lambda_handler(event, context):
    is_correct = False
    status_code_ok = 200

    def test_module(executable_module, task_id):
        if task_id == "1":
            try:
                _field_value = 3
                testSquare = executable_module.Square(_field_value, _field_value, _field_value)
                assert testSquare.cell_size == _field_value, "Something is wrong with cell_size"
                assert testSquare.x_position == _field_value, "Something is wrong with x_position"
                assert testSquare.y_position == _field_value, "Something is wrong with y_position"
            except:
                return False
            return True
        else:
            return False
        
    def execute_input(user_input):
        try:
            compiled = compile(user_input, '', 'exec')
            module = ModuleType("inputmodule")
            exec(compiled, module.__dict__)
            return module
        except:
            pass
        
    def check_correction(user_input, task_id):
        result = False
        executable_module = execute_input(user_input)
        if executable_module is not None:
            result = test_module(executable_module, task_id)
        return result

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
            
            is_correct = check_correction(editable, hidden)
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
                "jsonFeedback": { "test": is_correct },
                "htmlFeedback": "<div>Test: " + str(is_correct) + "</div>",
                "textFeedback": "Test result: " + str(is_correct),
            }
        )
    }

def lambda_handler(event, context):

	method = event.get('httpMethod',{}) 
	indexPage=open('index.html', 'r')

	if method == 'GET':
	    return {
	        "statusCode": 200,
	        "headers": {
	        'Content-Type': 'text/html',
	        },
	        "body": indexPage.read()
	    }
# BT3103

## Features:
- AWS Lambda deployed using Github Actions
- External website with interactive PyGame
- Python game using PyGame library as an example
- Github stored files as text source for course path



## PyGame in browser is possible thanks to this project:
[https://github.com/Petlja/pygame4skulpt](https://github.com/Petlja/pygame4skulpt)


## Links:
* #### PyGame integration:
  - ##### [Running Github page with PyGame](https://oziomek1.github.io/bt3103/)
  - ##### [Example game source code to run](https://github.com/oziomek1/bt3103/blob/master/example_snake.py)
* #### AWS Lambda:
  - ##### [Running AWS Lambda build with Github Actions](https://ykab5hzm96.execute-api.us-east-1.amazonaws.com/Prod/)
  - ##### [Source AWS Lambda](https://3x7o2gvbkg.execute-api.us-east-1.amazonaws.com/default/final_lambda_bt3013)

* #### Notebook with analytics:
Data is stored with every single POST request to our function. Example single input below:
```
solution_id - unique Id of entry
input - user solution for a task
result - fail or passed output after evaluation
task_id - Id of a task
time - Timestamp
user_token - unique user token taken from achievements. Token from website set to "EXTERNAL"
```

  - ##### [Analytics notebook](https://colab.research.google.com/drive/1ILk3aiRiOiSH1TYQpFyLvwIsXaxK6xpP)

## Images:
* #### Main course page
 <img src="/images/main.png" />

* ### Example game menu
 <img src="/images/game_menu.png" />

 * ### Example game play
  <img src="/images/game.png" />

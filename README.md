### test-ci
# A testing repo for continous integration (CI)

A basic calculator app with addition, subtraction, and multiplication.
Contains requirements.txt, calculator.py, and test_calculator.py
Each commit and push adds a new job to the Circle CI execution dashboard, where (according to the .circleci/config.yml file) a virtual docker environment is created, dependencies are installed (according to requirements.txt), and the code is tested using pytest (unit tests), as well as linted using flake8.
To add a new function to the app in calculator.py (eg. division), remember to add a corresponding unit test to test_calculator.py (eg. test_division).

## Version History
V 1.0
Added multiplication and accompanying unit test, passed CI tests
<img width="1423" alt="Screen Shot 2021-05-29 at 11 33 27 PM" src="https://user-images.githubusercontent.com/71274065/120092117-48b09b00-c0d6-11eb-8a91-7a92c91fafb3.png">

V 0.0 
Added repo with addition and subtraction, passed CI tests
<img width="1171" alt="Screen Shot 2021-05-29 at 11 35 23 PM" src="https://user-images.githubusercontent.com/71274065/120092163-8c0b0980-c0d6-11eb-8edb-720f0b30ce28.png">

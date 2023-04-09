# BJS_Assignment
### This Project includes Mini Python Tasks

##### Requirements: 
Python 3.11

##### Brief Description of Each Task:

1. task1.py - The code in this file demonstrates how to extract all the numbers from a given string using regular expressions in Python. The numbers are then converted                 to integers using the map() function and stored in a list. Finally, the list of numbers is printed to the console. This code can be useful in scenarios                   where we need to extract numeric values from a string for further processing or analysis.

2. task2(1).py - The function iterates over the input string character by character and sets flags a_occurred and b_occurred based on whether the characters 'a' or 'b'                   have occurred in the string. If the function encounters a 'b' character after an 'a' character, it returns False, indicating that the string does not                     meet the conditions. Otherwise, it returns True.
                  The code also includes several test cases that call the character_occurance function with different input strings and prints the results to the                           console. This code can be useful in scenarios where we need to check if a given string contains a sequence of characters that meet specific conditions.
 
 3. task3.py- The program evaluates the expression string for every possible combination of x and y values within the given range and returns the maximum value. The                   get_max_evaluated_value function takes two arguments: variables and expression_string. The variables argument is a dictionary containing the range of                     values for x and y, and the expression_string argument is a string containing the expression to be evaluated.The get_max_evaluated_value function calls the               getEquationValue function for every possible combination of x and y values within the given range. The getEquationValue function evaluates the expression                 for the given x and y values by parsing the expression string and performing the arithmetic operations in the correct order of operations. The getValue                   function evaluates the operands and operators by checking if they are numbers or variables and then performing the correct operation. Finally, max function               is used to return the maximum value evaluated from the range of x and y values.

##### Basic Deployment Steps:

1. Choose a platform: There are several platforms available for deploying Python code, including Heroku, AWS, Google Cloud, PythonAnywhere, and others.

2. Set up an account: Once you've chosen a platform, you'll need to create an account and set up the necessary configurations.

3. Create a repository: If your code is not already in a Git repository, you'll need to create one and push your code to it.

4. Configure your environment: Depending on the platform you've chosen, you may need to configure your environment to ensure that your code runs smoothly. This may involve specifying the required Python version, installing dependencies, and setting up any necessary environment variables.

5. Deploy your code: Once you've completed the above steps, you're ready to deploy your code. This typically involves pushing your code to the platform's servers and configuring any necessary settings to ensure that your code runs correctly.

6. Test your deployment: After deploying your code, it's important to test it thoroughly to ensure that everything is working correctly. This may involve running automated tests, performing manual tests, and monitoring your application to detect any issues.

##### Deployment on PythonAnywhere:
1. Created a free account on PythonAnywhere.
2. Opened console on PythonAnywhere and created ssh key to connect with github
3. Cloned git repository on console.
4. Run individual Python files using console.

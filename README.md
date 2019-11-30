<div align="left">
<h1>
    <img alt="header" src="/src/assets/Header.png" width="800"></img>
</h1>
Welcome to A December of Algorithms (2019). After the overwhelming response from last year, we present you with a new collection of algorithms to implement this December. Each Day, Each Algorithm ;) Finish them all to get prizes and certificate :)

**Send a pull request only after completing all 31 algorithms.**

**Please submit all PRs on or before January 10th 11:59 PM IST.**

## What Do I Do?
We have a small collection of algorithms, one for every day of the month. Scroll down to take a look at them. All you need to do is fork this repository, implement all 31  algorithms and send a pull request over to us. Check out our FAQ for more information.



## Index
  - [**December 1 - Sevenish Number**](#december-1---sevenish-number)
  - [**December 2 - Is this a valid credit card number?**](#december-2---is-this-a-valid-credit-card-number)
  - [**December 3 - The Decimation**](#december-3---the-decimation)
  - [**December 4 - Dr. Bruce Banner's H-Index**](#december-4---dr-bruce-banners-h-index)
  - [**December 5 - Convert CSV data to a HTML table**](#december-5---convert-csv-data-to-a-html-table)
  - [**December 6 - Fibonacci Prime number generation**](#december-6---fibonacci-prime-number-generation)
  - [**December 9 - Queued up**](#december-9---stack-up)
  - [**December 10 - Queued up**](#december-10---queued-up)
  - [**FAQ**](#faq)



## Algorithms

### **December 1 - Sevenish Number**
  - **Problem**
    - Let us now define what we mean by a sevenish number.
    - A "sevenish" number is a natural number which is either a power of 7, or the sum of unique powers of 7
    - The first 5 sevenish numbers are: `1`, `7`, `8`, `49`, `50`.
    - Now, implement an algorithm to find the `n`th sevenish number.
  - **Example**
      ```bash
      > sevenish_number(1)
        1
      > sevenish_number(5)
        50
      > sevenish_number(10)
        350
      ```
  - **Optional Task**
    - Create a Dynamic Programming solution to reduce the time complexity of your algorithm (if you used a brute-force approach before).
  - **Resources**
    - [Brute Force](https://stackoverflow.com/questions/8103050/what-exactly-is-the-brute-force-algorithm)
    - [Dynamic Programming](https://www.codechef.com/wiki/tutorial-dynamic-programming)
    - [Recursion](https://web.mit.edu/6.005/www/fa15/classes/10-recursion/)


### **December 2 - Is this a valid credit card number?**
  - **Problem**  
     Are credit card numbers just a random combination of the digits from 0-9? **NO!**  
     Credit card numbers are a systematic combination of numbers that can satisfy a single test. This test is created so that errors can be avoided while typing in credit card numbers as well as detect counterfeit cards!  
    
    The algorithm is as follows:
    - Reverse the order of the digits in the number.
    - Take the first, third, ... and every other odd digit in the reversed digits and sum them to form the partial sum s1
    - Taking the second, fourth ... and every other even digit in the reversed digits:
        * Multiply each digit by two and sum the digits if the answer is greater than nine to form partial sums for the even digits
        * Sum the partial sums of the even digits to form s2
    - If s1 + s2 ends in zero then the original number is in the form of a valid credit card number as verified by the Luhn test.  
    </br>
    
    ```
    Reverse the digits:
    61789372994
    Sum the odd digits:
      6 + 7 + 9 + 7 + 9 + 4 = 42 = s1
    The even digits:
        1,  8,  3,  2,  9
      Two times each even digit:
        2, 16,  6,  4, 18
      Sum the digits of each multiplication:
        2,  7,  6,  4,  9
      Sum the last:
        2 + 7 + 6 + 4 + 9 = 28 = s2

    s1 + s2 = 70 which ends in zero which means that 49927398716 passes the Luhn test
    ```
    Your task is to implement to check if a given credit card number is valid or not using the above algorithm.  
  - **Example**
      ```
      Input : 49927398716
      Output: 49927398716 passes the test
      ```
  - **Resources**
    - [This is cool! Tell me more](https://www.creditcards.com/credit-card-news/luhn-formula-credit-card-number-system-1273.php)


### **December 3 - The Decimation**
  - **Problem**
    - Well, this is day 3 so let's start with something easy. Perhaps an algorithm that might involve a list and the **Marvel Supervillain Thanos**!
    - While the list isn't sorted, snap half of all things (remove them from the list). Proceed until the list is sorted or only one item remains (which is sorted by default). This sorting algorithm may give varied results based on implementation.
    - The item removal (decimation) procedure is up to the implementation to decide, but the list should be half as long as before after one pass of the item removal procedure.
    - Your algorithm may commit to take away either the first half of the list, the last half of the list, all odd items, all even items, one at a time until the list is half as long, or any not specified above.
    - **Decide for yourself:** What would Thanos do if the universe carried an odd amount of living things?
 ![hello](/src/assets/thanos-snap.gif)
    - The list is sorted if no elements are smaller than any previous item. Duplicates may exist in the input and may exist in the output.
  - **Example**
      ```c
      // A sorted list remains sorted
      [1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5]
      // A list with duplicates may keep duplicates in the result
      [1, 2, 3, 4, 3] -> [1, 3, 3] // Removing every second item
      [1, 2, 3, 4, 3] -> [3, 4, 3] -> [4, 3] -> [3] // Removing the first half
      [1, 2, 3, 4, 3] -> [1, 2] // Removing the last half
      ```
  - **Resources**
    - [Arrays in C++](http://www.cplusplus.com/doc/tutorial/arrays/)
    - [Arrays in Java](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html)
    - [Arrays in Python](https://www.w3schools.com/python/python_lists.asp)


### **December 4 - Dr. Bruce Banner's H-Index**
  - **Problem**
    - Dr. Bruce Banner is a soft-spoken scientist and among Earth's most brilliant men. At this moment though, he needs your help to find his h-index.
    - In academia, the h-index is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:
    - A researcher has index h if at least h of his N papers have h citations each. If there are multiple h satisfying this formula, the maximum is chosen.
    - For example, suppose `N = 5`, and the respective citations of each paper are `[4, 3, 0, 1, 5]`
    - Then the h-index would be `3`, since the researcher has 3 papers with at least 3 citations.
    - Given a list of paper citations of Dr. Bruce Banner, calculate his h-index.
  - **Example**
      ```bash
      > h_index(5, [4,3,0,1,5])
        3
      > h_index(6, [4,5,2,0,6,4])
        4
      ```
  - **Resources**
    - [Arrays in C++](http://www.cplusplus.com/doc/tutorial/arrays/)
    - [Arrays in Java](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html)
    - [Arrays in JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
    - [Lists in Python](https://www.w3schools.com/python/python_lists.asp)


### **December 5 - Convert CSV data to a HTML table**
  - **Problem**
    - A comma-separated values (CSV) file is a delimited text file that uses a comma to separate values. A CSV file stores tabular data in plain text. Each line of the file is a data record. Each record consists of one or more fields, separated by commas. 
    - Data in a CSV file is not very easy to understand. Your task is to read data from a CSV file and convert into a code for a HTML table and store it another file with a .html extension. Use the CSV file given in the resources to build your algorithm. 
  - **Example**
      - **CSV**
        ```csv
        column1,column2,column3
        a,123,abc123
        b,234,bcd234
        c,345,cde345
        ```
    - **HTML**
        ```html
        <html>
            <body>
                <table>
                    <tr><th>column1</th><th>column2</th><th>column3</th></tr>
                    <tr><td>a</td><td>123</td><td>abc123</td></tr>
                    <tr><td>b</td><td>234</td><td>bcd234</td></tr>
                    <tr><td>c</td><td>345</td><td>cde345</td></tr>
                </table>
            </body>
        </html>
        ```
  - **Resources**
    - [CSV Source File](/src/res/csv_to_html_res.csv)
    - [What are CSV files?](https://www.lifewire.com/csv-file-2622708)
    - [File handling in C](https://www.geeksforgeeks.org/basics-file-handling-c/)
    - [File handling in C++](https://www.geeksforgeeks.org/file-handling-c-classes/)
    - [File handling in Java](https://www.geeksforgeeks.org/file-handling-java-using-filewriter-filereader/)
    - [File handling in Python](https://www.geeksforgeeks.org/file-handling-python/)
    - [Tables in HTML](https://www.w3schools.com/html/html_tables.asp)
    
    
### **December 6 - Fibonacci Prime Number Generation**
  - **Problem**
    - Fibonacci Numbers are a series of numbers where each number is the sum of preceding 2 numbers. 
    - Henry wants to generate prime numbers present in the Fibonacci Series. He needs your help to generate them.
       - For example, suppose `N = 3`
    - Then the series will have 3 Fibonacci prime numbers : 2,3,5
    - Given the count of prime numbers needed by Henry , compute the series for him.
  - **Example**
      ```
        Enter the value for (n): 5
        
        Generated Fibonacci Prime Number Generation upto (5): 
        2, 3, 5, 13, 89
      ```
  - **Resources**
    - [Fibonacci Numbers](https://en.wikipedia.org/wiki/Fibonacci_number)
  - **Fun Facts on Fibonacci**
    - Every positive integer can be written in a unique way as the sum of one or more distinct Fibonacci numbers in such a way that the sum does not include any two consecutive Fibonacci numbers. This is Zeckendorf Theorem.
    - Any three consecutive Fibonacci numbers, taken two at a time, are relatively prime.
    - No Fibonacci number greater than 8 is one greater or one less than any prime number.

### **December 9 - Stack up**

- **Understanding Stacks**
	- A stack is a container of objects that are inserted and removed according to the *last-in first-out* (LIFO) principle. 
	- A stack is a limited access data structure - elements can be added and removed from the stack only at the top. push adds an item to the top of the stack, pop removes the item from the top. 
	- A helpful analogy is to think of a stack of books; you can remove only the top book, also you can add a new book on the top.

- **Problem**
 	 It's day 10! Congrats on completing one-third of the challenge.The task for the day is to reverse a string using stack data structure.

	 The algorithm is as follows:
	 - Get the string
	 - Print the reversed string using stacks

- **Example**
      ```
      Enter string: abcdef<br>
	  The reversed string is: fedcba
      ```
- **Resources**
    - [Stacks and queues](https://www.cs.cmu.edu/~adamchik/15-121/lectures/Stacks%20and%20Queues/Stacks%20and%20Queues.html)
    - [Stack implementation](https://www.geeksforgeeks.org/stack-data-structure/)

 !<img src="https://media.giphy.com/media/WtCHRSPCuqS8E/giphy.gif" width=500 height=250>

### **December 10 - Queued up**

- **Problem**
 	 A medical clinic assigns a token number to every patient who visits. The token number starts from 1 and it is given based on the order of arrival, to the n patients who arrive. But, the receptionist accepts bribe and lets a person k in first. The task is to print the token number and the patient's name in the order in which they see the doctor.
 	
 	 The algorithm is as follows:

 	 - Get n
 	 - For every person that arrives, store their name and token number.
 	 - Get k
 	 - Print kth person's token number and name followed by the rest.


- **Example**
	```
	Enter n: 5
	Enter token no - name
	1 a
	2 b
	3 c
	4 d
	5 e
	Enter k: c
	The order is:
	3 c
	1 a
	2 b
	4 d
	5 e
	```
- **Resources**
    - [Understanding queue data structure](https://www.geeksforgeeks.org/queue-data-structure/)
    - [Stacks and queues](https://www.cs.cmu.edu/~adamchik/15-121/lectures/Stacks%20and%20Queues/Stacks%20and%20Queues.html)

 <img src="https://media.giphy.com/media/6kyrz1j5uhJdK/giphy.gif" width=500 height=250>
   
    
## Maintainers
- [K-Kraken](https://github.com/K-Kraken)
- [jyuvaraj03](https://github.com/jyuvaraj03)
- [mahavisvanathan](https://github.com/mahavisvanathan)
- [shrusri27](https://github.com/shrusri27)



FAQ:
======
  #### Who can join the Challenge?
  Anyone who is passionate about coding and can dedicate a little time a day for the challenge for the next 31 days.

  #### When should I submit the pull request?
  You don't need to submit it everyday. Just submit it once you're done with all 31 algorithms.

  #### What if I'm not able to code every day?
  Not a problem. While coding every day is nice, we understand that other commitments might interfere with it. Plus its holiday season. So you don't have to solve one problem every day. Go at your own pace. One per day or 7 a week or even all 30 in a day.

  #### What language should I use to code?
  Anything! New to C? Best way to practice it. Wanna find out what all this hype about Python is? Use it! Any and all languages are welcomed. Maybe you could try using a different language for every problem as a mini-challenge?

  #### Fork? Pull request? What is all that? I don't know how to use GitHub!
  If you are new to Git or GitHub, check out this [small tutorial from our team](https://github.com/ASS-G/Git-Training-Kit) and [GitHub](https://guides.github.com/activities/hello-world/)

  #### Where are the rest of the problems?
  Our code ninjas are hard at work preparing the rest of the problems. Don't worry, they'll be up soon.

  #### How should I complete these programs?
  We have a folder for each day of the month. Simply complete your code and move the file into that folder. Be sure to rename your file to the following format: `language_username` or `language_username_problemname`
  Some examples:
  `python_exampleUser.py`
  `c_exampleUser.c`
  **Please do not modify any existing files in the repository.**

  #### I forked the repository but some problems were added only after that. How do I access those problems?
  Not to worry! Open your nearest terminal or command prompt and navigate over to your forked repository. Enter these commands:
  ```bash
  git remote add upstream https://github.com/SVCE-ACM/A-December-of-Algorithms-2019.git
  git fetch upstream
  git merge upstream/master
  ```
  If you're curious, the commands simply add a new remote called upstream that is linked to this repository. Then it 'fetches' or retrieves the contents of the repository and attempts to merge it with your progress.
  Note that if you've already added the upstream repository, you don't need to re-add it in the future while fetching the newer questions.

  #### I received a merge error. What do I do?
  This shouldn't happen unless you modify an existing file in the repository. There's a lot of potential troubleshooting that might be needed, but the simplest thing to do is to make a copy of your code outside the repository and then clone it once again. Now repeat the steps from the answer above. Merge it and then add your code. Now proceed as usual. :)

  #### I'm facing difficulties with/need help understanding a particular question.
  Open up an [issue](https://github.com/SVCE-ACM/A-December-of-Algorithms-2019/issues) on this repository and we'll do our best to help you out.

###### [[Back to Top]](#----)

![wave](http://cdn.thekrishna.in/img/common/border.png)

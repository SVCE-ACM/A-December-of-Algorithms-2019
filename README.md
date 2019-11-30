<div align="left">
<h1>
    <img alt="header" src="/src/assets/Header.png" width="900" height="300"></img>
</h1>
Welcome to A December of Algorithms (2019). After the overwhelming response from last year, we present you with a new collection of algorithms to implement this December. Each Day, Each Algorithm ;) Finish them all to get prizes and certificate :)

**Send a pull request only after completing all 31 algorithms.**

**Please submit all PRs on or before January 10th 11:59 PM IST.**

## What Do I Do?
We have a small collection of algorithms, one for every day of the month. Scroll down to take a look at them. All you need to do is fork this repository, implement all 31  algorithms and send a pull request over to us. Check out our FAQ for more information.



## Index
  - [**December 1 - Sample Problem**](#december-1---sample-problem)
  - [**FAQ**](#faq)



## Algorithms
### **December 1 - Sample Problem**
  - **Problem**
    - Problem?
  - **Example**
      ```bash
      Sample Input and Output
      ```
  - **Resources**
    - [Resource Link](https://duckducgo.com/)

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


## Maintainers
- [Username](https://github.com/SVCE-ACM)




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

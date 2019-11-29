### **December {date} - Is This A Valid Email Address**
  - **Problem**
    - While signing up for a website, you must have seen that when an invalid email address is entered, you get a warning. This is because the website verifies whether the given email address is valid or not according to some rules (check the resources section to know the format of a valid email address). 
    - Now, for today's challenge implement your own email address verification algorithm.
    - For the sake of simplicity, assume that a valid email address has the following format:
      - `local_part@domain`
      - The `local_part` should contain only alphabets, numbers and the characters: `_`, `.`, `-`.
      - The `domain` should contain only alphabets followed by `.com`
  - **Example**
      ```
      // Valid email addresses
      john-doe420@gmail.com
      jane.austen_69@dnarifle.com
      ```
  - **Optional Problem**
    - Implement an algorithm to verify an email address based on the complete syntax specification (given in the resources section).
  - **Resources**
    - [Complete Syntax Specification of Email Addresses](https://en.wikipedia.org/wiki/Email_address#Syntax)
  - <details><summary><b>Still stuck?</b></summary>
      <ul>
          <li>Use Regular Expressions to verify the format of the email.</li>
          <li><a href="http://www.cplusplus.com/reference/regex/">Regular Expressions in C++</a></li>
          <li><a href="https://www.tutorialspoint.com/python/python_reg_expressions.htm">Regular Expressions in Python</a></li>
          <li><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions">Regular Expressions in JavaScript</a></li>
          <li><a href="https://www.javatpoint.com/java-regex">Regular Expressions in Java</a></li>
      </ul>
    </details>

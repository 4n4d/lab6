# Lab 6: Unit testing
Unit testing is a common methodology, gaining increasing importance, for ensuring correctness of software  and proofing for repeated mistakes. The main idea is to make testing systematic: instead of manually testing the functions and methods you write, a standardized framework is used to record useful test cases.

There are several advantages to unit tests.

* Instead of every programmer or team inventing their own test system, a well known system can be used. This makes it easy to read others tests and write new ones.
* You don't have to remember how you tested an old function when fix a bug in it or add a feature. 
* Just coming up with suitable test data is work you should not need to do more than once: using unit testing you have a simple way of storing the test data.
* Using unit tests enables systematic testing, reducing the risk of forgetting to test old functionality when adding features.

## Reading
Look at the documentation (linked) for two proposed unit test frameworks in Python, available as modules:

* doctest is a minimalistic system with minimal beginner's threshold, so it is easy to get started with it. It is however limited in what tests it can run and also very Python specific.
* unittest follows a pattern used for many other programming languages, specifically Java, which is the language that gave unit testing a "breakthrough". There is a bit more to learn when starting with unittest, but you get broader applicability. 

Then watch a tutorial available on YouTube: Unit Testing Your Code with the unittest Module.

## Assignment
Add comprehensive (as in: at least one test for all implemented methods) tests using the unittest module to your solutions to lab 4, binary search trees.

You code should of course pass all the tests! But you are also tasked with introducing a bug which a test case can find.

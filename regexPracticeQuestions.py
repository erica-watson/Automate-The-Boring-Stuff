'''Practice Questions

1. What is the function that creates Regex objects?
re.compile(pattern)

2. Why are raw strings often used when creating Regex objects?
because they often have escape characters and it's easier to read

3. What does the search() method return?
it returns a match object with the index of the match and the text string

4. How do you get the actual strings that match the pattern from a Match object?
use group() or group(0)

5. In the regex created from r'(\d\d\d)-(\d\d\d-\d\d\d\d)', what does group 0 cover? Group 1? Group 2?
group 0 is the entire match. group 1 is the area code and group 2 is the phone number

6. Parentheses and periods have specific meanings in regular expression syntax. How would you specify that you want a regex to match actual parentheses and period characters?
use an escape key before each paren or period

7. The findall() method returns a list of strings or a list of tuples of strings. What makes it return one or the other?
it returns a list of strings if there is one or zero groups in the regex. if there are two or more groups, it returns a list of tuples, where each tuple is a group

8. What does the | character signify in regular expressions?
it means "or"

9. What two things does the ? character signify in regular expressions?
? at the end of a group means it's an optional group (one or zero times)
? at the end of an expression means it will look for a non-greedy match

10. What is the difference between the + and * characters in regular expressions?
+ means one or more times
* means zero or more times

11. What is the difference between {3} and {3,5} in regular expressions?
{3} pattern must repeat 3 times for a match
{3, 5} will match if there are 3, 4, or 5 repeats of the pattern

12. What do the \d, \w, and \s shorthand character classes signify in regular expressions?
d- digits
w- alphanum and underscore
s- whitespace

13. What do the \D, \W, and \S shorthand character classes signify in regular expressions?
-everything except what the lowercse has

14. What is the difference between .* and .*??
they both mean "anything" but the former is greedy and the latter is non-greedy

15. What is the character class syntax to match all numbers and lowercase letters?
[a-z0-9]

16. How do you make a regular expression case-insensitive?
re.compile(r'string', re.I)

17. What does the . character normally match? What does it match if re.DOTALL is passed as the second argument to re.compile()?
anything except an underscore
includes the underscore

18. If numRegex = re.compile(r'\d+'), what will numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens') return?
X drummers, X pipers, five rings, X hens

19. What does passing re.VERBOSE as the second argument to re.compile() allow you to do?
allows you to use triple quotes and enter the pattern across multiple lines of code

20. How would you write a regex that matches a number with commas for every three digits? It must match the following:

    '42'
    '1,234'
    '6,368,745'

but not the following:

    '12,34,567' (which has only two digits between the commas)
    '1234' (which lacks commas)

((\d){1,3},)*
\d{1,3}

21. How would you write a regex that matches the full name of someone whose last name is Watanabe? You can assume that the first name that comes before it will always be one word that begins with a capital letter. The regex must match the following:

    'Haruto Watanabe'
    'Alice Watanabe'
    'RoboCop Watanabe'

but not the following:

    'haruto Watanabe' (where the first name is not capitalized)
    'Mr. Watanabe' (where the preceding word has a nonletter character)
    'Watanabe' (which has no first name)
    'Haruto watanabe' (where Watanabe is not capitalized)

[A-Z]([a-z])*

22. How would you write a regex that matches a sentence where the first word is either Alice, Bob, or Carol; the second word is either eats, pets, or throws; the third word is apples, cats, or baseballs; and the sentence ends with a period? This regex should be case-insensitive. It must match the following:

    'Alice eats apples.'
    'Bob pets cats.'
    'Carol throws baseballs.'
    'Alice throws Apples.'
    'BOB EATS CATS.'

but not the following:

    'RoboCop eats apples.'
    'ALICE THROWS FOOTBALLS.'
    'Carol eats 7 cats.'

testRegex = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs)\.', re.I)

'''



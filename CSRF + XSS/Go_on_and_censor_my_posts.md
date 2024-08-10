# Challenge `Go on and censor my posts` writeup

- Vulnerability: Cross-Site Scripting Lab (XSS)

- Where: textarea 'content' (lure admin)

- Impact: attacker is able to inject malicious code in the webpage by exploting the html vulnerability

---

## Steps to reproduce

1. Create a new post
2. Start listening on the nexus server
3. On 'content' field, close textarea element and then use the previous script to exploit the admin cookie again (finally open a new textarea element, to match the lone closed), like this:
- < /textarea> code < textarea>
4. Click on 'Update post and send it to admin review' (lure admin)
5. Check the connection response on the nexus server


[(POC)](Go_on_and_censor_my_posts.txt)


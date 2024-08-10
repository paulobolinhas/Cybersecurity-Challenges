# Challenge `Just my boring cookies` writeup

- Vulnerability: Cross-Site Scripting Lab (XSS) - Reflected XSS

- Where: search input

- Impact: attacker is able to inject malicious code in the webpage

---

## Steps to reproduce

1. Add a script to alert your cookie <script>alert(document.cookie)</script> on the search field or simply go to url:
 - http://mustard.stt.rnl.tecnico.ulisboa.pt:23251/?search=%3Cscript%3Ealert(document.cookie)%3C/script%3E

[(POC)](Just_my_boring_cookies.txt)


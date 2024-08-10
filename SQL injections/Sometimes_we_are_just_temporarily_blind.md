# Challenge `Sometimes we are just temporarily blind` writeup

- Vulnerability: SQL injection

- Where: search field [SQL: SELECT id, title, content FROM blog_post WHERE title LIKE '%'%' OR content LIKE '%' UNION SELEC%']

- Impact: attacker is able to inject malicious code in the webpage and get hidden posts

---

## Steps to reproduce

1. First you will have to find the hidden and unknown table name. For that you will re use last's challenge query.
2. You will have to iterate throught all the letters and '_'
  - 2.1. Add this to the query "AND name LIKE '{"current_string_match(table) - starts empty"}{letters and '_'}%'" (% is used here like a Ctrl + F to check all strings that start with the string before %)
  - 2.2. Inject the query 
  - 2.3. Check how many articles are found
  - 2.4. If they are 5, excluding the 4 already known(4 known files + 1 hidden), your string actual match is correct, so add that letter to the match string

  Loop like this:
  
    check 'a%' found 4 articles
    check 'c%' found 5 articles

    next ->

    check 'ca%' found 4 articles
    check 'cb%' found 5 articles

    next ->

    ... until a limit

3. Now, knowing the table name "{table_name} = super_s_sof_secrets" do the same loop to find the columns. For this, add this to the query: 
"name LIKE '{table_name}' AND sql LIKE '{"current_string_match(column) - starts empty"}{letters and '_'}%'"
  - 3.1. You will get the creation info "create_table_super_s_sof_secrets____id_integer_not_null____secret_text____primary_key__id___"
  - 3.2. Conclude that the column you want is "secret" type 'text'
4. Finally, it's time to find the flag. Do the same loop in order to find it. For this, formulate your query to check 'secret' column values:
"' UNION SELECT secret, secret, secret FROM {table_name} WHERE secret LIKE '{"current_string_match(flag) - starts empty"}{letters and '_'}%' --" 
  - 4.1. You will get the flag within this format: "in_case_i_forget_my_password_is__ssof_i_am_just_partially_blind_since_i_can_get_your_data_using_boolean_injection_"


[(POC)](Sometimes_we_are_just_temporarily_blind.py)

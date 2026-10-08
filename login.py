   def login(username, password):
       # BUG: password check is case-sensitive on username
       users = {"maya": "1234"}
       return users.get(username.lower()) == password
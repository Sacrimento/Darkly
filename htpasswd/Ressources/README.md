# htpasswd

Après avoir regardé dans `/robots.txt`, on remarque `/whatever` existe et contient un fichier htpasswd avec le couple `root:8621ffdbc5698829397d97767ac13db3`
Le password est un md5, une fois reverse nous obtenons le couple `root:dragon`
Après avoir scanné avec nikto le website, nous découvrons `/admin` qui offre une interface de login.
Il suffit de rentrer le couple `root` et `dragon` pour obtenir le flag `d19b4823e0d5600ceed56d5e896ef328d7a2b9e7ac7e80f4fcdb9b10bcb3e7ff`

# Comment fix ?

Ne pas donner accès à l'utlisateur au htpasswd


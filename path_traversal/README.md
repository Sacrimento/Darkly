# Path traversal

On remarque que le website fonctionne avec un système de `page=XXX` pour accéder aux différentes pages à partir de l'index.
Lorsque on rentre une page qui n'existe pas à la main, un `alert()` se lance et nous indique qu'on est sur le bon chemin.
Après différents tests, les `alert()`s changent lorsqu'on rentre un path type `/../../..` etc.
A l'aide d'un script, on descend l'arborescance jusqu'à trouver le flag `b12c4b2cb8094750ae121a676269aa9e2872d07c06e429d25a63196ec1c8c1d0` en accédant à `/etc/passwd`


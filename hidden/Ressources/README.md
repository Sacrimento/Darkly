# Hidden folder crawling

Après avoir regardé dans `/robots.txt`, on remarque que `/.hidden` existe et contient beaucoup de sous-dossiers ainsi que des READMEs.
A l'aide d'un script, on récupère tous les READMEs, et on isole chaque string unique.
On obtient finalement le flag `99dde1d35d1fdd283924d84e6d9f1d820`

# Comment fix ?

Rendre interdit l'accès à ce genre de dossiers


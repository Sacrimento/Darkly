# Cookie: I_am_admin

En analyzant les requêtes faites par le website, on remarque que le cookie `I_am_admin` est set avec la valeur `68934a3e9455fa72420237eb05902327`
`68934a3e9455fa72420237eb05902327` est un md5 qui une fois reverse nous donne la valeur `false`
Ca nous donne `I_am_admin=false`.
Une fois que nous savons que nous sommes pas admin, il suffit de remplacer la valeur du cookie par le md5 de `true`:
`md5(true) = b326b5062b2f0e69046810717534cb09`

Il suffira alors de remplacer la valeur du cookie `I_am_admin` dans une requête sur `/index.php` pour récupérer le flag dans un `alert()`: `df2eb4ba34ed059a1e3e89ff4dfc13445f104a1a52295214def1c4fb1693a5c3`

# Comment fix ?

Ne pas mettre de cookies de ce type alors qu'on est pas loggé.


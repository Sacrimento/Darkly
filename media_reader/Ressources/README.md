# Media reader

En cliquant sur la photo de la nsa, on s'aperçoit qu'un `get` est fait pour récupérer l'image sur `/?page=media&src=nsa`. On tente de changer la variable `src` et le website nous renvoie un `wrong answer`, on est sur la bonne voie.
Après différents tests on s'aperçoit que la valeur de src est urlencoded, on ne peut pas envoyer de caractères spéciaux tels que `/` ou `(`.
Après des recherches sur internet, il est possible d'encoder nos paramètres en base64, pour qu'ils soient décodés et interprétés.
Etant donné que le serveur accepte du `text/html` d'après la requête, il suffit d'encoder en base64 `<script>alert(1);</script>` et de l'envoyer en paramètre.
En rajoutant le media header (`data:[<mediatype>][;base64],<data>`), on obtient notre requête complète : `?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgxKTs8L3NjcmlwdD4=` et le flag `928d819fc19405ae09921a2b71227bd9aba106f9d2d37ac412e9e5a750f1506d`

# Comment fix ?

Etant donné que la fonction principale de la page media est d'afficher les images du website, on peut imaginer plutôt récupérer ces dernières en database directement. Aussi il faut ajouter un check qui vérifiera si l'image (ici la variable `src`) est bien en base.


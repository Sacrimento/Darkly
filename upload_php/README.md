# Upload page

Sur la page `page=upload`, on peut upload des images. Le but évident ici est d'upload autre chose qu'une image, par exemple du php, pour qu'il soit éxécuté.
Après différents tests, on remarque que seul les fichiers avec pour extension `.jpeg`/`.jpg` sont acceptés, sinon le website ne l'upload pas.
On remarque que le check de l'extension est fait seulement sur le header du fichier envoyé, on peut donc reproduire la requête qui enverra un fichier `php`, en gardant les headers du `jpeg`.
Une fois le header `Content-Type` set à `image/jpeg`, on peut envoyer un fichier `php` et on obtient `46910d9ce35b385885a9f7e2b336249d622f29b267a1771fbacf52133beddba8`

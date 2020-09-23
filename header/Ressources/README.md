# Header - Albatros page

On remarque que des commentaires sont présents dans l'html de la page de l'albatros, accessible en cliquant sur le lien BornToSec dans le footer.
On lisant de plus près on y découvre : `You must cumming from : "https://www.nsa.gov/" to go to the next step` et `Let's use this browser : "ft_bornToSec". It will help you a lot.`

Il suffit donc de faire la même requête avec dans les headers `Referer: https://www.nsa.gov/` et `User-Agent: ft_bornToSec`.

On obtient le flag: `f2a29020ef3132e01dd61df97fd33ec8d7fcd1388cc9601e7db691d17d4d6188`

# Comment fix ?

Ne pas commenter le code avec ce genre d'indications...


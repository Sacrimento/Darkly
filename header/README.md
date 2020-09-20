# Header - Albatros page

On remarque que des commentaires sont présents dans l'html de la page de l'albatros, accessible en cliquant sur le lien BornToSec dans le footer.
On lisant de plus près on y découvre : `You must cumming from : "https://www.nsa.gov/" to go to the next step` et `Let's use this browser : "ft_bornToSec". It will help you a lot.`

Il suffit donc de faire la même requête avec dans les headers `Referer: https://www.nsa.gov/` et `User-Agent: ft_bornToSec`.

On obtient le flag: ``


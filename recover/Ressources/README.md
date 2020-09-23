# Recover page

Sur la page `recover`, on peut en principe récupérer/changer un mot de passe oublié. Ici on inspecte les requêtes, et on remarque qu'un mail est envoyé en paramètre lorsqu'on clique sur `Submit`
On change le mail qui était écrit en dur, et on récupère le flag: `1d4855f7337c0c14b6f44946872c4eb33853f40b2d54393fbe94f49f1e19bbb0`

# Comment fix ?

Il aurait évidemment fallu rajouter un input à l'utilisateur pour qu'il puisse entrer son adresse mail, ou vérifier l'identité de l'utilisateur par un autre moyen, en admettant que la page ne serve qu'à récupérer le mot de passe du webmaster.


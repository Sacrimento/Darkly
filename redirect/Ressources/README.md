# Redirect links

Dans le footer du website, on remarque que le wesbite inclue une fonctionnalité de redirection sur `?page=redirect&site=XXX`.
Rapidement on constate que la variable `site` peut être changée, aucun check n'est fait par le website (on pourrait rediriger vers du phising en gardant l'url de base wbesite...).
Une fois `site` changé, on obtient le flag `b9e775a0291fed784a2d9680fcfad7edd6b8cdf87648da647aaf4bba288bcab3`

# Comment fix ?

Ne pas intégrer de feature de redirect, on a pas besoin de ça pour se faire rediriger (Un `Location` dans les headers suffit).


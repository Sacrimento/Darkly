# Feedback page

En testant d'executer du javascript sur `?page=feedback`, on remarque `<script>alert(1)</script>` fera apparaitre le flag dans l'historique des commentaires.
Après quelques tests, il suffit de mettre le mot-clef `alert` dans le message pour faire apparaitre le flag: `0FBB54BBF7D099713CA4BE297E1BC7DA0173D8B3C21C1811B916A3A86652724E`

# Comment fix ?

Il faut absolument sanitize les inputs, pour empêcher l'utilisateur d'executer du code, par exemple `htmlspecialchars()` en php.


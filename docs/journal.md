# Journal des décisions TP01

## Q1. Délai de changement
*Temps écoulé entre le premier commit et sa fusion sur main :*
Environ 2 à 3 heures (le temps de résoudre les problèmes d'environnement et de rebase).

## Q2. Indépendance vis-à-vis de GitHub
*Ce qui marcherait tel quel sur GitLab/Gitea :*
Toutes les commandes Git natives (`git switch`, `commit`, `rebase`, `push`, `tag`, résolution de conflits) et l'outil `pre-commit`.
*Ce qui changerait :*
La CLI `gh` (remplacée par `glab` ou interface web), les URLs distantes, et la gestion des permissions/Pull Requests spécifiques à l'API GitHub.

## Q3. Intérêt de la signature des commits
*Pourquoi signer si la forge vérifie qui pousse ?*
La signature garantit cryptographiquement l'identité de l'auteur directement dans l'objet Git, indépendamment de la plateforme d'hébergement. Si le dépôt est cloné, transféré vers une autre forge, ou si quelqu'un usurpe un nom/email dans la configuration locale, la signature empêche la falsification de la paternité du code.
## TP02 — Analyse des secrets avec Gitleaks

- Installation et intégration de Gitleaks 8.30.0 dans pre-commit.
- Analyse des fichiers indexés avant chaque commit.
- Test avec une fausse clé AWS : fuite détectée et commit bloqué.
- Analyse de l'historique Git : 14 commits analysés, aucune fuite détectée.
- Rapport JSON généré dans `docs/gitleaks.json` : `[]`.
- Aucun secret historique à révoquer identifié lors de cette analyse.
- En cas de découverte d'un véritable secret : révocation ou rotation immédiate, puis analyse de son exposition.
## TP02 — Questions d'observation

### 1. Pourquoi activer « Dismiss stale approvals » ?

Ça permet d'annuler une validation si quelqu'un modifie le code après la revue. Sinon, une personne pourrait faire valider sa PR, rajouter du code derrière et le fusionner sans que personne vérifie les nouvelles modifications.

### 2. Que se passe-t-il si le seul CODEOWNER est absent ?

La PR peut rester bloquée parce que personne d'autre ne peut la valider. Le mieux est de mettre plusieurs responsables sur les dossiers importants, comme ça il y a toujours quelqu'un pour faire la revue.

### 3. Comment ça se passe pour les PR de Dependabot ?

Même si c'est un bot qui crée la PR, elle doit respecter les mêmes règles que les autres. Il faut donc que les tests passent et qu'une personne autorisée valide la PR avant de la fusionner.

### 4. Quelles protections auraient pu empêcher un secret d'arriver sur main ?

Il y a la revue des PR et les CODEOWNERS pour la partie humaine. Pour la partie automatique, on a Gitleaks qui peut détecter les secrets avant un commit, et on peut aussi l'ajouter dans la CI.

Le plus fiable, c'est de combiner les deux, surtout avec un contrôle automatique obligatoire sur GitHub, parce qu'une personne peut passer à côté d'un secret pendant une revue.

### 5. Est-ce que Gitleaks protège un collègue qui n'a pas installé pre-commit ?

Non, parce que pre-commit fonctionne sur le PC de chaque développeur. Si quelqu'un ne l'a pas installé, Gitleaks ne se lancera pas automatiquement chez lui.

Pour éviter ça, il faudrait aussi lancer Gitleaks avec GitHub Actions et rendre le test obligatoire avant de pouvoir fusionner une PR.

### 6. Combien de temps un secret publié sur GitHub reste privé ?

Dès qu'un secret est publié sur un dépôt public, il faut considérer qu'il est compromis. Il existe des bots qui cherchent automatiquement ce genre d'informations.

GitHub peut aussi détecter certains jetons et faire en sorte qu'ils soient révoqués automatiquement, notamment certains tokens GitHub. Mais ça ne fonctionne pas pour tous les secrets, donc il faut quand même les révoquer et les remplacer dès qu'on remarque une fuite.

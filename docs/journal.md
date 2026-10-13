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

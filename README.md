# Portfolio Tracker
#### Description :

Portfolio Tracker est une application en ligne de commande écrite entièrement en Python, permettant à un utilisateur de suivre et de gérer un portefeuille d'actions boursières simulé. Le but de ce projet est de reproduire, de manière simplifiée, le fonctionnement d'une plateforme de trading comme celle utilisée dans le problem set "Finance" de CS50, mais en autonomie complète, sans dépendre d'une API externe et sans interface web.

L'application permet à l'utilisateur d'acheter et de vendre des actions fictives, de consulter la valeur actuelle de son portefeuille, d'observer l'évolution de son solde au fil du temps, et de visualiser ses performances sous forme de graphiques. Toutes les données (prix, transactions, solde) sont stockées et gérées localement, ce qui rend le projet entièrement fonctionnel hors ligne.

## Fonctionnalités principales

- **Achat et vente d'actions simulées** à partir de prix générés localement (aucune API externe n'est utilisée).
- **Suivi du solde et de la valeur du portefeuille** en temps réel dans le terminal.
- **Historique des transactions** consultable par l'utilisateur.
- **Visualisation graphique** de l'évolution du portefeuille ou des prix simulés.
- **Persistance des données** entre les sessions grâce à un fichier de stockage local.

## Structure du projet et rôle des fichiers

**`project.py`**
Point d'entrée principal du programme. Il orchestre l'ensemble des fonctionnalités : il affiche le menu principal en ligne de commande, récupère les choix de l'utilisateur, puis appelle les fonctions appropriées définies dans les autres modules (achat, vente, consultation, graphiques). C'est ce fichier qui contient la fonction `main()` exigée par CS50, ainsi qu'au moins trois autres fonctions personnalisées, chacune testée séparément dans `test_project.py`.

**`market.py`**
Ce module simule le marché boursier. Plutôt que d'interroger une API financière réelle, il génère des prix d'actions localement (par exemple via des valeurs aléatoires ou des règles de fluctuation prédéfinies). Cela permet de faire fonctionner l'application sans connexion internet ni clé API, ce qui simplifie grandement les tests et l'utilisation du programme.

**`portfolio.py`**
Contient la logique métier du portefeuille : gestion du solde de l'utilisateur, calcul de la valeur totale des actions détenues, exécution des ordres d'achat et de vente, et vérification que l'utilisateur dispose des fonds ou des actions nécessaires avant chaque transaction. C'est le cœur logique de l'application.

**`database.py`**
Gère la persistance des données via un fichier texte simple. Ce module lit et écrit les informations du portefeuille (solde, actions détenues, historique des transactions) afin que les données de l'utilisateur soient conservées d'une session à l'autre, sans avoir besoin d'une base de données comme SQLite.

**`charts.py`**
Permet de générer des représentations graphiques (par exemple l'évolution du solde ou des prix simulés dans le temps), afin de donner à l'utilisateur une vision visuelle claire de ses performances.

**`gui.py`**
Malgré son nom, ce module gère en réalité l'interface utilisateur en ligne de commande : affichage des menus, mise en forme des tableaux de résultats dans le terminal, et gestion des entrées utilisateur.

**`test_project.py`** et **`test_portfolio.py`**
Contiennent les tests unitaires (via `pytest`) pour vérifier le bon fonctionnement des fonctions principales de `project.py` et `portfolio.py`.

## Choix de conception

Le choix le plus important a été de simuler le marché boursier localement plutôt que d'utiliser une API externe. Cela évite les problèmes de limite de requêtes, de clés API expirées ou de dépendance à une connexion internet, tout en permettant de tester facilement toutes les fonctionnalités de l'application. De la même manière, le stockage des données dans un fichier texte simple (plutôt qu'une base SQLite) a été choisi pour sa simplicité, bien que cela limite les possibilités de requêtes complexes sur les données.

## Comment lancer le programme

```
python project.py
```

L'utilisateur est ensuite guidé à travers un menu interactif dans le terminal.

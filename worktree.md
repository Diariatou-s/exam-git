# Introduction aux Git Worktrees

Les **git worktrees** sont une fonctionnalité de Git permettant de travailler sur plusieurs branches simultanément dans des répertoires différents, tout en utilisant un seul dépôt Git.
Voici une explication assez détaillée avec des exemples.

## Concept de Base

- **Dépôt Git** : C'est l'endroit où Git stocke toutes les versions du code, les branches, et les informations de suivi.
- **Worktree** : C'est un répertoire supplémentaire qui est lié au dépôt Git principal mais qui permet de travailler sur une branche différente sans interférer avec le dépôt principal.

## Pourquoi Utiliser les Worktrees ?

- **Travailler sur plusieurs branches** : Lorsque l'on veut développer ou corriger des bugs dans plusieurs branches sans devoir constamment changer de branche dans le même répertoire.
- **Isolation des modifications** : Chaque worktree est indépendant, ce permet de travailler sur des modifications dans des des branches séparées sans risque de conflits.

## Exemple Pratique

Supposons que l'on ai un dépôt Git avec deux branches principales : `main` et `feature`.

### 1. Créer un Worktree pour une Nouvelle Branche

Nous pouvons ajouter un worktree pour la branche `feature` comme suit :
```bash
git worktree add ../feature-worktree feature
```

`../feature-worktree` est le chemin vers le nouveau répertoire de travail.
`feature` est le nom de la branche pour laquelle on souhaite créer un worktree.

Cela créera un nouveau répertoire `feature-worktree` où nous pouvons travailler sur la branche feature sans affecter notre répertoire principal.

### 2. Travailler dans le Nouveau Worktree

Accédons au répertoire `feature-worktree`:
```bash
cd ../feature-worktree
```

Nous pouvons maintenant effectuer des modifications, committer des changements et pousser des mises à jour comme on le ferait dans un dépôt Git normal.

### 3. Gérer les Worktrees

- Pour voir tous les worktrees associés au dépôt:

```bash
git worktree list
```

- Pour supprimer un worktree lorsque l'on en a plus besoin:

```bash
git worktree remove ../feature-worktree
```

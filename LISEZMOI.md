# Expos du moment

Application pour iPhone (web app installable) qui regroupe les expositions en cours à Paris et en Île-de-France, gratuites et payantes, par thématique et sur une carte.

## L'installer sur l'iPhone

1. Ouvrez l'adresse du site dans **Safari** (voir **Settings › Pages** du dépôt).
2. Touchez **Partager**, puis **Sur l'écran d'accueil**, puis **Ajouter**.

Chacun garde ses favoris et ses réglages sur son propre téléphone. Il n'y a pas de compte et rien n'est envoyé à un serveur.

## Fonctions

- Onglets **Gratuites / Payantes / Toutes**, recherche, thématiques.
- Filtres « Nouveautés », « Finit bientôt » et « Favoris » (un seul à la fois).
- Étoile ☆ sur chaque expo pour l'ajouter aux favoris.
- Tri « Fin la plus proche », « Les plus demandées » (affluence du lieu), « Ajoutées récemment », « Les plus proches de moi », « Prix croissant ».
- Carte, **Près de moi**, fiche avec itinéraire (Plans) et billetterie.
- Mode jour/nuit automatique selon l'heure (nuit de 20h à 7h).
- Fonctionne hors connexion avec la dernière liste chargée.

## Mise à jour automatique

Chaque jour à 5h40 UTC, `.github/workflows/expositions.yml` :

1. lit l'API ouverte **Que faire à Paris** de la Ville de Paris et la sélection manuelle `data/selection.json` ;
2. écarte les événements annexes (visites, ateliers…) et les expos terminées ;
3. marque les nouvelles expositions (étiquette **Nouveau** pendant 7 jours) ;
4. calcule l'affluence des lieux (`data/affluence.json` et le jeu « Fréquentation des Musées de France ») ;
5. enregistre la base, puis publie le site sur GitHub Pages.

| Fichier | Rôle |
|---|---|
| `app/` | L'application (page, icônes, carte Leaflet, mode hors connexion) |
| `refresh.py` | Renouvelle la base et repère les nouvelles expositions |
| `build.py` | Prépare `site/` pour la publication |
| `data/selection.json` | Expositions ajoutées à la main |
| `data/affluence.json` | Fréquentation des lieux, saisie à la main avec sources |
| `MODELE.md` | Le modèle de données |

## Première mise en place

1. **Settings › Pages** : dans **Source**, choisissez **GitHub Actions**.
2. **Actions › Expos du moment › Run workflow**.

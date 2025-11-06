# Conteneurisation-Orchestration
## Contexte du Projet

L'objectif de ce projet est de simuler le cycle de vie complet d'une application moderne, de sa conception en
microservices à son déploiement en production, en passant par l'automatisation.
Les étudiants devront non seulement développer une application fonctionnelle mais aussi construire toute
l'infrastructure sous-jacente pour la faire fonctionner de manière résiliente, scalable et automatisée.
Ce projet a pour but de vous placer dans la peau d'une équipe DevOps, où vous êtes responsables à la fois du
code (Dev) et de l'infrastructure (Ops). La présentation finale sera orientée pour valoriser ces compétences
techniques auprès d'un recruteur.

## Objectifs Pédagogiques
À la fin de ce projet, vous serez capable de :
Comprendre et appliquer les principes de la conteneurisation et des microservices.
Créer, exécuter et gérer des conteneurs avec Docker.
Écrire des fichiers Dockerfile optimisés pour définir des environnements reproductibles.
Configurer Docker Compose pour orchestrer une application multi-conteneurs en environnement de
développement.
Déployer, orchestrer et mettre à l'échelle des applications sur un cluster Kubernetes.
Définir les objets Kubernetes essentiels (Pods, Déploiements, Services, Volumes, etc.).
Appliquer des stratégies d'orchestration avancées (mises à jour sans interruption, auto-réparation).
Intégrer un pipeline CI/CD pour automatiser les déploiements conteneurisés en production.

## Taches 
- Extraction du dataset
- Récupération et préparation des données sources.
- Création des règles de gestion
- Définition des logiques métier et des transformations à appliquer aux données.
- Transformation des données
- Nettoyage, normalisation et enrichissement du dataset.
- Mise en place du connecteur MongoDB (API si nécessaire)
- Développement d’un connecteur pour interagir avec la base MongoDB.
- Dockerisation de l’ETL
- Conteneurisation du processus ETL via Docker.
- Déploiement de l’ETL sur Kubernetes
- Orchestration et gestion du pipeline ETL dans un cluster Kubernetes.
- Création d’un volume partagé (BDD + ETL)
- Configuration du stockage persistant pour la base de données et le processus ETL.
- Développement des API (Front & Back)
- Mise en place des interfaces de communication entre le front-end et le back-end.
- Création de l’image Docker du front-end
- Construction et déploiement de l’image du front-end dans l’environnement Docker/Kubernetes.
- Extraction MongoDB sur conteneur Docker
- Hébergement du service d’extraction Mongo dans un conteneur dédié.
- Mise en place du front-end
- Développement, intégration et déploiement de l’interface utilisateur.
- Automatisation avec GitHub Actions
- Configuration du pipeline CI/CD pour pousser automatiquement les versions vers Kubernetes ou Docker.

## Tâches optionnelles / Améliorations

- Intégration SonarQube
- Analyse de la qualité du code et des vulnérabilités.
- Scan des images Docker
- Vérification de la sécurité et conformité des images avant déploiement.

## Links

Dataset : https://www.kaggle.com/datasets/mrmars1010/cars-india-pre-owned
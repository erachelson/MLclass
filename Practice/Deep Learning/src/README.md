# Khumeia

!!! quote ""
    *alchimie, du latin médiéval alchemia issu de l’arabe كِيمِيَاءُ, (al)kîmiyâʾ (« (la) chimie, art de faire de l'or, art de purifier son coeur »), lui-même issu du grec ancien χυμεία, khumeía (« art de faire fondre les métaux »).*

*khumeia* est un petit framework d'aide à l'interaction avec les images satellites - qui sont des images de dimensions assez importantes de l'ordre de 6000x6000 pixels.

Il permet notamment de ne pas avoir à réécrire le décodage des fichiers labels, ni les fichiers, et vise à faciliter l'interaction avec la donnée avant et après l'entraînement du modèle en lui même (qui lui a pour but d'être fait en utilisant Keras).

Sont aussi mis à disposition des utilitaires tels que la gestion des zones d'intérêts ("tuiles") dans des grandes images, ainsi que des fenêtres glissantes, et d'une proposition d'implémentation de mécanismes d'échantillonages.

Les parties suivantes (API DOC) ainsi que les notebooks donnent un aperçu des fonctions d'utilitaires (que vous êtes libre de ne pas utiliser) ainsi que des exemples d'utilisation.

Si nécessaire, se référer en dernier recours [au code source](https://github.com/fchouteau/isae-practical-deep-learning/tree/master/src)


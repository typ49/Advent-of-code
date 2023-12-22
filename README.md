# advent-of-code-2023
>
> the advent of code 2023
>

---

## progress

|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|★|★|★|★|☆|★|☆|||||||||||||||||||

---

## content

>
> ***Day 1 : Trebuchet?!***
>
>- **Partie 1**
>>
>> Traiter un document de calibration contenant des lignes de texte. Chaque ligne contient un nombre caché formé du premier et du dernier chiffre numérique de la ligne. Par exemple, "1abc2" produit le nombre 12. Calculer la somme de ces nombres pour toutes les lignes du document.
>
>- **Partie 2**
>>
>> Les chiffres peuvent être écrits en lettres (ex: "one", "two", "three"). Identifier le premier et le dernier chiffre de chaque ligne, qu'ils soient sous forme numérique ou alphabétique, les convertir en nombres, puis les combiner pour former un nombre à deux chiffres. Par exemple, "two1nine" correspond à 29. Calculer la somme de ces nombres pour toutes les lignes du document.
>>
>
<!--  -->
>
> ***Day 2 : Cube Conundrum***
>
>- **Partie 1**
>>
>> Déterminer quels jeux auraient été possibles si le sac contenait uniquement 12 cubes rouges, 13 cubes verts et 14 cubes bleus. Chaque jeu est enregistré avec son numéro ID suivi d'une liste de sous-ensembles de cubes révélés du sac. Par exemple, dans le jeu 1, trois ensembles de cubes sont révélés. Calculer la somme des ID des jeux qui auraient été possibles avec cette configuration de cubes.
>
>- **Partie 2**
>>
>> Pour chaque jeu, trouver le nombre minimum de cubes de chaque couleur qui auraient dû être présents dans le sac pour rendre le jeu possible. La puissance d'un ensemble de cubes est égale au produit des nombres de cubes rouges, verts et bleus. Calculer la somme de la puissance de ces ensembles minimums pour chaque jeu.
>
<!--  -->
>
> ***Day 3 : Gear Ratios***
>
>- **Partie 1**
>>
>> Calculer la somme de tous les numéros de pièces dans un schéma de moteur. Dans le schéma, un numéro est considéré comme un numéro de pièce s'il est adjacent à un symbole, même en diagonale. Les chiffres qui ne sont pas adjacents à un symbole ne sont pas inclus dans la somme.
>
>- **Partie 2**
>>
>> Trouver la somme des rapports de tous les engrenages dans le schéma du moteur. Un engrenage est défini par un symbole * qui est adjacent exactement à deux numéros de pièces. Le rapport d'un engrenage est le produit de ces deux numéros.
>
<!--  -->
>
> ***Day 4 : Scratchcards***
>
>- **Partie 1**
>>
>> Déterminer la valeur totale des cartes à gratter en fonction des numéros gagnants. Chaque carte a deux listes de numéros séparées par une barre verticale : une liste de numéros gagnants et une liste de numéros possédés. La première correspondance entre ces deux listes donne un point, et chaque correspondance supplémentaire double la valeur de la carte.
>
>- **Partie 2**
>>
>> Calculer le nombre total de cartes à gratter, y compris les originales et les copies, en suivant les nouvelles règles imprimées au dos des cartes. Selon ces règles, chaque correspondance de numéro gagnant permet de gagner des copies des cartes suivantes, égales au nombre de correspondances. Les copies sont évaluées comme des cartes normales. Ce processus se répète jusqu'à ce qu'aucune copie supplémentaire ne soit gagnée.
>
<!--  -->
>
> ***Day 5 : If You Give A Seed A Fertilizer***
>
>- **Partie 1**
>>
>> Trouver le numéro de localisation le plus bas correspondant à n'importe lequel des numéros de graines initiaux, en utilisant les cartes de conversion fournies dans l'almanach. Ces cartes convertissent les numéros de graines en numéros de sol, de sol en engrais, d'engrais en eau, et ainsi de suite, jusqu'à la localisation. Les numéros non mappés correspondent au même numéro de destination.
>
>- **Partie 2**
>>
>> Les numéros de graines initiaux représentent en fait des plages de numéros. Chaque paire de valeurs dans la ligne "seeds:" décrit une plage de numéros de graines à planter. Utiliser les mêmes cartes de conversion pour trouver le numéro de localisation le plus bas correspondant à n'importe lequel des numéros de graines dans ces plages.
>
<!-- -->
>
> ***Day 6 : Wait For It***
>
>- **Partie 1**
>>
>> Calculer le nombre de façons de battre le record dans chaque course de bateaux jouets. Chaque course a une durée fixe et un record de distance à battre. La vitesse du bateau augmente de un millimètre par milliseconde pour chaque milliseconde passée à appuyer sur le bouton au début de la course. Le bouton ne peut être tenu qu'une seule fois et le temps passé à le tenir est déduit du temps total de la course.
>
>- **Partie 2**
>>
>> Contrairement à ce qui était initialement pensé, il n'y a qu'une seule course, et les nombres sur la feuille de papier doivent être lus en continu, sans tenir compte des espaces. Calculer le nombre de façons de battre le record de distance dans cette unique et longue course.
>
<!--  -->
>
> ***Day 7 : Camel Cards***
>
>- **Partie 1**
>>
>> Classer des mains de cartes dans le jeu de Camel Cards selon leur force. Chaque main est d'un type spécifique, allant de la plus forte à la plus faible : quinte flush royale, carré, full house, brelan, deux paires, une paire, et carte haute. Les mains sont d'abord classées par type, puis par la force des cartes individuelles en cas de type identique. Le but est de calculer les gains totaux en multipliant l'enchère de chaque main par son rang, où le rang est déterminé par la force relative de la main.
>
>- **Partie 2**
>>
>> Introduire une nouvelle règle où les cartes J sont des jokers pouvant prendre la valeur de n'importe quelle carte pour former la main la plus forte possible. Cependant, pour le classement, les J restent les cartes les plus faibles. Avec cette nouvelle règle, recalculer le classement des mains et les gains totaux en suivant le même processus que dans la première partie.
>
<!--  -->
>
> ***Day 8 : Haunted Wasteland***
>
>- **Partie 1**
>>
>> Calculer le nombre de pas nécessaires pour atteindre le nœud ZZZ en suivant une série d'instructions gauche/droite à travers un réseau de nœuds étiquetés. Chaque nœud est défini par une paire de nœuds adjacents (gauche et droite). Commencer au nœud AAA et suivre les instructions, répétant la séquence d'instructions autant de fois que nécessaire jusqu'à atteindre ZZZ. Le but est de déterminer en combien de pas le nœud ZZZ est atteint en suivant ce processus.
>
>- **Partie 2**
>>
>> Déterminer le nombre de pas nécessaires pour que tous les chemins partant de nœuds se terminant par A aboutissent simultanément à des nœuds se terminant par Z. Pour chaque étape, suivre simultanément les instructions gauche/droite à partir de chaque nœud actuel. Si seulement certains des nœuds actuels se terminent par Z, ils continuent de fonctionner comme des nœuds normaux et la progression continue. Le but est de trouver combien de pas sont nécessaires pour que tous les chemins atteignent des nœuds se terminant par Z en suivant ce processus.
>
<!--  -->
>
> ***Day 9 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 10 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 11 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 12 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 13 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 14 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 15 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 16 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 17 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 18 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 19 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 20 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 21 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 22 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 23 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 24 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
<!--  -->
>
> ***Day 25 :***
>
>- **Partie 1**
>>
>>
>
>- **Partie 2**
>>
>>
>
#############################################################################################################################
#                                                                                                                           #
#                                                        Personnages                                                        #
#                                                                                                                           #
#############################################################################################################################

define jp = Character('Jean Plank', color="#c8ffc8")
define lucien = Character('Lucien le Magicien Marabout', color="#c8ffc8")
define sj = Character('Saint Gède', color="#c8ffc8")
define lee = Character('Lee le Voyant', color="#c8ffc8")
define titto = Character('Titto', color="#c8ffc8")
define inconnu = Character('???', color="#c8ffc8")
define ryze = Character('Rize le Sorcier', color="#c8ffc8")
define ryzeS = Character('Rize le Grand Schtroumpf', color="#c8ffc8")
define tristana = Character('Tristana', color="#c8ffc8")
define poppy = Character('Poppy', color="#c8ffc8")
define karma = Character('Karma : Gardienne de Prison et Blague Prévisible', color="#c8ffc8")


#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 1                                                            #
#                                                                                                                           #
#############################################################################################################################

label start:

scene introjp3
play music "music/introjp3.ogg"

"Notre bien aimé Jean Plank avait reçu un gigantesque météore sur la tronche (Qu'il avait désormais très moche)."
"Sa demeure, sa compagne, et tous ses biens venaient d'être réduit à néant."
"Il allait falloir se venger pour tout ça !"
"Mais chaque chose en son temps."

#voice "doublages_jp2/scene1/scene1_jp1.ogg"
jp "Lucien ! On va chez Singed !"

show introjp3_lucien
"Malgré sa grande tolérence, Lucien ne put s'empêcher un léger rictus de dégoût en voyant l'hideux visage de Jean Plank."

#voice "doublages_jp2/scene1/scene1_lucien1.ogg"
lucien "Oh mes aïeux, mais qu'est-ce que t'es moche !"

#voice "doublages_jp2/scene1/scene1_jp2.ogg"
jp "C'est bon, je crois qu'on a compris !"

#voice "doublages_jp2/scene1/scene1_lucien2.ogg"
lucien "On ne peut décemment pas te laisser comme ça ! Attends ne bouge pas je vais essayer de trouver un morceau de toile ou quelque chose pour arranger ça."

#voice "doublages_jp2/scene1/scene1_jp3.ogg"
jp "Lucien, je n'ai aucune décence."

"Mais lucien n'écoutait pas"
#voice "doublages_jp2/scene1/scene1_lucien3.ogg"
lucien "Oh c'est pas mal ça.Sauf que c'est pas vraiment ta taille. Ah mais c'est la mienne !"

"Jean Plank, un peu agacé mais surtout incrédule regarda Lucien s'emmitoufler dans le bout de tissu pourrit qu'il venait de rammaser."
"Le resultat final était étrangement plus convainquant que ce qu'on aurait pu imaginer."

#voice "doublages_jp2/scene1/scene1_jp4.ogg"
jp "Je n'ai pas les mots..."
"Dit-il en se mettant en route."

scene jp_porte
"Quelques minutes plus tard, nos deux compères, l'un en colère l'autre en burqa, arrivaient devant la porte de Saint Gède."


#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 2                                                            #
#                                                                                                                           #
#############################################################################################################################


show fight
play music "music/religieux_shop.ogg"
play sound "sound/violent_open_door.ogg"
#voice "doublages_jp2/scene2/scene2_jp1.ogg"
jp "Saint Gède ! Rends moi mon visage sale escroc !"

#voice "doublages_jp2/scene2/scene1_sj1.ogg"
sj "Jean Plank ?! Oh mon Dieu, mais qu'est-ce que tu es moche !"

#voice "doublages_jp2/scene2/scene2_jp2.ogg"
jp "Ça va on a compris ! Et c'est ta faute, roulure ! Tu ne nous m'as jamais parlé d'effets secondaires !"

#voice "doublages_jp2/scene2/scene2_jp2.ogg"
sj "Sais tu au moins ce que signifie expériementale ? Et puis tu aurais pu t'en douter ! Tu crois vraiment que je garde cette tête par plaisir ?!"

"Jean Plank se rendit alors compte qu'en effet, il aurait pu s'en douter."
"Mais hors de question de perdre la face face à Saint Gède !"
"Ivre de colère, il balança sa meilleure punchline au visage hideux de son détracteur."

#voice "doublages_jp2/scene2/scene2_jp3.ogg"
jp "Filou !"

#voice "doublages_jp2/scene2/scene2_sj3.ogg"
sj "Bon, si tu n'as rien d'autre à vociférer, j'aimerais retourner à mon travail !"

"Encore un mot que Jean Plank ne comprenait pas."
"Ce qu'il comprenait en revanche c'est le fait que Saint Gède était en train de l'envoyer dans les roses."
"Et les roses, ça pique !"


#####################
# COMBAT SAINT GEDE #
#####################
label debut_combat:

hide fight
show fight
play music "music/fightsinged.ogg"
"N'écoutant plus sa faible raison et cédant à la rage de l'ivrogne qui était en lui, Jean Plank s'élança sur Saint Gède, dans le but de le taper pour lui faire mal."

menu:
    "Courir sur Saint Gède avec rage":
        "Jean Plank courut sur Saint Gède avec rage"

        label fight_sj_jp_est_a_terre:
        
        "Il tenta de lui asséner un coup la tête, mais son adversaire esquiva."
        "Pris dans son élan, il perdit l'équilibre."
        "Saint Gède, en tant que Moine Guerrier Humaniste Savant Progressiste, en profita pour lui mettre un violent uppercut qui souleva Jean dans les airs."
        show jp_sj_sol
        "Ce dernier retomba lourdement quelques mètres plus loin dans le stock de potions de Saint Gède."
        menu:
            "Se relever":    
                "Jean Plank tenta de se relever. "
                "Malheureusement Saint Gède était rapide et avant même que Jean ne soit sur pied, il lui asséna un coup sur la tête renvoya au sol le capitaine."
                menu:
                    "Lancer du sable dans les yeux de Saint Gède":
                        label lancer_sable:
                            "Pas de chance, Saint Gède venait de faire le ménage, il n'y avait donc pas un grain de sable sur le sol."
                            "Jean Plank leva les yeux au ciel."
                            scene crucifix
                            play music "music/mort.ogg"
                            play sound "sound/crane_enfonce.ogg"
                            "L'énorme crucifix taille XL en fer chromé à moins 50 \% sur www.MaBonneSecte.com de Saint Gède fut la dernière chose que Jean Plank vit avant de rejoindre le Valhalla."
                            jump game_over

                    "S'en remettre au destin":
                        jump fin_combat

            "Lancer des bouts de verre brisé sur Saint Gède":
                "Jean Plank observa autour de lui. De nombreux morceaux de verre brisé jonchaient le sol."
                "C'est alors que notre bon capitaine prit l'initiative de les ramasser pour les lancer sur Saint Gède."
                "Malheureusement pour lui, une potion de fragilité s'était brisée lors de son atterrissage mettant fin à sa toute puissance." #à sa win streak
                "Devant l'odeur de misère et de défaite que dégagait Jean Plank, Saint Gède réalisa qu'il était grand temps de débrasasser le monde de cet hérétique. Il installa donc Jean Plank sur un bûcher."
                "Bien que fatidieux, c'était l'occasion rêvée de se débarasser de son achat compulsif sur www.MaBonneSecte.com."
                "En même temps, à -60 \% ça aurait idiot de se priver."

                scene bucher
                play sound "sound/cri_bucher.ogg"
                play music "music/mort.ogg"
                "C'est ainsi que Jean Plank partit, purifié par le feu."
                jump game_over

    "Courir sur Saint Gède avec encore plus de rage":
        "Ignorant ses limites, Jean Plank courut sur Saint Gède avec bien plus de rage qu'il n'aurait dû le faire."
        "Ses yeux étaient si injectés de sang qu'il ne voyait plus rien !"
        "Saint Gède n'eut ainsi aucun mal à l'éviter."
        "Jean Plank, continuant sa charge, finit par se cogner dans un meuble."
        "Il roula sur le sol en jurant sous le regard médusé de Saint Gède."
        show jp_meuble
        "Il se releva péniblement, toisant Saint Gède du regard."
        
        #voice "doublages_jp2/scene2/scene2_jp4.ogg"
        jp "Je vois que toi aussi tu es devenu plus fort !"
        sj "..."

        menu:
            "Frapper Saint Gède":
                jump fight_sj_jp_est_a_terre
            "Laisser Saint Gède me frapper, de toute façon, je suis invincible grâce à la potion.":
                label jp_head_explode:
                "Jean Plank regarda le poing de Saint Gède se diriger vers son visage pensant pouvoir l'encaisser sans même froncer un sourcil."
                "Cependant il ne savait pas que l'invincibilité ne lui serait d'aucun secours."
                "Ce qu'il ne savait pas non plus, c'est que Saint Gède s'était mit à la musculation en plus d'avoir un patrimoine génétique avantageux."
                "Le poing de Saint Gède arriva sur le visage de Jean Plank,"
                "Déforma le visage de Jean Plank."
                "C'est à peu près à ce moment là que Jean compris que sa stratégie de rester immobile n'allait malheureusement pas fonctionner."
                "Ignorant hideux l'obsacle qui se dressait devant lui, le poing de Singed continua sa folle course à travers le visage de Jean Plank."
                scene entrepot_mort
                play music "music/mort.ogg"
                play sound "sound/crane_enfonce.ogg"
                #"Dans un bruit de crâne qui romp et de vieille éponge mouillée, la cervelle de notre bon capitaine éclaboussa soudain les murs de l'entrepôt."
                jump game_over

#########################
# FIN COMBAT SAINT GEDE #
#########################

label fin_combat:
"Déjà deux fois qu'il était à terre, et Jean Plank sentait très bien qu'il n'était plus invincible. Saint Gède avait décidément une force écrasante."
"Jean Plank n'avait plus 36 solutions, il lui fallait s'en remettre à l'univers."

#voice "doublages_jp2/scene2/scene2_sj4.ogg"
sj "Je n'ai plus ton temps Jean Plank !"
"Répondit Saint Gède en brandissant son crucifix de d'un mètre quatre-vingt-quinze."

scene lucienjp3
#voice "doublages_jp2/scene2/scene2_lucien1.ogg"
lucien "Par la puissance de Zhonya !"

"Gronda alors la voix de Lucien à travers la pièce."
"Saint Gède s'arrêta net."
"La formule interdite avait été prononcée."
"Il venait de se changer en une statue dorée."

play music "music/jp_theme.ogg"
show lucien_sj
#voice "doublages_jp2/scene2/scene2_jp2.ogg"
lucien "Tu aurais du le savoir, le mensonge donne des fleurs, mais pas de fruit !"
"Jean Plank regarda Lucien le magicien et réalisa qu'il ne pouvait vraiment pas compter sur l'univers."

show lucien_sj_jp
#voice "doublages_jp2/scene2/scene2_jp5.ogg"
jp "Pas mal ta magie, mais comment je fais pour récupérer mon visage maintenant ?"

#voice "doublages_jp2/scene2/scene2_lucien3.ogg"
lucien "Un simple merci aurait suffit !"

#voice "doublages_jp2/scene2/scene2_jp6.ogg"
jp "Je l'attache puis tu le libère ?"

#voice "doublages_jp2/scene2/scene2_lucien4.ogg"
lucien "Impossible, une fois le Zhonya activé on ne peut plus rien faire pendant 2,5 !"

#voice "doublages_jp2/scene2/scene2_jp7.ogg"
jp "2,5 quoi ?"

#voice "doublages_jp2/scene2/scene2_lucien5.ogg"
lucien "Aucune idée, quelqu'un a gribouillé dans mon livre !"

"Dubitatif, Jean Plank regarda Lucien dans les yeux."
"Après l'avoir bien regardé, la conclusion paraissait évidente."

#voice "doublages_jp2/scene2/scene2_jp8.ogg"
jp "Mmmh, il est quand même très noir."

#voice "doublages_jp2/scene2/scene2_lucien6.ogg"
lucien "Et toi tu es quand même très moche !"

#voice "doublages_jp2/scene2/scene2_jp9.ogg"
jp "Lucien, trouve une solution, après tout c'est ta faute !"

hide jpsinged_crayon1

"C'est vrai, c'était sa faute."
"Lucien se mit à réfléchir."

#voice "doublages_jp2/scene2/scene2_lucien7.ogg"
lucien "Je connais peut-être un magicien qui pourrait te rendre ton visage."

#voice "doublages_jp2/scene2/scene2_jp10.ogg"
jp "Eh bien, en avant !"

"Jean Plank ne savait pas trop où il allait, mais il aimait bien dire \"En avant !\"."
"Après quelques explications de Lucien, nos deux compères embarquèrent vers le continent en direction du mage qui pourrait peut-être rendre son visage si rempli de piété et de sympathie à Jean Plank."


#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 3                                                            #
#                                                                                                                           #
#############################################################################################################################

scene bateau
play music "music/bateau.ogg"
$renpy.sound.play("sound/sound_mer.ogg", loop=True)

"Voilà maintenant quelques jours que Lucien et Jean Plank avaient pris la mer."
"Les occupations venaient à manquer et l'équipage avait trop peu de QI pour tenir une conversation."
"Lucien trompait donc son ennui en tentant d'en apprendre plus sur la vie du capitaine."
"Lui qui était d'un ordinaire peu loquace était étrangement bavard depuis quelque temps."
"Probablement l'air marin."
"Ou peut-être la quantité astronomique de rhum dans ses veines."

show jpsinged
#voice "doublages_jp2/scene3/scene3_jp1.ogg"
jp "Mais bien sûr que sa mort m'attriste ! Tu ne m'as donc pas vu mes larmes viriles ?"

show lucien_droite1
#voice "doublages_jp2/scene3/scene3_lucien1.ogg"

lucien "Tête de coco, j'ai tout vu et c'est pour ton visage que tu as pleuré, pas pour Miss Fourtout !"

#voice "doublages_jp2/scene3/scene3_jp2.ogg"
jp "Peu importe. De toute façon ce n'était que le numéro après 49."

#voice "doublages_jp2/scene3/scene3_lucien2.ogg"
lucien "Le numéro 50 ?"

#voice "doublages_jp2/scene3/scene3_jp3.ogg"
jp "Bah oui, si c'est celui qui suit le 49."

#voice "doublages_jp2/scene3/scene3_lucien3.ogg"
lucien "Mais attends là ! Tu ne sais pas compter ?"

#voice "doublages_jp2/scene3/scene3_jp4.ogg"
jp "Et pas lire non plus !"

#voice "doublages_jp2/scene3/scene3_lucien4.ogg"
lucien "Mais attends ce n'est pas possible, je suis sûr de t'avoir vu compter les pièces de ton trésor !"

stop sound
play music "music/crayon.ogg"
#voice "doublages_jp2/scene3/scene3_jp5.ogg"
show jpsinged_crayon
jp "Lucien, l'humour est un refuge." #Lucien ? Quel trésors ?

show lucien_crayon
#voice "doublages_jp2/scene3/scene3_lucien5.ogg"
lucien "..."

hide jpsinged_crayon
hide lucien_crayon
play music "music/bateau2.ogg"
$renpy.sound.play("sound/sound_mer.ogg", loop=True)

#voice "doublages_jp2/scene3/scene3_jp6.ogg"
jp "De toute façon mon véritable amour, c'est l'océan." 

#voice "doublages_jp2/scene3/scene3_lucien6.ogg"
lucien "La grosse flaque salée là."

#voice "doublages_jp2/scene3/scene3_jp7.ogg"
jp "Ce n'est pas une simple flaque Lucien ! Dans ces eaux se cache une déesse à laquelle je suis lié."

#voice "doublages_jp2/scene3/scene3_lucien7.ogg"
lucien "Lié ? C'est-à-dire ?"

#voice "doublages_jp2/scene3/scene3_jp8.ogg"
jp "Nous avons été amants pendant des années !"

#voice "doublages_jp2/scene3/scene3_lucien8.ogg"
lucien "Ton histoire est un peu étrange."

#voice "doublages_jp2/scene3/scene3_jp9.ogg"
jp "Tu sais ce qu'on dit : c'est pas l'homme qui prend la mer, c'est la mer qui prend l'homme."

#voice "doublages_jp2/scene3/scene3_lucien9.ogg"
lucien "Ta, ta, ta, ça c'est des sottises. Et pourquoi ça c'est terminé ?"

#voice "doublages_jp2/scene3/scene3_jp10.ogg"
jp "Et bien, je navigue régulièrement en eaux douces, si tu vois ce que je veux dire."

"Non, Lucien ne voyait pas."
"Mais il savait au plus profond de son cœur qu'il ne voulait pas plus de détails."

#voice "doublages_jp2/scene3/scene3_lucien10.ogg"
lucien "Mais, du coup, elle t'a pardonné ?"

#voice "doublages_jp2/scene3/scene3_jp11.ogg"
jp "Bah non pourquoi ?"

stop sound
play music "music/finduvoyage.ogg"
show naufrage

#voice "doublages_jp2/scene3/scene3_naufrage.ogg"
window hide
pause

#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 4                                                            #
#                                                                                                                           #
#############################################################################################################################

scene plage
show jpsinged1

scene plage
show jpsinged1
$renpy.sound.play("sound/sound_mouettes.ogg" , loop=True)
play music "music/plage.ogg"
#voice "doublages_jp2/scene4/scene4_jp1.ogg"
jp "Encore un beau voyage sans encombre !"

show lucien_gauche
#voice "doublages_jp2/scene4/scene4_lucien1.ogg"
lucien "Comment ça \"sans encombre\" ?"

#voice "doublages_jp2/scene4/scene4_jp2.ogg"
jp "Gibier de potence ! On est arrivés à bon port."

#voice "doublages_jp2/scene4/scene4_lucien2.ogg"
lucien "Déjà ce n'est pas le port mais juste la plage, et je tiens à signaler qu'on a perdu le bateau !"

#voice "doublages_jp2/scene4/scene4_jp3.ogg"
jp "Il n'y avait rien dedans de toute façon."

#voice "doublages_jp2/scene4/scene4_lucien3.ogg"
lucien "Comment ça, là ? Et les 9 membres d'équipage qui sont morts ?"

#voice "doublages_jp2/scene4/scene4_jp4.ogg"
jp "Ils ne sont pas morts dans le bateau !"

#voice "doublages_jp2/scene4/scene4_lucien4.ogg"
lucien "Bah évidemment qu'ils sont pas morts dans le bateau, tu les as attachés pour faire un radeau !"

#voice "doublages_jp2/scene4/scene4_jp5.ogg"
jp "Tout le monde doit payer ! Et puis tu l'as aussi utilisé ce radeau."

#voice "doublages_jp2/scene4/scene4_lucien5.ogg"
lucien "Attends, attends, attends ! Moi j'étais là seulement pour marabouter leur esprit, pour que leur âme elle aille vers un monde meilleur."

#voice "doublages_jp2/scene4/scene4_jp6.ogg"
jp "Bon il est ou ton magicien ?"

#voice "doublages_jp2/scene4/scene4_lucien6.ogg"
lucien "Alors, ça je ne sais pas. Normalement on devait arriver proche du port du village mais à cause de ta miss tentacule je sais plus du tout où on est !"

#voice "doublages_jp2/scene4/scene4_jp7.ogg"
jp "Lucien ne t'inquiète pas."

#voice "doublages_jp2/scene4/scene4_lucien7.ogg"
lucien "Pourquoi ?"

#voice "doublages_jp2/scene4/scene4_jp8.ogg"
jp "Il est vrai que j'aurais dû t'en parler depuis longtemps mais les choses sont allées si vite. Il faut maintenant que je te révèle mon principal atout."

#voice "doublages_jp2/scene4/scene4_jp9.ogg"
jp "En fait je suis gaucher."

"Lucien regarda attentivement Jean Plank."
"Aucun doute il disait vrai."
"Mais cela ne les avançait pas beaucoup."
"C'est alors qu'apparut au yeux de notre bon capitaine un détail sur le visage de Lucien qui allait les sortir de là."

#voice "doublages_jp2/scene4/scene4_jp10.ogg"
jp "Lucien !"

#voice "doublages_jp2/scene4/scene4_lucien8.ogg"
lucien "Qu'est ce qu'il y a ?"

#voice "doublages_jp2/scene4/scene4_jp11.ogg"
jp "Ton nez Lucien, il est énorme."

#voice "doublages_jp2/scene4/scene4_lucien9.ogg"
lucien "Ecoute moi bien gros patapouf je ne vois pas bien ou tu veux en venir mais... "

scene jpsinged_crayon
$renpy.sound.set_volume(0.00, delay=0, channel='sound')
play music "music/crayon.ogg"

#voice "doublages_jp2/scene4/scene4_jp12.ogg"
jp "Lucien nous n'avons pas 36 solutions. "

scene lucien_crayon
#voice "doublages_jp2/scene4/scene4_lucien10.ogg"
lucien "Ohlàlà t'es très mal parti toi."

scene jpsinged_crayon
#voice "doublages_jp2/scene4/scene4_jp13.ogg"
jp "Mais Lucien, c'est un don du ciel. "

scene lucien_crayon
#voice "doublages_jp2/scene4/scene4_lucien11.ogg"
lucien "Je vois très bien où tu veux en venir et je t'assure que je vais te casser la gueule."

scene jpsinged_crayon
#voice "doublages_jp2/scene4/scene4_jp14.ogg"
jp "Mais Lucien..."

scene lucien_crayon
#voice "doublages_jp2/scene4/scene4_lucien12.ogg"
lucien "Oh putain ça part !"

$renpy.sound.set_volume(1.00, delay=0, channel='sound')
scene jpsinged_poulet

play music "music/jp_theme.ogg"

"Ne voulant pas se battre avec son magicien, Jean Plank, passé maître dans l'art de la corruption, sortit de sa poche un morceau de poulet."
"A la vue de la viande blanche dans la main du capitaine, la malediction qui pesait sur Lucien réapparut et ce dernier, contrain et forcé se jeta aux pieds du capitaine."

scene lucien_nez

"Le morceau de poulet disparu, il était temps pour Lucien de commencer sa besogne."
"Il regarda en l'air et tendit alors son très très gros nez."
"A sa grande surprise, il sentit quelque chose d'autre que l'air marin."
"Une odeur putride et malpropre, un immonde mélange entre un mauvais rhum et une odeur d'égout."
"Lucien décida alors de s'éloigner de Jean Plank."
"Il fit un nouvel essai."
"Il n'y avait pas d'odeur de magie dans l'air."
"En revanche odeur d'encens et de mirrhe avec peut-être un soupçon de thé vert vint lui carresser les narines."
"Aucune chance que ce soit celle d'u magicien mais elle semblait peu lointaine et Lucien pensa qu'il valait mieux la suivre plutôt que de rester là à ne rien faire."
"Ils trouveraient bien quelqu'un pour leur montrer le chemin."

#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 5                                                            #
#                                                                                                                           #
#############################################################################################################################

scene cabane
$renpy.sound.play("sound/sound_forêtambient.ogg" , loop=True)
play music "music/leesin.ogg"

"L'odeur les mena jusqu'à un petit cabanon. A l'entrée, on trouvait deux statues d'homme gros et gras à l'air niais, assises en position du lotus."
"Jean Plank reconnut immédiatement la sublime teinte du jade rouge dans lequel elles étaient taillées et entreprit donc d'arracher un bras à l'une des statues, histoire de se reconstruire un trésor."

#voice "doublages_jp2/scene5/scene5_leesin1.ogg"
inconnu "Jean Plank !"
"Fit alors une voix provenant de l'intérieur du cabanon."
"Jean Plank entra, suivi par Lucien."

scene interieur
stop sound
"Ils se retrouvèrent alors nez à nez avec leur interlocuteur, un moine ayant pour seuls vêtements des habits et un bandeau sur les yeux."

show jpsinged1
show leesin

#voice "doublages_jp2/scene5/scene5_leesin2.ogg"
lee "Je t'attendais, Jean Plank."

#voice "doublages_jp2/scene5/scene5_jp1.ogg"
jp "Comment connais-tu mon nom ?"

show leesin

#voice "doublages_jp2/scene5/scene5_leesin3.ogg"
lee "Je vois tout !"

"Si l'explication convaincut Jean Plank, elle laissa Lucien un peu dibitatif :"

hide jpsinged1
show lucien_droite

#voice "doublages_jp2/scene5/scene5_lucien1.ogg"
lucien "Bah non, toi tu ne vois rien !"

#voice "doublages_jp2/scene5/scene5_leesin4.ogg"
lee "Mais si, je suis voyant."

#voice "doublages_jp2/scene5/scene5_lucien2.ogg"
lucien "N'importe quoi ! Je vois très bien que tu as un bandeau sur les oeils !"

#voice "doublages_jp2/scene5/scene5_leesin5.ogg"
lee "Oui car je suis aveugle."

#voice "doublages_jp2/scene5/scene5_lucien3.ogg"
lucien "Eh bah voilà, tu vois bien que tu vois pas !"

hide leesin
hide lucien_droite

"Lee qui voyait très bien, que Lucien allait LUI CASSER LES COUILLES, lui mit un impressionant yokogeri qui le transporta hors de sa vue."
"Enfin non, hors de sa demeure."
"Vous aviez compris que Lee était aveugle ?"

show leesin
show jpsinged1

#voice "doublages_jp2/scene5/scene5_leesin6.ogg"
lee "Je disais donc que ce qui t'amène... Sois gentil, repose ce vase petit scarabée."

"Jean Plank reposa le vase."

#voice "doublages_jp2/scene5/scene5_leesin7.ogg"
lee "Tu veux détruire celui, qui t'a déshonoré !"

#voice "doublages_jp2/scene5/scene5_jp1.ogg"
jp "Oui !"

#voice "doublages_jp2/scene5/scene5_leesin8.ogg"
lee "Tu veux lui casser sa gueule, à cette raclure ! "

#voice "doublages_jp2/scene5/scene5_jp2.ogg"
jp "Oui !"

#voice "doublages_jp2/scene5/scene5_leesin9.ogg"
lee "Lui péter les genoux ! "

#voice "doublages_jp2/scene5/scene5_jp3.ogg"
jp "Oui !"

#voice "doublages_jp2/scene5/scene5_leesin10.ogg"
lee "Lui arracher les couilles avec les dents et en faire un pendentif !"

#voice "doublages_jp2/scene5/scene5_jp4.ogg"
jp "OUI !"

#voice "doublages_jp2/scene5/scene5_leesin11.ogg"
lee "Eh bah tu seras gentil, tu feras pas ça parce que c'est dégueulasse."

#voice "doublages_jp2/scene5/scene5_jp5.ogg"
jp "Comment dois-je me venger alors ?"

#voice "doublages_jp2/scene5/scene5_leesin16.ogg"
lee "Pour cela tu devras trouver certains artefacts sacrés !"

#voice "doublages_jp2/scene5/scene5_jp6.ogg"
jp "Et je les trouve où les artefacts ?"

#voice "doublages_jp2/scene5/scene5_leesin12.ogg"
lee "Dans ton cul ! Nan je rigole mais par contre repose ce verre en cristal ou je te défonce ta face de rat."

"Jean Plank reposa le verre en cristal."

#voice "doublages_jp2/scene5/scene5_leesin13.ogg"
lee "Sachant que ton ennemi est devenu les ténèbres, ce qu'il te faut c'est devenir la lumière, mais comme on approche du solstice l'éclairage diminue. Il faut donc tenir compte de l'inertie liée à la vitesse de rotation du soleil par rapport à la lune. Laisse moi refléchir un peu... Mmmh normalement si tu prends la prochaine à droite c'est tout bon."
"Jean Plank n'avait pas vraiment compris qui était son ennemi."
"Aussi posa t'il la seule question qui importait vraiment /"

#voice "doublages_jp2/scene5/scene5_jp7.ogg"
jp "La prochaine à droite c'est par où ?"

#voice "doublages_jp2/scene5/scene5_leesin14.ogg"
lee "C'est à droite ! Maintenant si tu pouvais te casser parce que j'ai un rendez-vous important pour l'introduction en bourse de ma startup voyance. Donc je n'ai pas le temps !"

#voice "doublages_jp2/scene5/scene5_jp8.ogg"
jp "D'accord mais..."

#voice "doublages_jp2/scene5/scene5_leesin15.ogg"
lee "Je n'ai pas le temps je te dis  ! Tu demanderas ton chemin ! Casse toi maintenant !"

"VOYANT que Jean Plank ne partait toujours pas, Lee se mit à lui lancer du riz en hurlant."

#voice "doublages_jp2/scene5/scene5_leesin16.ogg"
lee "Allez zou pch pchh !!"

scene cabane

"Jean désormais bien éclairé et couvert de riz rejoignit Lucien à l'extérieur."
"Il n'avait malheureusement pas pu se saisir de la moindre pièce du trésor qui dormait dans l'antre de Lee."
"Bien résolu à en prendre les plus beaux bibelots, il dessina une croix sur le sol pour se souvenir de son emplacement."

#voice "doublages_jp2/scene5/scene5_jp9.ogg"
jp "C'est bon, on peut y aller !"
"Lâcha-t-il en se dirigeant vers la première à droite comme Lee le leur avait indiqué."


#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 6                                                            #
#                                                                                                                           #
#############################################################################################################################

scene village
$renpy.sound.play("sound/sound_forêtambient.ogg" , loop=True)
play music "music/village.ogg"

"Nos deux protagonistes arrivèrent devant le village indiqué par Lucien."
"Une espèce de petit écureuil miteux vint les acceuillir."

show teemo

#voice "doublages_jp2//scene6/scene6_titto.ogg"
titto "Salut ! Vous venez voir Rize ?"
"Voyant ce petit être ignoble, Lucien fut pris d'un excès de rage sanguinaire."
"Il sortit sa baguette trop grosse et mit un magistral coup de pied à Titto qui partit s'écraser sur un rocher quelques mètres plus loin."

hide teemo
play sound "sound/teemo_punch.ogg"
$ renpy.movie_cutscene("teemo_mort.mpg")

"Il rangea ensuite sa baguette trop grosse avec difficulté, parce qu'elle était trop grosse."
"Jean Plank de son coté était un peu abasourdi."

#voice "doublages_jp2//scene6/scene6_jp1.ogg"
jp "Lucien, qu'est ce qui te prend ?"

#voice "doublages_jp2//scene6/scene6_lucien1.ogg"
lucien "J'ai du mal avec ce genre de bestiole."

#voice "doublages_jp2//scene6/scene6_jp2.ogg"
jp "Mais Lucien, il venait sans doute nous acceuillir !"

#voice "doublages_jp2//scene6/scene6_lucien2.ogg"
lucien "Cette vermine vehicule nombre de maladies ! Dans mon pays natal, des villes entières sont tombées parce qu'elles ne savaient pas prendre les décisions qui s'imposaient ! En plus tu verrais, ça se multiplie à une vitesse... On dirait des autruches !"

#voice "doublages_jp2//scene6/scene6_jp3.ogg"
jp "Mais Lucien, je crois que c'était un membre du village."

#voice "doublages_jp2//scene6/scene6_lucien3.ogg"
lucien "Rhoo ça va tu passes ton temps à faire des conneries toi là. Je t'en pose moi des questions ? En plus ne t'inquiète pas, j'ai la solution : je vais en faire un tapis."

#voice "doublages_jp2//scene6/scene6_jp4.ogg"
jp "Lucien ?"

#voice "doublages_jp2//scene6/scene6_lucien4.ogg"
lucien "Ehhh comme ça ils auront un souvenir de l'animal, un peu comme moi j'ai gardé un souvenir de Maman à ma ceinture."

#voice "doublages_jp2//scene6/scene6_jp5.ogg"
jp "Lucien ?"

show lucien_tete_reduite
#voice "doublages_jp2//scene6/scene6_lucien5.ogg"
lucien "Eh regarde comme elle est belle là, en plus tu trouves pas que j'ai un peu son sourire ?"
hide lucien_tete_reduite

#voice "doublages_jp2//scene6/scene6_jp6.ogg"
jp "Heu... Tout le monde doit payer ?"

"Ainsi Lucien récupéra rapidement l'animal."
"Il le dépeça tel un taxidermiste professionnel et hop, quelques secondes et une incantation plus tard, il avait transformé ce l'écureuil malchanceux en un magnifique paillasson."
"Il courut ensuite à la maisonnette la plus proche, et déposa son oeuvre davant la porte d'entrée."
play music "music/lucienencage.ogg"

scene lucien_cage
"Alors qu'il retournait vers Jean, il fut arrêté dans sa course."
"Il était emprisonné dans une cage bleutée à l'aura étrange et ornée de symboles runiques."

#voice "doublages_jp2/scene4/scene6_lucien6.ogg"
"\"Oh non, ça recommence\" pensa-t-il."
"Il se retourna."
scene ryze_court
"Un personnage à la peau bleue, tout vêtu de... bah de bleu, et à l'air mécontent et menaçant était en train de courir vers Jean Plank."

scene ryze_sortez
#voice "doublages_jp2//scene6/scene6_rize1.ogg"
inconnu "Rhaaaaaaaaaa vagabonds, voleurs, sortez de MON village !"

"Lucien le reconnut immédiatement."
scene jp_question
"Jean Plank, lui, ne le reconnut pas immédiatement."
"Cela dit c'était normal, puisqu'il ne le connaissait pas."

scene lucien_cage
#voice "doublages_jp2//scene6/scene6_lucien7.ogg"
lucien "Rize !"

scene ryze_sortez2
"Le personnage bleuté tourna la tête."

#voice "doublages_jp2//scene6/scene6_rize2.ogg"
ryze "Il n'y a qu'un seul être au monde possèdant une voix aussi mélodieuse !"

scene lucien_cage_sans_cage
"A ces mots, Lucien fut libéré de son étroite entrave."

play music "music/village2.ogg"

scene ryse_lucien_village
#voice "doublages_jp2//scene6/scene6_rize3.ogg"
ryze "Luchieng, au pied mon tout beau !"

scene ryse_lucien_village_2
#voice "doublages_jp2//scene6/scene6_lucien8.ogg"
lucien "Hé mais attends là mon coco, j'ai évolué depuis ce temps là, je suis maintenant moi aussi devenu un magicien !"

#voice "doublages_jp2//scene6/scene6_rize4.ogg"
ryze "Ouais tu m'en diras tant."

#voice "doublages_jp2//scene6/scene6_lucien9.ogg"
lucien "Nan mais regarde, je pratique la magie !"

#voice "doublages_jp2//scene6/scene6_rize5.ogg"
ryze "Ouais c'est ça ouais !"

scene lucien_carte
"Alors Lucien sortit un jeu de cartes, et devina quelle carte Rize avait choisi."

scene ryse_lucien_village_2
#voice "doublages_jp2//scene6/scene6_rize6.ogg"
ryze "Et bah mon salaud !"

scene jpsinged_inutile_de_le_presenter
#voice "sound/explosion_poudre.ogg"
"Jean Plank qui avait été oublié jusque ici, sortit un de ses fameux tonneaux et le fit exploser (oui, Jean Plank transportait toujours quelques tonneaux de poudre noire de très bonne qualité)."

"Rize fut surpris mais pas étonné."
#voice "doublages_jp2//scene6/scene6_rize7.ogg"
ryze "Luchieng, c'est qui ce mec là ?"

#voice "doublages_jp2//scene6/scene6_jp7.ogg"
jp "Haha, inutile de me présenter !"

#voice "doublages_jp2//scene6/scene6_rize8.ogg"
ryze "Oh mon Dieu, qu'est ce qu'il est moche !"

scene ryse_lucien_village_2

#voice "doublages_jp2//scene6/scene6_lucien10.ogg"
lucien "C'est la magie vaudoo maléfique qui lui a transfomé son visage. Nous sommes justement venus te demander ton aide pour lui rendre son faciès habituel."

scene vers-la-maison-de-ryse
#voice "doublages_jp2//scene6/scene6_rize9.ogg"
ryze "Rien de plus facile, suivez moi."

stop sound

"Ils suivirent alors Rize jusqu'à sa hutte de chef, au milieu du village."


#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 7                                                            #
#                                                                                                                           #
#############################################################################################################################

scene bureau_entree
play music "music/bureau.ogg"

"Ils entrèrent dans le bureau."
#voice "doublages_jp2//scene7/scene7_rize1.ogg"
ryze "Attendez ici et ne touchez à rien !"
"Dit-il en se dirigeant vers son immense bibliothèque."

scene bureau4
"Lucien, de sa vue perçante de chasseur ceuilleur confirmé, s'interessait aux étiquettes des potions présentes sur les étagères."
"S'il comprit rapidement à quoi pouvait servir une potion de vitesse, il aurait bien eu besoin de quelques explications quand à l'utilité d'une potion de matérialisation d'imperméable."
"Mais Rize étant concentré, Lucien garda le silence pour ne pas paraître impoli."
"Après quelques minutes à chercher, Rize revint avec un énorme ouvrage à la couverture sombre sur lequel on pouvait lire, \"Vaudoo maléfique et piraterie volume 12\"."

scene emmanuel-visage
#voice "doublages_jp2//scene7/scene7_rize2.ogg"
ryze "Et voilà, le livre d'Emmanuel Visage : \"Trucs et astuces pour rendre son visage à un pirate qui s'est fait voler son visage à cause du vaudoo maléfique\" !"
"Il ouvrit le livre, parcourut l'index puis tourna les pages jusqu'à la formule qui l'intéressait."
"Il s'exclama"
#voice "doublages_jp2//scene7/scene7_rize3.ogg"
ryze "Parfait, j'ai tout ce qu'il me faut."
"Il se dirigea vers son placard à flacons et en ramena trois."
scene emmanuel-visage3
"Il prit un de ses merveilleux Erlenmeyers en cristal."
"Oui \"merveilleux\", le truc est enchanté car Rize est un sorcier, suivez un peu !"
"Il y versa le contenu des deux premières fioles."
"Il fut très satisfait à la vue de la petite explosion et du nuage rosâtre qui s'en échappa."
"Il voulut alors verser le contenu de la troisième fiole mais se rendit compte qu'elle était vide."

scene ryse_fait_chier_jen_ai_plus
#voice "doublages_jp2//scene7/scene7_rize4.ogg"
ryze "Rhoo fait chier, j'en ai plus."


show gibier-de-potence
window hide 
pause
#voice "doublages_jp2//scene7/scene7_jp1.ogg"
#jp "Gi-Gi-Gibier de potence !"

scene ryse_que_racconte_l_autre_debile
#voice "doublages_jp2//scene7/scene7_rize5.ogg"
ryze "Qu'est ce qu'il raconte encore l'autre débile là ?"

scene bureau3

#voice "doublages_jp2//scene7/scene7_lucien1.ogg"
lucien "Attention à ne pas être trop aggressif, ça attire les mauvais esprits ! Qu'est ce qu'il te faudrait, mon ami ?"

scene bureau5
#voice "doublages_jp2//scene7/scene7_rize6.ogg"
ryze "T'inquiètes c'est rien je gère. Il me faut juste des larmes de schtroumpf."

#voice "doublages_jp2//scene7/scene7_lucien2.ogg"
lucien "Un schtroumpf, c'est quoi ce truc là encore ?"

#voice "doublages_jp2//scene7/scene7_rize7.ogg"
"Rize haussa les épaules en laissant échapper un petit grognement."


#voice "doublages_jp2//scene7/scene7_lucien3.ogg"
lucien "Alors comment tu vas faire ?"

#voice "doublages_jp2//scene7/scene7_rize8.ogg" #bcp de parasites sur le doublage
ryze "Oh mais tu vas voir ! Je vais utiliser un sortilège de changement de statut !"


#voice "doublages_jp2//scene7/scene7_lucien4.ogg"
lucien "Un changement de statut ? C'est quoi encore ça comme magie ?"

#voice "doublages_jp2//scene7/scene7_rize9.ogg"
ryze "C'est de la magie du 4ème mur, tu vas voir."

scene bureau4
"Rize ce concentra un instant puis, déterminé, récita sa formule."

scene ryse_grand_shtroumf_transformation_1
#voice "doublages_jp2//scene7/scene7_rize10.ogg"
ryze "Kongo wa watashi GURAND SCHTRUMFU DESU ! EVAT FERF OU TREUGURI MALU KINU !"

scene ryse_grand_shtroumf_transformation_2

#voice "doublages_jp2//scene7/scene7_rize11.ogg"
ryzeS "Et voilà le travail !"

scene lucien-4eme-mur
#voice "doublages_jp2//scene7/scene7_lucien5.ogg"
lucien "Ohhhh on dirait de la magie !"

scene bureau4-bonnet
#voice "doublages_jp2//scene7/scene7_rize12.ogg"
ryzeS "Oh, tu as l'oeil ! C'est effectivement une des raisons pour lesquelles on m'appelle le Magicien."

scene bureau5-bonnet

#voice "doublages_jp2//scene7/scene7_jp2.ogg"
jp  "Et pour les larmes ?"

scene bureau6-bonnet
"Rize se dirigea vers l'extérieur."

#scene bureau6-bonnet2
#voice "doublages_jp2//scene7/scene7_rize13.ogg"
ryzeS "Hé Tristana, viens donc voir papa !"

scene bureau_entree_tristana
"Quelques secondes plus tard, Rize revint dans la maisonnée suivi d'une fillette et d'un dragonnet."

scene bureau_tristana
#voice "doublages_jp2//scene7/scene7_tristana1.ogg"
tristana "C'est qui eux ?"

#voice "doublages_jp2//scene7/scene7_rize14.ogg"
ryzeS "Des visiteurs."

#voice "doublages_jp2//scene7/scene7_jp3.ogg"
jp "Venus d'ailleurs !"

#voice "doublages_jp2//scene7/scene7_tristana2.ogg"
tristana "Pourquoi ils sont ici ?"

#voice "doublages_jp2//scene7/scene7_lucien6.ogg"
lucien "Eh bien, on aurait besoin d'aide pour soigner le visage de mon compagnon !"

scene tristana-monsieur-tout-noir
#voice "doublages_jp2//scene7/scene7_tristana3.ogg"
tristana "Tonton  Rize, pourquoi il est tout noir le monsieur ?"

#voice "doublages_jp2//scene7/scene7_rize15.ogg"
ryzeS "Euhm ta gueule, ta gueule."

scene tristana-monsieur-tout-noir2
tristana "Et pourquoi celui là il est moche ?"

jp "Haha, je m'appelle Jean Plank !"

scene ryse_cest_chiant
ryzeS "Jean Plank, hein ? Espèce de connard ! Et toi, t'arrêtes avec tes questions ?! C'est chiant à la fin !"

scene tristana_incomprehension
tristana "Mais, mais ?"

scene lucien_c_malin
#voice "doublages_jp2//scene7/scene7_lucien7.ogg"
lucien "Oh c'est malin !"

#voice "doublages_jp2//scene7/scene7_jp4.ogg"
jp "Quoi donc ?"

#voice "doublages_jp2//scene7/scene7_lucien8.ogg"
lucien "Lui crier dessus afin que les larmes gagnent ses yeux."

#voice "doublages_jp2//scene7/scene7_jp5.ogg"
jp "Oui, plutôt malin en effet..."

scene jp_intense_reflexion
"Jean plank savait qu'il pouvait faire mieux."
"Il était temps de rapeller au monde qui était le héros de cette histoire."
"Son regard croisa alors celui du dragonnet tout sourire dans les bras de Tristana."
scene brigels_malice
"Perdu dans ses yeux pétillants de joie, il songea à quel point lui-même serait triste s'il perdait son animal de compagnie."
"L'idée du siècle venait de germer dans le cerveau de Jean Plank."
"Il adressa alors à Brigels le dragonnet un sourire malicieux."

stop music
scene jpsinged_tire

#voice "sound/pan.ogg"
"Puis il sortit son pistolet, et lui tira une balle entre les deux yeux."

play music "music/mortrigglestheme.ogg"

"Il prit alors une posture solennelle et entama un discours."

scene jp_ceremonial
#voice "doublages_jp2//scene7/scene7_jp6.ogg"
jp "Brigels, petit dragonnet parti trop tôt, tu laisses un vide immense derrière toi. Et c'est avec beaucoup de tristesse et de compassion que je présente nos plus sincères condoléances a ta..."
"Se faisant soudain empoigner par Ryse, il ne put finir convenablement ses adieux."
#voice "doublages_jp2//scene7/scene7_rize16.ogg"
ryzeS "Mais qu'est ce que tu fous bordel !"

"Visiblement cet idiot de Ryse n'avait pas compris l'astucieux stratagème de Jean Plank pour obtenir les larmes."

play sound "sound/tristanabruitfont.ogg"
show jpsinged_degueu

#voice "doublages_jp2//scene7/scene7_jp7.ogg"
jp "T'inquiètes frère, je vais le cautériser !"
hide jpsinged_degueu

#voice "doublages_jp2//scene7/scene7_rize17.ogg"
ryzeS "Comment ça, le cautériser ? Mais il est mort, putain !"

#voice "doublages_jp2//scene7/scene7_jp8.ogg"
jp "Attends je vais chercher la poudre..."

#scene bureau
#show tristpleure

#play music "music/tristanaost.ogg"
#play sound "sound/tristanaLarme.ogg"
"Réalisant peu à peu ce qu'il se passait, Tristana fondit en larmes."

#voice "doublages_jp2//scene7/scene7_rize18.ogg"
ryzeS "Mais bordel, mais il est totalement demeuré ton pote, Lucien ! Lucien ?"

"Lucien de son coté était en train de récolter les larmes sur les joues de Tristana."

#voice "doublages_jp2//scene7/scene7_lucien9.ogg"
lucien "Bah quoi ? On a des larmes maintenant."

play sound "sound/violent_open_door.ogg"
"Rize était sur le point de fracasser son énorme nez quand il fut interrompu par le bruit de sa porte s'ouvrant violemment."

scene poppy

#voice "doublages_jp2//scene7/scene7_poppy1.ogg"
poppy "Rize ! Titto est mort !"

#voice "doublages_jp2//scene7/scene7_rize19.ogg"
ryzeS "Quoi ? Comment ça ?!"

#voice "doublages_jp2//scene7/scene7_poppy2.ogg"
poppy "C'est atroce, quelqu'un l'a dépeçé et a lancé ses restes devant ma porte !"

#voice "doublages_jp2//scene7/scene7_rize20.ogg"
ryzeS "QUOI ? Mais, quel connard a bien pu faire ça ?"

#voice "doublages_jp2//scene7/scene7_poppy3.ogg"
poppy "Nous devons absolument trouver ce psychopathe avant qu'il ne recommence !"

#voice "doublages_jp2//scene7/scene7_rize21.ogg"
ryzeS "Mais comment ? Pourquoi ?"

#voice "doublages_jp2//scene7/scene7_lucien10.ogg"
lucien "Hé là mais il est très joli mon tapis !"

#voice "doublages_jp2//scene7/scene7_rize22.ogg"
ryzeS "Quoi ?"

show lucien_droite
#voice "doublages_jp2//scene7/scene7_lucien11.ogg"
lucien "En même temps, j'ai fait ce que j'ai pu, c'était pas vraiment du bon poil, on aurait dit qu'il avait la teigne votre truc !"

#voice "doublages_jp2//scene7/scene7_rize23.ogg"
ryzeS "Mais vous êtes complètement demeurés, c'est pas possible !"

show jpsinged_degueu
#voice "doublages_jp2//scene7/scene7_jp9.ogg"
jp "Attention, ça va péter !"

#voice "doublages_jp2//scene7/scene7_rize24.ogg"
ryzeS "Quoi ?!"

#voice "doublages_jp2/explosion_poudre.ogg"
scene ecran_noir

"30 minutes plus tard, deux agents de police arrêtaient nos deux protagonistes et les conduisaient à Piltover pour y être jugés."

scene tribunal
"Malgrès les protestations de Lucien, qui tentait désespérément de prouver qu'il s'agissait d'un malentendu culturel, ils furent jugés coupables."

scene prison

play music "music/prison.ogg"

#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 8                                                            #
#                                                                                                                           #
#############################################################################################################################


"Jean Plank n'était pas content."
"Il avait un visage à retrouver, une vengeance à accomplir, des trésors à piller et des femmes CONSENTENTES à violer et tout cela n'était pas possible depuis sa cellule !"
"Il détestait les prisons. Les murs étroits et humides lui rappelaient la malle dans laquelle son père l'enfermait quand il était enfant."
"En somme : pas vraiment de bons souvenirs."
"Il réflechissait donc à un moyen de sortir."

show prison_lucian
#voice "doublages_jp2/scene8/scene8_lucien1.ogg"
lucien "Hé pourquoi tu fais ta tête de grognon là ?"

#voice "doublages_jp2/scene8/scene8_jp1.ogg"
jp "Silence, laquais !"

"Notre capitaine avait beau réfléchir du mieux qu'il pouvait, il n'arrivait pas à trouver de solution pour sortir de ce cachot."
"Le taux d'humidité était malheureusement bien trop haut pour se concentrer."

#voice "doublages_jp2/scene8/scene8_lucien2.ogg"
lucien "Cesse donc de te triturer les meninges. J'ai là quelques malices qui vont te plaire, mon ami !"

#voice "doublages_jp2/scene8/scene8_jp2.ogg"
jp "Qu'est ce donc là que cette duperie encore ?"

#voice "doublages_jp2/scene8/scene8_lucien3.ogg"
lucien "J'ai discretement lu la page du livre d'Emmanuel Visage : \"Trucs et astuces pour rendre son visage à un pirate qui s'est fait voler son visage à cause du vaudoo maléfique\"."

#voice "doublages_jp2/scene8/scene8_jp3.ogg"
jp "Et alors ?"

#voice "doublages_jp2/scene8/scene8_lucien4.ogg"
lucien "La potion que Rize voulait te préparer t'aurait rendu ton visage immédiatement, il est vrai."

#voice "doublages_jp2/scene8/scene8_lucien5.ogg"
lucien "Mais j'ai aussi appris que les effets du mal qui t'affecte sont temporaires ! Tu devrais retrouver ton visage habituel, si rempli de piété et de sympathie, très bientot et ce même sans potion."

show jp_visage1
play music "music/recuperationvisage.ogg"
"Heureuse coïncidence, à peine ces mots prononcés, l'atmosphère de la piece changea."
"Brusquement, des ombres se mirent à partir du visage de Jean Plank, emportant peu à peu avec elles la magie qui mortifiait notre bon capitaine depuis maintenant si longtemps."
"Une horrible grimace apparut sur le faciès de Jean Plank déformant encore plus son visage déjà difforme."
"Pour les matheux : son visage était donc deux fois plus déformé."

show jp_visage2
"Ecœuré, Lucien vomit par terre."
"Jean hurla de plaisir sentant le visage de Saint Gède qui le quittait enfin."
"Soudain, à la manière d'un élastique de soutien-gorge que l'on relâcherait après l'avoir tiré en arrière au maximum..."

show jp_prison_lucien
play sound "sound/low2.ogg"
"Le visage de Jean Plank repris sa forme habituelle."
"Il se dirigea alors vers la flaque qui traînait dans le fond de la cellule et admira son reflet."
"Un sourire victorieux se dessina sur son visage."

$renpy.sound.set_volume(0.00, delay=0, channel='music')
play alder "music/crayon.ogg"

#voice "doublages_jp2/scene8/scene8_jp4.ogg"
jp "Lucien ! Du coup, si je résume bien toute notre aventure, et plus particulièrement toi, n'avez servi à rien ?"

#voice "doublages_jp2/scene8/scene8_lucien6.ogg"
lucien "Tu fais le malin, mais un jour le karma va te rattraper !"

$renpy.sound.set_volume(1.00, delay=0, channel='music')

"Apparut alors une geôliere plantureuse aux hanches larges faites pour enfanter." 

#voice "doublages_jp2/scene8/scene8_karma1.ogg"
karma "Jean Plank ?! Encore toi ?"

"Lucien était bouche bée, jamais une créature ne lui était apparue aussi magnifique."
"Il le savait, c'était l'amour de sa vie."

#voice "doublages_jp2/scene8/scene8_jp6.ogg"
jp "Haha, comme au bon vieux temps !"

#voice "doublages_jp2/scene8/scene8_karma2.ogg"
karma "Comment ça le bon vieux temps ? Il ne s'est même pas écoulé 3 semaines depuis que tu es sorti !"

#voice "doublages_jp2/scene8/scene8_jp7.ogg"
jp "Mais regarde, j'ai eu le temps de trouver un acolyte !"

"Lucien ne disait rien, il réfléchissait à la façon dont il allait faire sa demande en mariage."

#voice "doublages_jp2/scene8/scene8_karma3.ogg"
karma "J'aimerais que tu arrêtes d'entraîner du monde dans tes bêtises Jean Plank !"

"Jean Plank se tourna vers Karma."

#voice "doublages_jp2/scene8/scene8_jp8.ogg"
jp "Allez assez discuté, fais nous sortir d'ici !"

#voice "doublages_jp2/scene8/scene8_karma4.ogg"
karma "Pourquoi ça ?"

#voice "doublages_jp2/scene8/scene8_jp9.ogg"
jp "Ce serait trop long à expliquer."

#voice "doublages_jp2/scene8/scene8_karma5.ogg"
karma "Mais Jean Plank, je n'ai même pas les clefs."

#voice "doublages_jp2/scene8/scene8_jp10.ogg"
jp "Quoi ?!"

#voice "doublages_jp2/scene8/scene8_karma6.ogg"
karma "J'ai dit que je n'avais pas les clefs."

"N'écoutant que son coeur, Jean Plank passa son bras à travers les barreaux afin mettre un magistral direct du droit à Karma."

#voice "doublages_jp2/scene8/scene8_jp11.ogg"
jp "Inutile de te répéter, j'avais bien compris la première fois !"

"C'est alors que Lucien comprit quelque chose."
"Quelque chose qu'il n'avait jamais soupçonné mais qui, une fois mis en lumière, expliquait beaucoup d'autres choses."
"Jean Plank n'était en fait pas quelqu'un de bien."

"Il sentit alors une rage soudaine monter en lui."
"L'amour de sa vie depuis venait de se faire frapper par Jean Plank."
"Il se devait de défendre l'honneur de Karma !"
"Si lui ne le faisait pas, qui le ferait ?"
"Il tenta alors de gifler Jean Plank."
"Ce dernier l'avait néanmoins vu venir parce que Lucien, faisant de son mieux pour rendre la scène tragique, était en train de donner sa baffe au ralenti."
"Prenant la droite du véritable capitaine, il s'écroula au sol."

"Lucien était maintenant habité d'une colère froide."
"Son regard avait changé : pour la première fois il goûtait au fléau qui habitait Jean Plank depuis maintenant si longtemps."
"Tout son être criait vengeance."
"Ce sentiment lui donnait aussi un regard nouveau vis-à-vis de la devise de Jean Plank."
"Il se releva, toujours au ralenti."
"Jean Plank voulut demander pourquoi Lucien ne bougeait pas un peu plus vite mais il s'abstint, assistant patiemment au spectacle."
"Lucien fixa son regard noir dans celui de Jean Plank, qui frissonna."
"Jean Plank fit alors un discret pas chassé sur la droite pour ne pas rester dans le courant d'air."
"C'est alors que d'une voix cinglante et brutale, Lucien lâcha l'ultime punchline."

#voice "doublages_jp2/scene8/scene8_lucien7.ogg"
lucien "Jean Plank ! Ta mère le dalmatien !"

#voice "doublages_jp2/scene8/scene8_lucien8.ogg"
lucien "Tout le monde doit payer !"

"Un champ d'énergie recouvrit alors instantanément Lucien."
show explosion_prison
play sound "sound/explosion_prison.ogg"
"S'ensuivit alors une immense explosion."
show ecran_noir
"Son souffle fit immédiatement perdre connaissance à Jean Plank malgré le fait que ce dernier n'avait jamais eu quelque connaissance que ce soit."

#############################################################################################################################
#                                                                                                                           #
#                                                        SCENE 8                                                            #
#                                                                                                                           #
#############################################################################################################################

scene jplibre
play music "music/jp_epilogue.ogg"

"Quand Jean Plank reprit connaissance, quelques heures s'étaient écoulées"
"L'absence de toutes figures basanées laissait sous-entendre que Lucien s'en était allé, emportant Karma avec lui."
"L'explosion avait été si puissante que les lourds blocs de pierre qui composaient les murs de la prison avaient fondu. Il ne restait plus rien de la cellule."
"Jean Plank se demanda d'ailleurs comment il pouvait être encore en vie."
"Mais bon, il venait dejà de perdre son meilleur Lucien, si en plus il était mort, il se serait probablement foutu en l'air."
"Notre héroïque capitaine prenait tout de même les choses du bon coté."
"Il était désormais libre !"
"Libre et seul, il n'avait plus rien pour le freiner désormais."
"Lucien était parti, tant pis pour lui !"
"Il avait une vengeance à accomplir."
"Quelqu'un à faire payer."
"En pleine forme et satisfait, Jean Plank était enfin prêt !"
"Prêt à se venger !"

#############################################################################################################################
#                                                                                                                           #
#                                                        CREDITS                                                            #
#                                                                                                                           #
#############################################################################################################################


scene jplibrecredi


"Scénariste : Shiroi Maô\nConseiller scénaristique : Styrale"
"Réalisation : Monsieur Shiroi Maô\nCo-réalisateur : Monsieur Styrale\n"
"Montage : L'astucieux Monsieur Styrale\nL'autre partie du montage : Le Sublime Shiroi Maô\n"
"Directeur de recherche : Le très estimé Lucas HAMMERER\nAssistant chercheur : Thomas DOHERTY"
"Directeur artistique : Séphultura \nSous directeur artistique : LucianAteMyKFC"
"Digital Painteur presque de qualité : NO NEED\nDirecteurs Audio : Jean-Eudes PATRÉCHER et Gontran PEUCOUTEUX\n"
"Responsable photo : Personne"
"C'est pour ça qu'on a pas de photo."
"Digital Painteur presque de qualité (édité): Shaco le fou"
"Doublage :"
"MissFourtout : La très généreuse génitrice de Monsieur Styrale (Faute d'être présente dans cet arc, elle l'est dans nos coeurs !)"
"JeanPlank, Lucien le magichien : ShiroiMaô qui en reste sans voix"
"Leeeeee, Saint Gède, Titto : Monsieur Styrale qui a maintenant bien plus qu'une simple expérience professionelle dans le doublage."
"Tristana : La soeur de Thomas (la sympa pas l'autre)\nKarma, Poppy : Hildi la Best Girl"
"Rise : Le cancéreux nominé au Oscars, Sachatte Longe."
"Grands remerciements à Fré Derrick pour les locaux."
"Remerciements à Marie pour avoir fait preuve de beaucoup de..."
"pour avoir fait preuve."
"Remerciements à Monsieur Simon comme catalyseur de haine et surtout pour NE PAS AVOIR ÉTÉ LÀ !"
"A peut-être bientôt pour enfin la fin de l'aventure !"


jump end


label game_over:
show ecrant_game_over
window hide
pause
stop music
hide ecrant_game_over
stop sound
play music "music/fightsinged.ogg"
jump debut_combat

label end:
return

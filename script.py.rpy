

play music "jp_theme.ogg"

#scenes

##########################Scene1########################################
image intro = "intro.png"
image jp_porte = "jp_kick_singed_door.jpg"
image entrepot = "entrepot.png"
image fight = "fight.jpg"
image entrepot_mort = "entrepot_mort.png"
image crucifix = "crucifix.jpg"
image bucher = "bucher.png"
image zhonya = "zhonya.jpg"
image lucien = "lucien.jpg"
image exterieur_entrepot = "exterieur_entrepot.png"
image bataille_entrepot = "entrepot2.png"
image entrepot2_secret = "entrepot2_sg.png"
image bateau = "bateau.jpg"
image jpsinged_crayon = "jpsinged_crayon.jpg"
image plage = "plage.png"
image poulet = "jpsinged_poulet.png"
image nez = "lucien_nez.jpg"
image cabane = "cabane.jpg"
image interieur = "interieur.jpg"
image village = "village.jpg"
image bureau = "maison.jpg"
#image teemo_mort = Movie(play="teemo_mort.mpg")
image poppy = "poppy.png"
image village2 = "village2.jpg"
image jp_tireSurBriggle = "jpsinged_tire.png"
image bureau2 = "bureau2.png"
image zoomedBureau2 = "bureau2_zoom.png"
image prison = "prison.png"
image prisonporte = "prisonporte.jpg"
image karma = "karma.jpg"
image jplibre = "jp_libre.png"
image ecrannoir = "ecran_noir.png"
image police = "tribunal.jpg"

########################Scene2##########################################

########################Scene3#########################################
#sprites


#declaration perso####################################################

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
define karma = Character('Karma : Guardienne de prison et Blague prévisible', color="#c8ffc8")

######################################################################
label start:

label scene1:##############################################################################################################################Scene1

scene intro
play music "intro.ogg"

"Notre bien aimé Jean Plank venait de se prendre un gigantesque météore dans la gueule."
"Météore qui, au passage, avait réduit à néant sa demeure, sa femme, et tous ses biens."
"Il allait falloir se venger pour tout ça !"
"Mais Jean Plank devait avant ça s'occuper d'un problème beaucoup plus urgent :"
jp "Lucien !"
"Sortant de sa stase Lucien, malgré sa grande vivacité d'esprit ne put s'empêcher un léger rictus de dégoût en voyant l'hideux visage de Jean Plank."
lucien "Oh mes aïeux mais qu'est-ce que t'es moche !"
jp "J'ai vu, j'ai bien vu oui !"
lucien "Attends ne bouge pas je vais essayer de trouver un morceau de toile ou quelque chose pour arranger ça."
"Toile ?"
lucien "Oh c'est pas mal ça."
"Toile..."
lucien "Ouais c'est pas vraiment ta taille."
"Potion..."
lucien "Ah mais c'est la mienne."
"SAINT GEDE !"
"En une astucieuse pirouette le cerveau de Jean Plank venait de faire le lien !"
jp "Lucien! On va chez Saint Gède !"

"Quelques instants plus tard, nos deux compères, l'un en colère l'autre en burqa, arrivèrent devant la porte du précité."
scene jp_porte

#################################################################################
play sound "violent_open_door.ogg"
voice "scene1_jp1.ogg"
jp "Saint Gède ! Rends moi mon visage !"

scene entrepot

play music "religieux_shop.ogg"
show singed
voice "scene1_sj (1).ogg"
sj "Jean Plank ?! Oh mon Dieu mais qu'est-ce que tu es moche !"

jp "Je sais ! Et c'est ta faute roulure !" 

voice "scene1_jp6.ogg"
jp "Tu ne nous a jamais parlé d'effets secondaires !"

voice "scene1_sj6.ogg"
sj "Tu aurais pu t'en douter ! Tu crois vraiment que je garde cette tête par plaisir ?!"

"Jean Plank se rendi alors compte qu'en effet, il aurait pu s'en douter."
"Mais hors de question de perdre la face face à Saint Gède !"
"Ivre de colère, il balança sa meilleure punchline à l'hideux visage de son detracteur."
jp "Filou !"

sj "Le seul problème Jean Plank, c'est que tu es un attardé !"

"Jean Plank ne comprenait pas le mot attardé."
"Cependant il comprenait que Saint  Gède était en train de l'envoyer dans les roses."
"Et les roses, ça pique !"
"N'écoutant plus sa faible raison et cédant à la rage de l'ivrogne qui étaot en lui, Jean Plank s'élança sur Saint Gède."
#########################################################################################################################

#######################################################################################################################
#COMBAT SAINT GEDE
######################################################################################################################

menu:
    "Courir sur Saint Gède avec rage":
        "Jean Plank courut sur Saint Gède avec rage"
        "Il tenta de lui asséner un coup la tête, mais le pretre esquiva."
        "Pris dans son élan, il perdit l'équilibre."
        "Saint Gède, en tant que Moine Guerrier Humaniste Savant Progressiste, en profita pour lui mettre un violent uppercut qui souleva son adversaire, lequel retomba quelques mètres plus loin dans le stock de potions de Saint Gède."
        label fight_sj_jp_est_a_terre
        menu:
            "Se relever":    
                "Jean Plank tenta de se relever. "
                "Malheureusement Saint Gède était rapide et avant même que Jean n'ait pu se relever, il lui asséna un coup sur la tête qui fit retourner au sol le capitaine."
                menu:
                    "Lancer du sable dans les yeux de Saint Gède":
                        label lancer_sable:
                            "Pas de chance, Saint Gède venait de faire le ménage, il n'y a donc pas de sable sur le sol."
                            "Jean Plank leva les yeux au ciel."
                            scene crucifix
                            play music "mort.ogg"
                            play sound "crane_enfonce.ogg"
                            "L'énorme crucifix taille XL en fer chromé à moins 50 \% sur www.MaBonneSecte.com de Saint Gède fut la dernière chose que Jean Plank vit avant de rejoindre le Valhalla."
                            jump game_over

                    "Appeler aled":
                        jump aled

            "Lancer les bouts de verre brisé à Saint Gède":
                "Jean Plank observa autour de lui. De nombreux morceaux de verre brisé jonchaient le sol."
                "C'est alors que notre bon capitaine prit l'initiative de les ramasser pour les lancer sur Saint Gède."
                "Malheureusement pour lui, une potion d'anti-invulnérabilité s'était brisée lorsqu'il avait atterri."
                "En conséquence, quand Jean Plank prit les bouts de verre, il se coupa juste misérablement."
                "Saint Gède ayant compris les intentions du capitaine, réalisa que ses actions étaient celles d'un hérétique. Il installa donc Jean Plank sur un bûcher."
                "Il avait toujours un bûcher de prêt dans un coin de son église, au cas où."
                scene bucher
                play sound "cri_bucher.ogg"
                play music "mort.ogg"
                "C'est ainsi que Jean Plank partit, purifié par le feu."
                jump game_over

    "Courir sur saint Gède avec encore plus de rage":
        "Ignorant ses limite Jean Plank courrut sur saint Gède avec bien plus de rage qu'il n'aurait du le faire."
        "Ces yeux étaitent si injecté de sang qu'il ne voyait plut rien !"
        "Sait Gède n'eu aucun mal à l'evité."
        "Jean Plank continuant sa charge fini par ce cogner dans un meuble"
        "Il roula sur le sol en jurant sous le regard médusé de saint Gède."
        jp "Je vois que tu es devenu plus fort !"
        sj "Nan pas tant que ça non."
        menu:
            "Frapper Saint Gède":
                jump fight_sj_jp_est_a_terre
            "Laisser Saint Gède me frapper, de toute façon je suis invincible grâce à la potion.":
                label jp_head_explode:
                "Jean Plank regarda le poing de Saint Gède se diriger vers son visage pensant pouvoir l'encaisser sans même froncer un sourcil."
                "Cependant ce qu'il ne savait pas c'est que l'invincibilité s'annulait entre deux buveurs de potion."
                "Ce qu'il ne savait pas non plus, c'est que Saint Gède avait l'habitude de consommer une potion d'extrême force."
                "Le poing de Saint Gède arriva sur le visage de Jean Plank,"
                "Déforma le visage de Jean Plank."
                "Puis traversa le visage de Jean Plank."
                scene entrepot_mort
                play music "mort.ogg"
                play sound "crane_enfonce.ogg"
                "Eclaboussant ainsi son entrepôt de la cervelle de notre bon capitaine."
                jump game_over


#Fin combat Lucien
label aled:
"Déjà deux fois qu'il était à terre, et Jean Plank sentait très bien qu'il n'était plus invincible. Saint Gède avait décidément une force écrasante."
"Jean Plank n'avait plus 36 solutions, il lui fallait prononcer la formule qui résolvait tous les maux."

voice "scene1_jp10.ogg"
jp "LUCIEN ! AU SECOURS !"
scene crucifix

voice "scene1_sj8.ogg"
sj "Plus de pitié pour toi hérétique !"
"Répondit Saint Gède en brandissant son crucifix de d'un mètre quatre-vingt quinze."

voice "scene1_lucien 1.ogg"
lucien "Par la puissance de Zhonya !"

scene lucien

"Cria la voix de Lucien qui venait de répondre à l'invocation déséspérée de Jean Plank."
"Saint Gède s'arrrêta net."
"La formule interdite avait été prononcée."
"Il venait de se changer en or."

play music "jp_theme.ogg"
show lucien_gauche
voice "scene1_lucien 2.ogg"
lucien "Le mensonge donne des fleurs mais pas de fruit !"
"Jean Plank regarda Lucien le magicien et, ému d'avoir été sauvé par son ancien esclave, il lui dit la voix pleine d'émotion :"

show jpsinged
voice "scene1_jp11.ogg"
jp "Bah c'est pas trop tôt !"

#voice "scene1_lucien .ogg"
lucien "Un simple merci aurait suffit !"

#voice "scene1_jp11.ogg"
jp "Merci ?! Et puis quoi encore ? Comment je fais pour récuperer mon visage maintenant ? Rends lui sa forme normale !"

voice "scene1_lucien 3.ogg"
lucien "Impossible, une fois le Zhonya activé on peut plus rien faire pendant 2,5 !"

voice "scene1_jp13.ogg"
jp "2,5 quoi ?"

voice "scene1_lucien 3_2.ogg"
lucien "Aucune idée, la description du sort est en polonais et cette langue n'est pas assez sombre pour que je la traduise."
"Dubitatif, Jean Plank regarda Lucien dans les yeux."
"Après l'avoir bien regardé, la conclusion paraissait évidente."

voice "scene1_jp14.ogg"
jp "Mmmh, il est quand même très noir."

lucien "Et toi tu es quand même très moche !"

"Malgré le fait que Jean Plank n'était pas très patient, il voulut quand même essayer d'attendre."
"Cependant il échoua rapidement."
"C'était sûr en fait"

#crayon :
jp "Lucien !" 
jp "Trouve une solution, après tout c'est ta faute."

#fin crayon
"C'est vrai, c'était sa faute."
"Lucien se mit à réflechir."


lucien "Je connais peut-être un magicien qui pourrait te rendre ton visage."

jp "Eh bien, en avant !"

"Jean Plank ne savait pas trop où il allait mais il aimait bien dire \"en avant\"."
"Après quelques explications de Lucien, nos deux compères embarquèrent vers le continent en direction du mage qui pourrait peut-être rendre son visage si rempli de piété et de sympathie à Jean Plank."




label scene2:###############################################################################################################################scene2

scene bateau
play music "bateau.ogg"

"Voilà maintenant quelques jours que Lucien et Jean Plank avaient pris la mer."
"Les occupations venaient à manquer, et l'équipage avait trop peu de QI pour tenir une conversation."
"Lucien trompait donc son ennui en tentant d'en apprendre plus sur la vie de notre bon Capitaine."
"Lui qui était d'un ordinaire peu loquace était étrangement bavard depuis quelques temps."
"Probablement l'air marin."
"Ou peut-être la quantité astronomique de rhum dans ses veines."

show jpsinged
voice "scene2_jp1.ogg"
jp "Mais bien sûr que sa mort m'attriste ! Tu ne m'as donc pas vu mes larmes viriles ?"

show lucien_gauche
voice "scene2_lucien1.ogg"
lucien "Tête de coco, j'ai tout vu et c'est pour ton visage que tu as pleuré, pas pour Miss Fourtout !"

voice "scene2_jp2.ogg"
jp "Peu importe. De toute façon ce n'était que le numéro après 49."

voice "scene2_lucien2.ogg"
lucien "Le numéro 50 ?"

voice "scene2_jp3.ogg"
jp "Bah oui, si c'est celui qui suit le 49."

voice "scene2_lucien3.ogg"
lucien "Mais attends là ! Tu ne sais pas compter ?"

voice "scene2_jp4.ogg"
jp "Et pas lire non plus !"

voice "scene2_lucien4.ogg"
lucien "Mais attends ce n'est pas possible, je suis sûr de t'avoir vu compter les pièces de ton trésor !"

play music "crayon.ogg"
voice "scene2_jp5.ogg"
scene jpsinged_crayon
jp "Lucien, l'humour est un refuge."

scene lucien_crayon
voice "scene2_lucien5.ogg"
lucien "..."

jp "De toute façon mon véritable amour c'est l'océan." 

lucien "La grosse flaque salée là."

jp "Ce n'est pas une simple flaque Lucien ! Dans ces eaux se cache une déesse à laquelle je suis d'ailleurs lié."

lucien "Lié ? C'est a dire ?"

jp "Nous avons été amants pendant des années !"

lucien "Ton histoire est un peu étrange."

jp "Tu sais ce qu'on dit : c'est pas l'homme qui prend la mer, c'est la mer qui prend l'homme."

lucien "Et pourquoi ça c'est terminé ?"

jp "Et bien, je navige régulièrmeent en eaux douces, si tu vois ce que je veux dire."
"Non lucien ne voyait pas."
"Mais il savait au plus profond de son coeur qu'il ne voulait pas plus de détail."

lucien "Mais du coup elle t'a pardonné ?"

jp "Bah non pourquoi ?"

play music "finduvoyage.ogg"
show naufrage

voice "scene2_naufrage.ogg"
"   "


label scene3:###############################################################################################################################scene3

scene plage

show jpsinged

#jp et lucien viennent d'arriver sur la plage apres la destruction de leur navire
play music "plage.ogg"
voice "scene3_jp1.ogg"
jp "Alors, tu vois Lucien, aucun problème !"

show lucien_gauche

voice "scene3_lucien1.ogg"
lucien "Je ne dirais pas ça."

voice "scene3_jp2.ogg"
jp "Gibier de potence ! On est arrivés à bon port."

voice "scene3_lucien2.ogg"
lucien "Déjà ce n'est pas un port mais juste la plage, et je tiens a signaler qu'on a perdu le navire."

voice "scene3_jp3.ogg"
jp "Il n'y avait rien d'important dedans de toute façon."

voice "scene3_lucien3.ogg"
lucien "Rien d'important ? Et les 9 membres d'équipage qui sont morts ?"

voice "scene3_jp4.ogg"
jp "Eh bien ils ne sont pas morts dans le bateau !"

voice "scene3_lucien4.ogg"
lucien "Tu les as tous tué et attaché pour t'en faire un radeau."

voice "scene3_jp5.ogg"
jp "Tout le monde doit payer ! Et puis tu l'as aussi utilisé ce radeau."

voice "scene3_lucien5.ogg"
lucien "Mais moi c'était pour marabouter leur esprit, pour que leur âme aille vers un monde meilleur."

voice "scene3_jp6.ogg"
jp "Bon il est ou ton magicien ?"

voice "scene3_lucien6.ogg"
lucien "Alors, ça je ne sais pas. Normalement on devait arriver proche du port du village mais à cause de ta miss tentacule je sais plus du tout où on est !"

voice "scene3_jp7.ogg"
jp "Lucien ne t'inquiète pas."

voice "scene3_lucien7.ogg"
lucien "Pourquoi ?"

voice "scene3_jp8.ogg"
jp "Il est vrai que j'aurais dû t'en parler depuis longtemps mais les choses sont allées si vite. Il faut maintenant que je te révèle mon principal atout."
voice "scene3_jp9.ogg"
jp "En fait je suis gaucher."

"Lucien regarda attentivement Jean Plank."
"Aucun doute il disait vrai."
"Mais cela ne les avançait pas beaucoup."
"C'est alors qu'apparut au yeux de notre bon capitaine un détail sur le visage de Lucien qui allait les sortir de là."

voice "scene3_jp10.ogg"
jp "Lucien !"

voice "scene3_lucien8.ogg"
lucien "Qu'est ce qu'il y a ?"

voice "scene3_jp11.ogg"
jp "Ton nez Lucien, il est énorme."

voice "scene3_lucien9.ogg"
lucien "Ecoute moi bien gros patapouf je ne vois pas bien ou tu veux en venir mais... "

scene jpsinged_crayon
play music "crayon.ogg"
voice "scene3_jp12.ogg"
jp "Lucien nous n'avons pas 36 solutions. "

scene lucien_crayon
voice "scene3_lucien10.ogg"
lucien "Ohlàlà t'es très mal parti toi."

scene jpsinged_crayon
voice "scene3_jp13.ogg"
jp "Mais Lucien, c'est un don du ciel. "

scene lucien_crayon
voice "scene3_lucien11.ogg"
lucien "Je vois très bien où tu veux en venir et je t'assure que je vais te casser la gueule."

scene jpsinged_crayon
voice "scene3_jp14.ogg"
jp "Mais Lucien..."

scene lucien_crayon
voice "scene3_lucien12.ogg"
lucien "Oh putain ça part !"

scene poulet

play music "jp_theme.ogg"

"Ne voulant pas se battre avec son magicien, Jean Plank, passé maître dans l'art de la corruption, sortit de sa poche un morceau de poulet."
"A la vue de la viande blanche dans la main du capitaine, les instincts de Lucien réapparurent, et ce dernier se jeta aux pieds du capitaine en faisant le beau."

scene nez

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

scene cabane

play music "leesin.ogg"

"L'odeur les mena jusqu'à un petit cabanon. A l'entrée, on trouvait deux statues d'homme gros et gras à l'air niais, assises en position du lotus."
"Jean Plank reconnut immédiatement la sublime teinte du jade rouge dans lequel elles étaient taillées et entreprit donc d'arracher un bras à l'une des statues, histoire de se reconstruire un trésor."

voice "leesin1.ogg"
"Jean Plank !"
"Fit alors une voix provenant de l'intérieur du cabanon."
"Jean Plank entra, suivi par Lucien."

scene interieur

"Ils se retrouvèrent alors nez à nez avec leur interlocuteur, un moine ayant pour seuls vêtements des habits et un bandeau sur les yeux."

show jpsinged

lee "Je t'attendais, Jean Plank."

voice "scene3_jp15.ogg"
jp "Comment connais-tu mon nom ?"

show leesin

voice "leesin2.ogg"
lee "Je vois tout !"

"Si l'explication convaincut Jean Plank, elle laissa Lucien un peu dibitatif :"

hide jpsinged
show lucien_droite

voice "scene3_lucien13.ogg"
lucien "Bah non, toi tu ne vois rien !"

voice "leesin3.ogg"
lee "Mais si, je suis voyant."

voice "scene3_lucien14.ogg"
lucien "N'importe quoi ! Je vois très bien que tu as un bandeau sur les oeils !"

voice "leesin4.ogg"
lee "Oui car je suis aveugle."

voice "scene3_lucien15.ogg"
lucien "Eh bah voilà, tu vois bien que tu vois pas !"

hide leesin
hide lucien_droite

"Lee qui voyait très bien, que Lucien allait LUI CASSER LES COUILLES, lui mit un kick qui le transporta hors de sa vue."
"Enfin non, hors de sa demeure."
"Vous aviez compris que Lee était aveugle ?"

show leesin
show jpsinged

voice "leesin5.ogg"
lee "Je disais donc que ce qui t'amène... Sois gentil, repose ce vase petit scarabée."

"Jean Plank reposa le vase."

voice "leesin6.ogg"
lee "Tu veux détruire celui, qui t'a déshonoré !"

voice "scene3_jp16.ogg"
jp "Oui !"

voice "leesin7.ogg"
lee "Tu veux lui casser sa gueule, à cette raclure ! "

voice "scene3_jp17.ogg"
jp "Oui !"

voice "leesin8.ogg"
lee "Lui péter les genoux ! "

voice "scene3_jp18.ogg"
jp "Oui !"

voice "leesin10.ogg"
lee "Lui arracher les couilles avec les dents et en faire un pendentif !"

voice "scene3_jp20.ogg"
jp "OUI !"

voice "leesin11.ogg"
lee "Eh bah tu seras gentil, tu feras pas ça parce que c'est dégueulasse."

voice "scene3_jp25.ogg"
jp "Et comment je fais ça ?"

voice "leesin16.ogg"
lee "Pour cela tu devras trouver certains artefacts sacrés !"

voice "scene3_jp21.ogg"
jp "Et je les trouve où les artefacts ?"

voice "leesin12.ogg"
lee "Dans ton cul ! Nan je rigole mais par contre repose ce verre en cristal ou je te défonce ta face de rat."

"Jean Plank reposa le verre en cristal."

#choix d'un arc lux ou jp va violer lux et finir en taule
# legende de garen et l'ignite, bro complex
voice "leesin13.ogg"
lee "Sachant que ton ennemi est devenu les ténèbres, ce qu'il te faut c'est devenir la lumière, mais comme on approche du solstice l'éclairage diminue, donc si je multiplie par pi et que j'enlève trois fois la rotation de la Terre par Newton, ça nous donne \"Prends la prochaine à droite, gros con !\"."
"Jean Plank n'avait pas vraiment compris qui était son ennemi."
"Aussi posa t'il la seule question qui importait vraiment /"

voice "scene3_jp22.ogg"
jp "La prochaine à droite c'est par où ?"

voice "leesin14.ogg"
lee "C'est à droite ! Maintenant si tu pouvais te casser parce que j'ai un autre rendez-vous pour l'extension de ma startup voyance. Donc je n'ai pas le temps !"

voice "scene3_jp23.ogg"
jp "D'accord mais..."

voice "leesin15.ogg"
lee "Je n'ai pas le temps je te dis  ! Tu demanderas ton chemin ! Casse toi maintenant !"

"VOYANT que Jean Plank ne partait toujours pas, Lee se mit à lui lancer du riz en hurlant."
lee "Allez zou pch pchh !!"

scene cabane

"Jean avait maintenant rejoin Lucien à l'exterieur."
"Il n'avait malheureusement pas pu se saisir de la  moindre pièce du trésors qui dormaient dans l'antre de Lee."
"Bien résolu à en prendre les plus belles pièces, il dessina une croix sur le sol pour se souvenir de son emplacement."

voice "scene3_jp24.ogg"
jp "C'est bon, on peut y aller !"
"Lacha t'il en se dirigeant vers la première à droite comme Lee le leur avait indiqué."

label scene4:###############################################################################################################################scene4

scene village

play music "village.ogg"

"Nos deux protagonistes arrivèrent devant le village indiqué par Lucien."
"Une espèce de petit écureuil miteux vint les acceuillir."

show teemo

voice "scene4_titto.ogg"
titto "Salut ! Vous venez voir Rize ?"
"Voyant ce petit être ignoble, Lucien fut pris d'une rage que Jean Plank n'aurait jamais pu soupçonner venant de son ami."

#voice "souffrance.ogg"
#$ renpy.movie_cutscene("teemo_mort.m2v")
"Il sortit sa baguette trop grosse et mit un magistral coup de pied à Titto qui partit s'écraser sur un rocher quelques mètres plus loin."

hide teemo
play sound "teemo_punch.ogg"
$ renpy.movie_cutscene("teemo_mort.mpg")

"Il rangea alors sa baguette trop grosse avec difficulté, parce qu'elle était trop grosse."

show jpsinged
voice "scene4_jp1.ogg"
jp "Lucien, qu'est ce qui te prend ?"

show lucien_gauche

voice "scene4_lucien1.ogg"
lucien "Je ne sais pas j'ai juste un problème avec ce genre de bestiole."

voice "scene4_jp2.ogg"
jp "Mais Lucien, il venait sans doute nous acceuillir !"

voice "scene4_lucien2.ogg"
lucien "Ce genre de bestiole véhicule plein de maladies, moi je te le dis. En plus ça se multiplie comme des champignons maléfiques."

voice "scene4_jp3.ogg"
jp "Mais Lucien, je crois que c'était un membre du village."

voice "scene4_lucien3.ogg"
lucien "Rhoo ça va tu passes ton temps à faire des conneries toi là. Je t'en pose moi des questions ? En plus ne t'inquiète pas, j'ai la solution : je vais en faire un tapis."

voice "scene4_jp4.ogg"
jp "Lucien ?"

voice "scene4_lucien4.ogg"
lucien "Ehhh comme ça ils auront un souvenir de l'animal, un peu comme moi j'ai gardé un souvenir de Maman à ma ceinture."

voice "scene4_jp5.ogg"
jp "Lucien ?"

show lucien_tete_reduite
voice "scene4_lucien5.ogg"
lucien "Eh regarde comme elle est belle là, en plus tu trouves pas que j'ai son sourire là ?"
hide lucien_tete_reduite
voice "scene4_jp6.ogg"
jp "Heu... Tout le monde doit payer ?"

hide jpsinged
hide lucien_gauche

"Ainsi Lucien récupéra rapidement l'animal."
"Il le dépeça tel un taxidermiste professionnel et hop, quelques secondes et une incantation vaudoo bénéfique plus tard, il avait transformé ce putain d'écureuil en un magnifique paillasson."
"Il courut ensuite à la maisonnette la plus proche, et déposa son oeuvre davant la porte d'entrée."
play music "lucienencage.ogg"
scene cage
"Il retourna alors vers Jean en courant, mais fut arrêté dans sa course."
"Il était emprisonné dans une cage bleutée à l'aura étrange et ornée de symboles runiques."

voice "lucien_manquant.ogg"
"\"Oh non, ça recommence \" pensa-t-il en se remémorant sa capture par Jean Plank."
"Il se retourna."
"Un personnage à la peau bleue, tout vetu de... bah de bleu, et à l'air mécontent et menaçant était en train de courir vers Jean Plank."

show ryze_zoom

voice "scene4_rize1.ogg"
inconnu "Rhaaaaaaaaaa vagabonds, voleurs, sortez de MON village !"

"Lucien le reconnut immédiatement."
"Jean Plank lui ne le reconnut pas immédiatement."
"En même temps c'était normal, vu qu'il ne le connaîssait pas"

voice "scene4_lucien6.ogg"
lucien "Rize !"

"Le personnage bleuté tourna la tête."

voice "scene4_rize2.ogg"
ryze "Il n'y a qu'un seul chien au monde possèdant une voix aussi mélodieuse !"

"A ces mots, Lucien fut libéré de son étroite entrave."

scene village2
play music "village2.ogg"

show ryze
show lucien_droite

voice "scene4_rize3.ogg"
ryze "Luchieng, au pied mon tout beau !"

voice "scene4_lucien7.ogg"
lucien "Hé mais attends là mon coco, j'ai évolué depuis ce temps là, je suis maintenant moi aussi devenu un magicien !"

voice "scene4_rize4.ogg"
ryze "Ouais tu m'en diras tant."

voice "scene4_lucien8.ogg"
lucien "Nan mais regarde, je pratique la magie !"

voice "scene4_rize5.ogg"
ryze "Ouais c'est ça ouais !"

"Alors Lucien sortit un jeu de cartes, et devina quelle carte Rize avait choisi."

voice "scene4_rize6.ogg"
ryze "Et bah mon salaud !"

voice "explosion_poudre.ogg"
"Jean Plank qui avait été oublié jusque ici, sortit un de ses fameux tonneaux et le fit exploser (oui, Jean Plank transportait toujours quelques tonneaux de poudre noire de très bonne qualité)."

"Rize fut surpris mais pas étonné."
voice "scene4_rize7.ogg"
ryze "Luchieng, qui est ton compagnon ?"

hide lucien_droite
show jpsinged

voice "scene4_jp7.ogg"
jp "Haha, inutile de me présenter !"

voice "scene4_rize8.ogg"
ryze "Oh mon Dieu, qu'est ce qu'il est moche !"


hide jpsinged
show lucien_droite

voice "scene4_lucien9.ogg"
lucien "C'est la magie vaudoo maléfique qui lui a transfomé son visage. Nous sommes justement venus te demander ton aide pour lui rendre son faciès habituel."

voice "scene4_rize9.ogg"
ryze "Rien de plus facile, suivez moi."

"Ils suivirent alors Rize jusqu'à sa hutte de chef, au milieu du village."

scene bureau
play music "bureau.ogg"

"Ils entrèrent dans le bureau."

show ryze

voice "scene4_rize10.ogg"
ryze "Attendez ici et ne touchez à rien !"

"Dit-il en se dirigeant vers son immense bibliothèque."
"Lucien, de sa vue perçante de chasseur congolais confirmé, s'interessait aux étiquettes des potions présentes sur les étagères."
"S'il comprit rapidement à quoi pouvait servir une potion de vitesse, il aurait bien eu besoin de quelques explications quand à l'utilité d'une potion de matérialisation d'imperméable."
"Mais Rize étant concentré, Lucien garda le silence pour ne pas paraître impoli."
"Après quelques minutes à chercher, Rize revint avec un énorme ouvrage à la couverture sombre sur lequel on pouvait lire, \"Vaudoo maléfique et piraterie volume 12\"."

voice "scene4_rize11.ogg"
ryze "Et voilà, le livre d'Emmanuel Visage : \"Trucs et astuces pour rendre son visage à un pirate qui s'est fait voler son visage à cause du vaudoo maléfique\" !"
show lucien_droite

"Il ouvrit le livre, parcourut l'index puis tourna les pages jusqu'à la formule qui l'intéressait."
"Il s'exclama"
voice "scene4_rize12.ogg"
ryze "Parfait, j'ai tout ce qu'il me faut."

"Il se dirigea vers son placard à flacons et en ramena trois."
"Il prit un de ses merveilleux Erlenmeyers en cristal."
"Oui \"merveilleux\", le truc est enchanté car Rize est un sorcier, suivez un peu !"
"Il y versa le contenu des deux premières fioles."
"Il fut très satisfait à la vue de la petite explosion et du nuage rosâtre qui s'en échappa."
"Il voulut alors verser le contenu de la troisième fiole mais se rendit compte qu'elle était vide."

#Zoom sur la gueule de ryse qui est triggered
voice "scene4_rize13.ogg"
ryze "Rhoo fait chier, j'en ai plus."

hide lucien_droite
show jpsinged

voice "scene4_jp8.ogg"
jp "Gi-Gi-Gibier de potence !"

voice "scene4_rize14.ogg"
ryze "Qu'est ce qu'il raconte encore l'autre débile là ?"

hide jpsinged
show lucien_droite

voice "scene4_lucien11.ogg"
lucien "Attention à ne pas être trop aggressif, ça attire les mauvais esprits ! Qu'est ce qu'il te faudrait, mon ami ?"

voice "scene4_rize15.ogg"
ryze "T'inquiètes c'est rien je gère. Il me faut juste des larmes de schtroumpf."

voice "scene4_lucien12.ogg"
lucien "Un schtroumpf, c'est quoi ce truc là encore ?"

voice "scene4_rize16.ogg"
"Rize haussa les épaules en laissant échapper un petit grognement."

voice "scene4_lucien13.ogg"
lucien "Alors comment tu vas faire ?"

voice "scene4_rize17.ogg" #bcp de parasites sur le doublage
ryze "Je vais utiliser un sortilège de changement de statut !"

voice "scene4_lucien14.ogg"
lucien "Un changement de statut ? C'est quoi encore ça comme magie ?"

voice "scene4_rize18.ogg"
ryze "C'est de la magie du 4ème mur, tu vas voir."
"Rize récita alors sa formule."

voice "scene4_rize19.ogg"
ryze "Kongo wa watashi GURAND SCHTRUMFU DESU ! EVAT FERF OU TREUGRI MAL KIN !"

hide ryze
show ryze_bonnet

voice "scene4_rize20.ogg"
ryzeS "Et voilà !"

voice "scene4_lucien15.ogg"
lucien "Ohhhh on dirait de la magie !"

voice "scene4_rize21.ogg"
ryzeS "C'est bien pour ça qu'on m'appele le magicien."

hide lucien_droite
show jpsinged

voice "scene4_jp9.ogg"
jp  "Et pour les larmes ?"

hide ryze_bonnet

"Rize se dirigea vers l'extérieur."
voice "scene4_rize22.ogg"
ryzeS "Hé Tristana, viens donc voir papa !"

"Quelques secondes plus tard, Rize revint dans la maisonnée suivi d'une fillette et d'un dragonnet."

show ryze_bonnet
show trist

voice "scene4_tristana1.ogg"
tristana "C'est qui eux ?"

voice "scene4_rize23.ogg"
ryzeS "Des visiteurs."

voice "scene4_jp10.ogg"
jp "Venus d'ailleurs !"

voice "scene4_tristana2.ogg"
tristana "Pourquoi ils sont ici ?"

hide jpsinged
show lucien_droite

voice "scene4_lucien16.ogg"
lucien "Eh bien, on aurait besoin d'aide pour soigner le visage de mon compagnon !"

voice "scene4_tristana3.ogg"
tristana "Tonton  Rize, pourquoi il est tout noir le monsieur ?"

voice "scene4_rize75.ogg"
ryzeS "Euhm ta gueule, ta gueule."

tristana "Et pourquoi celui là il est moche ?"

ryzeS "Mais parce que c'est un connard ! T'arrête avec tes questions ?! C'est chiant à la fin !" #Parce que c'est un connard en exaspéré

tristana "Mais, mais ?"

voice "scene4_lucien17.ogg"
lucien "Oh c'est malin !"

voice "scene4_jp12.ogg"
jp "Quoi donc ?"

voice "scene4_lucien18.ogg"
lucien "Lui crier dessus afin que les larmes gagnent ses yeux."

voice "scene4_jp13.ogg"
jp "Oui, plutôt malin en effet..."

"Jean plank savait qu'il pouvait faire mieux."
"Il était temps de rapeller au monde qui était le héro de cette histoire."
"Son regard croisa alors celui du dragonnet tout sourire dans les bras de tristana."
"Perdu dans ses yeux pétillant de joie, il songea à quel point il serait triste s'il perdait son animal de compagnie"
"L'idée du siècle venait de germer dans le cerveau de Jean Plank."
"Il regarda Brigels et lui fit un sourire malicieux."

stop music
scene jp_tireSurBriggle

voice "pan.ogg"
"Puis il sortit son pistolet, et lui tira une balle entre les deux yeux."

#play music "mortrigglestheme.ogg"
 
"Il prit alors une posture solennel et entama un discours :"
jp "Brigels, petit dragonnet parti trop tôt, tu laisses un vide immense derrière toi. Et c'est avec beaucoup de tristesse et de compassion que je présente nos plus sincères condoléances a ta..."
"Se faisant soudain empoigner par Ryse, il ne pu finir convenablement ses adieux."
voice "scene4_rize29.ogg"
ryzeS "Mais qu'est ce que tu fous bordel !"

"Visiblement cet idiot de Ryse n'avait pas compris l'astucieux stratagème de Jean Plank pour obtenir les larmes."

#scene zoomedBureau2
#show ryze_zoom_bonnet

play sound "tristanabruitfont.ogg"

#show jpsinged_degueu
voice "scene4_jp14.ogg"
jp "T'inquiètes frère, je vais le cautériser !"

#hide jpsinged_degueu

show jpsinged_zoom
voice "scene4_rize30.ogg"
ryzeS "Comment ça, le cautériser ? Mais il est mort, putain !"

voice "scene4_jp15.ogg"
#hide jpsinged_zoom
jp "Attends je vais chercher la poudre..."

#scene bureau
#show tristpleure

#play music "tristanaost.ogg"
#play sound "tristanaLarme.ogg"
"Réalisant peu à peu ce qu'il se passait, Tristana fondit en larmes."

#scene zoomedBureau2
#show ryze_zoom_bonnet
voice "scene4_rize31.ogg"
ryzeS "Mais bordel, mais il est totalement demeuré ton pote, Lucien ! Lucien ?"
"Lucien de son coté était en train de récolter les larmes sur les joues de Tristana."
#hide ryze_zoom_bonnet
#show lucien_droite_zoom
#show ryze_zoom_bonnet

#play music "mortrigglestheme.ogg"
voice "scene4_lucien19.ogg"
lucien "Bah quoi ? On a des larmes maintenant."

play sound "violent_open_door.ogg"
"Rize était sur le point de fracasser son énorme nez quand il fut interrompu par le bruit de sa porte s'ouvrant violemment."

scene poppy

voice "scene4_poppy1.ogg"
poppy "Rize ! Titto est mort !"

show ryze_zoom_bonnet_droit
voice "scene4_rize32.ogg"
ryzeS "Quoi ? Comment ça ?!"

voice "scene4_poppy2.ogg"
poppy "C'est atroce, quelqu'un l'a dépeçé et a lancé ses restes devant ma porte !"

voice "scene4_rize33.ogg"
ryzeS "QUOI ?"

voice "scene4_poppy3.ogg"
poppy "Nous devons absolument trouver ce psychopathe avant qu'il ne recommence !"

voice "scene4_rize34.ogg"
ryzeS "Qui a pu commettre une telle atrocité ?"


voice "scene4_lucien20.ogg"
lucien "Hé là mais il est très joli mon tapis !"

hide ryze_zoom_bonnet_droit
show ryze_bonnet
voice "scene4_rize35.ogg"
ryzeS "Quoi ?"

show lucien_droite
voice "scene4_lucien21.ogg"
lucien "En même temps, j'ai fait ce que j'ai pu, c'était pas vraiment du bon poil, on aurait dit qu'il avait la teigne votre truc là !"

voice "scene4_rize36.ogg"
ryzeS "Mais vous êtes complètement demeurés putain !"

show jpsinged_degueu
voice "scene4_jp16.ogg"
jp "Attention, ça va péter !"

voice "scene4_rize37.ogg"
ryzeS "Quoi ?!"

voice "explosion_poudre.ogg"
scene ecran_noir

"30 minutes plus tard, deux agents de police arrêtaient nos deux protagonistes et les conduisaient à Piltover pour y être jugés."

scene police
"Malgrès les protestations de Lucien, qui tentait désespérément de prouver qu'il s'agissait d'un malentendu culturel, ils furent jugés coupables."

scene prison

play music "prison.ogg"


show jpsinged_gauche
"Jean Plank était de mauvaise humeur."
"Il avait un visage à retrouver, une vengeance à accomplir mais surtout des trésors à piller et des femmes consententes à violer."
"Il détestait les prisons. Les murs étroits et humides lui rappelaient la malle dans laquelle son père l'enfermait quand il était enfant."
"En somme : pas vraiment de bons souvenirs."
"Il réflechissait donc à un moyen de sortir."

show lucien_droite
voice "scene5_lucien1.ogg"
lucien "Hé pourquoi tu fais ta tête de grognon là ?"

voice "scene5_jp1.ogg"
jp "Silence Lucien !"

"Notre capitaine avait beau réfléchir du mieux qu'il pouvait, il n'arrivait pas à trouver de solution pour sortir de ce cachot."
"Le taux d'humidité était malheureusement bien trop haut pour se concentrer."

voice "scene5_lucien3.ogg"
lucien "Cesse donc de te triturer les meninges. J'ai là quelques malices qui vont te plaire, mon ami !"

voice "scene5_jp2.ogg"
jp "Qu'est ce donc là que cette duperie encore ?"

voice "scene5_lucien4.ogg"
lucien "J'ai discretement lu la page du livre d'Emmanuel Visage : \"Trucs et astuces pour rendre son visage à un pirate qui s'est fait voler son visage à cause du vaudoo maléfique\"."

jp "Et alors !"

lucien "La potion que Rize voulait te préparer t'aurait rendu ton visage immédiatement, il est vrai."
lucien "Mais j'ai aussi appris que l'effet du mal qui t'affecte est temporaire !"
lucien "Tu devrais retrouver ton visage habituel, si rempli de piété et de sympathie, très bientot et ce même sans potion."

"Heureseuse coincidence, à peine ces mots prononcés, l'atmosphère de la piece changea brusquement."
"Des ombres se mirent alors à partir du visage de Jean Plank, emportant peu à peu avec elles la magie qui mortifiait notre bon capitaine depuis maintenant si longtemps."
"Un horrible grimace apparut sur le faciès de Jean Plank déformant alors son visage déjà déformé."
"Pour les matheux : son visage était donc deux fois plus déformé."
"Ecœuré, Lucien vomit par terre."
"Jean hurla de plaisir sentant le visage de Saint Gède qui le quittait enfin."
"Soudain, à la manière d'un élastique de soutien-gorge que l'on relâcherait après l'avoir tiré en arrière au maximum,"
play sound "low2.ogg"
"Le visage de Jean Plank repris sa forme habituelle."
"Il se dirigea alors vers la flaque qui traînait dans le fond de la cellule et admira son reflet."
"Un sourire victorieux se dessina sur son visage."

#Crayon
jp "Lucien"
jp "Du coup tu n'a servit à rien !"
Lucien "Tu fais le malin, mais un jour le karma va te rattraper !"

karma "Jean Plank ?! Encore toi ?"
"Lucien était bouche bée, jamais une créature ne lui était apparue aussi magnifique."
"Il le savait, c'était l'amour de sa vie."
jp "Ha ha, comme au bon vieux temps !"
karma "Comment ça le bon vieux temps ? ça ne fait même pas 3 semaines qut tu es sorti !"
jp "Mais regarde j'ai eu le temps de trouver un acolyte !"
"Lucien ne disais rien, il reflechissait à la façon dont il allait faire sa demande en mariage"
karma "J'aimerais que tu arrètes d'entrainer du monde dans tes bétises Jean Plank !"

"Jean Plank se tourna vers karma."
jp "Allez assez discuté, fais nous sortir d'ici !"

karma "Mais Jean Plank, je n'ai pas les clefs."

jp "Quoi ?!"

karma "J'ai dit que je n'avais pas les clefs."

"N'écoutant que son coeur, Jean Plank passa son bras à travers les barreaux afin mettre un magistrale direct du droit à Karma."
jp "Inutile de te repeter, j'avais bien compris la première fois !"

"C'est alors que Lucien comprit quelque chose."
"Quelque chose qu'il n'avait jamais soupçonné mais qui, une fois mis en lumière, expliquait beaucoup de choses."
"Jean Plank n'était en fait pas quelqu'un de bien."

"Il sentit alors une rage soudaine monter en lui."
"L'amour de sa vie depuis maintenant 2 minutes venait de se faire frapper par Jean Plank !"
"Il se devait de défendre l'honneur de Karma !"
"Si lui ne le faisait pas, qui le ferait ?"
"Il tenta alors de gifler Jean Plank !"
"Sauf que Jean Plank l'avait vu venir parce que Lucien, dans un souci de rendre la scène tragique, était en train de donner sa baffe au ralenti."
"Prenant la droite du véritable capitaine, il s'écroula au sol."

"Lucien, était maintenant habité d'une colère froide."
"Son regard avait changé : pour la première fois il goutait au fléau qui habitait Jean Plank depuis maintenant si longtemps."
"Tout son être criait vengeance !"
"Ce sentiment lui donnait aussi un regard nouveau vis-à-vis de la devise de Jean Plank."
"Il se releva"
"Jean Plank voulut demander pourquoi Lucien ne bougeait pas un peu plus vite mais il s'abstint, assistant patiemment au spectacle."
"Lucien fixa son regard noir dans celui de Jean Plank, qui frissonna."
"Jean Plank fit alors un discret pas chassé sur la droite pour ne pas rester dans le courant d'air."
"C'est alors que d'une voix cinglante et brutale, Lucien lâcha l'ultime punchline."
lucien "Jean Plank !"
voice "scene5_lucien18.ogg"
lucien "Tout le monde doit payer !"

"Un champ d'énergie recouvrit alors instantanément Lucien."
scene explosion_prison
play sound "explosion_prison.ogg"
"S'ensuivit alors une immense explosion."
"Son souffle fit immédiatement perdre connaissance à Jean Plank malgré le fait que ce dernier n'avais pas de connaissances quelles qu'elles soient."
scene ecran_noir
""

scene jplibre
play music "jp_epilogue.ogg"

"Quand Jean Plank reprit connaissance, quelques heures s'étaient écoulées"
"L'absence de toutes figures basanées laissait sous-entendre que Lucien s'en était allé, emportant Karma avec lui."
"L'explosion avait été si puissante que les lourds blocs de pierre qui composaient les murs de la prison avaient fondu. Il ne restait plus rien de la cellule."
"Jean Plank se demanda d'ailleurs comment il pouvait être encore en vie."
"Mais bon, il venait dejà de perdre son meilleur Luchien."
"Si en plus il était mort je pense qu'il se serait foutu en l'air."
"Notre héroique capitaine prenait tout de meme les choses du bon coté."
"Il était désormais libre !"
"Libre et seul, il n'avait plus rien pour le freiner désormais."
"Lucien était parti, tant pis pour lui !"
"Il avait une vengeance à accomplir."
"Quelqu'un à faire payer."
"En pleine forme et satisfait, Jean Plank était enfin prêt !"
"Prêt à se venger !"

scene jplibrecredi


"Scénariste : Shiroi Maô\n
Conseiller scénaristique : Styrale"

"Réalisation : Monsieur Shiroi Maô\n
Co-réalisateur : Monsieur Styrale\n"

"Montage : L'astucieux Monsieur Styrale\n
 L'autre partie du montage : Le Sublime Shiroi Maô\n"

"Directeur de recherche : Le très estimé Lucas HAMMERER\n
Assistant chercheur : Thomas DOHERTY"

"Directeur artistique : Séphultura \n
Sous directeur artistique : LucianAteMyKFC"

"Digital Painteur presque de qualité : NO NEED\n
Directeurs Audio : Jean-Eudes PATRÉCHER et Gontran PEUCOUTEUX\n"

"Responsable photo : Personne"
"C'est pour ça qu'on a pas de photo."

"Digital Painteur presque de qualité (édité): Shaco le fou"
"Doublage :"

"MissFourtout : La très généreuse génitrice de Monsieur Styrale (Faute d'être présente dans cet arc, elle l'est dans nos coeurs !)"
"JeanPlank, Lucien le magichien : ShiroiMaô qui en reste sans voix"
"Leeeeee, Saint Gède, Titto : Monsieur Styrale qui a maintenant bien plus qu'une simple expérience professionelle dans le doublage."
"Tristana : La soeur de Thomas (la sympa pas l'autre)\n
Karma, Poppy : Hildi la Best Girl"
"Rise : Le cancéreux nominé au Oscars, Sachatte Longe."
"Grands remerciements à Fré Derrick pour les locaux."
"Remerciements à Marie pour avoir fait preuve de beaucoup de..."
"pour avoir fait preuve."
"Remerciements à Monsieur Simon comme catalyseur de haine et surtout pour NE PAS AVOIR ÉTÉ LÀ !"
"Jeu réalisé avec le moteur Renpy"
"Grimalkin à toi de jouer pour la version web !"
""
"FUCK ME PLEASE !"
""


jump end


label game_over:
show ecrant_game_over
""
stop music
hide ecrant_game_over
stop sound
play music "fightsinged.ogg"
jump debut_combat

label end:
return

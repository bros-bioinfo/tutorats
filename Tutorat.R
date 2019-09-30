#Tutorat R 
#Domitille COQ--ETCHEGARAY // Elsa CLAUDE 

### Info R 

rm(list=ls())
#Le repertoire de Travail : 
setwd("")

#L'installation de package // MacOs : type = "binary"
install.packages("FactoMineR")

#L'utilisation des librairies : 
library(datasets)
library(ggplot2)
library(plyr)
datasets::iris

#Help
?subset 

#Création de variable
fleur = iris
fleur <- iris
View(fleur)

#Manipulation de données 

#Selection d'une colonne
SepalL <- fleur[,1] #Attention indexation 1... pas de 0
SepalL2 <- fleur$Sepal.Length
print(SepalL)
print(SepalL2)
#Selection d'une ligne
Val1 <- fleur[1,]
print(Val1)
#Concaténation de variables
SepalL <- fleur$Sepal.Length
PetalL <- fleur$Petal.Length
DdSepPet <- cbind(SepalL,PetalL) #cbind column rbind row
DdSepPet <- c(SepalL,PetalL) #Montrer la diff entre cbind() et c()
#Selection par une variable Ex : SepalL et PetalL de setosa
tabSetosa <- subset(fleur, Species == "setosa",select = c(Sepal.Length,Petal.Length))
#Changer nom colonne
colnames(tabSetosa) <-c("Omnia","Sakura") 
#rownames() attention il faut qu'il y est le même nombre de colonne ou ligne que d'argument

#Quelques calculs
mean(SepalL)
colMeans(tabSetosa) #Existe pour row 
colSums(tabSetosa) #Existe pour row
median(SepalL)
sum(SepalL)
range(SepalL)
sd(SepalL)
scale(SepalL) #Standardisation valeur centré réduite 

#Informations et affichage variable
str(tabSetosa)
class(tabSetosa)
class(SepalL)
summary(tabSetosa)
names(tabSetosa)
View(tabSetosa)
head(tabSetosa)

#Gestion des NA
tabSetosa[1,1] <- NA
mean(tabSetosa$Omnia)
tabSetosa <- na.omit(tabSetosa)
mean(tabSetosa$Omnia)

#Quelques Graphs
#Boxplot
boxplot(fleur$Petal.Width~fleur$Species)
points(tapply(fleur$Petal.Width, fleur$Species, mean,na.rm=T),  col="red",pch=16)
#Barplot
Petmean <- tapply(fleur$Petal.Width, fleur$Species, mean,na.rm=T)
barplot(Petmean,xlab="Species",ylab="PetalWidth", main="Diagramme en barre (moyenne)")
#Plot
plot(fleur$Sepal.Length~fleur$Sepal.Width)

#Hist
#Freq Brutes
hist(fleur$Petal.Width,main="Effectifs bruts",xlab="PetWidth",ylab="Effectifs bruts",proba=F)
#Freq relatives
hist(fleur$Petal.Width,main="Effectifs relatifs",xlab="PetWidth", ylab="Effectifs relatifs",proba=T)

#Pairs
pairs(fleur)
#combiner la représentation des graphiques par paire (à gauche) au coefficient 
#de corrélation de Spearman à droite proportionnel à leur intensité avec des étoiles reportant 
#le niveau de significativité
#* pour p-value <0,05, ** pour p-value <0,01 et*** pour p-value <0,001
panel.cor.spearman <- function(x, y, digits=2, prefix="", cex.cor)  
{
  usr <-par("usr"); on.exit(par(usr))
  par(usr = c(0, 1, 0, 1))
  r <- (cor(x, y))
  txt <- format(c(r,0.123456789), digits=digits)[1]
  txt <- paste(prefix, txt,sep="")
  if(missing(cex.cor)) cex <-0.8/strwidth(txt)
  test <-cor.test(x,y,method="spearman")
  Signif <- symnum(test$p.value, corr =FALSE, na = FALSE,
                   cutpoints= c(0, 0.001, 0.01, 0.05, 0.1, 1),
                   symbols = c("***","**", "*", ".", " "))
  text(0.5, 0.5, txt, cex =cex * abs(r))
  text(.8, .8, Signif, cex=cex, col=2)
}
pairs (fleur, lower.panel=panel.smooth, upper.panel=panel.cor.spearman)


#Camembert 
count <- count(fleur,.(Species))
pie(count$freq,labels=count$Species, radius=0.7, col=c("blue","cyan","black"))



### Biostat 
#Exo 1 : 
#Etude d'un gaz nocif : 
#Question : Le taux est-il significativement supérieur au seuil tolérable admis de 50 (risque de 1%)?
#Importer le fichier csv et regarder les données 
gaz <- read.csv()
gaz <- as.matrix(gaz)
class(gaz)
View(gaz)

hist(gaz)
#Présence de NA ? Si oui, il faut les retirer

#Travail sur quelles types de variables, qualitatives // quantitatives ?
#Détermination du Test : Comparaison de moyennes cf clé détermination p24
#Poser les hypothèses H0//H1
#Conditions d'applications :
shapiro.test() #-> Quel test ? P-value ? 

#Paramétrique : 
t.test(gaz,alternative="greater",conf.level=0.99,mu=50) #Hésitez pas à poser des questions sur les arguments 
#cf p.30

#Non Paramétrique : 
wilcox.test(gaz,50, paired=FALSE, alternative="greater")
#Conclusion ?

#Exo2 : 
#Les huîtres
#Question : Les proportions 
#ou effectifs en espèce sont-elle statistiquement différentes entre les 2 stations (risque de 5%) ?
#Importer le fichier csv et regarder les données 
huitres <- read.csv()
View(huitres)
#Présence de NA ? Si oui, il faut les retirer

#Travail sur quelles types de variables, qualitatives // quantitatives ?
#Détermination du Test : Comparaison des distributions cf clé détermination p23
#Poser les hypothèses H0//H1
#Conditions d'applications :
tab<-table() #-> Travail sur deux variables lesquelles ? 
print(tab)

#Paramétrique : 
chisq.test(tab)

#Non Paramétrique : 
fisher.test(tab)

#Exo3 : 
#Modèle linéaire : 
#Question : Peut-on conclure a un effet du pH sur la prolifération de Nesseria gonorrhoeae ?
#Importer le fichier csv et regarder les données 
plant <- read.csv()
View(plant)
str(plant)
donnees_cibles = data.frame(Millsonia=plant$millsonia,Surface_aerienne=plant$bmaer)
plot = data.frame(Avec=plant[plant$millsonia== "TRUE", c("bmaer")],Sans=plant[plant$millsonia== "FALSE", c("bmaer")])
boxplot(plot)
#Présence de NA ? Si oui, il faut les retirer

#Travail sur quelles types de variables, qualitatives // quantitatives ?
#Détermination du Test : Modèle linéaire cf clé détermination p25
#Poser les hypothèses H0//H1

#Deux possibilités de travail : 
#lm
#aov
#Conditions d'applications sur résidus
an <- aov(log(plant$bmaer)~plant$millsonia)
summary(an)
#Graph 
par(mfrow=c(2,2))
plot(an)
#Normalité
shapiro.test(an$res) #p-value  H0 Les résidus suivent une loi normale 
#Homoscedasticité
car::leveneTest(an$res,plant$millsonia) #p-value H0 Homoscédastcité des résidus 
#Indépendances
lmtest::dwtest(an) #p-value H0 Indépendance des résidus (attention ne pas prendre en compte !)

#ANNOVA 
anova(an)
#Test post Hoc ? Quand deux groupes non nécessaires si plus de deux groupes nécessaires
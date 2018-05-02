Everything will be translated to English soon.


Aurinkokuntasimulaattori

Ohjelma simuloi aurinkokuntaa, jossa on keskipisteenä yksi kappale, jonka suhteen kaikki liike tapahtuu. Käyttöliittymä on merkkipohjainen. Laskenta perustuu Runge-Kutta metodiin.

Ohjelma vaatii toimiakseen numpy-kirjaston.

Ohjelma käynnistyy navigoimalla Skriptit-kansioon ja kirjoittamalla komentoriville "python3 main.py". Tarkemmat käyttöliittymäohjeet löytyvät dokumentaatiosta.

Koordinaatit voi kätevästi piirtää gnuplotilla.

GNUPlot ajokomento: plot for [i = 0:X:4] "filename" using (column(2+i)):(column(3+i)) title 'Cel'.i

, jossa "X" korvataan luvulla, joka on 4*(taivaankappaleiden_lkm - 1), ja "filename" korvataan simulointituloksien tiedostonimellä.


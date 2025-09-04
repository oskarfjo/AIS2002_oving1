import matplotlib.pyplot as plt

tick = 0
maxTick = 20000

rho = 1.225
V = 30
c = 1000
U = 0.5

T_0 = 280
referanse = 21

kelvinKonstant = 273.15

temperatur = 283.15

temperaturListe = [temperatur-kelvinKonstant]
pådragListe = [0]


def varmeovn(temp, ref):
    on = 400
    off = 0
    hysterese = 0.5
    if temp <= ref+hysterese and temp >= ref-hysterese:
        return pådragListe[-1]
    elif temp < ref:
        return on
    else:
        return off
    
def prosess(pådrag, ute):
    global temperatur

    temperatur += (pådrag + (ute-temperatur)*U)/(c*rho*V)
    temperaturListe.append(temperatur-kelvinKonstant)

while(tick < maxTick):
    
    u = varmeovn(temperatur, referanse+kelvinKonstant)
    pådragListe.append(u)

    prosess(u, T_0)
    tick += 1


plt.figure(figsize=(12, 5))
plt.subplot(2, 1, 1)
plt.plot(temperaturListe, label="Temperatur (°C)")
plt.axhline(y=referanse, color="r", linestyle="--", label="Referanse")
plt.ylabel("Temperatur i rom")
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(pådragListe, label="Pådrag (W)", color="orange")
plt.ylabel("Effekt fra varmeovn")
plt.legend()
plt.grid(True)

plt.show()
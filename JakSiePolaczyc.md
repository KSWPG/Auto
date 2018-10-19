## Łączenie się po Ethernet
1. Przewodowo możemy połączyć się z RPi za pośrednictwem switcha znajdującego się w sali. 
W tym celu wystarczy podłączyć do wybranego switcha swój komputer oraz RPi 
1. Można również połączyć RPi ze swoim komputerem bezpośrednio łącząc je za pomocą skrętki. 
Wtedy konieczne jest zmienienie adresu IP swojego komputera, jak to zrobić można znaleźć [tutaj](https://trybawaryjny.pl/jak-zmienic-ip/) 
w punkcie trzecim artykułu. Na swoim komputerze należy ustawić IP zgodne z tym ustawionym na RPi np.:
   - adres IP: 192.168.1.2
   - maska: 255.255.255.0
   - brama: zostawić puste
   
## Łączenie po WiFi
- Stwórz hotspot na swoim laptopie, jak to zrobić znajdziesz [tutaj](https://support.microsoft.com/pl-pl/help/4027762/windows-use-your-pc-as-a-mobile-hotspot)
lub dla win7 [tutaj](https://www.pcninja.us/turn-your-windows-7-laptop-into-a-wifi-hotspot/)
- Skonfiguruj hotspot zgodnie z poniższymi informacjami inaczej RPi się nie połączy:
  - SSID: KSW
  - Hasło: []  
- Aby połączenie było możliwe musisz jeszcze zmienić adres IP swojej karty sieciowej, jak to zrobić znajdziesz [tutaj](https://trybawaryjny.pl/jak-zmienic-ip/) w punkcie trzecim artykułu.
Aby RPi miało połączenie z Internetem za pośrednictwem naszego laptopa należy ustawić następujące IP:
  - adress IP: 192.168.2.1
  - maska: 255.255.255.0
  - brama: zostawić puste   

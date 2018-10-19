## Adresy IP
Ethernet: 192.168.1.10  
Wi-Fi: 192.168.2.9  (obecnie nie działa)
Sposób łączenia się do odpowiedniej sieci zostanie opisany w pliku [JakSiePolaczyc.md](JakSiePolaczyc.md)

## Konta użytkowników
Login: pi  
Hasło: raspberry  
  
Login: Root - konto administratora  
Hasło: []  
  
Na konto root nie da się zalogować bezpośrednio po SSH, najpierw należy się zalogować na użytkownika **pi**, a następnie dopiero wpisać komendę `sudo`, która pozwoli zalogować się na **roota**.

## Wykaz wykorzystanych pinów RPi
|Zastosowanie|BCM|GPIO Header|WiringPi|
|------------|----------|----------|----|
|BRIDGE ENABLE|4|7|7|
|PWM P|13|33|23|
|PHASE P|22|15|3|
|PWM L|12|32|26|
|PHASE L|23|16|4|

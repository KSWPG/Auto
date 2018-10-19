EESchema Schematic File Version 4
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L RASPBERRY_PI-rescue:STEROWNIK_DRV8835 U?
U 1 1 5BB8F86E
P 2500 1850
F 0 "U?" H 2525 2437 60  0000 C CNN
F 1 "STEROWNIK_DRV8835" H 2525 2331 60  0000 C CNN
F 2 "" H 2500 2300 60  0001 C CNN
F 3 "" H 2500 2300 60  0001 C CNN
	1    2500 1850
	-1   0    0    -1  
$EndComp
$Comp
L RASPBERRY_PI-rescue:RaspberryPi U?
U 1 1 5BB8F93C
P 6800 2400
F 0 "U?" H 6775 4137 60  0000 C CNN
F 1 "RaspberryPi" H 6775 4031 60  0000 C CNN
F 2 "" H 6800 2500 60  0001 C CNN
F 3 "" H 6800 2500 60  0001 C CNN
	1    6800 2400
	1    0    0    -1  
$EndComp
Wire Wire Line
	2850 1550 3200 1550
Wire Wire Line
	3200 1550 3200 1250
Wire Wire Line
	2850 1650 3300 1650
Wire Wire Line
	3300 1650 3300 1250
Wire Wire Line
	2850 1750 3400 1750
Wire Wire Line
	3400 1750 3400 1250
Wire Wire Line
	2850 1850 3500 1850
Wire Wire Line
	3500 1850 3500 1250
Wire Wire Line
	2850 1950 3600 1950
Wire Wire Line
	3600 1950 3600 1250
Wire Wire Line
	2850 2050 3700 2050
Wire Wire Line
	3700 2050 3700 1250
Text GLabel 3200 1250 1    50   Input ~ 0
GND_RPi
Text GLabel 3300 1250 1    50   Input ~ 0
5V_RPi
Text GLabel 3400 1250 1    50   Input ~ 0
PWM_RPi
Text GLabel 3500 1250 1    50   Input ~ 0
GPIO_RPi
Text GLabel 3600 1250 1    50   Input ~ 0
PWM_RPi
Text GLabel 3700 1250 1    50   Input ~ 0
GPIO_RPi
Wire Wire Line
	2850 2150 3300 2150
Wire Wire Line
	3300 2150 3300 1650
Connection ~ 3300 1650
Wire Wire Line
	2150 1550 1950 1550
Wire Wire Line
	1950 1550 1950 1250
Wire Wire Line
	2150 1650 1850 1650
Wire Wire Line
	1850 1650 1850 1250
Text GLabel 1950 1250 1    50   Input ~ 0
GND_PS
Text GLabel 1850 1250 1    50   Input ~ 0
11V_PS
$Comp
L Motor:Motor_DC M?
U 1 1 5BB90873
P 1150 1650
F 0 "M?" V 855 1600 50  0000 C CNN
F 1 "Motor_R" V 946 1600 50  0000 C CNN
F 2 "" H 1150 1560 50  0001 C CNN
F 3 "~" H 1150 1560 50  0001 C CNN
	1    1150 1650
	0    1    1    0   
$EndComp
$Comp
L Motor:Motor_DC M?
U 1 1 5BB908E2
P 1150 2250
F 0 "M?" V 855 2200 50  0000 C CNN
F 1 "Motor_L" V 946 2200 50  0000 C CNN
F 2 "" H 1150 2160 50  0001 C CNN
F 3 "~" H 1150 2160 50  0001 C CNN
	1    1150 2250
	0    1    1    0   
$EndComp
Wire Wire Line
	1700 2250 1700 2050
Wire Wire Line
	1700 2050 2150 2050
Wire Wire Line
	1350 2250 1700 2250
Wire Wire Line
	850  2250 850  1950
Wire Wire Line
	850  1950 2150 1950
Wire Wire Line
	850  1850 2150 1850
Wire Wire Line
	850  1650 850  1850
Wire Wire Line
	1350 1650 1500 1650
Wire Wire Line
	1500 1650 1500 1750
Wire Wire Line
	1500 1750 2150 1750
NoConn ~ 2150 2150
Wire Notes Line
	4000 600  4000 2700
Wire Notes Line
	4000 2700 600  2700
Wire Notes Line
	600  2700 600  600 
Wire Notes Line
	600  600  4000 600 
Text Label 1300 700  2    50   ~ 0
MotorControl_(MC)
Wire Wire Line
	6450 3550 5650 3550
Text GLabel 5650 3550 0    50   Input ~ 0
MC
Wire Wire Line
	6250 2050 5650 2050
Text GLabel 5650 2050 0    50   Input ~ 0
MC
Wire Wire Line
	7350 3250 8000 3250
Text GLabel 8000 3250 2    50   Input ~ 0
MC
Wire Wire Line
	7350 2050 8000 2050
Text GLabel 8000 2050 2    50   Input ~ 0
MC
$EndSCHEMATC

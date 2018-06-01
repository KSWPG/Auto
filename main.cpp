#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include "libraries/motorControl.h"

int main()
{
	
	if (wiringPiSetup () == -1)
    exit (1);
	pinMode (7, OUTPUT);
	digitalWrite (7, HIGH);
	
	Motor motorR(23,3);
	Motor motorL(26,4);
	
	motorR.changeSpeed(500);
	motorL.changeSpeed(500);
	delay(2000);
	turnLeft(motorR,motorL);
	delay(2000);
	turnRight(motorR,motorL);
	delay(2000);
	straight(motorR,motorL);
	delay(2000);
	rotateInPoint(motorR,motorL,500,1);
	delay(2000);
	rotateInPoint(motorR,motorL,500,-1);
	delay(2000);
	
	motorR.changeSpeed(0);
	motorL.changeSpeed(0);
	
	
	return 0;
}
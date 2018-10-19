#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include "motorControl.h"

Motor::Motor(int pinPWM_K,int pinDirection_K)
	{
		pinPWM=pinPWM_K;
		pinDirection=pinDirection_K;
		if (wiringPiSetup () == -1)
			exit(1);
		pinMode (pinDirection, OUTPUT);
		digitalWrite (pinDirection, HIGH);
		pinMode (pinPWM, PWM_OUTPUT);
			
	}
		
void Motor::changeSpeed(int new_speed)
	{
		speed=new_speed;
		pwmWrite(pinPWM, speed);
	}
		
void Motor::changeDirection(int new_direction)
	{
		direction=new_direction;
		if (direction==-1)
			direction=0;
		digitalWrite (pinDirection, direction);
	}
		
int Motor::showSpeed()
	{
		return speed;
	}
		
int Motor::showDirection()
	{
		return direction;
	}		

void turnLeft(Motor ML,Motor MR)
{
	int speedL=ML.showSpeed()-100;
	int speedR=MR.showSpeed()+100;
	
	ML.changeSpeed(speedL);
	MR.changeSpeed(speedR);
}

void turnRight(Motor ML,Motor MR)
{
	int speedL=ML.showSpeed()+100;
	int speedR=MR.showSpeed()-100;
	
	ML.changeSpeed(speedL);
	MR.changeSpeed(speedR);
}

void straight(Motor ML,Motor MR)
{
	int speedL=ML.showSpeed();
	int speedR=MR.showSpeed();
	
	int speed=(speedL+speedR)/2;
	
	ML.changeSpeed(speed);
	MR.changeSpeed(speed);
}

void rotateInPoint(Motor ML,Motor MR,int speed,int direction)		//direction 1 w prawo -1 w lewo
{
	ML.changeSpeed(0);
	MR.changeSpeed(0);
	
	ML.changeDirection(direction);
	MR.changeDirection((-1)*direction);
	
	ML.changeSpeed(speed);
	MR.changeSpeed(speed);
}



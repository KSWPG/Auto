#include <wiringPi.h>
//#include <stdio.h>
//#include <stdlib.h>
//#include <stdint.h>

class Motor{
	private:
		int pinPWM;
		int pinDirection;
		int speed;
		int direction;		//1 do przodu, -1 do tyłu
		
	public:
		Motor(int,int);
		
		void changeSpeed(int);
		
		void changeDirection(int);
		
		int showSpeed();
		
		int showDirection();
};

void turnLeft(Motor,Motor);

void turnRight(Motor,Motor);

void straight(Motor,Motor);

void rotateInPoint(Motor,Motor,int,int);		//direction 1 w prawo -1 w lewo

#include <wiringPi.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

class Motor{
	private:
		int pinPWM;
		int pinDirection;
		int speed=0;
		int direction=1;		//1 do przodu, -1 do tyłu
		
	public:
		Motor(int pinPWM_K, int pinDirection_K)
		{
			pinPWM=pinPWM_K;
			pinDirection=pinDirection_K;
			if (wiringPiSetup () == -1)
			exit (1) ;
			pinMode (pinDirection, OUTPUT);
			digitalWrite (pinDirection, HIGH);
			pinMode (pinPWM, PWM_OUTPUT)
		}
		
		void changeSpeed(int new_speed)
		{
			speed=new_speed;
			pwmWrite(pinPWM, speed);
		}
		
		void changeDirection(int new_direction)
		{
			direction=new_direction;
			if (direction==-1)
				direction=0;
			digitalWrite (pinDirection, direction);
		}
		
		int showSpeed()
		{
			return speed;
		}
		
		int showDirection()
		{
			return direction;
		}		
};

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

void prosto(Motor ML,Motor MR)
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


int main()
{	
	if (wiringPiSetup () == -1)
    		exit (1);
	
	pinMode (7, OUTPUT);
	digitalWrite (7, HIGH);
	
	Motor motor1(23,3);
	Motor motor2(26,4);
	
	motor1.changeSpeed(500);
	motor2.changeSpeed(500);
	delay(2000);
	turnLeft(motor1,motor2);
	delay(2000);
	turnRight(motor1,motor2);
	delay(2000);
	prosto(motor1,motor2);
	delay(2000);
	rotateInPoint(motor1,motor2,500,1);
	delay(2000);
	rotateInPoint(motor1,motor2,500,-1);
	delay(2000);
	
	motor1.changeSpeed(0);
	motor2.changeSpeed(0);

	return 0;
}

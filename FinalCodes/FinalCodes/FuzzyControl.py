from fuzzylogic.classes import Domain, Set, Rule
from fuzzylogic.hedges import very
from fuzzylogic.functions import R, S, triangular
from fuzzylogic.classes import Domain, Set
from fuzzylogic.functions import (sigmoid, gauss, trapezoid, 
                             triangular_sigmoid, rectangular)

class FuzzyControl:
    def get_PWM(self,proximity, velocity):
        prox = Domain("Proximity", 0, 30, res=0.1)
        speed = Domain("Speed", 0, 3, res=0.1)
        pwm = Domain("PWM", 0, 100, res=0.1)
        
        prox.very_near = S(0, 25)
        prox.near = triangular(10, 40)
        prox.medium = triangular(25,  50)
        prox.far = triangular(35, 100)
        prox.very_far = R(95, 200)

        speed.very_slow = S(0, 0.004)
        speed.slow = triangular(0.002, 0.006)
        speed.medium = triangular(0.005, 0.009)
        speed.fast = triangular(0.006, 0.015)
        speed.very_fast = R(0.015, 0.04)


        pwm.stop = S(0,  10)
        pwm.low = triangular(5, 30)
        pwm.medium = triangular(20, 70)
        pwm.high = R(60,  100)
        
        

        R1 = Rule({(prox.very_near, speed.very_slow): pwm.stop})
        R2 = Rule({(prox.near, speed.very_slow): pwm.high})
        R3 = Rule({(prox.medium, speed.very_slow): pwm.high})
        R4 = Rule({(prox.very_near, speed.slow): pwm.stop})
        R5 = Rule({(prox.near, speed.slow): pwm.high})
        R6 = Rule({(prox.medium, speed.slow): pwm.high})
        R7 = Rule({(prox.very_near, speed.medium): pwm.stop})
        R8 = Rule({(prox.near, speed.medium): pwm.low})
        R9 = Rule({(prox.medium, speed.medium): pwm.medium})
        R10 = Rule({(prox.very_near, speed.fast): pwm.stop})
        R11 = Rule({(prox.very_near, speed.very_fast): pwm.stop})
        R12 = Rule({(prox.near, speed.fast): pwm.low})
        R13 = Rule({(prox.near, speed.very_fast): pwm.low})
        R14 = Rule({(prox.medium, speed.fast): pwm.medium})
        R15 = Rule({(prox.medium, speed.very_fast): pwm.low})
        R16 = Rule({(prox.far, speed.very_slow): pwm.high})
        R17 = Rule({(prox.far, speed.slow): pwm.high})
        R18 = Rule({(prox.far, speed.medium): pwm.high})
        R19 = Rule({(prox.far, speed.fast): pwm.medium})
        R20 = Rule({(prox.far, speed.very_fast): pwm.low})
        R21 = Rule({(prox.very_far, speed.very_slow): pwm.high})
        R22 = Rule({(prox.very_far, speed.slow): pwm.high})
        R23 = Rule({(prox.very_far, speed.medium): pwm.high})
        R24 = Rule({(prox.very_far, speed.fast): pwm.medium})
        R25 = Rule({(prox.very_far, speed.very_fast): pwm.medium})
        
        
        rules = Rule({(prox.very_near, speed.very_slow): pwm.stop,
                    (prox.near, speed.very_slow): pwm.high,
                    (prox.medium, speed.very_slow): pwm.high,
                    (prox.very_near, speed.slow): pwm.stop,
                    (prox.near, speed.slow): pwm.high,
                    (prox.medium, speed.slow): pwm.high,
                    (prox.very_near, speed.medium): pwm.stop,
                    (prox.near, speed.medium): pwm.low,
                    (prox.medium, speed.medium): pwm.medium,
                    (prox.very_near, speed.fast): pwm.stop,
                    (prox.very_near, speed.very_fast): pwm.stop,
                    (prox.near, speed.fast): pwm.low,
                    (prox.near, speed.very_fast): pwm.low,
                    (prox.medium, speed.fast): pwm.medium,
                    (prox.medium, speed.very_fast): pwm.low,
                    (prox.far, speed.very_slow): pwm.high,
                    (prox.far, speed.slow): pwm.high,
                    (prox.far, speed.medium): pwm.high,
                    (prox.far, speed.fast): pwm.medium,
                    (prox.far, speed.very_fast): pwm.high,
                    (prox.very_far, speed.very_slow): pwm.high,
                    (prox.very_far, speed.slow): pwm.high,
                    (prox.very_far, speed.medium): pwm.high,
                    (prox.very_far, speed.fast): pwm.high,
                    (prox.very_far, speed.very_fast): pwm.high,
                    })
        rules == R1 | R2 | R3 | R4 | R5 | R6 | R7 | R8 | R9 | R10 | R11 | R12 | R13 | R14 | R15 | R16 | R17 | R18 | R19 | R20| R21 | R22 | R23 | R24 | R25== sum([R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, R21, R22. R23. R24. R25 ])
        values = {prox : proximity, speed:  velocity}
        return rules(values)


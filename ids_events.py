from dataclasses import dataclass


@dataclass
class ConfusionMatrix:
    """Class for calculating IDS system events from terminology table
    _____________________________________________________________________
    |                    | Attack Event          | Acceptable Event      |
    _____________________________________________________________________
    |Alarm Triggered     | True Positive (TP)    | False Positive (FP)   |
    |--------------------|-----------------------|-----------------------|
    |Alarm Not Triggered | False Negative (FN)   | True Negative (TN)    |
    |_____________________________________________________________________
    """

    tp: int  # True Positive (Alarm Triggered & Attack Event)
    fp: int  # False Positive (Alarm Triggered & Acceptable Event)

    fn: int  # False Negative (Alarm Not Triggered & Attack Event)
    tn: int  # True Negative (Aalarm Not Triggered & Acceptable Event)

    def rates(self) -> str:
        print(self)
        self.false_positive_rate = (self.fp / (self.fp + self.tn))
        print(f"False Positive = {self.false_positive_rate:.2%}")
        self.false_negative_rate = (self.fn / (self.tp + self.fn))
        print(f"False Negative = {self.false_negative_rate:.2%}")
        print()



"""     
IDS Events

12 of all 345 acceptable events triggered the IDS alarms
678 of all 890 attack events triggered the IDS alarms
678 True Positive, 890-678 = False Negative
12 False Positive, 345-12 True Negative
"""
events_2a = ConfusionMatrix(tp=678, fp=12, fn=(890 - 678), tn=(345 - 12))
events_2a.rates()

"""
COVID19 Events

195 of all 200 COVID-19 carriers are tested positive
7 of all 100 non-COVID-10 carriers are tested positive
195 True Positive, 5 False Negative
7 False Positive, 100 True Negative
"""
events_3a = ConfusionMatrix(tp=195, fp=7, fn=5, tn=100)
events_3a.rates()

"""
Extra Credit
P(Infected | Negative Test) =   (P(Negative Test)P(Negative Test|Infected)P )/ (Infected)

"""
P_infected = 200 / 300
P_neg_test_given_infected = events_3a.false_negative_rate
P_neg_test_given_not_infected = 1 - events_3a.false_positive_rate
P_not_infected = 100/300
P_negative = (P_neg_test_given_infected * P_infected) + (P_neg_test_given_not_infected * P_not_infected)

P_infected_neg_test = P_neg_test_given_infected * P_infected / P_negative


print(f"Probability you might still carry COVID-19 If you tested negative: \n{P_infected_neg_test:.2%}")

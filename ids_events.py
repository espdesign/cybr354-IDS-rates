from dataclasses import dataclass


@dataclass
class IntrusionEvents:
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
        print("Rates:")
        print(f"False Positive = {(self.fp / (self.fp + self.tn)):.2%}")
        print(f"False Negative = {(self.fn / (self.tp + self.fn)):.2%}")
        print()

# IDS(true positive, false positive, false negative, true negative)
events_2a = IntrusionEvents(678, 12, (890 - 678), (345 - 12))
events_2a.rates()

events_3a = IntrusionEvents(195,7,5,100)
events_3a.rates()

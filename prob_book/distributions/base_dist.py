class Distribution:
    prob_operations = ["="]

    def operator(self,op: str):
        ops = {
            "=":self.eq
        }
        return ops[op]

class Distribution:
    def operator(self,op: str):
        ops = {
            "equal":self.eq
        }
        return ops[op]

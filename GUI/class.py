
class configurator:
    def __init__(self, configure):
        self.configuration = configure

    def create_slit(self, dimen, slt_sz, slt_res, scr_sz, scr_res):
        slt_grid = int(slt_sz/slt_res)
        scr_grid = int((scr_sz*1000)/scr_res)
        factor1 = scr_res/slt_res
        factor2 = 10000/slt_res
        self.parameters = (slt_sz, slt_res, slt_grid, scr_sz,
                           scr_res, scr_grid, factor1, factor2)
        Slit = 0.0
        for i in range(dimen):
            Slit = [Slit]*slt_grid
        self.slit = Slit
        return Slit


S1 = configurator('Single_Slit')
Z = 2, 10, 2, 3, 4
print(S1.configuration)
x = S1.create_slit(*Z)

print(x)


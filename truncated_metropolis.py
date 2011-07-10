class TruncatedMetropolis(pymc.Metropolis):
    def __init__(self, stochastic, low_bound, up_bound, *args, **kwargs):
        self.low_bound = low_bound
        self.up_bound = up_bound
        pymc.Metropolis.__init__(self, stochastic, *args, **kwargs)

    # Propose method generates proposal values
    def propose(self):
        tau = 1./(self.adaptive_scale_factor * self.proposal_sd)**2
        self.stochastic.value = \
            pymc.rtruncnorm(self.stochastic.value, tau, self.low_bound, self.up_bound)

    # Hastings factor method accounts for asymmetric proposal distribution
    def hastings_factor(self):
        tau = 1./(self.adaptive_scale_factor * self.proposal_sd)**2
        cur_val = self.stochastic.value
        last_val = self.stochastic.last_value

        lp_for = pymc.truncnorm_like(cur_val, last_val, tau, \
            self.low_bound, self.up_bound)
        lp_bak = pymc.truncnorm_like(last_val, cur_val, tau, \
            self.low_bound, self.up_bound)

        if self.verbose > 1:
            print self._id + ': Hastings factor %f'%(lp_bak - lp_for)
        return lp_bak - lp_for
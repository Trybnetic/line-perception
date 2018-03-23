#!/usr/bin/env python3
#
# Copyright 2018 by Marc Weitz
#
# This script is licensed under the MIT-license.
# See https://opensource.org/licenses/MIT for more information

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")


np.random.seed(1337)  # set seed to create reproducable results

misjudgement = (list(np.random.normal(0, 0.19, 100)) +
                list(np.random.normal(-0.17, 0.22, 100)) +
                list(np.random.normal(-0.3, 0.27, 100)))
degree = (["1"] * 100) + (["2"] * 100) + (["3"] * 100)

data = pd.DataFrame({"misjudgement": misjudgement,
                     "degree": degree})

g = sns.factorplot(x="degree", y="misjudgement",
                   data=data, capsize=.2, palette="YlGnBu_d", size=3,
                   aspect=1.5)

plt.savefig('../plots/results.pdf', bbox_inches='tight',
            dpi=120, transparent=True)

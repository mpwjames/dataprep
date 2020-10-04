"""
    module for testing clean_email() function.
"""

import pandas as pd
import numpy as np
df = pd.DataFrame({"messy_email": 
                   ["yi@gmali.com","yi@sfu.ca","y i@sfu.ca","Yi@gmail.com","H ELLO@hotmal.COM","hello", np.nan, "NULL"]
                  })
df


from dataprep.clean import clean_email
clean_email(df, "messy_email")
# GitHub: AleGV258
# Script donde pruebo el código
# Y el código de la Kata 0

from datetime import *
from dateutil.relativedelta import *

now = datetime.now()
print(now)
now = now + relativedelta(months=1, weeks=1, hour=10)
print(now)

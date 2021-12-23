from appwings_script.sco_rpc_data_v import des_encrypt,des_decrypt,eight_random_str,md5_hash
import time
import json
import random
import string

SYSTEM_SECRET = {
    'S1': 'SSO',
    'S2': 'ERP',
    'S3': 'CRM',
    'S4': 'NC',
    'S5': 'OA',
    'S6': 'Mall',
    'S7': 'App',
    'S8': 'Chat',
    'S9': 'UsedCar',
    'S10': 'EHR',
}

data = "3TQ%2BjlYgpZsLz1vIFL77DOHCU20iehqH4TFTq629kJPY7ZadfrproNc1EbakA%2B2zuLyBcGspYLvykMWsTeBlZa/C/NqOoQrneWKCX4slMO4D2wxAAAGvrgtu%2Bhu%2BF1O2t1Ik06lOo20LLUWRwj0qKajJRQmrxIUEMfpN6tEAbPYDn4QZPTguGJDlijsul5akchY8fjN9/cSXaALcb2CfBRrKWyePb2x9I7gnfLwrt8dYP9i7Gj0kEubB52w3xJtrEbmll05eXDcVMzZB2jqIBHXfuz%2BI6%2BgU7jcGSs1BL1vh1/TQUWPnch2S7zS5mr8ks/Jb/d5FHaK7WbnaAfxtXAFdDRtHLPB12GmEdmaWh9RbkiXMqwdrb5Snjvjt7c6qfbGbaKXDiYBL3mCt0Ox7r2TQhwwQocvw7Ezuq2vs6ohoekRkREfFzi7R9D0pnrpYYF3kPIkmHOranjcOTnITlQL7iw5TevUDRaJx0Xq2QpL4h3Mt%2B7igxQ%3D%3D"
id_code = "32ebf050afe161357da13b56295c6def"
time1 = "1611823909F76CB21B"

a = des_decrypt('App',data)
print(a)


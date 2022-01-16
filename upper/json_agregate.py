import glob
import os
import shutil
import json
import re

try:
  os.mkdir('./processed')
except OSError:
  print("'/processed' directory already exist")

# receipts = glob.glob('./receipts/receipt-[0-9]*.json')
receipts = [f for f in glob.glob('./receipts/receipt-[0-9]*.json') if re.match(r'./receipts\\receipt-[0-9]*[02468].json', f)]
print(receipts)
subtotal = 0.0

for path in receipts:
  with open(path) as f:
    content = json.load(f)
    subtotal += float(content['value'])
  # name = path.split('\\')[-1]
  # destination = f'./processed\{name}'
  destination = path.replace('receipts', 'processed')
  shutil.move(path, destination)
  print(f"moved '{path}' to '{destination}'")

print("Receipt subtotal: $%.2f" % subtotal)
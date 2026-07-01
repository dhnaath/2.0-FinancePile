import re

with open("src/components/AddCardView.tsx", "r") as f:
    content = f.read()

pattern = re.compile(r'<div className="relative border border\[#2a2a2a\] rounded-2xl px-4 py-3 bg\[#1e1e1e\] flex flex-col justify-center.*?<label.*?</label>.*?</div>', re.DOTALL)
matches = pattern.findall(content)
print(f"Found {len(matches)} matches")

import re

with open("src/components/AddCardView.tsx", "r") as f:
    content = f.read()

# Pattern to replace:
# <div className="relative border border-[#2a2a2a] rounded-2xl px-4 py-3 bg-[#1e1e1e] flex flex-col justify-center gap-2">
# <label className="text-xs font-medium text-gray-400">Nama Pinjaman</label>
# <input required name="name" value={formData.name} onChange={handleChange} type="text" className="w-full bg-transparent outline-none font-medium text-gray-100 placeholder:text-gray-600 text-base" placeholder="KPR Mandiri" />
# </div>

def replacer(match):
    div_start = match.group(1)
    label_text = match.group(2)
    inner = match.group(3)
    
    # We want to change the wrapper to fieldset, the label to legend
    fieldset_start = '<fieldset className="relative border border-[#2a2a2a] rounded-2xl px-4 pt-1.5 pb-2 bg-[#1e1e1e] focus-within:border-gray-500">'
    legend = f'<legend className="text-xs font-medium text-gray-400 px-1 ml-1 bg-[#121212] -mt-0.5">{label_text}</legend>'
    
    # modify inner to add px-1 pb-1
    # find className="..."
    if 'className="' in inner:
        inner = inner.replace('className="', 'className="px-1 pb-1 ', 1)
        
    return f"{fieldset_start}\n    {legend}\n    {inner}\n</fieldset>"

# regex for the block:
pattern = re.compile(
    r'<div className="relative border border\[#2a2a2a\] rounded-2xl px-4 py-3 bg\[#1e1e1e\] flex flex-col justify-center(?: gap-2)?">\s*<label className="text-xs font-medium text-gray-400(?: mb-1)?">(.*?)</label>\s*(.*?)\s*</div>',
    re.DOTALL
)

matches = pattern.findall(content)
print(f"Found {len(matches)} matches")

new_content = pattern.sub(replacer, content)

with open("src/components/AddCardView.tsx", "w") as f:
    f.write(new_content)

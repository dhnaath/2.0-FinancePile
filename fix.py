import re

with open("src/components/AddCardView.tsx", "r") as f:
    text = f.read()

# Replace <div ...> with <fieldset ...>
text = text.replace('<div className="relative border border-[#2a2a2a] rounded-2xl px-4 py-3 bg-[#1e1e1e] flex flex-col justify-center gap-2">', '<fieldset className="relative border border-[#2a2a2a] rounded-2xl px-4 pt-1.5 pb-2 bg-[#1e1e1e] focus-within:border-gray-500">')
text = text.replace('<div className="relative border border-[#2a2a2a] rounded-2xl px-4 py-3 bg-[#1e1e1e] flex flex-col justify-center">', '<fieldset className="relative border border-[#2a2a2a] rounded-2xl px-4 pt-1.5 pb-2 bg-[#1e1e1e] focus-within:border-gray-500">')

# Replace <label ...>Label</label> with <legend ...>Label</legend>
text = re.sub(r'<label className="text-xs font-medium text-gray-400(?: mb-1)?">(.*?)</label>', r'<legend className="text-xs font-medium text-gray-400 px-1 ml-1 bg-[#121212] -mt-0.5">\1</legend>', text)

# For the inputs, let's just leave them or replace them
text = text.replace('className="w-full bg-transparent outline-none', 'className="px-1 pb-1 w-full bg-transparent outline-none')
text = text.replace('className="flex items-center gap-3"', 'className="flex items-center gap-3 px-1 pb-1"')
text = text.replace('className="grid grid-cols-3 gap-2"', 'className="grid grid-cols-3 gap-2 px-1 pb-1"')

# Need to replace the closing </div> of these specific ones with </fieldset>.
# Actually this is tricky because of nested divs.
with open("src/components/AddCardView.tsx", "w") as f:
    f.write(text)


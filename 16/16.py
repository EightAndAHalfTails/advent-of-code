print [t.items()<={'children':3,'cats':7,'samoyeds':2,'pomeranians':3,'akitas':0,'vizslas':0,'goldfish':5,'trees':3,'cars':2,'perfumes':1}.items() for t in [{l.split()[i].rstrip(':'):int(l.split()[i+1].rstrip(',')) for i in [2,4,6]} for l in open("input.txt")]].index(True)+1, [all([{'children':3,'cats':7,'samoyeds':2,'pomeranians':3,'akitas':0,'vizslas':0,'goldfish':5,'trees':3,'cars':2,'perfumes':1}[i]<n if i=='cats'or i=='trees'else {'children':3,'cats':7,'samoyeds':2,'pomeranians':3,'akitas':0,'vizslas':0,'goldfish':5,'trees':3,'cars':2,'perfumes':1}[i]>n if i=='pomeranians'or i=='goldfish'else {'children':3,'cats':7,'samoyeds':2,'pomeranians':3,'akitas':0,'vizslas':0,'goldfish':5,'trees':3,'cars':2,'perfumes':1}[i]==n for i, n in {l.split()[i].rstrip(':'):int(l.split()[i+1].rstrip(',')) for i in [2,4,6]}.items()])for l in open("input.txt")].index(True)+1

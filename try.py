value = 10
symbol = "♥"
figure = "K"

carta = [f"""
┌─────────┐
│{value}        │
│    {symbol}    │
│         │
│    {symbol}    │   
│        {value}│
└─────────┘
""",
f""""
┌─────────┐
│{value}   {symbol}    │
│         │
│    {symbol}    │
│         │   
│    {symbol}   {value}│
└─────────┘
""",
f"""
┌─────────┐
│{value}        │
│  {symbol}   {symbol}  │
│         │
│  {symbol}   {symbol}  │   
│        {value}│
└─────────┘
""",
f"""
┌─────────┐
│{value}        │
│  {symbol}   {symbol}  │
│    {symbol}    │
│  {symbol}   {symbol}  │   
│        {value}│
└─────────┘
""",
f"""
┌─────────┐
│{value}   {symbol}    │
│  {symbol}   {symbol}  │
│    {symbol}    │
│  {symbol}   {symbol}  │   
│        {value}│
└─────────┘
""",
f"""
┌─────────┐
│{value}   {symbol}    │
│  {symbol}   {symbol}  │
│    {symbol}    │
│  {symbol}   {symbol}  │   
│    {symbol}   {value}│
└─────────┘
""",
f"""
┌─────────┐
│{value}   {symbol}    │
│  {symbol}   {symbol}  │
│{symbol}   {symbol}    │
│  {symbol}   {symbol}  │   
│    {symbol}   {value}│
└─────────┘
""",
f"""
┌─────────┐
│{value}   {symbol}    │
│  {symbol}   {symbol}  │
│{symbol}   {symbol}   {symbol}│
│  {symbol}   {symbol}  │   
│    {symbol}   {value}│
└─────────┘
""",
f"""
┌─────────┐
│{value} {symbol} {symbol}   │
│  {symbol}   {symbol}  │
│ {symbol}     {symbol} │
│  {symbol}   {symbol}  │   
│   {symbol} {symbol} {value}│
└─────────┘
"""
]

['\n┌─────────┐\n│10        │\n│    ♥    │\n│         │\n│    ♥    │   \n│        10│\n└─────────┘\n', 
'"\n┌─────────┐\n│10   ♥    │\n│         │\n│    ♥    │\n│         │   \n│    ♥   10│\n└─────────┘\n',
'\n┌─────────┐\n│10        │\n│  ♥   ♥  │\n│         │\n│  ♥   ♥  │   \n│        10│\n└─────────┘\n',
'\n┌─────────┐\n│10        │\n│  ♥   ♥  │\n│    ♥    │\n│  ♥   ♥  │   \n│        10│\n└─────────┘\n',
'\n┌─────────┐\n│10   ♥    │\n│  ♥   ♥  │\n│    ♥    │\n│  ♥   ♥  │   \n│        10│\n└─────────┘\n',
'\n┌─────────┐\n│10   ♥    │\n│  ♥   ♥  │\n│    ♥    │\n│  ♥   ♥  │   \n│    ♥   10│\n└─────────┘\n',
'\n┌─────────┐\n│10   ♥    │\n│  ♥   ♥  │\n│♥   ♥    │\n│  ♥   ♥  │   \n│    ♥   10│\n└─────────┘\n',
'\n┌─────────┐\n│10   ♥    │\n│  ♥   ♥  │\n│♥   ♥   ♥│\n│  ♥   ♥  │   \n│    ♥   10│\n└─────────┘\n',
'\n┌─────────┐\n│10 ♥ ♥   │\n│  ♥   ♥  │\n│ ♥     ♥ │\n│  ♥   ♥  │   \n│   ♥ ♥ 10│\n└─────────┘\n']

a = [r'\n┌─────────┐\n│{value}        │\n│    {symbol}    │\n│         │\n│    {symbol}    │   \n│        {value}│\n└─────────┘\n',
r'\n┌─────────┐\n│{value}   {symbol}    │\n│         │\n│    {symbol}    │\n│         │   \n│    {symbol}   {value}│\n└─────────┘\n',
r'\n┌─────────┐\n│{value}        │\n│  {symbol}   {symbol}  │\n│         │\n│  {symbol}   {symbol}  │   \n│        {value}│\n└─────────┘\n',
r'\n┌─────────┐\n│{value}        │\n│  {symbol}   {symbol}  │\n│    {symbol}    │\n│  {symbol}   {symbol}  │   \n│        {value}│\n└─────────┘\n',
r'\n┌─────────┐\n│{value}   {symbol}    │\n│  {symbol}   {symbol}  │\n│    {symbol}    │\n│  {symbol}   {symbol}  │   \n│        {value}│\n└─────────┘\n',
r'\n┌─────────┐\n│{value}   {symbol}    │\n│  {symbol}   {symbol}  │\n│    {symbol}    │\n│  {symbol}   {symbol}  │   \n│    {symbol}   {value}│\n└─────────┘\n', 
r'\n┌─────────┐\n│{value}   {symbol}    │\n│  {symbol}   {symbol}  │\n│{symbol}   {symbol}    │\n│  {symbol}   {symbol}  │   \n│    {symbol}   {value}│\n└─────────┘\n', 
r'\n┌─────────┐\n│{value}   {symbol}    │\n│  {symbol}   {symbol}  │\n│{symbol}   {symbol}   {symbol}│\n│  {symbol}   {symbol}  │   \n│    {symbol}   {value}│\n└─────────┘\n', 
r'\n┌─────────┐\n│{value} {symbol} {symbol}   │\n│  {symbol}   {symbol}  │\n│ {symbol}     {symbol} │\n│  {symbol}   {symbol}  │   \n│   {symbol} {symbol} {value}│\n└─────────┘\n']

finura =[r"""
┌─────────┐
│{figure}       {symbol}│
│    {symbol}    │
│    {figure}    │
│    {symbol}    │
│{symbol}       {figure}│
└─────────┘         
"""
]
print(finura)
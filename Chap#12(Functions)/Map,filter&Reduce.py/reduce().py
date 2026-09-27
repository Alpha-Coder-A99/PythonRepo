#Reduce()
# Sab ko jama/aik karna.
# Functools ka Matlab: "Function Tools". Yani aise auzaar (tools) jo functions ki taqat barhane ke kaam aate hain.
from functools import reduce

prices = [100, 500, 250, 150]

# Step 1: Filter lagao (Sirf 200 se baray numbers chuno)
# filter(lambda x: x > 200, prices) humein [500, 250] dega.

# Step 2: Reduce lagao (In bache hue numbers ko jama kar do)
total_expensive = reduce(lambda x, y: x + y, filter(lambda x: x > 200, prices))

print(f"Total of items > 200: {total_expensive}") 
# Output: 750 (Kyunke 500 + 250 = 750)
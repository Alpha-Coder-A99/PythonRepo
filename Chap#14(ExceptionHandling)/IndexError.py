"""
IndexError tab aata hai jab aap kisi sequence (jaise List ya Tuple) mein aisi index (position) ko
access karne ki koshish karte hain jo uski hadd (range) se bahar ho.
"""

numbers = [10, 20, 30]  # Isme indexes hain: 0, 1, 2

# Index 5 list mein mojood hi nahi hai, is liye IndexError aayega:
try:
    print(numbers[5])
except IndexError as err:
    print(f"Index not found: {err}")
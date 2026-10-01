try:
    import non_existent_module
except ImportError as e:
    print(f"ImportError occurred: {e}")

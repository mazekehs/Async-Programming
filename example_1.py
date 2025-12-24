import time


# Fully Synchronous code...complete one task fully then move to another
def fetch_data(param):
    print(f"Do something with {param}...")
    time.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"

def main():
    result1=fetch_data(1)
    print("Fetch 1 fully copmpleted")
    result2=fetch_data(2)
    print("Fetch 2 fully completed")
    return [result1, result2]

t1=time.perf_counter()
results=main()
print(results)

t2=time.perf_counter()
print(f"Finished in {t2-t1:.2f} seconds")
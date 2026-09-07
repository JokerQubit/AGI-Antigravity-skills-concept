import os
import sys

def check_rules():
    rules_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'rules')
    files = sorted([f for f in os.listdir(rules_dir) if f.endswith('.md')])
    print(f"{'File':<40} {'Bytes':<10} {'Est. Tokens':<15} {'Status'}")
    print("-" * 75)
    all_ok = True
    total_bytes = 0
    total_tokens = 0
    for f in files:
        path = os.path.join(rules_dir, f)
        with open(path, 'rb') as fp:
            data = fp.read()
        has_bom = data.startswith(b'\xef\xbb\xbf')
        length = len(data)
        total_bytes += length
        # Approximate token count: words * 1.3 or length / 3.8
        text = data.decode('utf-8', errors='replace')
        words = len(text.split())
        est_tokens = int(words * 1.35)
        total_tokens += est_tokens
        
        status = "OK"
        if has_bom:
            status = "BOM FOUND"
            all_ok = False
        elif length < 3800:
            status = f"TOO SMALL ({length} < 3800)"
            all_ok = False
        elif length > 5800:
            status = f"TOO LARGE ({length} > 5800)"
            all_ok = False
            
        print(f"{f:<40} {length:<10} {est_tokens:<15} {status}")
        
    print("-" * 75)
    print(f"Total: {len(files)} files, {total_bytes} bytes, ~{total_tokens} tokens total.")
    return all_ok

if __name__ == '__main__':
    ok = check_rules()
    sys.exit(0 if ok else 1)

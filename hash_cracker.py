import hashlib
import sys

# Target profile for the demonstration
# This is the SHA-256 hash of the password "password123"
TARGET_HASH = "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
MOCK_WORDLIST = ["123456", "admin", "qwerty", "password123", "letmein1"]

print("-" * 55)
print("🔑 IDENTITY ASSURANCE: DICTIONARY HASH CRACKER 🔑")
print("-" * 55)
print(f"[*] Target SHA-256 Hash: {TARGET_HASH}")
print(f"[*] Parsing wordlist iterations...\n")

found = False

for word in MOCK_WORDLIST:
    print(f"[+] Compiling trial string: '{word}'")
    
    # Calculate SHA-256 hash of current word
    guess_hash = hashlib.sha256(word.encode('utf-8')).hexdigest()
    
    if guess_hash == TARGET_HASH:
        print(f"\n🔓 SUCCESS: Plaintext match extracted!")
        print(f"   🎯 Cleartext Password: {word}")
        print(f"   🔒 Matched Signature:  {guess_hash}")
        found = True
        break

if not found:
    print("\n[-] Attack Exhausted: No cleartext signature match found in dictionary.")

print("-" * 55)

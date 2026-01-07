// --- CONFIGURATION ---

// The "Dictionary" of Constant Signs from Godel's 1931 Paper
const godelMap = {
    '~': 1n,  // Not
    'v': 2n,  // Or
    '>': 3n,  // If... Then (Implies)
    'E': 4n,  // There Exists
    '=': 5n,  // Equals
    '0': 6n,  // Zero
    's': 7n,  // Successor
    '(': 8n,  // Open Paren
    ')': 9n,  // Close Paren
    ',': 10n  // Punctuation
    // Variables (x, y, z) usually start at 11, 13...
};

// --- HELPER FUNCTIONS ---

// Returns the n-th prime number (0 -> 2, 1 -> 3, 2 -> 5, etc.)
function getNthPrime(n) {
    const primes = [];
    let candidate = 2;
    while (primes.length <= n) {
        let isPrime = true;
        for (let i = 2; i <= Math.sqrt(candidate); i++) {
            if (candidate % i === 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) primes.push(candidate);
        candidate++;
    }
    return BigInt(primes[n]);
}

// --- MAIN FUNCTION ---

/**
 * Encodes a sequence of symbols into a single Godel Number.
 * @param {string[]} symbolArray - Array of symbols, e.g., ['0', '=', '0']
 * @returns {BigInt} The unique Godel Number
 */
function encode(symbolArray) {
    let result = 1n;

    console.log(`\n--- Encoding: "${symbolArray.join(' ')}" ---`);

    symbolArray.forEach((char, index) => {
        const symbolValue = godelMap[char];
        
        if (symbolValue === undefined) {
            throw new Error(`Unknown symbol: ${char}`);
        }

        // Get the prime number for this position
        const primeBase = getNthPrime(index);

        // Math: result = result * (prime ^ symbolValue)
        const factor = primeBase ** symbolValue;
        
        result = result * factor;
        
        // Visual logging for your article/debugging
        console.log(`Pos ${index} (Prime ${primeBase}): Symbol '${char}' -> ID ${symbolValue}. Multiplying by ${primeBase}^${symbolValue}`);
    });

    return result;
}

// --- EXECUTION ---

// Example 1: "0 = 0"
const gn1 = encode(['0', '=', '0']);
console.log(`Result: ${gn1}`); 

// Example 2: "~(0=s0)" -> "It is not true that 0 equals 1"
const gn2 = encode(['~', '(', '0', '=', 's', '0', ')']);
console.log(`Result: ${gn2}`);
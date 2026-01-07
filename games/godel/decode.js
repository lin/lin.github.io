// --- CONFIGURATION ---
const godelMap = {
    '~': 1n, 'v': 2n, '>': 3n, 'E': 4n, '=': 5n, 
    '0': 6n, 's': 7n, '(': 8n, ')': 9n, ',': 10n,
    'x': 11n, 'y': 13n, 'z': 17n
};

// Create a Reverse Map (1n -> '~', 2n -> 'v', etc.) automatically
const reverseGodelMap = {};
for (const [key, value] of Object.entries(godelMap)) {
    reverseGodelMap[value] = key;
}

// --- HELPER FUNCTIONS ---
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

// --- MAIN FUNCTIONS ---

/**
 * Decodes a Godel Number back into a sequence of symbols.
 * @param {BigInt} godelNumber - The large integer to decode
 * @returns {string[]} The sequence of symbols
 */
function decode(godelNumber) {
    let currentNumber = godelNumber;
    const decodedSymbols = [];
    let primeIndex = 0;

    console.log(`\n--- Decoding: ${godelNumber} ---`);

    // We loop until the number has been reduced to 1
    while (currentNumber > 1n) {
        const currentPrime = getNthPrime(primeIndex);
        
        let exponent = 0n;

        // Count how many times we can divide by this prime
        while (currentNumber % currentPrime === 0n) {
            currentNumber = currentNumber / currentPrime;
            exponent++;
        }

        // If exponent is 0, it means there was a "gap" in primes. 
        // In valid Godel numbering for formulas, this shouldn't typically happen 
        // unless the format is strictly defined. We will assume 0 is a break or check for validity.
        if (exponent === 0n) {
             console.log(`Warning: Prime ${currentPrime} was skipped. Logic check needed.`);
        }

        // Map the exponent back to a symbol
        const symbol = reverseGodelMap[exponent];
        
        if (!symbol) {
             throw new Error(`Decoded ID ${exponent} has no matching symbol in map!`);
        }

        console.log(`Prime ${currentPrime} divides input ${exponent} times -> ID ${exponent} is "${symbol}"`);
        decodedSymbols.push(symbol);
        
        primeIndex++;
    }

    return decodedSymbols;
}

// --- ENCODER (Included for testing) ---
function encode(symbolArray) {
    let result = 1n;
    symbolArray.forEach((char, index) => {
        result = result * (getNthPrime(index) ** godelMap[char]);
    });
    return result;
}

// --- EXECUTION ---

// 1. Let's create a number first (0 = 0)
// Math: 2^6 * 3^5 * 5^6
const originalSentence = ['0', '=', '0'];
const bigNumber = encode(originalSentence);

console.log(`Original: ${originalSentence.join(" ")}`);
console.log(`Encoded:  ${bigNumber}`);

// 2. Now, let's decode that big number to see if we get "0 = 0" back
const decodedSentence = decode(bigNumber);

console.log(`\nFinal Result: ${decodedSentence.join(" ")}`);
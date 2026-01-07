// --- SIMPLIFIED GODEL NUMBERING (TEXT-AS-NUMBER) ---

/**
 * Encodes any text string into a single unique BigInt.
 * Concept: Treats the text as a sequence of bytes, read as one large number.
 * @param {string} text - The mathematical statement or text
 * @returns {BigInt} The unique integer ID
 */
function encode(text) {
    // 1. Convert text to a Buffer (raw bytes in UTF-8)
    const buffer = Buffer.from(text, 'utf8');
    
    // 2. Turn that buffer into a Hexadecimal string (e.g., "783d30")
    // This effectively turns the text into a number in base-16
    const hexString = '0x' + buffer.toString('hex');
    
    // 3. Convert Hex string to a standard BigInt
    return BigInt(hexString);
}

/**
 * Decodes a BigInt back into the original text string.
 * @param {BigInt} number - The unique integer ID
 * @returns {string} The original text
 */
function decode(number) {
    // 1. Convert BigInt to Hex String (Base 16)
    let hexString = number.toString(16);

    // 2. Ensure we have an even number of characters (bytes are pairs of hex digits)
    // If the number is small (like 0xA), we need "0A" to parse it correctly as a byte.
    if (hexString.length % 2 !== 0) {
        hexString = '0' + hexString;
    }

    // 3. Convert Hex string back to Buffer (Bytes)
    const buffer = Buffer.from(hexString, 'hex');
    
    // 4. Convert Buffer to String (UTF-8)
    return buffer.toString('utf8');
}

// --- EXECUTION EXAMPLE ---

const statement = "x = 0";

console.log(`Original: "${statement}"`);

// 1. Encode the statement into a number
const godelNumber = encode(statement);
console.log(`Godel Number: ${godelNumber}`);
// This number represents "x = 0" uniquely.

// 2. Decode the number back into text
const result = decode(godelNumber);
console.log(`Decoded:  "${result}"`);

// 3. Verify it works for complex sentences too
const complexID = encode("~(0 = s0)");
console.log(`Complex ID: ${complexID}`);
console.log(`Complex Decoded: "${decode(complexID)}"`);
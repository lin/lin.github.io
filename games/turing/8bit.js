// Import required functions from 1bit.js
const { full_adder } = require('./1bit');

/**
 * 8-bit Adder: Adds two 8-bit binary numbers (represented as arrays)
 * and returns the sum and carry-out bit
 * 
 * @param {number[]} byte1 - First 8-bit number as array of bits [LSB...MSB]
 * @param {number[]} byte2 - Second 8-bit number as array of bits [LSB...MSB]
 * @param {number} [carryIn=0] - Carry-in bit (0 or 1)
 * @returns {number[]} Array containing [sum, carryOut]
 */
function eight_bit_adder(byte1, byte2, carryIn = 0) {
  let carry = carryIn;
  const sum = [];
  
  // Process each bit from LSB to MSB
  for (let i = 0; i < 8; i++) {
    const [sumBit, newCarry] = full_adder(byte1[i], byte2[i], carry);
    sum[i] = sumBit;
    carry = newCarry;
  }
  
  return [sum, carry];
}

/**
 * Converts a decimal number to an 8-bit binary array (LSB first)
 * @param {number} decimal - Number between 0 and 255
 * @returns {number[]} 8-bit array [LSB...MSB]
 */
function decimalToByte(decimal) {
  if (decimal < 0 || decimal > 255) {
    throw new Error('Decimal must be between 0 and 255');
  }
  const bits = [];
  for (let i = 0; i < 8; i++) {
    bits.push((decimal >> i) & 1);
  }
  return bits;
}

/**
 * Converts an 8-bit binary array (LSB first) to a decimal number
 * @param {number[]} byte - 8-bit array [LSB...MSB]
 * @returns {number} Decimal number
 */
function byteToDecimal(byte) {
  return byte.reduce((acc, bit, index) => acc + (bit << index), 0);
}

// Example usage:
// const byte1 = decimalToByte(166); // [0, 1, 1, 0, 0, 1, 0, 1]
// const byte2 = decimalToByte(63);  // [1, 1, 1, 1, 0, 0, 0, 0]
// const [sum, carryOut] = eight_bit_adder(byte1, byte2);
// console.log('Sum:', byteToDecimal(sum)); // 229
// console.log('Carry Out:', carryOut);    // 0

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = {
    eight_bit_adder,
    decimalToByte,
    byteToDecimal
  };
}
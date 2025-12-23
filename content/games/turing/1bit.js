/**
 * NAND gate: Returns false only when both inputs are true
 * Truth table:
 * a | b | nand(a,b)
 * 0 | 0 | 1
 * 0 | 1 | 1
 * 1 | 0 | 1
 * 1 | 1 | 0
 */
function nand(a, b) {
  if (a == 0 && b == 0) return 1;
  if (a == 0 && b == 1) return 1;
  if (a == 1 && b == 0) return 1;
  if (a == 1 && b == 1) return 0;
}

/**
 * NOT gate: Inverts the input
 * Implemented using NAND gate (NAND with both inputs tied together)
 * Truth table:
 * a | not(a)
 * 0 | 1
 * 1 | 0
 */
function not(a) {
  return nand(a, a);
}

/**
 * AND gate: Returns true only when both inputs are true
 * Implemented using NAND and NOT gates: AND(a,b) = NOT(NAND(a,b))
 * Truth table:
 * a | b | and(a,b)
 * 0 | 0 | 0
 * 0 | 1 | 0
 * 1 | 0 | 0
 * 1 | 1 | 1
 */
function and(a, b) {
  return not(nand(a, b));
}

/**
 * OR gate: Returns true when at least one input is true
 * Implemented using NAND and NOT gates: OR(a,b) = NAND(NOT(a), NOT(b))
 * Truth table:
 * a | b | or(a,b)
 * 0 | 0 | 0
 * 0 | 1 | 1
 * 1 | 0 | 1
 * 1 | 1 | 1
 */
function or(a, b) {
  return nand(not(a), not(b));
}

/**
 * NOR gate: Returns true only when both inputs are false
 * Implemented using OR and NOT gates: NOR(a,b) = NOT(OR(a,b))
 * Truth table:
 * a | b | nor(a,b)
 * 0 | 0 | 1
 * 0 | 1 | 0
 * 1 | 0 | 0
 * 1 | 1 | 0
 */
function nor(a, b) {
  return not(or(a, b));
}

/**
 * ALWAYS_ON: Always returns 1 regardless of input
 * Implemented using OR and NOT gates: ALWAYS_ON(a) = OR(a, NOT(a))
 * This works because either a is 1, or NOT(a) is 1, so OR always returns 1
 */
function on(a) {
  return or(a, not(a));
}

/**
 * AND_NOT: Returns 1 only when first input is 1 and second input is 0
 * Implemented using AND and NOT gates: AND_NOT(a,b) = AND(a, NOT(b))
 * Truth table:
 * a | b | and_not(a,b)
 * 0 | 0 | 0
 * 0 | 1 | 0
 * 1 | 0 | 1
 * 1 | 1 | 0
 */
function and_not(a, b) {
  return and(a, not(b));
}

/**
 * XOR gate: Returns true when inputs are different
 * XOR(a,b) = OR(AND_NOT(a,b), AND_NOT(b,a))
 * This simplifies to: (a AND NOT b) OR (b AND NOT a)
 */
function xor(a, b) {
  return or(and_not(a, b), and_not(b, a));
}

/**
 * XNOR gate: Returns true when inputs are the same (both true or both false)
 * XNOR(a,b) = NOT(XOR(a,b))
 * This means it's the complement of XOR
 * Truth table:
 * a | b | xnor(a,b)
 * 0 | 0 | 1
 * 0 | 1 | 0
 * 1 | 0 | 0
 * 1 | 1 | 1
 */
function xnor(a, b) {
  return not(xor(a, b));
}

/**
 * Half Adder: Adds two single-bit binary numbers
 * Returns an object with sum and carry outputs
 * Truth table:
 * a | b | sum | carry
 * 0 | 0 | 0   | 0
 * 0 | 1 | 1   | 0
 * 1 | 0 | 1   | 0
 * 1 | 1 | 0   | 1
 * 
 * Sum = XOR(a, b) - outputs 1 when inputs are different
 * Carry = AND(a, b) - outputs 1 only when both inputs are 1
 */
function half_adder(a, b) {
  return [
    xor(a, b),  // sum at index 0
    and(a, b)   // carry at index 1
  ];
}

/**
 * Full Adder: Adds three single-bit binary numbers (A, B, and C)
 * Returns an object with sum and carry-out
 * 
 * Truth table:
 * a | b | c | sum | cout
 * 0 | 0 |  0  |  0  |  0
 * 0 | 0 |  1  |  1  |  0
 * 0 | 1 |  0  |  1  |  0
 * 0 | 1 |  1  |  0  |  1
 * 1 | 0 |  0  |  1  |  0
 * 1 | 0 |  1  |  0  |  1
 * 1 | 1 |  0  |  0  |  1
 * 1 | 1 |  1  |  1  |  1
 * 
 * Implementation using two half adders:
 * 1. First half adder adds a and b
 * 2. Second half adder adds the sum from first half adder with c
 * 3. Final sum is the sum from second half adder
 * 4. Carry-out is OR of both carry outputs from the half adders
 */
function full_adder(a, b, c) {
  const first = half_adder(a, b);
  const second = half_adder(first[0], c);
  
  return [
    second[0],                   // sum
    or(first[1], second[1])     // carry
  ];
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { nand, not, and, or, nor, on, and_not, xor, xnor, half_adder, full_adder };
}

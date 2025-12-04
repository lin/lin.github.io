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



// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { nand, not, and, or, nor };
}

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

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { nand, not };
}

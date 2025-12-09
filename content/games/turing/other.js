// Import basic gates from nand.js
const { and, not } = require('./nand.js');

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

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { and_not };
}

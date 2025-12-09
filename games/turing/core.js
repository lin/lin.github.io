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
 * Three-input OR gate: Returns true when at least one of the three inputs is true
 * Implemented using two OR gates: OR3(a,b,c) = OR(OR(a,b), c)
 * Truth table:
 * a | b | c | or3(a,b,c)
 * 0 | 0 | 0 | 0
 * 0 | 0 | 1 | 1
 * 0 | 1 | 0 | 1
 * 0 | 1 | 1 | 1
 * 1 | 0 | 0 | 1
 * 1 | 0 | 1 | 1
 * 1 | 1 | 0 | 1
 * 1 | 1 | 1 | 1
 */
function or3(a, b, c) {
  return or(or(a, b), c);
}

/**
 * At-least-two gate: Returns true when at least two of the four inputs are true
 * Logic: (a AND b) OR (a AND c) OR (a AND d) OR (b AND c) OR (b AND d) OR (c AND d)
 * This checks all possible pairs - if any pair is true, then at least 2 inputs are on
 */
function atLeastTwo(a, b, c, d) {
  const ab = and(a, b);
  const ac = and(a, c);
  const ad = and(a, d);
  const bc = and(b, c);
  const bd = and(b, d);
  const cd = and(c, d);
  
  return or3(or3(ab, ac, ad), or3(bc, bd, cd));
}

/**
 * Four-input XOR gate: Returns true when an odd number of inputs are true
 * This is a parity checker - output is 1 when there's an odd number of 1s
 * Implemented by chaining XOR gates: XOR4(a,b,c,d) = XOR(XOR(XOR(a,b),c),d)
 */
function xor4(a, b, c, d) {
  return xor(xor(xor(a, b), c), d);
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
function halfAdder(a, b) {
  return {
    sum: xor(a, b),
    carry: and(a, b)
  };
}

/**
 * Delay Line: Creates a 1-bit memory element (D flip-flop behavior)
 * Stores a value and outputs it on the next cycle
 * Returns a function that takes input and returns the previous stored value
 * 
 * Usage:
 *   const delay1 = delay();
 *   delay1(1); // returns 0 (initial state)
 *   delay1(0); // returns 1 (previous input)
 *   delay1(1); // returns 0 (previous input)
 * 
 * @param {number} initialValue - Initial stored value (default: 0)
 * @returns {function} A delay function that maintains internal state
 */
function delay(initialValue = 0) {
  let stored = initialValue;
  
  return function(input) {
    const output = stored;
    stored = input;
    return output;
  };
}

/**
 * Odd Ticks: Outputs 1 on odd ticks, 0 on even ticks when input is 1
 * Creates a toggle flip-flop that alternates output each time input is 1
 * Uses a delay line with XOR feedback to create the toggle behavior
 * 
 * Truth table (sequential):
 * tick | input | output
 *   1  |   1   |   1
 *   2  |   1   |   0
 *   3  |   1   |   1
 *   4  |   1   |   0
 * 
 * Circuit: NOT(input) -> XOR with delayed_output -> delay -> NOT -> output
 * The XOR output feeds back through the delay line
 * 
 * @returns {function} A function that takes input and returns toggled output
 */
function oddTicks() {
  const delayLine = delay(0);
  let currentXor = 0;
  
  return function(input) {
    const notInput = not(input); // NOT gate on input
    const previousXor = delayLine(currentXor); // Get previous XOR, store current
    currentXor = xor(notInput, previousXor); // XOR NOT(input) with delayed feedback
    return not(currentXor); // NOT gate on current XOR output
  };
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { nand, not, and, or, nor, on, and_not, xor, or3, atLeastTwo, xor4, halfAdder, delay, oddTicks };
}

/**
 * Checks if 'proofSequence' is a valid proof for 'targetFormula'.
 * @param {string[]} proofSequence - Examples: ["A", "A>B", "B"]
 * @param {string} targetFormula - Example: "B"
 * @returns {boolean} True if valid, False if invalid
 */
function is_proof_of(proofSequence, targetFormula) {
    
    // 1. The final step of the proof MUST be the target formula
    const lastStep = proofSequence[proofSequence.length - 1];
    if (lastStep !== targetFormula) {
        console.log("Fail: The proof does not end with the target formula.");
        return false;
    }

    // 2. We must validate every single step in the chain
    // Every step must be either an AXIOM or a DERIVATION from previous steps.
    for (let i = 0; i < proofSequence.length; i++) {
        const currentStep = proofSequence[i];
        let isValidStep = false;

        // CHECK A: Is it an Axiom?
        // (In our mini-system, let's say "A" and "A>B" are given axioms for simplicity)
        const axioms = ["A", "A>B", "B>C"]; 
        if (axioms.includes(currentStep)) {
            isValidStep = true;
            console.log(`Step ${i} ("${currentStep}") is an Axiom.`);
        }

        // CHECK B: Is it a Logical Consequence? (Modus Ponens)
        // We look at all PREVIOUS steps (j and k) to see if they produce currentStep.
        // We are looking for pattern: Step J is "P", Step K is "P>currentStep"
        if (!isValidStep) {
            for (let j = 0; j < i; j++) {
                for (let k = 0; k < i; k++) {
                    const premise1 = proofSequence[j]; // "P"
                    const premise2 = proofSequence[k]; // "P>Q"
                    
                    // Does premise2 look like "premise1 > currentStep"?
                    if (premise2 === `${premise1}>${currentStep}`) {
                        isValidStep = true;
                        console.log(`Step ${i} ("${currentStep}") derived from steps ${j} and ${k}.`);
                        break;
                    }
                }
                if (isValidStep) break;
            }
        }

        // If a step is neither an axiom nor a derivation, the proof is broken.
        if (!isValidStep) {
            console.log(`Fail: Step ${i} ("${currentStep}") comes from nowhere.`);
            return false;
        }
    }

    console.log("Success: The proof is valid.");
    return true;
}

// We want to prove "B".
// Valid Proof: 
// 1. A (Axiom)
// 2. A>B (Axiom)
// 3. B (Derived from 1 & 2)
const myProof = ["A", "A>B", "B"];
const myTarget = "B";

const result = is_proof_of(myProof, myTarget);
// Output: True
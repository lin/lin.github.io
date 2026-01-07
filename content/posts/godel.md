---
title: "Gödel's Proof using Python"
date: 2025-06-16
math: true
---

<style>
p code {
  font-family: 'Fira Code', 'Courier New', Courier, monospace;
  font-size: 0.95em;
  background-color: #f5f5f5;
  color: #c7254e;
  padding: 0.2em 0.4em;
  border-radius: 4px;
  border: 1px solid #e1e1e8;
  white-space: pre-wrap;
  word-break: break-word;
}
</style>

## Goal of the Task

The statement _7 is a prime number._ is true and we can prove it formally using axioms and inference rules. So is the statemtents like _2209 is a square number._ and _1597 is a Fibonacci number._.

Gödel showed us there a type of number $\theta$ with a  number $q$.

**$q$ is a $\theta$ number**, the same as 7 is a prime number, the statement is true but we can't mechanically prove it from a fixed set of axioms.

The whole idea is to define the $\theta$, and find the $q$.

## Encoding and Decoding

If we accept the fact that programming can be mechanically done, we can encode any text into a number if we can write a python program, like following:

```py
def encode(text):
    return int(text.encode('utf-8').hex(), 16)
```

For example, `encode('1 + 1 = 2')` is `211178044722`.

The reverse action would be:

```py
def decode(number):
    byte_count = (number.bit_length() + 7) // 8
    return number.to_bytes(byte_count, 'big').decode('utf-8')
```

For example, `decode(273861846916120310563305513)` gives us `∀x(x+0=x)`.

### Encoding Statements

The statement `3 is a prime number` can be expressed a little big longer:

$$
\forall x (\forall y(x\times y = 3 \to
((x=1 \wedge y = 3)\vee(x = 3 \wedge y=1))))
$$

And the function call `encode('∀x(∀y(x×y=3→((x=1∧y=3)∨(x=3∧y=1))))')` gives us

`34866652169611433353558731771603039911116713485514898318782071023779878676580404623913947424679492999390325956487465`

### Encoding Formulas

The statement has to return true or false. We can define a class of statements, for example, instead of stating $3$ is a prime number, we can define:

$$
\mathrm{isPrime}(z) = \forall x (\forall y(x\times y = z \to
((x=1 \wedge y = z)\vee(x = z \wedge y=1))))
$$

Replacing $3$ with $z$, we define a formula with one free varible (not associating with $\forall$ or $\exists$ ) that if you plugin a number, it will turn into a normal statement.

Such a formula with $z$ can also be encoded to a unique number:

`2407446714671960661684017502465934769344525857188784286837374252857560807533789189320063964694640296626875411133665922890255481032586519234707017191823576884826025179701560314258408468859228381387370826090594053365359696218701174888257366313`


## Using Python

We can use python to argue the Gödel's proof.

```py
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```

We can encode the function using `inspect`

```py
import inspect
encode(inspect.getsource(is_prime))
```

The the `is_prime` becomes a number

`124563657395992973459423124433160591155887831920030510532410700710229237692588238535348680957649931630333633945462884102906156294002163749547084814365117696989779431735486222753897427000536583957527982637667016997657898994778376451044487325847968755340632532049394079266285850361205303693776904923331508559773080873577668933910894092892082469929610006297683455195730950133502010634`

### Encode and Decode in Python

```py
import inspect

def encode(obj):
    text = inspect.getsource(obj) if callable(obj) else str(obj)
    return int(text.encode('utf-8').hex(), 16)

def decode(number):
    byte_count = (number.bit_length() + 7) // 8
    decoded_text = number.to_bytes(byte_count, 'big').decode('utf-8')
    
    local_scope = {}
    try:
        exec(decoded_text, {}, local_scope)
        for value in local_scope.values():
            if callable(value):
                return value
    except:
        pass
    return decoded_text
```

### An Example

Not every number can be decoded as a valid statement or formula. So the number that can be decoded has to be a valid one.

Similar to argument type checking in programming, the decoded mathematical stuff may not be suitable for function parameters.

The following is valid, which asks whether the number that encodes $\mathrm{isOdd}$ is a prime number or not.

$$
\mathrm{decode}(\mathrm{encode}(\mathrm{isPrime}(x)))(\mathrm{encode}(\mathrm{isOdd}(x)))
$$

In Python way:

```py
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
    
def isOdd(n):
    return n % 2 != 0

decode(encode(isPrime))(encode(isOdd))
```

`encode(idOdd)` is a number `195036360125036444117266947858712823150716611928214970173155623117324581861098629640202`, which is not a prime number.

## The Unprovable Statement

### Checking proofs is a definable formula

Gödel shows that checking a proof for a statement is an algorithm that can be run on a computer.

So if you give me a proof of Goldbach's conjecture, I can directly put it into a computer and wait for the computer to tell me whether this proof is valid or not. This can be decided in bounded time.

That is to say that $\mathrm{isProof}(y, x) $, where $x$ is a number that encodes a statement and $y$ is a number that encodes a proof, can be written as a formula in terms of the normal logical statement in metamathematics.

```py
def isProof(y, x):
    proof_steps = decode(y)
    target_statement = decode(x) 

    known_facts = []
    for step in proof_steps:
        if isAxiom(step):
            known_facts.append(step)
        elif isModusPonens(step, known_facts):
            known_facts.append(step)
        elif isGeneralization(step, known_facts):
            known_facts.append(step)
        elif isSubstitution(step, known_facts):
            known_facts.append(step)
        else:
            return False

    return proof_steps[-1] == target_statement
```

All you need to know here is that $\mathrm{isProof}(y, x)$ is a long sequence of symbols that can be precisely written down, like a python function is a long sequence of symbols that can be precisely written down. And it can be encoded as a single integer number, like a python function can be represented by a binary number.

Why is this important? Let's say, if something you can proof with finite steps mechanically, it seems less interesting, like checking whether 6911 is a prime number or not, it can be tedious, but not too magical. But if you can show that for every rectangle triangles, $a^2 + b^2 = c^2$, this is amazing and magical for the first you see, and find it useful as well. For those Euclidean (plane) geometry statements, every such statement ($a^2 + b^2 = c^2$) is either provable or its negation is provable from the axioms.

But for the Peano Arithmetic, something like Twin Prime Conjecture 

$$
\forall n\;\exists p\;\bigl(n < p \;\wedge\; \mathrm{Prime}(p)\;\wedge\;\mathrm{Prime}(p + 2)\bigr)
$$

Or in its expanded long form:

$$
\forall n\;\exists p\;\exists k\;
\Bigl(
  n + S(k) = p
  \;\wedge\;
  \bigl(2 \le p \;\wedge\;\forall a\,\forall b\,(p = a\cdot b \to (a=1\lor b=1))\bigr)
  \;\wedge\;
  \bigl(2 \le p + S(S(0))\;\wedge\;\forall a\,\forall b\,(p + S(S(0)) = a\cdot b \to (a=1\lor b=1))\bigr)
\Bigr)
$$

is interesting and we can mechanically check its correctness. We hope PA has the potential to proof this from axioms. But PA is not powerful enough.

### A New Class of Numbers

Now we define a class of numbers as:

$$
\mathrm{isNotProvable}(x) = \neg ( \exists y\ (\mathrm{isProof}(y, x) )) \newline
$$

where $x$ is a number that encodes a statement and $y$ is a number that encodes a proof.

Just like prime numbers, there is a class of number called `isNotProvable` numbers. 

```py
def isNotProvable(x):
    encoded_proof = 0
    while True:
        if isProof(encoded_proof, x):
            return False
        encoded_proof += 1
    return True
```

Now let's define another class of numbers:

$$\theta(x) = \mathrm{isNotProvable}(\text {encode} ( \text {decode} (x)(x)))$$

```py
def theta(x):
    return isNotProvable(decode(x)(x))
```

where $x$ is a number that encodes a formula with one free variable.

Let's call this new class of number as `theta` numbers. 

### The Unprovable True Statement

Since,

$$\mathrm{encode}(\theta(x))$$

is a number that encodes a formula with one free variable.

So,

$$\theta (\mathrm{encode}(\theta(x))) $$

is a valid statement which means 

> The number that encodes the formula of `theta` is a `theta` number.

This statement is true but not provable in the system.

That means given `encode`, `decode` and `isProof` are well-defined algorithms, the following programming will run forever without finding a proof.

You can argue `theta(encode(theta))` is true, but you can't find a proof to show its truth.

```python
def theta(x):
    encoded_statement = decode(x)(x)
    encoded_proof = 0
    while True:
        proof_steps = decode(encoded_proof)
        target_statement = decode(encoded_statement)

        is_proof = True
        known_facts = []
        for step in proof_steps:
            if isAxiom(step):
                known_facts.append(step)
            elif isModusPonens(step, known_facts):
                known_facts.append(step)
            elif isGeneralization(step, known_facts):
                known_facts.append(step)
            elif isSubstitution(step, known_facts):
                known_facts.append(step)
            else:
                is_proof = False
                break

        if is_proof and proof_steps[-1] == target_statement:
            return False

        encoded_proof += 1
    return True

theta(encode(theta))
```

`theta(133514517884384239898787351071441124097111921492735779120166497037102969969484145641870968779000743913117166577832441300605181260780458156826842166648906036311545855953400624143099223130979671362232330349195462116495111908299926176876690213743988269562025551505029849931116322610471774599440599052466809914994638128616264127245543742277556021977507387690601591646116904920664374964895430622280258990165822647831534735374775825764717668774815322548663759382929537135373165331282413673109912434355816873642554235743493213458428083144741450614559166854058253673292732126219368015250289351907851553591156047931030796923687091946678222995746274580068349884577231676267887755193312637470654331581715381927725894120266517341885672472699223131412523869898463628985119979813497557062137906319427521415683642938264606635314559946929981154764309265186187376987212461548809479487959230036826677649629847049782516492212509072837639424336974446860661416524437700037240837172557299172089831642823482470576402123156756568583437643751230122283410915735732499486772674993731951835251114990529006558812324827640759494211313474203677350236135774817484841648898477461768056240271400458125152389861276672290135747113761766967941565602892256009391494328571899597840998845146977885801547581630508406673906992080933836417975342457160791232427070563663665768072144747537826733225931590481418393210646717694437937536277163304723338782837812849085772857986585940684644856264604633877015794481977874623898180982175899053246939284650556002235506619338102747926424895515978567895419062240591159923180093272089256454200192306473204463868354314205177845176880692765007363508385032962329550838047447560659739008791102423078969725972309991404883242214550693475383626971185558781900198462266536510958909257182616206833707553694858593909753075207371560717581490781245204238763472182304675696381723036460536964977581989223380330019259771436851588334649934493086698065692007130495915799570211080575965816074)`

If you run this line in a python program, it will run forever without halting.

### The Proof

$$\theta(\text{encode}(\theta(x)))$$ 

is the same as:

$$\mathrm{isNotProvable}(\text{encode}(\text{decode}(\text{encode}(\theta(x)))(\text{encode}(\theta(x)))))$$

Since $\text{decode}(\text{encode}(\theta(x)))$ means $\theta(x)$, so

$$
\theta(\text{encode}(\theta(x))) \leftrightarrow \mathrm{isNotProvable}(\text{encode}(\theta(\text{encode}(\theta(x)))))
$$

That is:

$$
\theta(\text{encode}(\theta(x))) \leftrightarrow  \mathrm{isNotProvable}(\text{encode}(\theta(\text{encode}(\theta(x)))))
$$

If $\theta(\text{encode}(\theta(x)))$ returns `false`, that implies $\mathrm{isNotProvable}(\text{encode}(\theta(\text{encode}(\theta(x)))))$ returns `false`, which says it is provable, but this is a false statement. That means we have a contradiction here.

So if the system can't contain contradiction, $\theta(\text{encode}(\theta(x)))$ has to return `true`, that implies $\mathrm{isNotProvable}(\text{encode}(\theta(\text{encode}(\theta(x)))))$, which says it is not provable. There is a true statement you can't prove.

## Reinvent the Wheel

Since we have been familiar with those functions, let us make some convinient shortcuts:

$$
\begin{aligned}
\phi &= \mathrm{isNotProvable} \newline
\epsilon &= \mathrm{encode} \newline
\delta &= \mathrm{decode}
\end{aligned}
$$

For example the statement $\theta(\text{encode}(\theta(x)))$ can be expanded as:

$$
\phi(\epsilon (\delta(x)(x)))(\epsilon(\phi(\epsilon (\delta(x)(x)))))
$$

### The Starting Point

The liar paradox which states "this statement is false" is easily to come to mind. If we borrow this idea, we can find out our goal is to find a statement that means:

> This statement is not provable.

$$ G \leftrightarrow \phi(\epsilon(G)) $$

And $G$ can be defined as a combination of our three well-defined functions $\phi$, $\epsilon$ and $\delta$.

### First Heuristic Trial

Apparently, $\phi$ is a great choice, signaling something like `Not provable is not provable`. At the same time, we should make one free variable formula becomes a statement. The goto choice for the parameter apparently should be self-referenced to make it possible to push the searching area by using more tools since we only have very limited definations here. That means:

$$ G = \phi(\epsilon(\phi)) $$

but $\phi$ is a formula with one free variable, and it only accepts numbers encodes statements. Since $\epsilon(\phi)$ is a number encodes a formula with one free variable not a statement, this choice is invalid. But it gives us a hint that maybe we should use a formula with one free variable and this variable requires a number encodes a formula with one free variable.

### Find the Right Relation

Let's say $\rho$, and it might in a form like $\rho(x) = f(\delta(x), x)$. And also:

$$ \rho(\epsilon(\rho(x))) \leftrightarrow \phi(\epsilon(\rho(\epsilon(\rho(x))))) $$

If we want to find $\rho(x)$, there are many hints to solve this:

1. we should make first $\rho$ in the right hand side disappear.

2. we should introduce $\epsilon(\rho(x))$, like in $f(\sin x) = \cos 2x$, we should introduce $\sin x$

3. we should introdue $\delta(x)$, that might indicate $\rho$ accepts a number encodes a formula with one free variable.

We now should replace the first $\rho$ as $\delta(\epsilon(\rho(x)))$, it becomes:

$$ \rho(\epsilon(\rho(x))) \leftrightarrow \phi(\epsilon(\delta(\epsilon(\rho(x)))(\epsilon(\rho(x))))) $$

Noticing $\epsilon(\rho(x))$ is a number we plug in, so we find a suitable $\rho$: 

$$ \rho(x) =  \phi(\epsilon(\delta(x)(x)))$$

with the statement $G$ as:

$$ G =  \rho(\epsilon(\rho(x))) $$

## Gödel's Paper

This article is an explanation for the following paragraphs in the Gödel's 1931 paper.

![](../img/godel-1.png)

The $[\text{R}(x); y]$ is defined as:

$$
[\text{R}(x); y]:=\text{decode}(x)(y)
$$

And $[\text{R}(x); x]$ is  

$$
[\text{R}(x); x]= \text{decode}(x)(x)
$$

And $\overline {\text{Bew}}$ is $\text{isNotProvable}$, and $\text {S} (x)$ is same as above $\theta (x)$:

$$
\text{S}(x) := \text{isNotProvable}(\text{encode}([\text{R}(x); x])) \newline
$$

$$
\text{S}(x) = \text{isNotProvable}(\text{encode}(\text{decode}(x)(x)))
$$

![](../img/godel-2.png)

And $\text K$ means when $n \in \text{K}$, $\text{S}(n)$ is true. The number $q$ is the Gödel number:

$$
q := \text{encode}(\text{S}(x))
$$

The unprovable statement is:

$$
\begin{aligned}
[\text{R}(q); q] &= \text{decode}(q)(q) \newline
& = \text{decode}(\text{encode}(\text{S}(x)))(\text{encode}(\text{S}(x))) \newline
& = \text{S}(\text{encode}(\text{S}(x)))
\end{aligned}
$$

It is easy to show:

$$
[\text{R}(q); q]  = \text{isNotProvable}(\text{encode}([\text{R}(q); q]))
$$
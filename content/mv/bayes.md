## Bayes

## $P(B\mid A)$

The equation $E=mc^2$ may be the most celebrated in science, but its practical impact on our everyday lives is limited it dazzles more than it delivers. Even Feynman’s championing of atomic theory, though fundamentally important, doesn’t always translate into direct, universal benefits. In contrast, the principle of Bayesian inference expressed as

$$
P(B\mid A)
$$

the probability of $B$ given that $A$ has occurred provides a versatile, widely applicable tool for updating beliefs and guiding decisions in countless real‑world situations.

The deductive world of logic and computation only means all $P(B\mid A)$ is always near 1 or near 0.

<img src='/img/awb.svg' height="100">

You can also think of the inference as standing on one node, with a probability to jump to another node.

## Naive Frequency Updates

In the above expression, $P(B\mid A)$ denotes the conditional probability of $B$ given $A$, which, in the absence of full information, can be approximated by the empirical frequency:

$$
\frac{\text{count}(A\cap B)}{\text{count}(A)}
$$

The frequency is a fact to summarize what we are seeing. When predicting a new observation, however, we instead rely on a parameterized hypothesis distribution.

The position order is important in this senario, given "Name: Jordan", you may think about "Michael", but given "Name: Michael", your response will not as high as the previous one. 

This naive frequency is simply stating a fact or a computation, it doesn't provide a high level generating machine for future instance, to do so we need an assumption of data distribution so we could predict next instance based on what we have at hand. This naive frequency corresponds to doing inference without a prior, or equivalently, a flat prior.

At first, the brain might count co-occurrences (a simple Hebbian rule: “what fires together wires together”). Over time, the brain adjusts precision, forms structured priors, and learns latent causes. So frequency counts could be the brain’s initial or fast path to an approximation of likelihoods. Later, more abstract layers build causal models and priors ,  and inference becomes more Bayesian.

Hebbian Co-Occurrence Counting, basic rule Whenever two neurons fire together, the connection between them strengthens “a little bit.” Over thousands of such joint firings, only those feature combinations that recur reliably build up strong connections. Tallying frequency Implicitly your brain is keeping a running count of how often feature A and feature B appear together. If they co-occur far more than chance, that joint pattern becomes a candidate latent cause. Synaptic Plasticity and Thresholds Incremental changes Each co-occurrence yields a tiny synaptic weight update. Repeated trials accumulate these updates. Potentiation threshold Only when the total weight crosses a biological threshold does that neuron ensemble start firing on its own to signal the new pattern. That guards against random coincidences being encoded.


## Bayes' Theorem

[Bayes’ Theorem](./notes/bayes) provides a framework for encoding information in a normalized form, which reduces the effort required for updating and managing data. For example, we might categorize and update records by gender, an easily identifiable feature, while handling other attributes through more systematic bookkeeping. This is analogous to choosing a convenient basis (for instance, projecting onto easy‑to‑compute eigenvectors) in linear algebra or adopting a common “lingua franca” for data‑management tasks.

In both our brains and pattern‑recognition models, incoming information is compressed by an internal model that keeps track of what we have observed, extracts regularities, and filters out redundant details. By centralizing data management in this way, Bayes’ Theorem becomes the natural mechanism for updating our beliefs or models, reflecting a fundamental aspect of how we interact with reality.

$$
P(H \mid D) = \frac{P(D \mid H) \cdot P(H)}{P(D)}
$$

Why prediction is important? Wherever direct measurement is impossible, impractical or prohibitively expensive whether because the sample would be destroyed, there are too few examples, the cost per measurement is too high, the environment is inaccessible or the time horizon is too long organizations turn to predictive modeling. By training on cheaper, proxy data and learning the hidden relationships, you gain actionable insight without ever touching or wasting the precious thing you wish to know.

## Class Level Observations

> All men are mortal. Socrates is a man, therefore, Socrates is mortal.

"All men are mortal" is a class property. "Socrates" is a class instance. "Socrates is mortal" means a class instance has to follow class properties.

Whenever a class A almost surely has property B in context H, any instance R of that class will also almost surely have property B in the same context.

$$
\bigl(R\subseteq A\\;\wedge\\;P(B\mid A,H)\ge1-\varepsilon\bigr)\\;\Longrightarrow\\;P(B\mid R,H)\ge1-\varepsilon.
$$

This is based on the assumption that additional information provided by R gives you no extra information about whether property B holds. 

$$
P\bigl(B \mid A,\\,H,\\,R\bigr)
\\;=\\;
P\bigl(B \mid A,\\,H\bigr)
$$

When we observe the reality, for each instance data we collect, we also gather the class level connections. When we think about instant-level priors, its class-level priors, which might be observed by a lot of times, should also be considered so that we are not losing too much the information gain by previous observations.

### Physics provides strong priors

That is why a more knowledgable person can have generally better conclusions with high class-level priors.

### The Triumph of Idiots

Class‑level observations can give us strong priors and thus high confidence but intuitively lumping data into broad categories doesn’t always lead to correct conclusions. Racism is a prime example: people reinforce the false belief that someone’s birthplace is the decisive cause of negative traits or outcomes.

### Russell’s turkey is doing its best

When the turkey’s world has only two outcomes “fed” or “not fed” each morning, and it starts with a uniform Beta (1, 1) prior, the Bayesian predictive probability of breakfast tomorrow after $k$ feedings in $n$ days is

$$
P(\text{fed tomorrow}\mid k,n)=\frac{k+1}{n+2}.
$$

This Beta–binomial formula is the optimal forecast under those assumptions.
For instance, after 100 straight days of being fed ($k=n=100$) the turkey believes

$$
P(\text{fed tomorrow})=\frac{101}{102}\approx 0.99,
$$

i.e., a 99 % chance of one more meal.
Absent any other evidence no knowledge of Thanksgiving, butcher‑shop trucks, or class‑level information this $(k+1)/(n+2)$ rule is the best the turkey can do.

### Connection to the *p‑value* and the weight of reality

A frequentist *p‑value* answers one narrowly defined question:

$$
p = P\bigl(\text{data at least this surprising}\mid H_0\bigr),
$$

the probability of seeing evidence as extreme as ours **if** the null hypothesis $H_0$ holds exactly.

When our current sample is tiny and virtually every prior observation in everyday life has agreed with $H_0$, this number can **look** like a Bayesian update in which $H_0$ carries an enormous prior weight: it merely flags that the new result would be rare under the long‑standing pattern.

But the practical question is different: Given all we already know about the world, is the alternative $H_1$ now more credible than $H_0$?

To answer that, a Bayesian compares **posterior odds**

$$
\frac{P(H_1 \mid \text{data})}{P(H_0 \mid \text{data})}
=\\;
\overset{\text{likelihood ratio}}
       {\frac{P(\text{data}\mid H_1)}{P(\text{data}\mid H_0)}}
\\;\times\\;
\overset{\text{prior odds}}
       {\frac{P(H_1)}{P(H_0)}}.
$$


* **Likelihood ratio**: How well each hypothesis explains the *limited* data we have just collected.
* **Prior odds**: The vast “reality archive” of earlier observations, most of which have already favored $H_0$.

A low p‑value signals that the new data are surprising under $H_0$; it says nothing about how plausible $H_1$ is once those towering prior odds are taken into account. Only by multiplying surprise (the likelihood ratio) by these priors do we learn whether our handful of fresh observations truly dents or merely ripples the immense body of evidence built up from everyday reality.

In short, **p‑values measure surprise, not believability**. Deciding whether $H_1$ “really works” demands folding that surprise into the giant pool of experience that has, so far, mostly vindicated $H_0$.


### Rooster's Crow and Sunrise

$$
P\bigl(\text{sunrise}\mid \text{rooster crow},\\,\text{dawn}\bigr) = 1
$$

$$
\forall t.\\, P\bigl(\text{sunrise}\mid \text{rooster crow},\\,t \bigr) = 1
$$


## Lexemes

> Lexemes are the currency of intelligence.

Lexeme Mining as the Core of Intelligence Compression and generalization By discovering the hidden causes that explain clusters of sensory data, we collapse thousands of details into a handful of high-utility units. Those units drive rapid prediction, reasoning and transfer across domains.

In statistics we often work with continuous streams of numbers, but in everyday life it can be far more effective to think in discrete units (lexemes) as our atomic building blocks. When we learn or fit a model, we update its parameters to reduce prediction errors, for example by computing

$$
P(\text{model}\mid \text{signal}, \text{response}, \text{context})
$$

after observing new data. A lexeme plays the same role as a feature: it links an observable cue (signal) to a likely outcome (response). We can formalize this as

$$
P(\text{response}\mid \text{signal}, \text{context}, \text{model})
$$

Whenever a particular response has very high probability given its signal and context, we treat that signal–response pair as a lexeme. In practice lexemes sharpen our predictions, reduce ambiguity, and boost our chances of success, while remaining simple to manage. Examples include:

1. At a road intersection (signal), predicting which direction you are most likely to turn (response).
2. Faced with a Japanese word (signal), selecting its English equivalent (response).
3. In a Zelda dungeon room (signal), choosing which door to open next (response).
4. Encountering the term “entropy” in a textbook (signal), activating related concepts or formulas (response).

By organizing knowledge into lexemes, we convert a complex, continuous world into a set of reliable, discrete predictions that are easy to store, retrieve, and apply. Latent causes as the “glue” of perception The world’s raw data are high‑dimensional and noisy. Our brains seek hidden causes that explain clusters of correlated inputs， these causes become lexemes. By representing a whole bundle of sensory features with one latent‑cause lexeme, we compress complexity into a manageable form.

Initial clustering Early sensory areas and mid-level cortices flag a grouping of features that co-occur more often than chance—a “lexeme candidate.” At this stage the representation is coarse: you know “there’s something here,” but not yet all its defining details. Precision weighting In predictive-processing terms, that lexeme candidate carries high surprise (prediction error), so the brain boosts the precision (synaptic gain) on the relevant input channels. Neuromodulators like acetylcholine and noradrenaline increase the signal-to-noise ratio for those features, effectively turning the “spotlight of attention” onto them. A High-Resolution Lexeme Tighter cluster After repeated, precision-weighted exposures, the lexeme’s neural assembly responds only to the truly diagnostic features—noise and irrelevant variations get filtered out. Energy efficiency Once refined, that compact assembly can fire sparsely and reliably whenever the lexeme appears, slashing overall spike counts.


The creation of a new lexeme is just the brain expanding its generative model to explain a cluster of sensory regularities that no existing latent cause can account for. The reason it works is precisely that, once you introduce the right new cause, the myriad features you’ve been observing become conditionally independent of each other and of the rest of the world conditional only on that cause.

Once $z_{\rm new}$ is in place, all those features become independent of one another conditional on $z_{\rm new}$. In graphical‑model terms, the Markov blanket of $z_{\rm new}$ “insulates” its children (the sensory feature nodes) from external states. That factorization is precisely what makes the world more compressible and predictions more accurate.

Forming new concepts is essentially the brain’s way of compressing rich sensory data into compact, useful summaries. In probabilistic and information‐theoretic terms, each concept acts as a latent variable that explains away many degrees of freedom in the raw inputs, thereby reducing entropy and making inference tractable.

Limited exposures let you pick up the “low‑hanging fruit.” As you accumulate more data, rarer co‑occurrences (second‑order correlations) get sampled enough times so their prediction errors can drive synaptic updates. Thus the generative map $g$ grows richer, encoding subtler patterns that only emerge over many exposures.More exposures leads to better understaning, better retentions and better emotions.

As in learning, we may find knowledge that is less dependent to existing knowledge, makes us hard to attach to a scheme easily, which give you a sense of conceptual leap, like in quantum mechanics.

In the brain, model updating happens in parallel with inference:

1. **Exposure‑driven strengthening**
   Every repetition of a given signal–response pairing incrementally potentiates the synaptic connections that encode that association.

2. **Feedback‑driven reinforcement**
   When a response produces strong retention, through reward, surprise, or other salient feedback, the corresponding signal–response link is further consolidated.

3. **Decay‑driven weakening**
   In the absence of repeated exposure or feedback, synaptic connections gradually depotentiate, causing rarely used associations to weaken or be pruned over time.

> Bayesian inference is leading the way towards efficient, goal‑directed reasoning.

In feature extraction, Bayesian inference gives us a principled way to compress raw observations into a compact, informative representation by updating our model’s parameters to best explain the data.  Then, when computing features for prediction, Bayesian inference steers us toward the most relevant variables and highest‑reward outcomes, guiding decisions that solve the task at hand as effectively as possible.


### Benefits of Lexemes Perspective

Every neural spike has a metabolic cost. Activating a single lexeme node instead of dozens of low‑level feature detectors saves energy and reduces overlap between representations. This sparse code makes perception faster and more robust.

1. **Productivity gains depend primarily on the lexemes we master**
   Mastering core signal–response units lets you spot and apply the right pattern instantly. Every time you recognize a familiar lexeme, you bypass hours of problem solving or analysis, so your output grows dramatically with each new lexeme you master.

2. **Educational success hinges on both the quantity and the quality of one’s lexemes**
   Having more lexemes broadens the range of problems you can tackle, while high‑quality lexemes (those that capture patterns accurately and precisely) ensure you solve them correctly. Students who build a rich, precise lexicon of concepts learn faster and perform better on varied tasks.

3. **Individuals are limited by the size of their vocabulary**
   Your mental “toolbox” can only hold as many concepts as you’ve internalized. If you lack the lexeme for a key idea, you literally cannot think about it or solve problems that depend on it. Expanding your lexicon directly expands your thinking capacity.

4. **Poor judgments generate low‑resolution lexemes, which undermine shared understanding**
   When you form vague or overly broad lexemes, say, lumping many distinct causes under one label, you lose critical distinctions. Communication breaks down because others interpret that lexeme differently, and decisions based on it become error‑prone.

5. **We can predict how long it takes students to internalize a lexeme fluently**
   Each lexeme has a characteristic “mining time” (number of exposures, practice trials, and feedback cycles needed). By measuring these factors, teachers can estimate how many hours or sessions a student will need to reach automaticity with each concept.

6. **Altering core lexemes within a culture can bring about profound social change**
   Shifting the lexical roots of public discourse, for example redefining “success” to include community well‑being, or “progress” to include sustainability, reshapes how people think and act. New cultural lexemes propagate through education, media, and policy, transforming behaviors at scale.

7. **Academia’s role is to discover and refine lexemes**
   Researchers isolate fundamental patterns, test their limits, and formalize them into definitions, theorems, or models. By subjecting each lexeme to peer review and replication, academia ensures that the concepts we teach and use are robust and broadly applicable.

8. **The time required to “mine” a lexeme correlates with its level of abstraction**
   Simple, concrete patterns (like “object permanence” in child psychology) are learned quickly. Deeply abstract ideas (like “entropy” in thermodynamics) require far more examples, derivations, and applications before they become stable lexemes in your mind.

9. **Consciously improving key lexemes in everyday life leads to better decision making**
   By identifying where your mental models rely on weak or outdated lexemes, say, “success = salary” or “intelligence = test score”, you can replace them with richer, evidence‑based concepts. That targeted lexeme upgrade sharpens your judgments and guides wiser choices.

10. **Adult vocabulary size doesn’t grow much with age**
    After a certain point, spontaneous lexeme acquisition slows. Without deliberate practice, adults rarely add new high‑utility concepts to their mental toolkit, which limits their ability to learn new skills or adapt to unfamiliar challenges.

11. **Adults often cling to erroneous beliefs and become less flexible in assimilating new ideas**
    Established lexemes create strong priors. When a new fact conflicts with an existing lexeme, people discount or ignore it rather than update their mental model. That rigidity makes it hard to replace low‑resolution lexemes with more accurate ones.

12. **Rapidly reducing the entropy of a subject’s core concepts can dramatically boost learners’ competence and ease**
    By front‑loading the handful of lexemes that explain most canonical examples, you collapse uncertainty and confusion. Learners quickly see how new material fits into the compressed framework, lowering barriers and accelerating mastery.

13. **The lexeme perspective is powerful because it applies across all levels of knowledge and contexts**
    Whether you’re decoding a poem, solving a differential equation, diagnosing a medical condition, or negotiating a contract, the same lexeme logic, identify the signal, apply the relation, yield the response, underlies expert performance. This universality makes the approach a versatile lens on any domain.


### Benefits of Ample Exposures

1. Fluency and Skill Mastery
1. Comfort and Confidence
1. Increased Interest and Motivation
1. Deep Features Extractions and Understanding
1. Closing Learning Gaps

Each time students retrieve or review the material, it strengthens the neural pathways associated with that knowledge, making future recall faster and more automatic. When we repeat an action or recall, our brain’s neural network becomes more efficient (often by strengthening connections and even adding myelin around neurons), which makes the skill faster and easier to perform

Repetition builds fluency and automaticity: With enough practice, skills that once took effort can become second nature. Think of how a new driver has to concentrate on every move, but an experienced driver operates the car almost on autopilot. In learning, the same happens – repetition can turn slow, halting efforts into smooth, fluent performance. For example, practicing mental math or vocabulary frequently will eventually let students perform calculations or recall words without having to think through each step.

Importantly, seeing material repeatedly also makes it feel easier. New topics can be intimidating, but each subsequent exposure tends to increase a student’s comfort level. The exposure effect, which is the tendency for people to develop a preference for things simply because they’ve become familiar with them. This familiarity can lower anxiety, making students more willing to engage with the material instead of avoiding it.

High utility lexemes are hard to mine, it is used everday but can't be recognized as a universal tool these are the exact reason why such lexemes are hard to notice.

2. Fluent Computation
3. Fluent Abstract Computation 

Especially Active Exposures

1. increase pragmatic gain
2. attention allocation

### Benefits of Key Lexemes Fluency

> Less is more.

> Exposure matters most.

> Motivation is king.

Most domains follow a Pareto‑like distribution: roughly 20 percent of concepts account for 80 percent of the results. By zeroing in on that vital 20 percent, the core lexemes you capture the backbone of the subject. Everything else becomes a variation on those fundamentals. When you’ve internalized the key lexemes, your brain can automatically bundle new information into those existing “chunks.” Instead of processing every detail from scratch, you slot new data into familiar patterns. That slashes cognitive load and makes learning novel material feel intuitive. Think of those lexemes as pillars in a building. Once they are in place and sturdy, you can add floors and rooms without worrying about the foundation. In practice, that means advanced topics become accessible sooner, because they rest on concepts you already own. They provide exponential returns on practice.

By mastering a small set of core ideas up front, you can remove the heaviest roadblocks in learning and make the entire process more rewarding, smoother, and long‑lasting. Focusing on a few pivotal concepts lets you ignore peripheral details. You free up working memory to connect new information directly to those anchors, rather than juggling dozens of loosely related facts. Early wins from drilling high‑impact patterns build confidence. As those lexemes become second nature, you navigate more complex material without hesitation, turning once‑effortful steps into instinctive actions. Each core concept generalizes across many problems. Instead of hundreds of specialized exercises, a handful of signal–response drills covers most of the terrain, slashing practice time by orders of magnitude.

Signal–response reflex, a high‑confidence lexeme becomes an almost automatic prediction: when you see the signal, the response springs to mind without effort. Over time, these reactions require less attention and become second nature, just like recognizing a familiar word or spotting a chess pattern. Automatic retrieval frees up working memory to focus on new or more complex aspects of a problem, accelerating skill mastery.

Limiting hypothesis space, every time you introduce a lexeme you narrow down the plausible interpretations of incoming data. Instead of considering dozens of possible responses, you only consider the handful linked to your existing lexemes. Reducing ambiguity, lexemes act like labels or “tags” on data streams, guiding your attention to the most relevant features and pruning irrelevant details. Strong core ideas serve as bridges between domains. You spot analogies more quickly, adapt strategies to novel problems, and turn rote practice into inventive problem solving.

They are worth to be Decay‑resistant nodes, high‑utility lexemes, being reinforced frequently through exposure and feedback, become more resistant to forgetting. High‑leverage concepts, reinforced through repeated exposure and feedback, become decay‑resistant. When you make an error, you can update that one lexeme without upsetting other parts of your model, preserving overall coherence

On the contrary, textbooks often present every theorem, every corollary, every special case, all at once. You spend hours slogging through notation and side‑topics rather than mastering the handful of core patterns that actually power 80 percent of solutions. Important signal–response pairings remain buried in a sea of low‑utility examples.

Swamped by extraneous details and definitions you rarely use, your working memory gets taxed. Excessive “extraneous load” leaves little room to integrate or deeply encode the few truly valuable concepts. You may remember isolated facts but can’t fluently retrieve the core ideas when you really need them. By treating every subtopic as equally important, you waste time on low‑impact details (rarely needed lemmas or niche applications) and overlook the 20 percent of concepts that unlock 80 percent of progress.

In many real‑world classrooms both teachers and students fall into a “more haste, less speed” trap: eager to move on, they assume that mastering key concepts requires little time and effort. This well‑intentioned zeal often backfires. Illusion of simplicity: A concept that seems intuitive to an expert can mask subtle pitfalls for novices. Skimming it gives students only a superficial grasp. Racing through many topics floods working memory. Instead of integrating each concept, students juggle half‑learned ideas, increasing anxiety. Frequent failure on more advanced material, because the fundamentals weren’t solid, erodes confidence, making learning feel punishing rather than rewarding.

Textbook‑style learning buries you in definitions, proofs, side‑cases, footnotes. Your working memory juggles dozens of loosely related facts at once. When you focus on a few core lexemes, everything else becomes “noise” you can ignore. You free up mental bandwidth to integrate new examples instead of wrestling with peripheral detail. Rather than slogging through every exercise in the chapter, you drill only the signal–response drills that yield the greatest payoff.

Grading yourself on broad content leads to frequent failure and discouragement. Rapid wins from mastering a few lexemes build confidence. You stay motivated because every practice session feels productive, not punishing.

Any feature you hope to learn has variability and noise. You need enough samples so that the consistent pattern stands out above the noise. Only once the brain’s estimate crosses a stability threshold does it commit resources to encode that feature as a lasting lexeme. Neurophysiologically, synapses strengthen in proportion to repeated co‑activations. If a pattern only fires once or twice, the weight change is too small and quickly decays. Reaching a minimum number of repetitions is necessary for long‑term potentiatio, otherwise the “candidate” feature never survives the decay‑driven weakening phase.

Simple first‑order features emerge with relatively few examples. But subtler, second‑order correlations require many more observations before their prediction error signal is strong enough to drive synaptic updates. If you rush past these early exposures, you never sample enough to extract those richer features.

## Features

Less precise

### shared features

## Bias Prone Machine

Emotional salience, events that surprise or frighten you (a dramatic headline, a frightening story) generate large prediction-error spikes. Hebbian plasticity then over-strengthens any co-active connections, even if the underlying pattern isn’t generally valid.

Repetition without feedback, hearing the same claim repeatedly (on social media or in conversation) boosts its lexeme strength through sheer frequency, even if it’s false. Without corrective signals, the wrong pattern becomes your go-to “explanation.”
import React, { useState, useEffect, useRef, useCallback } from 'react';

// --- ICONS (Inline to avoid external dependency errors) ---

const PlayIcon = ({ size = 24, className = "" }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}>
    <polygon points="5 3 19 12 5 21 5 3"></polygon>
  </svg>
);

const PauseIcon = ({ size = 24, className = "" }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}>
    <rect x="6" y="4" width="4" height="16"></rect>
    <rect x="14" y="4" width="4" height="16"></rect>
  </svg>
);

const RefreshIcon = ({ size = 24, className = "" }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}>
    <path d="M23 4v6h-6"></path>
    <path d="M1 20v-6h6"></path>
    <path d="M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"></path>
  </svg>
);

const StepForwardIcon = ({ size = 24, className = "" }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}>
    <polygon points="5 4 15 12 5 20 5 4"></polygon>
    <line x1="19" y1="5" x2="19" y2="19"></line>
  </svg>
);

const SettingsIcon = ({ size = 24, className = "" }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}>
    <circle cx="12" cy="12" r="3"></circle>
    <path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"></path>
  </svg>
);

const NetworkIcon = ({ size = 24, className = "" }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}>
    <circle cx="18" cy="5" r="3"></circle>
    <circle cx="6" cy="12" r="3"></circle>
    <circle cx="18" cy="19" r="3"></circle>
    <line x1="8.59" y1="13.51" x2="15.42" y2="17.49"></line>
    <line x1="15.41" y1="6.51" x2="8.59" y2="10.49"></line>
  </svg>
);

const InfoIcon = ({ size = 24, className = "" }) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className={className}>
    <circle cx="12" cy="12" r="10"></circle>
    <line x1="12" y1="16" x2="12" y2="12"></line>
    <line x1="12" y1="8" x2="12.01" y2="8"></line>
  </svg>
);

// --- MATH UTILITIES ---

// 1. Generate random number normal distribution (Box-Muller transform)
const randn = () => {
  let u = 0, v = 0;
  while (u === 0) u = Math.random();
  while (v === 0) v = Math.random();
  return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v);
};

// 2. Multivariate Gaussian PDF
// Calculates probability density of point x given mean mu and covariance sigma
const gaussianPdf = (point, mean, cov) => {
  const n = 2; // 2 dimensions
  const det = cov[0][0] * cov[1][1] - cov[0][1] * cov[1][0];
  
  // Prevent division by zero or negative determinant issues
  if (det <= 1e-10) return 1e-10;

  const invCov = [
    [cov[1][1] / det, -cov[0][1] / det],
    [-cov[1][0] / det, cov[0][0] / det]
  ];

  const diff = [point.x - mean.x, point.y - mean.y];

  // Mahalanobis distance squared
  const mahalanobis = 
    (diff[0] * invCov[0][0] + diff[1] * invCov[1][0]) * diff[0] +
    (diff[0] * invCov[0][1] + diff[1] * invCov[1][1]) * diff[1];

  const normalization = 1 / (Math.pow(2 * Math.PI, n / 2) * Math.sqrt(det));
  
  return normalization * Math.exp(-0.5 * mahalanobis);
};

// --- COMPONENT ---

const GMMVisualizer = () => {
  // Constants
  const WIDTH = 600;
  const HEIGHT = 400;
  const K = 3; // Number of clusters
  const COLORS = ['#ef4444', '#3b82f6', '#22c55e', '#eab308']; // Tailwind red, blue, green, yellow

  // State
  const [points, setPoints] = useState([]);
  const [clusters, setClusters] = useState([]);
  const [iteration, setIteration] = useState(0);
  const [isRunning, setIsRunning] = useState(false);
  const [showConfidence, setShowConfidence] = useState(true);
  const [showVectors, setShowVectors] = useState(false); // New State for Vectors
  const [converged, setConverged] = useState(false);
  const canvasRef = useRef(null);

  // --- INITIALIZATION LOGIC ---

  const generateData = useCallback(() => {
    const newPoints = [];
    const centers = [
      { x: WIDTH * 0.3, y: HEIGHT * 0.3 },
      { x: WIDTH * 0.7, y: HEIGHT * 0.3 },
      { x: WIDTH * 0.5, y: HEIGHT * 0.75 }
    ];

    // Create 3 blobs with different spreads/shapes
    centers.forEach((center, idx) => {
      // Random spread parameters
      const sx = 20 + Math.random() * 30;
      const sy = 20 + Math.random() * 30;
      // Random rotation
      const angle = (Math.random() * Math.PI) / 2;
      const cos = Math.cos(angle);
      const sin = Math.sin(angle);

      for (let i = 0; i < 100; i++) {
        const rx = randn() * sx;
        const ry = randn() * sy;
        
        // Rotate and translate
        const x = center.x + rx * cos - ry * sin;
        const y = center.y + rx * sin + ry * cos;

        newPoints.push({ x, y, probabilities: Array(K).fill(1/K) });
      }
    });

    setPoints(newPoints);
    initializeClusters(newPoints);
    setIteration(0);
    setConverged(false);
    setIsRunning(false);
  }, []);

  const initializeClusters = (currentPoints) => {
    // Initialize with random points from the dataset (Forgy method equivalent)
    const newClusters = [];
    for (let i = 0; i < K; i++) {
      const randomPoint = currentPoints[Math.floor(Math.random() * currentPoints.length)];
      newClusters.push({
        mean: { x: randomPoint.x + randn(), y: randomPoint.y + randn() },
        // Initialize covariance as somewhat spherical but large
        cov: [[2500, 0], [0, 2500]], 
        pi: 1 / K, // Uniform weights initially
        color: COLORS[i]
      });
    }
    setClusters(newClusters);
  };

  // --- EM ALGORITHM STEPS ---

  const runEMStep = () => {
    if (points.length === 0) return;

    // 1. EXPECTATION STEP (E-Step)
    // Calculate responsibilities: P(cluster k | point i)
    let newPoints = points.map(p => {
      const likelihoods = clusters.map(c => c.pi * gaussianPdf(p, c.mean, c.cov));
      const sumLikelihood = likelihoods.reduce((a, b) => a + b, 0);
      
      // Normalize to get probabilities (gamma)
      const probabilities = likelihoods.map(l => (sumLikelihood > 0 ? l / sumLikelihood : 1/K));
      return { ...p, probabilities };
    });

    // 2. MAXIMIZATION STEP (M-Step)
    // Re-estimate parameters based on probabilistic assignment
    let maxShift = 0;
    const newClusters = clusters.map((cluster, k) => {
      // Calculate N_k (effective number of points in cluster k)
      let Nk = 0;
      let sumX = 0;
      let sumY = 0;

      newPoints.forEach(p => {
        const gamma = p.probabilities[k];
        Nk += gamma;
        sumX += gamma * p.x;
        sumY += gamma * p.y;
      });

      // Avoid numerical instability if cluster dies out
      if (Nk < 1) return cluster;

      // New Mean
      const newMean = { x: sumX / Nk, y: sumY / Nk };

      // New Covariance
      let sumCovXX = 0, sumCovXY = 0, sumCovYY = 0;
      newPoints.forEach(p => {
        const gamma = p.probabilities[k];
        const dx = p.x - newMean.x;
        const dy = p.y - newMean.y;
        sumCovXX += gamma * dx * dx;
        sumCovXY += gamma * dx * dy;
        sumCovYY += gamma * dy * dy;
      });

      // Add small epsilon to diagonal for numerical stability (regularization)
      const newCov = [
        [(sumCovXX / Nk) + 1e-6, sumCovXY / Nk],
        [sumCovXY / Nk, (sumCovYY / Nk) + 1e-6]
      ];

      // New Mixing Coefficient
      const newPi = Nk / newPoints.length;

      // Check convergence shift
      const dist = Math.sqrt(Math.pow(newMean.x - cluster.mean.x, 2) + Math.pow(newMean.y - cluster.mean.y, 2));
      if (dist > maxShift) maxShift = dist;

      return {
        ...cluster,
        mean: newMean,
        cov: newCov,
        pi: newPi
      };
    });

    setPoints(newPoints);
    setClusters(newClusters);
    setIteration(prev => prev + 1);

    if (maxShift < 0.5) {
      setConverged(true);
      setIsRunning(false);
    }
  };

  // --- RENDERING HELPERS ---

  // Helper to get ellipse parameters (radii, rotation) from Covariance Matrix
  const getEllipseParams = (cov) => {
    const a = cov[0][0];
    const b = cov[0][1];
    const c = cov[1][1];
    
    // Eigenvalues
    const trace = a + c;
    const det = a * c - b * b;
    const term = Math.sqrt(Math.pow(trace, 2) / 4 - det);
    const lambda1 = trace / 2 + term;
    const lambda2 = trace / 2 - term;

    // Angle
    const theta = 0.5 * Math.atan2(2 * b, a - c);

    // Radii (2 sigma for 95% confidence)
    const rx = 2 * Math.sqrt(Math.max(0, lambda1));
    const ry = 2 * Math.sqrt(Math.max(0, lambda2));

    return { rx, ry, theta };
  };

  const draw = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    // Clear canvas
    ctx.clearRect(0, 0, WIDTH, HEIGHT);
    
    // Draw Grid (subtle background)
    ctx.strokeStyle = '#f3f4f6';
    ctx.lineWidth = 1;
    for(let i=0; i<WIDTH; i+=40) { ctx.beginPath(); ctx.moveTo(i,0); ctx.lineTo(i,HEIGHT); ctx.stroke(); }
    for(let i=0; i<HEIGHT; i+=40) { ctx.beginPath(); ctx.moveTo(0,i); ctx.lineTo(WIDTH,i); ctx.stroke(); }

    // --- NEW: DRAW AFFINITY VECTORS ---
    if (showVectors) {
      points.forEach(p => {
        p.probabilities.forEach((prob, k) => {
          // Only draw if probability is significant to reduce clutter
          if (prob > 0.02) { 
            const cluster = clusters[k];
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(cluster.mean.x, cluster.mean.y);
            ctx.strokeStyle = cluster.color;
            // Width and Opacity scaled by probability (E-step result)
            ctx.lineWidth = Math.max(0.5, prob * 2.5);
            ctx.globalAlpha = prob * 0.4; 
            ctx.stroke();
          }
        });
      });
      ctx.globalAlpha = 1.0; // Reset opacity
    }

    // Draw Points
    points.forEach(p => {
      // Find strongest cluster
      let maxProb = 0;
      let clusterIdx = 0;
      p.probabilities.forEach((prob, idx) => {
        if (prob > maxProb) {
          maxProb = prob;
          clusterIdx = idx;
        }
      });

      const color = clusters[clusterIdx].color;
      
      // Opacity calculation: if confidence is high, opaque. If low (near 1/K), transparent.
      // 1/K is pure uncertainty. 1.0 is pure certainty.
      // Scale alpha from 0.2 to 1.0 based on this.
      const normalizedConfidence = (maxProb - (1/K)) / (1 - (1/K));
      const alpha = showConfidence ? Math.max(0.2, Math.min(1, 0.2 + normalizedConfidence * 0.8)) : 1;

      ctx.beginPath();
      ctx.arc(p.x, p.y, 4, 0, 2 * Math.PI);
      ctx.fillStyle = color;
      ctx.globalAlpha = alpha;
      ctx.fill();
      ctx.globalAlpha = 1.0;
    });

    // Draw Gaussian Ellipses
    clusters.forEach(c => {
      const { rx, ry, theta } = getEllipseParams(c.cov);
      
      ctx.beginPath();
      // Draw 2-sigma contour
      ctx.ellipse(c.mean.x, c.mean.y, rx, ry, theta, 0, 2 * Math.PI);
      ctx.strokeStyle = c.color;
      ctx.lineWidth = 2;
      ctx.stroke();

      // Draw Mean center
      ctx.beginPath();
      ctx.arc(c.mean.x, c.mean.y, 6, 0, 2 * Math.PI);
      ctx.fillStyle = c.color;
      ctx.fill();
      ctx.strokeStyle = '#fff';
      ctx.lineWidth = 2;
      ctx.stroke();
    });
  };

  // --- EFFECTS ---

  useEffect(() => {
    generateData();
  }, [generateData]);

  useEffect(() => {
    draw();
  }, [points, clusters, showConfidence, showVectors]);

  useEffect(() => {
    let interval;
    if (isRunning && !converged) {
      interval = setInterval(() => {
        runEMStep();
      }, 100);
    }
    return () => clearInterval(interval);
  }, [isRunning, converged, points, clusters]);


  return (
    <div className="flex flex-col items-center w-full max-w-3xl mx-auto p-4 bg-white rounded-xl shadow-lg font-sans">
      <div className="text-center mb-4">
        <h1 className="text-2xl font-bold text-gray-800">Gaussian Mixture Model (GMM) Playground</h1>
        <p className="text-gray-500 text-sm">Visualize Expectation-Maximization (EM) fitting soft clusters to data.</p>
      </div>

      {/* CANVAS CONTAINER */}
      <div className="relative border-2 border-gray-200 rounded-lg overflow-hidden bg-white shadow-inner mb-6">
        <canvas 
          ref={canvasRef} 
          width={WIDTH} 
          height={HEIGHT}
          className="block bg-white"
        />
        
        {/* Iteration Badge */}
        <div className="absolute top-2 right-2 bg-gray-800/80 text-white px-3 py-1 rounded-full text-xs font-mono">
          Iter: {iteration} {converged && " (Converged)"}
        </div>
      </div>

      {/* CONTROLS */}
      <div className="w-full grid grid-cols-1 md:grid-cols-2 gap-4">
        
        {/* Simulation Controls */}
        <div className="flex flex-col gap-2 p-4 bg-gray-50 rounded-lg">
          <h3 className="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Simulation</h3>
          <div className="flex gap-2">
            <button 
              onClick={generateData}
              className="flex-1 flex items-center justify-center gap-2 bg-white border border-gray-300 hover:bg-gray-100 text-gray-700 py-2 px-4 rounded transition-colors text-sm"
            >
              <RefreshIcon size={16} /> Reset Data
            </button>
            <button 
              onClick={() => runEMStep()}
              disabled={isRunning || converged}
              className="flex-1 flex items-center justify-center gap-2 bg-indigo-100 hover:bg-indigo-200 text-indigo-700 py-2 px-4 rounded transition-colors text-sm disabled:opacity-50"
            >
              <StepForwardIcon size={16} /> Step
            </button>
          </div>
          <button 
            onClick={() => setIsRunning(!isRunning)}
            disabled={converged}
            className={`w-full flex items-center justify-center gap-2 py-2 px-4 rounded text-white font-medium transition-colors text-sm ${isRunning ? 'bg-orange-500 hover:bg-orange-600' : 'bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400'}`}
          >
            {isRunning ? <><PauseIcon size={16} /> Pause</> : <><PlayIcon size={16} /> Auto Run</>}
          </button>
        </div>

        {/* View Options */}
        <div className="flex flex-col gap-2 p-4 bg-gray-50 rounded-lg">
          <h3 className="text-xs font-bold text-gray-500 uppercase tracking-wider mb-2">Visualization</h3>
          
          <div className="flex items-center justify-between bg-white p-2 rounded border border-gray-200">
            <span className="text-sm text-gray-700 flex items-center gap-2">
              <SettingsIcon size={14} /> Soft Clustering View
            </span>
            <button 
              onClick={() => setShowConfidence(!showConfidence)}
              className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${showConfidence ? 'bg-blue-600' : 'bg-gray-200'}`}
            >
              <span className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${showConfidence ? 'translate-x-6' : 'translate-x-1'}`} />
            </button>
          </div>

          <div className="flex items-center justify-between bg-white p-2 rounded border border-gray-200">
            <span className="text-sm text-gray-700 flex items-center gap-2">
              <NetworkIcon size={14} /> Show Affinity Vectors
            </span>
            <button 
              onClick={() => setShowVectors(!showVectors)}
              className={`relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${showVectors ? 'bg-blue-600' : 'bg-gray-200'}`}
            >
              <span className={`inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${showVectors ? 'translate-x-6' : 'translate-x-1'}`} />
            </button>
          </div>

          <div className="bg-blue-50 p-3 rounded text-xs text-blue-800 leading-relaxed border border-blue-100">
            <strong className="flex items-center gap-1 mb-1"><InfoIcon size={12}/> How it works:</strong>
            1. <b>E-Step:</b> Calc probabilities (Vectors/Alpha).<br/>
            2. <b>M-Step:</b> Update shapes based on weights.
          </div>
        </div>
      </div>
    </div>
  );
};

export default GMMVisualizer;
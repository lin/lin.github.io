var __Widget_GMMVisualizer__ = (() => {
  var __create = Object.create;
  var __defProp = Object.defineProperty;
  var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
  var __getOwnPropNames = Object.getOwnPropertyNames;
  var __getProtoOf = Object.getPrototypeOf;
  var __hasOwnProp = Object.prototype.hasOwnProperty;
  var __commonJS = (cb, mod) => function __require() {
    return mod || (0, cb[__getOwnPropNames(cb)[0]])((mod = { exports: {} }).exports, mod), mod.exports;
  };
  var __export = (target, all) => {
    for (var name in all)
      __defProp(target, name, { get: all[name], enumerable: true });
  };
  var __copyProps = (to, from, except, desc) => {
    if (from && typeof from === "object" || typeof from === "function") {
      for (let key of __getOwnPropNames(from))
        if (!__hasOwnProp.call(to, key) && key !== except)
          __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
    }
    return to;
  };
  var __toESM = (mod, isNodeMode, target) => (target = mod != null ? __create(__getProtoOf(mod)) : {}, __copyProps(
    // If the importer is in node compatibility mode or this is not an ESM
    // file that has been converted to a CommonJS file using a Babel-
    // compatible transform (i.e. "__esModule" has not been set), then set
    // "default" to the CommonJS "module.exports" for node compatibility.
    isNodeMode || !mod || !mod.__esModule ? __defProp(target, "default", { value: mod, enumerable: true }) : target,
    mod
  ));
  var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

  // react-ns:react
  var require_react = __commonJS({
    "react-ns:react"(exports, module) {
      module.exports = window.React;
    }
  });

  // static/js/widgets/GMMVisualizer.js
  var GMMVisualizer_exports = {};
  __export(GMMVisualizer_exports, {
    default: () => GMMVisualizer_default
  });
  var import_react = __toESM(require_react());
  var PlayIcon = ({ size = 24, className = "" }) => /* @__PURE__ */ import_react.default.createElement("svg", { width: size, height: size, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: "2", strokeLinecap: "round", strokeLinejoin: "round", className }, /* @__PURE__ */ import_react.default.createElement("polygon", { points: "5 3 19 12 5 21 5 3" }));
  var PauseIcon = ({ size = 24, className = "" }) => /* @__PURE__ */ import_react.default.createElement("svg", { width: size, height: size, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: "2", strokeLinecap: "round", strokeLinejoin: "round", className }, /* @__PURE__ */ import_react.default.createElement("rect", { x: "6", y: "4", width: "4", height: "16" }), /* @__PURE__ */ import_react.default.createElement("rect", { x: "14", y: "4", width: "4", height: "16" }));
  var RefreshIcon = ({ size = 24, className = "" }) => /* @__PURE__ */ import_react.default.createElement("svg", { width: size, height: size, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: "2", strokeLinecap: "round", strokeLinejoin: "round", className }, /* @__PURE__ */ import_react.default.createElement("path", { d: "M23 4v6h-6" }), /* @__PURE__ */ import_react.default.createElement("path", { d: "M1 20v-6h6" }), /* @__PURE__ */ import_react.default.createElement("path", { d: "M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15" }));
  var StepForwardIcon = ({ size = 24, className = "" }) => /* @__PURE__ */ import_react.default.createElement("svg", { width: size, height: size, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: "2", strokeLinecap: "round", strokeLinejoin: "round", className }, /* @__PURE__ */ import_react.default.createElement("polygon", { points: "5 4 15 12 5 20 5 4" }), /* @__PURE__ */ import_react.default.createElement("line", { x1: "19", y1: "5", x2: "19", y2: "19" }));
  var SettingsIcon = ({ size = 24, className = "" }) => /* @__PURE__ */ import_react.default.createElement("svg", { width: size, height: size, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: "2", strokeLinecap: "round", strokeLinejoin: "round", className }, /* @__PURE__ */ import_react.default.createElement("circle", { cx: "12", cy: "12", r: "3" }), /* @__PURE__ */ import_react.default.createElement("path", { d: "M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z" }));
  var NetworkIcon = ({ size = 24, className = "" }) => /* @__PURE__ */ import_react.default.createElement("svg", { width: size, height: size, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: "2", strokeLinecap: "round", strokeLinejoin: "round", className }, /* @__PURE__ */ import_react.default.createElement("circle", { cx: "18", cy: "5", r: "3" }), /* @__PURE__ */ import_react.default.createElement("circle", { cx: "6", cy: "12", r: "3" }), /* @__PURE__ */ import_react.default.createElement("circle", { cx: "18", cy: "19", r: "3" }), /* @__PURE__ */ import_react.default.createElement("line", { x1: "8.59", y1: "13.51", x2: "15.42", y2: "17.49" }), /* @__PURE__ */ import_react.default.createElement("line", { x1: "15.41", y1: "6.51", x2: "8.59", y2: "10.49" }));
  var InfoIcon = ({ size = 24, className = "" }) => /* @__PURE__ */ import_react.default.createElement("svg", { width: size, height: size, viewBox: "0 0 24 24", fill: "none", stroke: "currentColor", strokeWidth: "2", strokeLinecap: "round", strokeLinejoin: "round", className }, /* @__PURE__ */ import_react.default.createElement("circle", { cx: "12", cy: "12", r: "10" }), /* @__PURE__ */ import_react.default.createElement("line", { x1: "12", y1: "16", x2: "12", y2: "12" }), /* @__PURE__ */ import_react.default.createElement("line", { x1: "12", y1: "8", x2: "12.01", y2: "8" }));
  var randn = () => {
    let u = 0, v = 0;
    while (u === 0)
      u = Math.random();
    while (v === 0)
      v = Math.random();
    return Math.sqrt(-2 * Math.log(u)) * Math.cos(2 * Math.PI * v);
  };
  var gaussianPdf = (point, mean, cov) => {
    const n = 2;
    const det = cov[0][0] * cov[1][1] - cov[0][1] * cov[1][0];
    if (det <= 1e-10)
      return 1e-10;
    const invCov = [
      [cov[1][1] / det, -cov[0][1] / det],
      [-cov[1][0] / det, cov[0][0] / det]
    ];
    const diff = [point.x - mean.x, point.y - mean.y];
    const mahalanobis = (diff[0] * invCov[0][0] + diff[1] * invCov[1][0]) * diff[0] + (diff[0] * invCov[0][1] + diff[1] * invCov[1][1]) * diff[1];
    const normalization = 1 / (Math.pow(2 * Math.PI, n / 2) * Math.sqrt(det));
    return normalization * Math.exp(-0.5 * mahalanobis);
  };
  var GMMVisualizer = () => {
    const WIDTH = 600;
    const HEIGHT = 400;
    const K = 3;
    const COLORS = ["#ef4444", "#3b82f6", "#22c55e", "#eab308"];
    const [points, setPoints] = (0, import_react.useState)([]);
    const [clusters, setClusters] = (0, import_react.useState)([]);
    const [iteration, setIteration] = (0, import_react.useState)(0);
    const [isRunning, setIsRunning] = (0, import_react.useState)(false);
    const [showConfidence, setShowConfidence] = (0, import_react.useState)(true);
    const [showVectors, setShowVectors] = (0, import_react.useState)(false);
    const [converged, setConverged] = (0, import_react.useState)(false);
    const canvasRef = (0, import_react.useRef)(null);
    const generateData = (0, import_react.useCallback)(() => {
      const newPoints = [];
      const centers = [
        { x: WIDTH * 0.3, y: HEIGHT * 0.3 },
        { x: WIDTH * 0.7, y: HEIGHT * 0.3 },
        { x: WIDTH * 0.5, y: HEIGHT * 0.75 }
      ];
      centers.forEach((center, idx) => {
        const sx = 20 + Math.random() * 30;
        const sy = 20 + Math.random() * 30;
        const angle = Math.random() * Math.PI / 2;
        const cos = Math.cos(angle);
        const sin = Math.sin(angle);
        for (let i = 0; i < 100; i++) {
          const rx = randn() * sx;
          const ry = randn() * sy;
          const x = center.x + rx * cos - ry * sin;
          const y = center.y + rx * sin + ry * cos;
          newPoints.push({ x, y, probabilities: Array(K).fill(1 / K) });
        }
      });
      setPoints(newPoints);
      initializeClusters(newPoints);
      setIteration(0);
      setConverged(false);
      setIsRunning(false);
    }, []);
    const initializeClusters = (currentPoints) => {
      const newClusters = [];
      for (let i = 0; i < K; i++) {
        const randomPoint = currentPoints[Math.floor(Math.random() * currentPoints.length)];
        newClusters.push({
          mean: { x: randomPoint.x + randn(), y: randomPoint.y + randn() },
          // Initialize covariance as somewhat spherical but large
          cov: [[2500, 0], [0, 2500]],
          pi: 1 / K,
          // Uniform weights initially
          color: COLORS[i]
        });
      }
      setClusters(newClusters);
    };
    const runEMStep = () => {
      if (points.length === 0)
        return;
      let newPoints = points.map((p) => {
        const likelihoods = clusters.map((c) => c.pi * gaussianPdf(p, c.mean, c.cov));
        const sumLikelihood = likelihoods.reduce((a, b) => a + b, 0);
        const probabilities = likelihoods.map((l) => sumLikelihood > 0 ? l / sumLikelihood : 1 / K);
        return { ...p, probabilities };
      });
      let maxShift = 0;
      const newClusters = clusters.map((cluster, k) => {
        let Nk = 0;
        let sumX = 0;
        let sumY = 0;
        newPoints.forEach((p) => {
          const gamma = p.probabilities[k];
          Nk += gamma;
          sumX += gamma * p.x;
          sumY += gamma * p.y;
        });
        if (Nk < 1)
          return cluster;
        const newMean = { x: sumX / Nk, y: sumY / Nk };
        let sumCovXX = 0, sumCovXY = 0, sumCovYY = 0;
        newPoints.forEach((p) => {
          const gamma = p.probabilities[k];
          const dx = p.x - newMean.x;
          const dy = p.y - newMean.y;
          sumCovXX += gamma * dx * dx;
          sumCovXY += gamma * dx * dy;
          sumCovYY += gamma * dy * dy;
        });
        const newCov = [
          [sumCovXX / Nk + 1e-6, sumCovXY / Nk],
          [sumCovXY / Nk, sumCovYY / Nk + 1e-6]
        ];
        const newPi = Nk / newPoints.length;
        const dist = Math.sqrt(Math.pow(newMean.x - cluster.mean.x, 2) + Math.pow(newMean.y - cluster.mean.y, 2));
        if (dist > maxShift)
          maxShift = dist;
        return {
          ...cluster,
          mean: newMean,
          cov: newCov,
          pi: newPi
        };
      });
      setPoints(newPoints);
      setClusters(newClusters);
      setIteration((prev) => prev + 1);
      if (maxShift < 0.5) {
        setConverged(true);
        setIsRunning(false);
      }
    };
    const getEllipseParams = (cov) => {
      const a = cov[0][0];
      const b = cov[0][1];
      const c = cov[1][1];
      const trace = a + c;
      const det = a * c - b * b;
      const term = Math.sqrt(Math.pow(trace, 2) / 4 - det);
      const lambda1 = trace / 2 + term;
      const lambda2 = trace / 2 - term;
      const theta = 0.5 * Math.atan2(2 * b, a - c);
      const rx = 2 * Math.sqrt(Math.max(0, lambda1));
      const ry = 2 * Math.sqrt(Math.max(0, lambda2));
      return { rx, ry, theta };
    };
    const draw = () => {
      const canvas = canvasRef.current;
      if (!canvas)
        return;
      const ctx = canvas.getContext("2d");
      ctx.clearRect(0, 0, WIDTH, HEIGHT);
      ctx.strokeStyle = "#f3f4f6";
      ctx.lineWidth = 1;
      for (let i = 0; i < WIDTH; i += 40) {
        ctx.beginPath();
        ctx.moveTo(i, 0);
        ctx.lineTo(i, HEIGHT);
        ctx.stroke();
      }
      for (let i = 0; i < HEIGHT; i += 40) {
        ctx.beginPath();
        ctx.moveTo(0, i);
        ctx.lineTo(WIDTH, i);
        ctx.stroke();
      }
      if (showVectors) {
        points.forEach((p) => {
          p.probabilities.forEach((prob, k) => {
            if (prob > 0.02) {
              const cluster = clusters[k];
              ctx.beginPath();
              ctx.moveTo(p.x, p.y);
              ctx.lineTo(cluster.mean.x, cluster.mean.y);
              ctx.strokeStyle = cluster.color;
              ctx.lineWidth = Math.max(0.5, prob * 2.5);
              ctx.globalAlpha = prob * 0.4;
              ctx.stroke();
            }
          });
        });
        ctx.globalAlpha = 1;
      }
      points.forEach((p) => {
        let maxProb = 0;
        let clusterIdx = 0;
        p.probabilities.forEach((prob, idx) => {
          if (prob > maxProb) {
            maxProb = prob;
            clusterIdx = idx;
          }
        });
        const color = clusters[clusterIdx].color;
        const normalizedConfidence = (maxProb - 1 / K) / (1 - 1 / K);
        const alpha = showConfidence ? Math.max(0.2, Math.min(1, 0.2 + normalizedConfidence * 0.8)) : 1;
        ctx.beginPath();
        ctx.arc(p.x, p.y, 4, 0, 2 * Math.PI);
        ctx.fillStyle = color;
        ctx.globalAlpha = alpha;
        ctx.fill();
        ctx.globalAlpha = 1;
      });
      clusters.forEach((c) => {
        const { rx, ry, theta } = getEllipseParams(c.cov);
        ctx.beginPath();
        ctx.ellipse(c.mean.x, c.mean.y, rx, ry, theta, 0, 2 * Math.PI);
        ctx.strokeStyle = c.color;
        ctx.lineWidth = 2;
        ctx.stroke();
        ctx.beginPath();
        ctx.arc(c.mean.x, c.mean.y, 6, 0, 2 * Math.PI);
        ctx.fillStyle = c.color;
        ctx.fill();
        ctx.strokeStyle = "#fff";
        ctx.lineWidth = 2;
        ctx.stroke();
      });
    };
    (0, import_react.useEffect)(() => {
      generateData();
    }, [generateData]);
    (0, import_react.useEffect)(() => {
      draw();
    }, [points, clusters, showConfidence, showVectors]);
    (0, import_react.useEffect)(() => {
      let interval;
      if (isRunning && !converged) {
        interval = setInterval(() => {
          runEMStep();
        }, 100);
      }
      return () => clearInterval(interval);
    }, [isRunning, converged, points, clusters]);
    return /* @__PURE__ */ import_react.default.createElement("div", { className: "flex flex-col items-center w-full max-w-3xl mx-auto p-4 bg-white rounded-xl shadow-lg font-sans" }, /* @__PURE__ */ import_react.default.createElement("div", { className: "text-center mb-4" }, /* @__PURE__ */ import_react.default.createElement("h1", { className: "text-2xl font-bold text-gray-800" }, "Gaussian Mixture Model (GMM) Playground"), /* @__PURE__ */ import_react.default.createElement("p", { className: "text-gray-500 text-sm" }, "Visualize Expectation-Maximization (EM) fitting soft clusters to data.")), /* @__PURE__ */ import_react.default.createElement("div", { className: "relative border-2 border-gray-200 rounded-lg overflow-hidden bg-white shadow-inner mb-6" }, /* @__PURE__ */ import_react.default.createElement(
      "canvas",
      {
        ref: canvasRef,
        width: WIDTH,
        height: HEIGHT,
        className: "block bg-white"
      }
    ), /* @__PURE__ */ import_react.default.createElement("div", { className: "absolute top-2 right-2 bg-gray-800/80 text-white px-3 py-1 rounded-full text-xs font-mono" }, "Iter: ", iteration, " ", converged && " (Converged)")), /* @__PURE__ */ import_react.default.createElement("div", { className: "w-full grid grid-cols-1 md:grid-cols-2 gap-4" }, /* @__PURE__ */ import_react.default.createElement("div", { className: "flex flex-col gap-2 p-4 bg-gray-50 rounded-lg" }, /* @__PURE__ */ import_react.default.createElement("h3", { className: "text-xs font-bold text-gray-500 uppercase tracking-wider mb-2" }, "Simulation"), /* @__PURE__ */ import_react.default.createElement("div", { className: "flex gap-2" }, /* @__PURE__ */ import_react.default.createElement(
      "button",
      {
        onClick: generateData,
        className: "flex-1 flex items-center justify-center gap-2 bg-white border border-gray-300 hover:bg-gray-100 text-gray-700 py-2 px-4 rounded transition-colors text-sm"
      },
      /* @__PURE__ */ import_react.default.createElement(RefreshIcon, { size: 16 }),
      " Reset Data"
    ), /* @__PURE__ */ import_react.default.createElement(
      "button",
      {
        onClick: () => runEMStep(),
        disabled: isRunning || converged,
        className: "flex-1 flex items-center justify-center gap-2 bg-indigo-100 hover:bg-indigo-200 text-indigo-700 py-2 px-4 rounded transition-colors text-sm disabled:opacity-50"
      },
      /* @__PURE__ */ import_react.default.createElement(StepForwardIcon, { size: 16 }),
      " Step"
    )), /* @__PURE__ */ import_react.default.createElement(
      "button",
      {
        onClick: () => setIsRunning(!isRunning),
        disabled: converged,
        className: `w-full flex items-center justify-center gap-2 py-2 px-4 rounded text-white font-medium transition-colors text-sm ${isRunning ? "bg-orange-500 hover:bg-orange-600" : "bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400"}`
      },
      isRunning ? /* @__PURE__ */ import_react.default.createElement(import_react.default.Fragment, null, /* @__PURE__ */ import_react.default.createElement(PauseIcon, { size: 16 }), " Pause") : /* @__PURE__ */ import_react.default.createElement(import_react.default.Fragment, null, /* @__PURE__ */ import_react.default.createElement(PlayIcon, { size: 16 }), " Auto Run")
    )), /* @__PURE__ */ import_react.default.createElement("div", { className: "flex flex-col gap-2 p-4 bg-gray-50 rounded-lg" }, /* @__PURE__ */ import_react.default.createElement("h3", { className: "text-xs font-bold text-gray-500 uppercase tracking-wider mb-2" }, "Visualization"), /* @__PURE__ */ import_react.default.createElement("div", { className: "flex items-center justify-between bg-white p-2 rounded border border-gray-200" }, /* @__PURE__ */ import_react.default.createElement("span", { className: "text-sm text-gray-700 flex items-center gap-2" }, /* @__PURE__ */ import_react.default.createElement(SettingsIcon, { size: 14 }), " Soft Clustering View"), /* @__PURE__ */ import_react.default.createElement(
      "button",
      {
        onClick: () => setShowConfidence(!showConfidence),
        className: `relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${showConfidence ? "bg-blue-600" : "bg-gray-200"}`
      },
      /* @__PURE__ */ import_react.default.createElement("span", { className: `inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${showConfidence ? "translate-x-6" : "translate-x-1"}` })
    )), /* @__PURE__ */ import_react.default.createElement("div", { className: "flex items-center justify-between bg-white p-2 rounded border border-gray-200" }, /* @__PURE__ */ import_react.default.createElement("span", { className: "text-sm text-gray-700 flex items-center gap-2" }, /* @__PURE__ */ import_react.default.createElement(NetworkIcon, { size: 14 }), " Show Affinity Vectors"), /* @__PURE__ */ import_react.default.createElement(
      "button",
      {
        onClick: () => setShowVectors(!showVectors),
        className: `relative inline-flex h-6 w-11 items-center rounded-full transition-colors ${showVectors ? "bg-blue-600" : "bg-gray-200"}`
      },
      /* @__PURE__ */ import_react.default.createElement("span", { className: `inline-block h-4 w-4 transform rounded-full bg-white transition-transform ${showVectors ? "translate-x-6" : "translate-x-1"}` })
    )), /* @__PURE__ */ import_react.default.createElement("div", { className: "bg-blue-50 p-3 rounded text-xs text-blue-800 leading-relaxed border border-blue-100" }, /* @__PURE__ */ import_react.default.createElement("strong", { className: "flex items-center gap-1 mb-1" }, /* @__PURE__ */ import_react.default.createElement(InfoIcon, { size: 12 }), " How it works:"), "1. ", /* @__PURE__ */ import_react.default.createElement("b", null, "E-Step:"), " Calc probabilities (Vectors/Alpha).", /* @__PURE__ */ import_react.default.createElement("br", null), "2. ", /* @__PURE__ */ import_react.default.createElement("b", null, "M-Step:"), " Update shapes based on weights."))));
  };
  var GMMVisualizer_default = GMMVisualizer;
  return __toCommonJS(GMMVisualizer_exports);
})();
// Auto-register the widget
if (typeof __Widget_GMMVisualizer__ !== 'undefined' && __Widget_GMMVisualizer__.default) {
  window.registerWidget && window.registerWidget('GMMVisualizer', __Widget_GMMVisualizer__.default);
}

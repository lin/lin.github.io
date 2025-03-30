// 创建场景
const scene = new THREE.Scene();

// 创建相机
const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(15, 15, 20);
camera.lookAt(scene.position);

// 创建渲染器
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setClearColor(0xEEEEEE);
renderer.shadowMap.enabled = true;
document.body.appendChild(renderer.domElement);

// 计算更精确的顶点坐标
const AC = 8;
const BC = 6;
const CH = 3;
const BH = 3 * Math.sqrt(3);
const AH = AC - CH;

// 计算点A, B, C的坐标
const A = new THREE.Vector3(AH + CH, 0, 0);
const B = new THREE.Vector3(CH, BH, 0);
const C = new THREE.Vector3(CH, 0, 0);

// 假设C1在C的正上方，距离为BC
const C1 = new THREE.Vector3(CH, 0, BC);

// 根据∠B1BC = 45°，计算B1的坐标
const B1 = new THREE.Vector3(CH, BH, BC);

// 假设A1在A的正上方，距离为BC
const A1 = new THREE.Vector3(AH + CH, 0, BC);

// 创建几何体
const geometry = new THREE.BufferGeometry();
const vertices = new Float32Array([
  C.x, C.y, C.z,  // C
  A.x, A.y, A.z,  // A
  B.x, B.y, B.z,  // B
  C1.x, C1.y, C1.z, // C1
  A1.x, A1.y, A1.z, // A1
  B1.x, B1.y, B1.z  // B1
]);
geometry.setAttribute('position', new THREE.BufferAttribute(vertices, 3));
geometry.setIndex([
  0, 1, 2,
  3, 4, 5,
  0, 2, 5, 3,
  0, 1, 4, 3,
  1, 2, 5, 4
]);

// 创建材质
const material = new THREE.MeshLambertMaterial({ color: 0x0000FF, wireframe: false });

// 创建网格
const mesh = new THREE.Mesh(geometry, material);
mesh.castShadow = true;
scene.add(mesh);

// 添加环境光
const ambientLight = new THREE.AmbientLight(0x404040);
scene.add(ambientLight);

// 添加点光源
const pointLight = new THREE.PointLight(0xffffff, 1.5, 100);
pointLight.position.set(15, 15, 15);
pointLight.castShadow = true;
scene.add(pointLight);

// 添加地面
const planeGeometry = new THREE.PlaneGeometry(20, 20);
const planeMaterial = new THREE.MeshLambertMaterial({ color: 0x999999 });
const plane = new THREE.Mesh(planeGeometry, planeMaterial);
plane.rotation.x = -Math.PI / 2;
plane.position.y = 0;
plane.receiveShadow = true;
scene.add(plane);

// 添加坐标轴辅助线
const axesHelper = new THREE.AxesHelper(10);
scene.add(axesHelper);

// 添加旋转控制
const controls = new THREE.OrbitControls(camera, renderer.domElement);

// 渲染循环
function animate() {
  requestAnimationFrame(animate);
  controls.update();
  renderer.render(scene, camera);
}
animate();
# Beyond Andromeda — Developer Workspace

> **"Beyond space, beyond thinking."**  
> Complete modern React + TypeScript + Three.js + Tailwind CSS codebase ready for collaboration.

---

## 🌟 Architecture & Directory Structure

```text
worlds-beyond-andromeda/
├── src/
│   ├── components/
│   │   ├── GlobeViewer.tsx       # Three.js 3D WebGL globe, revolving clouds, atmosphere, raycasting, markers
│   │   ├── FlatMap.tsx           # 2D equirectangular map projection with coordinate crosshairs
│   │   ├── ExplorePanel.tsx      # Side panel: Discover, Coordinates (DMS/decimal), About this world
│   │   ├── Header.tsx            # Navigation bar, world switcher, destination search with live dropdown
│   │   ├── Footer.tsx            # NASA fact sheet & texture attribution
│   │   └── ProvenanceBadge.tsx   # Color-coded NASA/model provenance badges & tooltips
│   ├── pages/
│   │   ├── Home.tsx              # Intro cinema overlay + Mission Console dashboard & 3D portals
│   │   ├── Explore.tsx           # 3D planetary explorer with URL lat/lon support
│   │   ├── Compare.tsx           # Multi-world comparison matrix with similarity scoring
│   │   └── Methodology.tsx       # Scientific formulas, solar irradiance, citations
│   ├── data/
│   │   ├── planets.ts            # Earth, Moon, Mars physical facts, atmosphere, orbit context
│   │   ├── sites.ts              # 11 curated named sites with exact coordinates & elevations
│   │   └── parameters.ts         # 11 comparative parameters, units, spans, normalization
│   ├── utils/
│   │   ├── geo.ts                # Decimal to DMS, latitude band classifier, spherical vector trig
│   │   └── similarity.ts         # Multi-parameter similarity mathematical models
│   ├── types/
│   │   └── index.ts              # Full TypeScript definitions & interfaces
│   ├── App.tsx                   # Client-side router & application shell
│   ├── main.tsx                  # React 18 DOM root entrypoint
│   └── index.css                 # Tailwind CSS directives, space themes, glow effects
├── public/
│   ├── textures/                 # Photorealistic planet maps (Solar System Scope CC BY 4.0)
│   │   ├── earth.jpg
│   │   ├── earth-clouds.jpg
│   │   ├── moon.jpg
│   │   └── mars.jpg
│   └── favicon.ico
├── dist/                         # Optimized production build
├── index.html                    # Vite HTML entrypoint
├── vite.config.ts                # Vite configuration
├── tailwind.config.js            # Tailwind theme tokens
├── tsconfig.json                 # TypeScript compiler options
├── package.json                  # Dependencies & scripts
└── serve.py                      # Zero-dependency Python SPA server
```

---

## 🚀 Running the Project

### 1. View the Live Site (Currently Running)
The local server is already running in the background:
- 🌍 **3D Earth Explorer (Lat 27.9974, Lon 77.9769):** [http://localhost:8080/explore/earth?lat=27.9974&lon=77.9769](http://localhost:8080/explore/earth?lat=27.9974&lon=77.9769)
- 🚀 **Mission Console / Homepage:** [http://localhost:8080](http://localhost:8080)
- ⚖️ **Compare Worlds Tool:** [http://localhost:8080/compare](http://localhost:8080/compare)
- 📚 **Methodology:** [http://localhost:8080/methodology](http://localhost:8080/methodology)

### 2. Development Mode with Instant Hot-Reload
To work on components live with instant hot-reloading:
```powershell
cd C:\Users\Jagdish\.gemini\antigravity\scratch\worlds-beyond-andromeda
deno run -A npm:vite
```
*(or `npm run dev` if you prefer standard npm)*

### 3. Rebuilding the Production Bundle
Whenever you make changes to TypeScript files:
```powershell
deno run -A npm:vite build
```

---

## 🛠️ How We Can Collaborate on This Project

You can now ask me to make any adjustments or enhancements, for example:
- **Add new celestial bodies** (e.g., Venus, Jupiter, Europa, Titan in `src/data/planets.ts`).
- **Add more custom named sites** or let users save bookmarks locally in `src/data/sites.ts`.
- **Customize 3D visual effects** (e.g., night lights on Earth, bump/normal maps, ring systems in `src/components/GlobeViewer.tsx`).
- **Extend the comparison tool** with custom charts, radar diagrams, or downloadable reports in `src/pages/Compare.tsx`.
- **Modify styling, typography, colors, or animations** in `src/index.css` or Tailwind config.

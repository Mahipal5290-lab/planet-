/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        space: '#070b14',
        portal: '#0c1222',
        hairline: 'rgba(255, 255, 255, 0.08)',
      },
      fontFamily: {
        sans: ['Roboto', 'sans-serif'],
        mono: ['"Roboto Mono"', 'monospace'],
        display: ['"Orbitron"', 'Roboto', 'sans-serif'],
        scifi: ['"Orbitron"', 'sans-serif'],
      },
    },
  },
  plugins: [],
};

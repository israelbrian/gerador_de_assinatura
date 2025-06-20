/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", // Aponta para todos os arquivos .html dentro da pasta templates
    "./static/js/**/*.js"   // Aponta para todos os arquivos .js dentro da pasta static/js
  ],
  theme: {
    extend: {
       colors: {
       'violet-blue': '#3c67f0',
       'violet-dark': '#1913ff',
    },
     fontFamily: {
       fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
    }
    },
  },
  plugins: [],
}


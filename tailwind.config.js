/** @type {import('tailwindcss').Config} */
module.exports = {
  
  content: ['./templates/**/**/*.html', './templates/components/**/*.html', './static/**/*.js', './static/**/*.css'],

  theme: {
    extend: {
      colors: {
        primary: '#a61766',
        secondary: '#27276c',
        neutral: '#96c83c',
      },
      backgroundImage: {
        'gradient-announcement': 'linear-gradient(90deg, #a61766, #27276c, #96c83c)',
      },
      keyframes: {
        gradient: {
          '0%': { backgroundPosition: '0% center' },
          '50%': { backgroundPosition: '100% center' },
          '100%': { backgroundPosition: '0% center' },
        },
        marquee: {
          '0%': { transform: 'translateX(0)' },
          '100%': { transform: 'translateX(-50%)' },
        },
      },
      animation: {
        gradient: 'gradient 6s linear infinite',
        marquee: 'marquee 20s linear infinite',
      },
    },
  },
  plugins: [require('daisyui')],
  daisyui: {
    themes: [
      {
        light: {
          "primary": '#a61766',
          "secondary": '#27276c',
          "neutral": '#96c83c',
          "base-100": "#FFFFFF",
          "background": '#000000'
        },
      },
    ],
  },
};

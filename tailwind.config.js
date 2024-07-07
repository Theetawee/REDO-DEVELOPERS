/** @type {import('tailwindcss').Config} */
const plugin = require("tailwindcss/plugin");

module.exports = {
  darkMode: "class",

  content: ["./templates/**/*.html", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      colors: {
        primary: {
          50: "#eff9ff",
          100: "#def2ff",
          200: "#b6e7ff",
          300: "#75d6ff",
          400: "#2cc1ff",
          500: "#00a4ef",
          600: "#0087d4",
          700: "#006bab",
          800: "#005b8d",
          900: "#064c74",
          950: "#04304d",
        },

        gray: {
          50: "#ffffff",
          100: "#efefef",
          200: "#dcdcdc",
          300: "#bdbdbd",
          400: "#989898",
          500: "#7c7c7c",
          600: "#656565",
          700: "#525252",
          800: "#464646",
          900: "#3d3d3d",
          950: "#292929",
        },
        secondary: {
          50: "#eff5fe",
          100: "#e8f0fd",
          200: "#cbdcfa",
          300: "#acc4f5",
          400: "#8ba3ee",
          500: "#6e84e6",
          600: "#5361d8",
          700: "#444ebe",
          800: "#39429a",
          900: "#353e7a",
          950: "#1f2347",
        },
      },
    },
  },
  plugins: [
    require("flowbite/plugin"),

    require('@tailwindcss/forms'),

  ],
};

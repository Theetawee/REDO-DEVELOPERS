/** @type {import('tailwindcss').Config} */
const plugin = require("tailwindcss/plugin");

module.exports = {
  darkMode: "class",

  content: ["./templates/**/*.html", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      colors: {
        primary: {
          50: "#fef7e0",
          100: "#fff1c2",
          200: "#ffe089",
          300: "#ffc745",
          400: "#fdad12",
          500: "#ed9305",
          600: "#cc6e02",
          700: "#a34b05",
          800: "#863c0d",
          900: "#723111",
          950: "#431705",
        },
        gray: {
          50: "#f2f2f2",
          100: "#e6e6e6",
          200: "#cccccc",
          300: "#b3b3b3",
          400: "#999999",
          500: "#808080",
          600: "#666666",
          700: "#4d4d4d",
          800: "#333333",
          900: "#1a1a1a",
        },
        secondary: {
          '50': '#eff5fe',
          '100': '#e8f0fd',
          '200': '#cbdcfa',
          '300': '#acc4f5',
          '400': '#8ba3ee',
          '500': '#6e84e6',
          '600': '#5361d8',
          '700': '#444ebe',
          '800': '#39429a',
          '900': '#353e7a',
          '950': '#1f2347',
      },
      
      },
    },
  },
  plugins: [
    require("flowbite/plugin"),

    plugin(function ({ addVariant, e, postcss }) {
      addVariant("firefox", ({ container, separator }) => {
        const isFirefoxRule = postcss.atRule({
          name: "-moz-document",
          params: "url-prefix()",
        });
        isFirefoxRule.append(container.nodes);
        container.append(isFirefoxRule);
        isFirefoxRule.walkRules((rule) => {
          rule.selector = `.${e(
            `firefox${separator}${rule.selector.slice(1)}`
          )}`;
        });
      });
    }),
  ],
};

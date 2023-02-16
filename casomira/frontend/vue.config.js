const { defineConfig } = require("@vue/cli-service");

module.exports = defineConfig({
  publicPath : "http://127.0.0.1:8080",
  outputDir : "../static/dist",
  indexPath : "../../templates/main/entry.html",
  transpileDependencies: true,
});

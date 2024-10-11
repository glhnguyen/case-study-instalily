const { createProxyMiddleware } = require("http-proxy-middleware");

const port = process.env.SERVER_PORT;

module.exports = function (app) {
  app.use(createProxyMiddleware(`http://localhost:${port}/api`));
};

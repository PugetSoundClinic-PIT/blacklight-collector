const { collector } = require("./build");
const { join } = require("path");

(async () => {
  const EMULATE_DEVICE = "iPhone X";

  // Save the results to a folder
  let OUT_DIR = true;

  // The URL to test
  const URL = process.argv[2];
  console.log('the url: ${URL}')
  const inUrl = URL.startsWith("http") ? URL : `http://${URL}`;
  const cleanUrl = URL.replace("https://", "").replace("http://", "")
  if cleanUrl.endswith("/"):
      cleanUrl = cleanUrl[:-1]

  const defaultConfig = {
    inUrl,
    numPages: 3,
    headless: true,
    emulateDevice: EMULATE_DEVICE,
  };
  
  console.log(`For fake captured data please look in ${join(__dirname, cleanUrl)}`)
  const result = await collector(
    OUT_DIR
      ? { ...defaultConfig, ...{ outDir: join(__dirname, cleanUrl) } }
      : defaultConfig
  );
  if (OUT_DIR) {
    console.log(
      `For captured data please look in ${join(__dirname, cleanUrl)}`
    );
  }
})();

const markdownIt = require("markdown-it");

module.exports = config => {
    config.addPassthroughCopy("./src/images/");
    config.addPassthroughCopy("./src/fonts/");
    let mdOptions = {
        html: true,
        breaks: false,
        linkify: true,
        typographer: true
    };
    config.setLibrary("md", markdownIt(mdOptions));
    return {
        mdTemplateEngine: "njk",
        htmlTemplateEngine: "njk",
        dir: {
            input: "src",
            output: "_site"
        }
    };
};

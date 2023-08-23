const markdownIt = require("markdown-it");

function acronymsFilter(text){
    const pattern = /([A-Z][A-Z]+)/g;
    return text.replace(pattern, "<abbr class='acronym'>$1</abbr>");
}

module.exports = config => {
    config.addPassthroughCopy("./src/images/");
    config.addPassthroughCopy("./src/fonts/");
    config.addFilter("acronyms", acronymsFilter);
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

module.exports = config => {
    config.addPassthroughCopy("./src/images/");
    config.addPassthroughCopy("./src/fonts/");
    return {
        mdTemplateEngine: "njk",
        htmlTemplateEngine: "njk",
        dir: {
            input: "src",
            output: "_site"
        }
    };
};

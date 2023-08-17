module.exports = config => {
    config.addPassthroughCopy("./src/images/");
    return {
        mdTemplateEngine: "njk",
        htmlTemplateEngine: "njk",
        dir: {
            input: "src",
            output: "_site"
        }
    };
};

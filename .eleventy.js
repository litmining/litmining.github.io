module.exports = config => {
    config.addPassthroughCopy("./src/images/");
    return {
        htmlTemplateEngine: "njk",
        dir: {
            input: "src",
            output: "_site"
        }
    };
};

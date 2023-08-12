module.exports = config => {
    config.addPassthroughCopy("**/*.png");
    return {
        dir: {
            input: "src",
            output: "_site"
        }
    };
};

module.exports = config => {
    config.addPassthroughCopy("src/*.svg");
    return {
        dir: {
            input: "src",
            output: "_site"
        }
    };
};

module.exports = config => {
    config.addPassthroughCopy("src/*.png");
    return {
        dir: {
            input: "src",
            output: "_site"
        }
    };
};

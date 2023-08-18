const crypto = require("crypto");

module.exports = {
    randomString() {
        return crypto.randomBytes(8).toString('hex');
    }
};

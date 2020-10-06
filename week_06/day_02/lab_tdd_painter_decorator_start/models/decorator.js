const PaintCan = require('./paint_can.js');


const Decorator = function(paintStock) {
    this.paintStock = [];
};

Decorator.prototype.addCanOfPaint = function(can) {
    this.paintStock.push(can);
}

Decorator.prototype.calculateAmountOfPaint = function() {
    let total = 0;
    for (paint of this.paintStock) {
        total += paint.litresOfPaint
    }
    return total;
}

Decorator.prototype.hasEnoughPaint = function(room) {
    if (this.calculateAmountOfPaint() >= room.areaInSquareMeters) {
        return true;
    } else {
        return false;
    };
};

Decorator.prototype.paintRoom = function(room) {
    if (this.hasEnoughPaint(room) === true) {
        room.paint()
    };
};

// Decorator.prototype.decreasePaintStock = function(room) {
//     if (this.hasEnoughPaint(room)) {
//         let counter = room.areaInSquareMeters;
//         let usedPaint = 0;
//         while (usedPaint < counter) {
//             if (this.paintStock.litresOfPaint > 0) {
//                 paintStock.litresOfPaint -= 1;
//                 usedPaint += 1
//             };
//         };
//     };
// };



module.exports = Decorator;
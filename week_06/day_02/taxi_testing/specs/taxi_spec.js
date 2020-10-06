const assert = require('assert');
const Taxi = require('../taxi.js');

describe('Taxi', function(){

    let taxi;

    beforeEach(function(){
        taxi = new Taxi('Toyota', 'Prius', 'David');
    });

    it('should have a manufacturer', function(){
        // Arrange
        // Act
        const actual = taxi.manufacturer;
        // Assert
        assert.strictEqual(actual, 'Toyota');
    });

    it('should have a model', function(){
        const actual = taxi.model;
        assert.strictEqual(actual, 'Prius');
    });

    it('should have a driver', function(){
        const actual = taxi.driver;
        assert.strictEqual(actual, 'David');
    });

    describe('passengers', function(){

        it('should start with no panssengers', function(){
            const actual = taxi.passengers;
            assert.deepStrictEqual(actual, []);
        });

        it('should have a number of passengers', function(){
            const actual = taxi.numberOfPassengers();
            assert.deepStrictEqual(actual, 0);
        });

        it('should be able to add a passenger', function(){
            taxi.addPassenger('Kyle');
            const actual = taxi.numberOfPassengers();
            assert.deepStrictEqual(actual, 1);
        });

        it('should be able to remove a passenger by name', function(){
            taxi.addPassenger('Kyle');
            taxi.addPassenger('Antonia');
            taxi.removePassengerByName('Kyle');
            const actual = taxi.numberOfPassengers();
            assert.deepStrictEqual(actual, 1);
        });
    });

});
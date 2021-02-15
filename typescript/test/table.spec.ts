import { Table } from '../src/index';
import { expect } from 'chai';
import 'mocha';

/**
 * Test All 100 nonZeroIndex
 */
describe('Table class - test all 100 nonZero', () => {
    it('should return true', () => {
        let result = true;
        for (let X = 1; X <= 100; X++) {
            for (let Y = 1; Y <= 100; Y++) {
                const myXY: Table = new Table(X, Y, false);
                for (let i = 1; i <= X * Y; i++) {
                    const [ai, bi] = myXY.GetElementsAtIndex(i);
                    const index = myXY.GetIndexOfElements(ai, bi);
                    if (i != index) {
                        result = false;
                    }
                }
            }
        }
        expect(result).to.equal(true);
    });
});

/**
 * Test All 100 zeroBasedIndex
 */
describe('Table class - test all 100 zero', () => {
    it('should return true', () => {
        let result = true;
        for (let X = 1; X <= 100; X++) {
            for (let Y = 1; Y <= 100; Y++) {
                const myXY: Table = new Table(X, Y, true);
                for (let i = 0; i <= X * Y - 1; i++) {
                    const [ai, bi] = myXY.GetElementsAtIndex(i);
                    const index = myXY.GetIndexOfElements(ai, bi);
                    if (i != index) {
                        result = false;
                    }
                }
            }
        }
        expect(result).to.equal(true);
    });
});

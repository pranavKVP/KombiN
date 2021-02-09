package ninja.pranav.algorithms.kombin;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

/**
 * Unit test for Table class.
 */
public class TableTest {

    /**
     * Rigorous Test :-) All 100 False
     */
    @Test
    public void testAll100false() {
        boolean result = true;
        for (int X = 1; X <= 100; X++) {
            for (int Y = 1; Y <= 100; Y++) {
                Table myXY = new Table(X, Y, false);
                for (long i = 1; i <= X * Y; i++) {
                    Pair ai_bi = myXY.GetElementsAtIndex(i);
                    long index = myXY.GetIndexOfElements(ai_bi.ai, ai_bi.bi);
                    if (i != index) {
                        result = false;
                    }
                }
            }
        }
        assertEquals(true, result);
    }

    /**
     * Rigorous Test :-) All 100 True
     */
    @Test
    public void testAll100True() {
        boolean result = true;
        for (int X = 1; X <= 100; X++) {
            for (int Y = 1; Y <= 100; Y++) {
                Table myXY = new Table(X, Y, true);
                for (long i = 0; i <= (X * Y) - 1; i++) {
                    Pair ai_bi = myXY.GetElementsAtIndex(i);
                    long index = myXY.GetIndexOfElements(ai_bi.ai, ai_bi.bi);
                    if (i != index) {
                        result = false;
                    }
                }
            }
        }
        assertEquals(true, result);
    }
}

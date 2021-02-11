
using System;
using Xunit;

[assembly: CLSCompliant(true)]
namespace Ninja.Pranav.Algorithms.Kombin.tests {

    /// <summary>
    /// Tests for Table class.
    /// </summary>
    public class TestTable {

        /// <summary>
        /// Rigorous Test :-) All 100 False
        /// </summary>
        [Fact]
        public void TestAll100False() {
            bool result = true;
            for (int X = 1; X <= 100; X++) {
                for (int Y = 1; Y <= 100; Y++) {
                    Table myXY = new Table(X, Y, false);
                    for (long i = 1; i <= X * Y; i++) {
                        long ai, bi;
                        (ai, bi) = myXY.GetElementsAtIndex(i);
                        long index = myXY.GetIndexOfElements(ai, bi);
                        if (i != index) {
                            result = false;
                        }
                    }
                }
            }
            Assert.True(result);
        }

        /// <summary>
        /// Rigorous Test :-) All 100 True
        /// </summary>
        [Fact]
        public void TestAll100True() {
            bool result = true;
            for (int X = 1; X <= 100; X++) {
                for (int Y = 1; Y <= 100; Y++) {
                    Table myXY = new Table(X, Y, true);
                    for (long i = 0; i <= (X * Y) - 1; i++) {
                        long ai, bi;
                        (ai, bi) = myXY.GetElementsAtIndex(i);
                        long index = myXY.GetIndexOfElements(ai, bi);
                        if (i != index) {
                            result = false;
                        }
                    }
                }
            }
            Assert.True(result);
        }
    }
}

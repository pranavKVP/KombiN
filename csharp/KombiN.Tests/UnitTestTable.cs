
using System;
using Xunit;

[assembly: CLSCompliant(true)]
namespace KombiN.Tests {
    public class UnitTestTable {
        [Fact]
        public void TestAll60False() {
            bool result = true;
            for (int X = 1; X <= 60; X++) {
                for (int Y = 1; Y <= 60; Y++) {
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

        [Fact]
        public void TestAll60True() {
            bool result = true;
            for (int X = 1; X <= 60; X++) {
                for (int Y = 1; Y <= 60; Y++) {
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

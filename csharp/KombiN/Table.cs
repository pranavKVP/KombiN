// MIT License
// 
// Copyright (c) 2020 Pranavkumar Patel
// 
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
// 
// The above copyright notice and this permission notice shall be included in all
// copies or substantial portions of the Software.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
// SOFTWARE.

/// <summary>
/// KombiN is an algorithm to get index for combination pair and
/// to get combination pair from index, where all possible
/// combination pairs from two finite sets are sorted by their weight
/// in ascending order.
/// </summary>

using System;

[assembly: CLSCompliant(true)]
namespace KombiN {
    /// <summary>
    /// Provides a methods to get index of combination pair
    /// and to get combination pair from index value.
    /// </summary>
    public class Table {
        /// <summary>
        /// Initializes a new instance of the <see cref="Table"/> class.
        /// <summary>
        /// <param name="lengthOfA">Number of elements in first set.</param>
        /// <param name="lengthOfB">Number of elements in second set.</param>
        /// <param name="zeroBasedIndex">True if sets index starts with zero otherwise False.</param>
        /// <returns><see cref="Table"/> object.</returns>
        /// <exception cref="ArgumentOutOfRangeException">
        /// if <paramref name="lengthOfA" /> or <paramref name="lengthOfB" /> is 0 or less.
        /// </exception>
        public Table(long lengthOfA, long lengthOfB, bool zeroBasedIndex) {
            if (lengthOfA < 1 || lengthOfB < 1) {
                throw new ArgumentOutOfRangeException(paramName: nameof(lengthOfA) + " || " + nameof(lengthOfB),
                    message: "Length of both sets must be grater than 0.");
            }
            this.LengthOfA = lengthOfA;
            this.LengthOfB = lengthOfB;
            this.ZeroBasedIndex = zeroBasedIndex;
            this.MaxIndexRange1 = this.MaxIndexRange2 = this.MaxIndexRange3 = 0;
            this.MaxSumRange1 = this.MaxSumRange2 = this.MaxSumRange3 = 0;
            this.Abstract();
        }

        public long LengthOfA { get; private set; }
        public long LengthOfB { get; private set; }
        public long LowerLength { get; private set; }
        public long MaxSumRange1 { get; private set; }
        public long MaxSumRange2 { get; private set; }
        public long MaxSumRange3 { get; private set; }
        public long MaxIndexRange1 { get; private set; }
        public long MaxIndexRange2 { get; private set; }
        public long MaxIndexRange3 { get; private set; }
        public bool ZeroBasedIndex { get; private set; }

        /// <summary>
        /// Sets an abstract values useful to get index and combination pair.
        /// </summary>
        /// <returns>none</returns>
        /// <exception cref="OverflowException">
        /// if arithmetic operation resultes in an overflow.
        /// </exception>
        private void Abstract() {
            checked {
                this.LowerLength = this.LengthOfA < this.LengthOfB ? this.LengthOfA : this.LengthOfB;
                long higherLength = this.LengthOfA > this.LengthOfB ? this.LengthOfA : this.LengthOfB;
                long difference = higherLength - this.LowerLength;
                long product = higherLength * this.LowerLength;
                long sum = higherLength + this.LowerLength;
                this.MaxSumRange1 = this.LowerLength + 1;
                if (difference == 0) {
                    this.MaxIndexRange1 = (product * this.MaxSumRange1) / sum;
                } else if (difference == 1) {
                    this.MaxIndexRange1 = product / 2;
                } else if (difference >= 2) {
                    this.MaxSumRange2 = higherLength;
                    this.MaxIndexRange1 = (product - this.LowerLength * (sum - 1 - 2 * this.LowerLength)) / 2;
                    this.MaxIndexRange2 = (product + this.LowerLength * (sum - 1 - 2 * this.LowerLength)) / 2;
                }

                if (product >= 2) {
                    this.MaxSumRange3 = sum;
                    this.MaxIndexRange3 = product;
                }
            }
        }

        /// <summary>
        /// Get index value for the combination pair.
        /// </summary>
        /// <param name="ai">Element index of set A.</param>
        /// <param name="bi">Element index of set B.</param>
        /// <returns>Index value for the given combination pair.</returns>
        /// <exception cref="ArgumentOutOfRangeException">
        /// if <paramref name="ai" /> or <paramref name="bi" /> has invalid value.
        /// </exception>
        /// <exception cref="OverflowException">
        /// if arithmetic operation resultes in an overflow.
        /// </exception>
        public long GetIndexOfElements(long ai, long bi) {
            if (this.ZeroBasedIndex) {
                if (ai < 0 || bi < 0) {
                    throw new ArgumentOutOfRangeException(paramName: nameof(ai) + " || " + nameof(bi),
                        message: "Both element index values must be 0 or more.");
                }
                ai++;
                bi++;
            } else if (ai < 1 || bi < 1) {
                throw new ArgumentOutOfRangeException(paramName: nameof(ai) + " || " + nameof(bi),
                    message: "Both element index values must be 1 or more.");
            }

            long index, previousIndex;
            checked {
                long sum = ai + bi;

                if (sum <= this.MaxSumRange1) {
                    previousIndex = sum - 2;
                    index = (previousIndex % 2 == 0 ? (previousIndex / 2) * (previousIndex + 1)
                            : (((previousIndex - 1) / 2) * previousIndex) + previousIndex)
                        + ai;
                } else if (sum <= this.MaxSumRange2) {
                    index = this.MaxIndexRange1
                        + ((sum - (this.MaxSumRange1 + 1)) * this.LowerLength)
                        + (this.LengthOfA < this.LengthOfB ? ai : (this.LengthOfB + 1) - bi);
                } else if (sum <= this.MaxSumRange3) {
                    previousIndex = this.MaxSumRange3 - sum + 1;
                    index = this.MaxIndexRange3
                        - (previousIndex % 2 == 0 ? (previousIndex / 2) * (previousIndex + 1)
                            : (((previousIndex - 1) / 2) * previousIndex) + previousIndex)
                        + (this.MaxIndexRange3 < 2 ? ai : (this.LengthOfB + 1) - bi);
                } else {
                    throw new ArgumentOutOfRangeException($"Sum of both the element index values must not be greater than {this.MaxSumRange3}");
                }
            }

            if (this.ZeroBasedIndex) {
                index--;
            }

            return index;
        }

        /// <summary>
        /// Get the combination pair for given index value.
        /// </summary>
        /// <param name="index">Index value of combination pair.</param>
        /// <returns>combination pair<returns>
        /// <exception cref="ArgumentOutOfRangeException">
        /// if <paramref name="index" /> has invalid value.
        /// </exception>
        /// <exception cref="OverflowException">
        /// if arithmetic operation resultes in an overflow.
        /// </exception>
        public (long, long) GetElementsAtIndex(long index) {
            if (this.ZeroBasedIndex) {
                if (index < 0) {
                    throw new ArgumentOutOfRangeException(paramName: nameof(index),
                        message: "Index value must be 0 or more.");
                }
                index++;
            } else if (index < 1) {
                throw new ArgumentOutOfRangeException(paramName: nameof(index),
                    message: "Index value must be 1 or more.");
            }

            long ai, bi;
            long previousIndex, sum;

            checked {
                if (index <= this.MaxIndexRange1) {
                    sum = Convert.ToInt64(Math.Ceiling((Math.Sqrt((index * 8) + 1) + 1) / 2));
                    ai = index - ((sum - 1) * (sum - 2) / 2);
                    bi = sum - ai;
                } else if (index <= this.MaxIndexRange2) {
                    sum = this.MaxSumRange1
                        + ((index - this.MaxIndexRange1) / this.LowerLength)
                        - (((index - this.MaxIndexRange1) % this.LowerLength == 0) ? 1 : 0)
                        + 1;
                    previousIndex = this.MaxIndexRange1 + ((sum - 1 - this.MaxSumRange1) * this.LowerLength);
                    if (this.LengthOfA >= this.LengthOfB) {
                        bi = (this.LengthOfB + 1) - (index - previousIndex);
                        ai = sum - bi;
                    } else {
                        ai = index - previousIndex;
                        bi = sum - ai;
                    }
                } else if (index <= this.MaxIndexRange3) {
                    long generic_maxSumRange3 = this.MaxSumRange3 - (this.MaxSumRange2 == 0 ? this.MaxSumRange1 : this.MaxSumRange2);
                    long generic_index = index - (this.MaxIndexRange2 == 0 ? this.MaxIndexRange1 : this.MaxIndexRange2);
                    long b = (2 * generic_maxSumRange3) + 1;
                    long generic_Sum = Convert.ToInt64(Math.Ceiling((b - Math.Sqrt(b * b - 8 * generic_index)) / 2));
                    sum = (this.MaxSumRange2 == 0 ? this.MaxSumRange1 : this.MaxSumRange2) + generic_Sum;
                    previousIndex = (this.MaxIndexRange2 == 0 ? this.MaxIndexRange1 : this.MaxIndexRange2)
                        + (generic_Sum == 1 ? 0 : ((generic_Sum - 1) * (b - generic_Sum + 1)) / 2);
                    if (this.MaxIndexRange3 >= 2) {
                        bi = (this.LengthOfB + 1) - (index - previousIndex);
                        ai = sum - bi;
                    } else {
                        ai = index - previousIndex;
                        bi = sum - ai;
                    }
                } else {
                    throw new ArgumentOutOfRangeException(paramName: nameof(index),
                        message: $"Index value must not be greater than {this.MaxIndexRange3}");
                }
            }

            if (this.ZeroBasedIndex) {
                ai--;
                bi--;
            }

            return (ai, bi);
        }
    }
}

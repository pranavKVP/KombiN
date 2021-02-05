package kombin;

public class Table {
    public final long LengthOfA;
    public final long LengthOfB;
    public final long LowerLength;
    public final long MaxSumRange1;
    public final long MaxSumRange2;
    public final long MaxSumRange3;
    public final long MaxIndexRange1;
    public final long MaxIndexRange2;
    public final long MaxIndexRange3;
    public final boolean ZeroBasedIndex;

    public Table(long lengthOfA, long lengthOfB, boolean zeroBasedIndex) {
        if (lengthOfA < 1 || lengthOfB < 1) {
            throw new IllegalArgumentException("Length of both sets must be grater than 0.");
        }
        this.LengthOfA = lengthOfA;
        this.LengthOfB = lengthOfB;
        this.ZeroBasedIndex = zeroBasedIndex;
        // Getting Abstract values
        this.LowerLength = this.LengthOfA < this.LengthOfB ? this.LengthOfA : this.LengthOfB;
        long higherLength = this.LengthOfA > this.LengthOfB ? this.LengthOfA : this.LengthOfB;
        long difference = higherLength - this.LowerLength;
        long product = higherLength * this.LowerLength;
        long sum = higherLength + this.LowerLength;
        this.MaxSumRange1 = this.LowerLength + 1;
        if (difference == 0) {
            this.MaxSumRange2 = this.MaxIndexRange2 = 0;
            this.MaxIndexRange1 = (product * this.MaxSumRange1) / sum;
        } else if (difference == 1) {
            this.MaxSumRange2 = this.MaxIndexRange2 = 0;
            this.MaxIndexRange1 = product / 2;
        } else if (difference >= 2) {
            this.MaxSumRange2 = higherLength;
            this.MaxIndexRange1 = (product - this.LowerLength * (sum - 1 - 2 * this.LowerLength)) / 2;
            this.MaxIndexRange2 = (product + this.LowerLength * (sum - 1 - 2 * this.LowerLength)) / 2;
        } else {
            this.MaxSumRange2 = this.MaxIndexRange1 = this.MaxIndexRange2 = 0;
        }

        if (product >= 2) {
            this.MaxSumRange3 = sum;
            this.MaxIndexRange3 = product;
        } else {
            this.MaxSumRange3 = this.MaxIndexRange3 = 0;
        }
    }

    public long GetIndexOfElements(long ai, long bi) {
        if (this.ZeroBasedIndex) {
            if (ai < 0 || bi < 0) {
                throw new IllegalArgumentException("Both element index values must be 0 or more.");
            }
            ai++;
            bi++;
        } else if (ai < 1 || bi < 1) {
            throw new IllegalArgumentException("Both element index values must be 1 or more.");
        }

        long index;
        long previousIndex;
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
            throw new IllegalArgumentException("Sum of both the element index values must not be greater than " + this.MaxSumRange3);
        }

        if (this.ZeroBasedIndex) {
            index--;
        }
        return index;
    }

    //
    public Pair GetElementsAtIndex(long index) {
        if (this.ZeroBasedIndex) {
            if (index < 0) {
                throw new IllegalArgumentException("Index value must be 0 or more.");
            }
            index++;
        } else if (index < 1) {
            throw new IllegalArgumentException("Index value must be 1 or more.");
        }

        long ai;
        long bi;
        long previousIndex;
        long sum;

        if (index <= this.MaxIndexRange1) {
            sum = (long)(Math.ceil((Math.sqrt((index * 8) + (double)1) + 1) / 2));
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
            long generic_Sum = (long)(Math.ceil((b - Math.sqrt((double)b * b - 8 * generic_index)) / 2));
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
            throw new IllegalArgumentException("Index value must not be greater than " + this.MaxIndexRange3);
        }

        if (this.ZeroBasedIndex) {
            ai--;
            bi--;
        }

        return new Pair(ai, bi);
    }

}

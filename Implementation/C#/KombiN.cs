namespace AlgoKombiN
{
    class KombiN
    {
        //Get Abstract Values using length of two sets
        private static void GetAbstract(ulong XLength, ulong YLength,
                                       out ulong S1, out ulong S2, out ulong S3,
                                       out ulong I1, out ulong I2, out ulong I3,
                                       out ulong T2, out ulong Z2, out ulong Z3)
        {
            checked
            {
                ulong diffXY = (XLength > YLength ? XLength - YLength
                                                  : YLength - XLength);
                ulong multiXY = XLength * YLength;
                ulong sumXY = XLength + YLength;
                ulong US1 = (XLength <= YLength ? XLength : YLength);
                ulong US2 = (diffXY <= 1 ? 0 : (sumXY - 1) - (US1 * 2));
                ulong nI2 = ((sumXY - 1 - US2) / 2) * US2;

                S1 = US1 + 1;
                S2 = (diffXY <= 1 ? 0 : (XLength > YLength ? XLength : YLength));
                S3 = (multiXY < 2 ? 0 : sumXY);

                T2 = (diffXY <= 1 ? 0 : (XLength < YLength ? XLength : YLength));
                Z2 = (diffXY <= 1 ? 0 : (XLength < YLength ? 0 : YLength));
                Z3 = (multiXY < 2 ? 0 : YLength);

                I1 = (diffXY == 0 ? (multiXY * S1) / sumXY
                        : (diffXY == 1 ? multiXY / 2
                            : ((multiXY - nI2) / 2)));
                I2 = (diffXY <= 1 ? 0 : ((multiXY - nI2) / 2) + nI2);
                I3 = (multiXY < 2 ? 0 : multiXY);
            }
        }

        //Get Index value for Combination values
        public static ulong GetIndex(ulong X, ulong Y,
                                    ulong XLength, ulong YLength,
                                    bool zeroBasedIndex = true)
        {
            if (zeroBasedIndex) { X++; Y++; }
            GetAbstract(XLength, YLength,
                        out ulong S1, out ulong S2, out ulong S3,
                        out ulong I1, out ulong I2, out ulong I3,
                        out ulong T2, out ulong Z2, out ulong Z3);

            ulong Index = 0, xIndex;
            checked
            {
                ulong Sum = X + Y;
                ushort Range = (ushort)(Sum <= S1 ? 1
                                                  : (Sum <= S2 ? 2
                                                               : (Sum <= S3 ? 3
                                                                            : 0)));
                switch (Range)
                {
                    case 1:
                        xIndex = Sum - 2;
                        Index += (xIndex % 2 == 0 ? (xIndex / 2) * (xIndex + 1)
                                    : (((xIndex - 1) / 2) * xIndex) + xIndex);
                        Index += X;
                        break;
                    case 2:
                        Index += I1 + ((Sum - (S1 + 1)) * T2)
                                    + (Z2 == 0 ? X : (Z2 + 1) - Y);
                        break;
                    case 3:
                        Index += (I2 == 0 ? I1 : I2);
                        xIndex = S3 - Sum + 1;
                        Index += (I3 - (I2 == 0 ? I1 : I2))
                              - ((xIndex % 2 == 0 ? (xIndex / 2) * (xIndex + 1)
                                    : (((xIndex - 1) / 2) * xIndex) + xIndex));
                        Index += (Z3 == 0 ? X : (Z3 + 1) - Y);
                        break;
                }
            }
            if (zeroBasedIndex) { Index--; }
            return Index;
        }

        // Get Combination values for Index value
        public static void GetCombination(ulong Index,
                                          ulong XLength, ulong YLength,
                                          out ulong X, out ulong Y,
                                          bool zeroBasedIndex = true)
        {
            if (zeroBasedIndex) { Index++; }
            GetAbstract(XLength, YLength,
                        out ulong S1, out ulong S2, out ulong S3,
                        out ulong I1, out ulong I2, out ulong I3,
                        out ulong T2, out ulong Z2, out ulong Z3);

            ulong MaxIndex = X = Y = 0;
            ulong XSum, XIndex, Sum;
            ushort Range = (ushort)(Index <= I1 ? 1
                                                : (Index <= I2 ? 2
                                                               : (Index <= I3 ? 3
                                                                              : 0)));
            checked
            {
                switch (Range)
                {
                    case 1:
                        for (XSum = 2; MaxIndex < Index; XSum++)
                        {
                            MaxIndex += XSum - 1;
                        }
                        Sum = XSum - 1;
                        XIndex = MaxIndex - (Sum - 1);

                        X = Index - XIndex;
                        Y = Sum - X;
                        break;
                    case 2:
                        XIndex = I1;
                        XSum = S1;

                        bool IsLast = (Index - XIndex) % T2 == 0;
                        ulong Pre = ((Index - XIndex) / T2)
                                    - (ushort)(IsLast ? 1 : 0);

                        XSum += Pre;
                        XIndex += Pre * T2;

                        Sum = XSum + 1;
                        if (Z2 == 0)
                        {
                            X = (Index - XIndex);
                            Y = Sum - X;
                        }
                        else
                        {
                            Y = (Z2 + 1) - (Index - XIndex);
                            X = Sum - Y;
                        }
                        break;
                    case 3:
                        XIndex = (I2 == 0 ? I1 : I2);
                        MaxIndex += XIndex;
                        for (XSum = (S2 == 0 ? S1 : S2) + 1; MaxIndex < Index; XSum++)
                        {
                            MaxIndex += (S3 - XSum + 1);
                        }
                        Sum = XSum - 1;
                        XIndex = MaxIndex - (S3 - Sum + 1);

                        if (Z3 == 0)
                        {
                            X = (Index - XIndex);
                            Y = Sum - X;
                        }
                        else
                        {
                            Y = (Z3 + 1) - (Index - XIndex);
                            X = Sum - Y;
                        }
                        break;
                }
            }
            if (zeroBasedIndex) { X--; Y--; }
        }
    }
}

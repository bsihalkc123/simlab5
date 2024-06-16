def calculate_probability():
    # Given probabilities
    P_Rt_given_Rt = 0.4  # P(R_t+1 | R_t)
    P_notRt_given_Rt = 0.6  # P(not R_t+1 | R_t)
    P_Rt_given_notRt = 0.2  # P(R_t+1 | not R_t)
    P_notRt_given_notRt = 0.8  # P(not R_t+1 | not R_t)

    # Calculate P(not R_t+2 | not R_t)
    P_notRt2_given_notRt = (
        P_notRt_given_notRt * 1  # P(not R_t+2 | not R_t, not R_t+1) = 1
        + P_notRt_given_Rt * 0.8  # P(not R_t+2 | not R_t, R_t+1) = 0.8
    )

    return P_notRt2_given_notRt

# Call the function to calculate the probability
result = calculate_probability()
print(f"The probability that it will not rain the day after tomorrow given that it is not raining today is: {result}")

def calculate_probability():
    # Given probabilities
    P_C_given_C = 0.9  # P(C_t+1 | C_t)
    P_C_given_P = 0.2  # P(C_t+1 | P_t)
    P_P_given_P = 0.8  # P(P_t+1 | P_t) 

    # Calculate P(C_t+2 | P_t)
    P_C2_given_P = (
        P_C_given_P * P_C_given_C  # P(C_t+2 | P_t, C_t+1)
        + P_C_given_P * P_P_given_P  # P(C_t+2 | P_t, P_t+1)
    )

    return P_C2_given_P

# Call the function to calculate the probability
result = calculate_probability()
print(f"The probability of purchasing Coke two purchases from now, given currently purchasing Pepsi, is: {result}")

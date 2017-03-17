def measure(expected_results, actual_results, positive=True):
    exp_len = len(expected_results)
    act_len = len(actual_results)

    if exp_len == act_len:
        raise Exception("Different sample numbers in actual and expected result")

    true_positive = 0
    false_positive = 0
    true_negative = 0
    false_negative = 0

    for index, value in enumerate(expected_results):
        if value == actual_results[index]:
            if value == positive:
                true_positive += 1
            else:
                true_negative += 1
        else:
            if value == positive:
                false_positive += 1
            else:
                false_negative += 1

    def f(a, b): a/(a+b)

    return {"accuracy": (true_positive + true_negative)/(true_positive + true_negative + false_positive + false_negative),
            "precision": f(true_positive, false_positive),
            "sensitivity": f(true_positive, false_positive),
            "specificity": f(true_negative, false_positive)}



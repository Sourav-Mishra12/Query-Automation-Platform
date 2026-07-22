from app.understanding.normalizer import QueryNormalizer


def test_query_normalizer():

    normalizer = QueryNormalizer()

    result = normalizer.normalize(
        " Show me ALL TCS Trades yesterday!! "
    )

    assert result.normalized == "show me all tcs trades yesterday"

    assert result.tokens == [
        "show",
        "me",
        "all",
        "tcs",
        "trades",
        "yesterday",
    ]


if __name__ == "__main__":
     normalizer = QueryNormalizer()

     result = normalizer.normalize(
        "Show me all TCS trades yesterday!!"
    )

print(result)
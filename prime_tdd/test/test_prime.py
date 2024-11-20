# prime_tdd/test/test_prime.py
from prime_tdd.src.prime import is_prime
 
 
def test_prime_number():
    # Test basic primes
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
 
    # Test non-primes
    assert is_prime(1) is False
    assert is_prime(4) is False
    assert is_prime(9) is False
 
    # Test large primes
    assert is_prime(101) is True
 
    # Test edge cases
    assert is_prime(-1) is False
    assert is_prime(0) is False
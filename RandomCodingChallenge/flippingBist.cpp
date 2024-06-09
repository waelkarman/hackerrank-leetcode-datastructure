long flippingBits(long n) {
    uint32_t nr = (uint32_t)n;
    nr=~nr;
    return (long)nr;    
}

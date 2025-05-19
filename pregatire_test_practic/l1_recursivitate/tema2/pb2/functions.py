def produs_scalar(x, y, len) :
    if len == 0 :
        return 0
    else :
        return x[len - 1] * y[len - 1] + produs_scalar(x, y, len - 1)
    

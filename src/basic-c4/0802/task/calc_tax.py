# 消費税率
TAX_RATE = 0.08

def calc_incl_tax(excl_tax):
    """
    税込み金額を計算する

    Parameters
    ----------
    excl_tax: int
        税抜き金額

    Returns
    -------
    int
        税込み金額
    """
    return round(excl_tax * (1 + TAX_RATE), 0)

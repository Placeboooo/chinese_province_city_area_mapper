
from cpca.matcher import Matcher
from cpca import AddrInfo


def test_matcher():
    matcher = Matcher("([省市]|特别行政区|自治区)$")
    matcher.add_addr_info(AddrInfo("不测自治区", "111111000000", 1, 1))
    matcher.add_addr_info(AddrInfo("测试区", "111112000000", 1, 1))
    matcher.add_addr_info(AddrInfo("测试区", "111113000000", 3, 2))

    matcher.complete_add()

    res = list(matcher.iter("不测"))
    assert len(res) == 1
    assert len(res[0].attr_infos) == 1
    assert res[0].attr_infos[0].name == "不测自治区"
    assert res[0].end_index == 1

    res = list(matcher.iter("不测自治区"))
    assert res[0].end_index == 4

    res = list(matcher.iter("测试区"))
    assert len(res) == 1
    assert len(res[0].attr_infos) == 2
    assert res[0].attr_infos[0].adcode == "111112"
    assert res[0].attr_infos[1].adcode == "111113"

    res = list(matcher.iter("哈哈"))
    assert len(res) == 0


const data = [
    //分别为左边，右边，数据
    ['天猫', '上海', 15216, 25216],
    ['线下自营店', '上海', 11278, 13244],
    ['苏宁易购', '上海', 27, 24],
    ['网上自营店', '上海', 27648, 35411],
    ['线下代理商', '上海', 1551, 1545],
    ['京东', '上海', 22141, 25441],
    ['天猫', '广州', 15453, 15353],
    ['线下自营店', '广州', 24683, 24623],
    ['苏宁易购', '广州', 1862, 654],
    ['线下代理商', '广州', 16228, 13228],
    ['天猫', '北京', 15001, 18001],
    ['线下自营店', '北京', 15001, 1654],
    ['苏宁易购', '北京', 5001, 6541],
    ['网上自营店', '北京', 28648, 29648],
    ['线下代理商', '北京', 9648, 9648],
    ['天猫', '深圳', 3313, 541],
    ['线下自营店', '深圳', 22396, 24396],
    ['苏宁易购', '深圳', 3362, 3762],
    ['网上自营店', '深圳', 22396, 21396],
    ['线下代理商', '深圳', 2473, 2973],
    ['京东', '深圳', 16541, 11541],
    ['苏宁易购', '杭州', 3541, 3599],
    ['线下代理商', '杭州', 3541, 8741],
    ['京东', '杭州', 3654, 9874],
    ['天猫', '武汉', 1738, 110],
    ['线下自营店', '武汉', 12925, 13],
    ['苏宁易购', '武汉', 15413, 0],
    ['线下自营店', '重庆', 2166, 654],
    ['苏宁易购', '重庆', 2286, 3654],
    ['网上自营店', '重庆', 348, 3654],
    ['线下代理商', '重庆', 4244, 3654],
    ['京东', '重庆', 1536, 1654],
    ['线下自营店', '长沙', 351, 654],
    ['线下代理商', '长沙', 405, 541],
    ['线下自营店', '成都', 914, 654],
    ['苏宁易购', '成都', 127, 354],
    ['线下代理商', '成都', 1470, 654],
    ['京东', '成都', 516, 354],
    ['天猫', '东莞', 43, 0],
    ['线下自营店', '东莞', 667, 654],
    ['苏宁易购', '东莞', 172, 354],
    ['网上自营店', '东莞', 149, 541],
    ['线下代理商', '东莞', 1380, 3254],
    ['京东', '东莞', 791, 754],
    ['线下自营店', '苏州', 541, 687],
    ['线下代理商', '苏州', 654, 541],
    ['线下自营店', '南京', 1070, 654],
    ['线下代理商', '南京', 1171, 1541],
    ['京东', '南京', 33, 45],
    ['线下自营店', '佛山', 407, 654],
    ['苏宁易购', '佛山', 541, 874],
    ['线下代理商', '佛山', 457, 674],
    ['京东', '佛山', 541, 365],
    ['线下自营店', '天津', 557, 654],
    ['苏宁易购', '天津', 167, 541],
    ['网上自营店', '天津', 95, 100],
    ['线下代理商', '天津', 1090, 1321],
    ['京东', '天津', 676, 541],
    ['天猫', '合肥', 1195, 1654],
    ['线下自营店', '合肥', 5412, 6541],
    ['苏宁易购', '合肥', 212, 241],
    ['线下代理商', '合肥', 1509, 1654],
    ['天猫', '温州', 3899, 389],
    ['线下自营店', '温州', 147, 321],
    ['苏宁易购', '温州', 455, 541],
    ['网上自营店', '温州', 321, 254],
    ['线下代理商', '温州', 4100, 4512],
    ['天猫', '南宁', 123, 133],
    ['线下自营店', '南宁', 634, 654],
    ['苏宁易购', '南宁', 749, 541],
    ['网上自营店', '南宁', 119, 654],
    ['线下代理商', '南宁', 3705, 4574],
    ['京东', '南宁', 3456, 4000],
    ['线下自营店', '厦门', 828, 1201],
    ['苏宁易购', '厦门', 2808, 3541],
    ['网上自营店', '厦门', 1452, 2000],
    ['线下代理商', '厦门', 2625, 1541],
    ['京东', '厦门', 1920, 1234],
    ['线下自营店', '西安', 1146, 1541],
    ['苏宁易购', '西安', 212, 321],
    ['网上自营店', '西安', 223, 241],
    ['线下代理商', '西安', 1803, 2000],
    ['京东', '西安', 761, 465],
    ['线下自营店', '长春', 527, 654],
    ['苏宁易购', '长春', 90, 120],
    ['线下代理商', '长春', 930, 1241],
    ['京东', '长春', 395, 410],
    ['天猫', '哈尔滨', 7232, 8451],
    ['线下自营店', '哈尔滨', 1272, 2141],
    ['苏宁易购', '哈尔滨', 1896, 3541],
    ['网上自营店', '哈尔滨', 200, 1241],
    ['线下代理商', '哈尔滨', 10782, 15412],
    ['京东', '哈尔滨', 1911, 2000],
    ['线下自营店', '青岛', 495, 521],
    ['苏宁易购', '青岛', 432, 541],
    ['网上自营店', '青岛', 241, 320],
    ['线下代理商', '青岛', 1557, 1600],
    ['京东', '青岛', 24, 30],
    ['线下自营店', '沈阳', 460, 541],
    ['网上自营店', '沈阳', 88, 99],
    ['线下代理商', '沈阳', 956, 365],
    ['线下自营店', '济南', 232, 365],
    ['苏宁易购', '济南', 71, 99],
    ['线下代理商', '济南', 575, 654],
    ['京东', '济南', 368, 354]
  ]


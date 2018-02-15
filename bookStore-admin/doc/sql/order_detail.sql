CREATE TABLE `order_detail` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '自增id',
  `order_id` int(20) DEFAULT NULL COMMENT '对应订单的id',
  `book_name` varchar(255) DEFAULT NULL COMMENT '书名',
  `isbn` int(11) DEFAULT NULL COMMENT 'ISBN编号',
  `origin_price` decimal(5,0) DEFAULT NULL COMMENT '定价',
  `actual_price` decimal(5,0) DEFAULT NULL COMMENT '实价',
  `discount` decimal(5,0) DEFAULT NULL COMMENT '折扣',
  `order_quantity` int(5) DEFAULT NULL COMMENT '购买数',
  `deliveried_quantity` int(11) DEFAULT NULL COMMENT '配送数',
  `warehouse` varchar(255) DEFAULT NULL COMMENT '库区',
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `order_id` (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
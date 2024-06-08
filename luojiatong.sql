create database if not exists luojiatong;

use luojiatong;

CREATE TABLE affair (
                        id INT PRIMARY KEY AUTO_INCREMENT comment '主键ID', -- ID，主键，自增
                        type INT NOT NULL comment '事务类型', -- 类型，不允许为空
                        name VARCHAR(255) NOT NULL comment '事务名称', -- 事项名称，不允许为空
                        place VARCHAR(255) comment '事务地点', -- 事项地点，允许为空
                        content TEXT comment '事务内容', -- 事项内容，允许为空
                        startTime DATETIME NOT NULL comment '事务开始时间',-- 事项时间，不允许为空
                        endTime DATETIME NOT NULL comment '事务结束时间'-- 事项时间，不允许为空
)comment '事务表';
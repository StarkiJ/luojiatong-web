package com.starki.pojo;

import com.fasterxml.jackson.annotation.JsonFormat;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

/**
 * 事项实体类
 */
@Data //getter/setter
@NoArgsConstructor //无参构造
@AllArgsConstructor //全参构造
public class Affair {
    private Integer id; //ID
    private Integer type; //类型: 1.课程 2.运动 3.图书馆 4.其他
    private String name; //事项名称
    private String place; //事项地点
    private String content; //事项内容
    @JsonFormat(pattern="yyyy-MM-dd HH:mm:ss")
    private LocalDateTime startTime; //事项开始时间
    @JsonFormat(pattern="yyyy-MM-dd HH:mm:ss")
    private LocalDateTime endTime; //事项结束时间
}

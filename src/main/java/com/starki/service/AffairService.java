package com.starki.service;

import com.starki.pojo.Affair;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;

public interface AffairService {

    /**
     * 条件查询事务
     * @param type
     * @param name
     * @param place
     * @param content
     * @param startTime
     * @param endTime
     * @return
     */
    List<Affair> list(Integer type, String name, String place, String content, LocalDateTime startTime, LocalDateTime endTime);

    /**
     * 添加事务
     * @param affair
     */
    void add(Affair affair);

    /**
     * 删除事务
     * @param ids
     */
    void delete(List<Integer> ids);

    /**
     * 更新事务
     * @param affair
     */
    void update(Affair affair);
}

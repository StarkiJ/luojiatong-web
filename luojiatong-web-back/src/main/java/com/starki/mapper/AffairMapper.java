package com.starki.mapper;

import com.starki.pojo.Affair;
import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;

/**
 * 事务管理
 */
@Mapper
public interface AffairMapper {

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
    @Insert("insert into affair(type,name,place,content,startTime,endTime) values(#{type},#{name},#{place},#{content},#{startTime},#{endTime})")
    void insert(Affair affair);

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

package com.starki.controller;

import com.starki.pojo.Affair;
import com.starki.pojo.Result;
import com.starki.service.AffairService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;

@Slf4j
@RequestMapping("/affairs")
@RestController
public class AffairController {

    @Autowired
    private AffairService affairService;

    /**
     * 测试
     *
     * @return
     */
    @GetMapping("/hello")
    public Result hello() {
        log.info("hello");
        return Result.success("hello");
    }

    /**
     * 条件查询事务
     *
     * @param startTime
     * @param endTime
     * @return
     */
    @GetMapping()
    public Result list(Integer type, String name,
                       String place, String content,
                       @DateTimeFormat(pattern = "yyyy-MM-dd") LocalDateTime startTime,
                       @DateTimeFormat(pattern = "yyyy-MM-dd") LocalDateTime endTime) {
        log.info("条件查询事务：{},{},{},{},{},{}", type, name, place, content, startTime, endTime);
        List<Affair> affairList = affairService.list(type, name, place, content, startTime, endTime);
        return Result.success(affairList);
    }

    /**
     * 新增事务
     *
     * @param affair
     * @return
     */
    @PostMapping
    public Result add(@RequestBody Affair affair) {
        log.info("新增事务, 参数: {}", affair);
        affairService.add(affair);
        return Result.success();
    }

    /**
     * 删除事务
     * @param ids
     * @return
     */
    @DeleteMapping("/{ids}")
    public Result delete(@PathVariable List<Integer> ids) {
        log.info("删除事务, ids: {}", ids);
        affairService.delete(ids);
        return Result.success();
    }

    /**
     * 修改事务
     * @param affair
     * @return
     */
    @PutMapping
    public Result update(@RequestBody Affair affair) {
        log.info("修改事务, 参数: {}", affair);
        affairService.update(affair);
        return Result.success();
    }
}

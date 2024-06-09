package com.starki.service.impl;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.datatype.jsr310.JavaTimeModule;
import com.starki.mapper.AffairMapper;
import com.starki.pojo.Affair;
import com.starki.service.AffairService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.IOException;
import java.time.LocalDateTime;
import java.util.List;

@Service
public class AffairServiceImpl implements AffairService {

    @Autowired
    private AffairMapper affairMapper;

    @Override
    public List<Affair> list(Integer type, String name, String place, String content, LocalDateTime startTime, LocalDateTime endTime) {
        return affairMapper.list(type, name, place, content, startTime, endTime);
    }

    @Override
    public void add(Affair affair) {
        affairMapper.insert(affair);
    }

    @Override
    public void delete(List<Integer> ids) {
        affairMapper.delete(ids);
    }

    @Override
    public void update(Affair affair) {
        affairMapper.update(affair);
    }

    @Override
    public void deleteCourse(List<String> names) {
        affairMapper.deleteCourse(names);
    }

    @Override
    public void listCourse() {
        ObjectMapper objectMapper = new ObjectMapper();
        // 注册 JavaTimeModule 以支持 Java 8 日期和时间类型
        objectMapper.registerModule(new JavaTimeModule());

        try {
            File file = new File("src/main/resources/schedule.json");
            List<Affair> affairs = objectMapper.readValue(file, new TypeReference<List<Affair>>() {});
            for(Affair affair:affairs)
            {
                affairMapper.insert(affair);
                System.out.println(affair);
            }
        }catch (IOException e){
            e.printStackTrace();
        }
    }

}

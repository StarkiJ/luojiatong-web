package com.starki.service.impl;

import com.starki.mapper.AffairMapper;
import com.starki.pojo.Affair;
import com.starki.service.AffairService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
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
}

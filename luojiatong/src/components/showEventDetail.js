// 测试用日程数组
export const events = [
    {
        name: '上课1',
        startTime: '05-30',
        endTime: '结束时间1',
        location: '教五',
        discription: '描述1',
    },
    {
        name: '上课2',
        startTime: '05-30',
        endTime: '结束时间1',
        location: '教五',
        discription: '描述1',
    },
    {
        name: '上课3',
        startTime: '05-30',
        endTime: '结束时间1',
        location: '教五',
        discription: '描述1',
    },
    {
        name: '吃饭',
        startTime: '05-31',
        location: '梅园',
        discription: '描述2',
    },
    {
        name: '跑步',
        startTime: '05-01',
        discription: '描述3',
    },
    {
        name: '事务4',
        startTime: '06-01',
        discription: '描述4',
    },
];

// 获取指定日期的事件
export const getEventsByDate = (date) => {
    const monthDay = date.split('-').slice(1).join('-');
    return events.filter(event => event.startTime === monthDay);
};

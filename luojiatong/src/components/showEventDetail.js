
// 测试用日程数组
// export const events = [
//    {
//         name: '上课1',
//         startTime: '05-30',
//         endTime: '结束时间1',
//         location: '教五',
//         discription: '描述1',
//     },
//     {
//         name: '上课2',
//         startTime: '05-30',
//         endTime: '结束时间1',
//         location: '教五',
//         discription: '描述1',
//     },
//     {
//         name: '上课3',
//         startTime: '05-30',
//         endTime: '结束时间1',
//         location: '教五',
//         discription: '描述1',
//     },
//     {
//         name: '吃饭',
//         startTime: '05-31',
//         location: '梅园',
//         discription: '描述2',
//     },
//     {
//         name: '跑步',
//         startTime: '05-01',
//         discription: '描述3',
//     },
//     {
//         name: '事务4',
//         startTime: '06-01',
//         discription: '描述4',
//     },
// ];

//事务列表模型
export const events = [
    {
        id: 12,
        type: 3,
        name: "考研数学",
        place: "总图",
        content: "好好学习",
        startTime: "2024-06-21T15:00:00",
        endTime: "2024-06-21T17:00:00"
    },
    {
        id: 4,
        type: 2,
        name: "羽毛球",
        place: "卓尔体育馆",
        content: null,
        startTime: "2024-06-23T15:00:00",
        endTime: "2024-06-23T17:00:00"
    },
];

import { hello, getAffairs } from '@/api/affairs.js';

const helloTry = () => {
    return new Promise((resolve, reject) => {
        hello().then(res => {
            console.log(res.data);
            resolve();
        }).catch(err => {
            console.log(err);
        });
    });
}
helloTry();

//测试
// const getMAffairs = (type, name, place, content, startTime, endTime) => {
//     const affair = {
//         type: type,
//         name: name,
//         place: place,
//         content: content,
//         startTime: startTime,
//         endTime: endTime
//     };

//     console.log(affair);
//     return new Promise((resolve, reject) => {
//         getAffairs(affair).then(res => {
//             console.log(res.data);
//             resolve();
//         }).catch(err => {
//             console.log(err);
//         });
//     });
// }
// getMAffairs(null, null, null, null, null, null);

//获取事务列表数据
// export const affairList = async (type, name, place, content, startTime, endTime) => {
//     let params = {
//         type: type,
//         name: name,
//         place: place,
//         content: content,
//         startTime: startTime,
//         endTime: endTime
//     }
//     //console.log(params);
//     let result = await getAffairs(params);
//     // console.log("r: ");
//     // console.log(result);

//     //渲染视图
//     affairs = result.data;
//     // console.log("a: ");
//     // console.log(affairs);
//     return result;
// }


// 获取指定日期的事件
// export const getEventsByDate = async (date) => {
//     const startTime = date+'T'+'00:00:00';
//     const endTime = date+'T'+'23:59:59';
//     affairList(null, null, null, null, startTime, endTime);
//     // console.log("event: ");
//     // console.log(affairs);
//     return affairs;
// };

// 获取指定日期的事件
// export const getEventsByDate = (date) => {
//     const monthDay = date.split('-').slice(1).join('-');
//     console.log(monthDay);
//     console.log(events);
//     return events.filter(event => event.startTime === monthDay);
// };

// 获取指定日期的事件
// export const getEventsByDate = (date) => {
//     console.log(date);
//     return events.filter(event => comp(event, date)===true);
// };

// const comp = (event, date) => {
//     const start = date + 'T' + '00:00:00';
//     const end = date + 'T' + '23:59:59';
//     console.log(event);
//     // console.log(Date.parse(event.endTime));
//     // console.log(Date.parse(start));
//     // console.log(Date.parse(event.startTime));
//     // console.log(Date.parse(end));
//     console.log((Date.parse(event.endTime) >= Date.parse(start) && Date.parse(event.startTime) <= Date.parse(end)));
//     return (Date.parse(event.endTime) >= Date.parse(start) && Date.parse(event.startTime) <= Date.parse(end));
// }
<template>
    <div>其实是草稿本</div>

    <div class="p-4 font-bold text-2xl">
        <el-icon size="25" style="vertical-align: middle" >
            <Calendar />
        </el-icon>
        <span style="vertical-align: middle">   月历</span>
    </div>
    <el-calendar>
        <template #date-cell="{ data }">
            <p :class="data.isSelected ? 'is-selected' : ''">
                {{ data.day.split('-').slice(1).join('-') }}
            </p>
            <el-scrollbar max-height="calc(100% - 15px)">
                <p v-for="(event, index) in getEventsByDate(data.day)" :key="index" class="EventInCalendar">
                    {{ event.name }}
                </p> 
            </el-scrollbar>
        </template>
    </el-calendar>
</template>

<script setup>
    import { ref, reactive } from 'vue'

    document.title='其实是草稿本'

    // 测试用日程数据，换成从数据库里按startTime对应日期查到的
    // 日期必须为"MM-DD"的格式
    const events = [{
        name: '上课',
        startTime: '05-30',
        endTime: '结束时间1',
        location: '教五',
        discription: '描述1',
    },{
        name: '上课',
        startTime: '05-30',
        endTime: '结束时间1',
        location: '教五',
        discription: '描述1',
    },{
        name: '上课',
        startTime: '05-30',
        endTime: '结束时间1',
        location: '教五',
        discription: '描述1',
    },{
        name: '上课',
        startTime: '05-30',
        endTime: '结束时间1',
        location: '教五',
        discription: '描述1',
    },{
        name: '吃饭',
        startTime: '05-31',
        location: '梅园',
        discription: '描述2',
    },{
        name: '跑步',
        startTime: '05-01',
        discription: '描述3',
    },{
        name: '事务4',
        startTime: '06-01',
        discription: '描述4',
    }]

    const getEventsByDate = (date) => {
        const monthDay = date.split('-').slice(1).join('-')
        return events.filter(event => event.startTime === monthDay)
    }

</script>

<style scoped>
    /* 日历，选中的日期 */
    .is-selected {
        color: #14b8a6;
    }
    .EventInCalendar {
        @apply
        bg-teal-100
        rounded-default
        p-1
        my-1;
    }
</style>
<template>
    <div id="MonthView-Head" class="p-4 font-bold text-2xl">
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
                <p v-for="(event, index) in getEventsByDate(data.day)" 
                    :key="index" 
                    class="EventInCalendar"
                >
                <div @click.native="showEventDetail(event)">
                    {{ event.name }}
                </div>
                    
                </p> 
            </el-scrollbar>
        </template>
    </el-calendar>

    <!-- 日程详情 -->
    <el-dialog v-model="eventDetailVisible" width="500" :title=selectedEvent?.name>
        <div class='p-1'>
            <el-icon style="vertical-align: middle" ><Clock /></el-icon>
            <span style="vertical-align: middle" class='p-2'>
                {{ selectedEvent?.startTime }} - {{ selectedEvent?.endTime }}
            </span>
        </div>
        <div class='p-1'>
            <el-icon style="vertical-align: middle" ><Location /></el-icon>
            <span style="vertical-align: middle" class='p-2'>
                {{ selectedEvent?.location }}
            </span>
        </div>
        <div class='p-1'>
            <el-icon style="vertical-align: middle" ><MoreFilled /></el-icon>
            <span style="vertical-align: middle" class='p-2'>
                {{ selectedEvent?.discription }}
            </span>
        </div>

        <template #footer>
            <div class="dialog-footer">
                <el-button @click="eventDetailVisible = false">确定</el-button>
            </div>
        </template>
    </el-dialog>
</template>

<script setup>
    import { ref } from 'vue';
    import { events, getEventsByDate } from './showEventDetail.js';

    const eventDetailVisible = ref(false);
    const selectedEvent = ref(null);

    const showEventDetail = (event) => {
        selectedEvent.value = event;
        eventDetailVisible.value = true;
    };
</script>

<style scoped>
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

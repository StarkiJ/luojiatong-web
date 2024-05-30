<template>
    <div id="DayView-Head" class="p-4 text-2xl">
        <el-icon size="25" style="vertical-align: middle" >
            <List />
        </el-icon>
        <span style="vertical-align: middle">   本日事务</span>
    </div>

    <el-scrollbar max-height="400px"  style="max-width: 600px">
        <div id="TimeLine">
            <el-timeline style="max-width: 600px">
                <el-timeline-item 
                    placement="top"
                    v-for="(event, index) in todayEvents"
                    :key="index"
                    :timestamp="event.startTime"
                    @click.native="showEventDetail(event)"
                >
                <el-card style="max-width: 480px">
                    <el-row>
                        <el-col :span="8">
                            <div class="text-2xl font-bold p-2">
                                {{ event.name }}
                            </div>
                        </el-col>
                        <el-col :span="16">
                            <div class='p-1'>
                                <el-icon style="vertical-align: middle" ><Clock /></el-icon>
                                <span style="vertical-align: middle" class='p-2'>{{ event.startTime }} - {{ event.endTime }}</span>
                            </div>
                            <div class='p-1'>
                                <el-icon style="vertical-align: middle" ><Location /></el-icon>
                                <span style="vertical-align: middle" class='p-2'>{{ event.location }}</span>
                            </div>
                        </el-col>
                    </el-row>
                </el-card>
                </el-timeline-item>
            </el-timeline>
        </div>
    </el-scrollbar>

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
    import { events } from './showEventDetail.js';

    const eventDetailVisible = ref(false);
    const selectedEvent = ref(null);

    const today = new Date();
    const todayStr = ('0' + (today.getMonth() + 1)).slice(-2) + '-' + ('0' + today.getDate()).slice(-2);
    const todayEvents = events.filter(event => event.startTime === todayStr);

    const showEventDetail = (event) => {
        selectedEvent.value = event;
        eventDetailVisible.value = true;
    };
</script>

<style scoped>
</style>

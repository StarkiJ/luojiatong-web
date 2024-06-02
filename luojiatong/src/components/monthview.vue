<template>
    <div id="MonthView-Head" class="p-4 font-bold text-2xl">
        <el-icon size="25" style="vertical-align: middle">
            <Calendar />
        </el-icon>
        <span style="vertical-align: middle"> 月历</span>
        <!-- <el-button type="text" class="float-right" @click="affairList0()">刷新</el-button> -->
    </div>
    <el-calendar>
        <template #date-cell="{ data }">
            <p :class="data.isSelected ? 'is-selected' : ''">
                {{ data.day.split('-').slice(1).join('-') }}
            </p>
            <el-scrollbar max-height="calc(100% - 15px)">
                <p v-for="(event, index) in getEventsByDate(data.day)" :key="index" :class="getCardClass(event.type)">
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
            <el-icon style="vertical-align: middle">
                <Clock />
            </el-icon>
            <span style="vertical-align: middle" class='p-2'>
                {{ showTime(selectedEvent?.startTime) }} - {{ showTime(selectedEvent?.endTime) }}
            </span>
        </div>
        <div class='p-1'>
            <el-icon style="vertical-align: middle">
                <Menu />
            </el-icon>
            <span style="vertical-align: middle" class='p-2'>
                {{ eventType(selectedEvent?.type) }}
            </span>
        </div>
        <div class='p-1'>
            <el-icon style="vertical-align: middle">
                <Location />
            </el-icon>
            <span style="vertical-align: middle" class='p-2'>
                {{ selectedEvent?.place }}
            </span>
        </div>
        <div class='p-1'>
            <el-icon style="vertical-align: middle">
                <MoreFilled />
            </el-icon>
            <span style="vertical-align: middle" class='p-2'>
                {{ selectedEvent?.content }}
            </span>
        </div>

        <template #footer>
            <div class="dialog-footer">
                <el-button type="danger" @click="onDelete(selectedEvent)">删除</el-button>
                <el-button type="primary" @click="editEvent(selectedEvent)">编辑</el-button>                
                <el-button @click="eventDetailVisible = false">确定</el-button>
            </div>
        </template>
    </el-dialog>
    
    <!-- 编辑日程 -->
    <el-dialog v-model="editEventDialogVisible" title="编辑日程" width="500">
        <el-form :model="editForm" label-width="auto" style="max-width: 480px">
            <el-form-item label="名称">
                <el-input v-model="editForm.name" />
            </el-form-item>

            <el-form-item label="时间">
                <el-col :span="11">
                    <el-date-picker v-model="editForm.startTime" type="datetime" placeholder="开始时间"
                        format="YYYY-MM-DD HH:mm:ss" value-format="YYYY-MM-DD HH:mm:ss" style="width: 100%" />
                </el-col>
                <el-col :span="2" class="text-center">
                    <span class="text-gray-500">-</span>
                </el-col>
                <el-col :span="11">
                    <el-date-picker v-model="editForm.endTime" type="datetime" placeholder="结束时间"
                        format="YYYY-MM-DD HH:mm:ss" value-format="YYYY-MM-DD HH:mm:ss" style="width: 100%" />
                </el-col>
            </el-form-item>

            <el-form-item label="类型">
                <el-select v-model="editForm.type">
                    <el-option label="课程" value="1" />
                    <el-option label="运动" value="2" />
                    <el-option label="图书馆" value="3" />
                    <el-option label="其他" value="4" />
                </el-select>
            </el-form-item>

            <el-form-item label="地点">
                <el-input v-model="editForm.place" />
            </el-form-item>

            <el-form-item label="备注">
                <el-input v-model="editForm.content" type="textarea" />
            </el-form-item>
        </el-form>

        <template #footer>
            <div class="dialog-footer">
                <el-button type="primary" @click="onEditSubmit(editForm)">保存</el-button>
                <el-button @click="editEventDialogVisible = false">取消</el-button>
            </div>
        </template>
    </el-dialog>
</template>

<script setup>
import { ref, computed, reactive } from 'vue';
import { getAffairs } from '@/api/affairs.js';
//import { getEventsByDate } from '@/components/showEventDetail.js';

// const affairs = ref([
//     {
//         "id": 12,
//         "type": 3,
//         "name": "考研数学",
//         "place": "总图",
//         "content": "好好学习",
//         "startTime": "2024-06-21T15:00:00",
//         "endTime": "2024-06-21T17:00:00"
//     },
//     {
//         "id": 4,
//         "type": 2,
//         "name": "羽毛球",
//         "place": "卓尔体育馆",
//         "content": null,
//         "startTime": "2024-06-2T15:00:00",
//         "endTime": "2024-06-2T17:00:00"
//     },
// ])

const eventType = (type) => {
    switch (type) {
        case 1:
            return '课程';
        case 2:
            return '运动';
        case 3:
            return '图书馆';
        case 4:
            return '其他';
        default:
            return '其他';
    }
}

const getCardClass = (type) => {
    switch (type) {
        case 1:
            return 'type1';
        case 2:
            return 'type2';
        case 3:
            return 'type3';
        case 4:
            return 'type4';
        default:
            return 'type4';
    }
};

let affairs = ref([
    {
        id: 12, // ID，由MySQL自动生成
        type: 3, // 类型，1-课程 2-运动 3-图书馆 4（默认）-其他
        name: "数学", // 名称，必填
        place: "图", // 地点
        content: "学习", // 备注
        startTime: "2024-06-21T15:00:00", // 开始时间，必填，格式为YYYY-MM-DD HH-mm-ss
        endTime: "2024-06-21T17:00:00" // 中间的T为SpringBoot自动生成，输出时去掉
    },
    {
        id: 4,
        type: 2,
        name: "羽毛球",
        place: "体育馆",
        content: null,
        startTime: "2024-06-23T15:00:00",
        endTime: "2024-06-23T17:00:00"
    },
])

const eventDetailVisible = ref(false);
const selectedEvent = ref(null);

const showEventDetail = (event) => {
    selectedEvent.value = event;
    eventDetailVisible.value = true;
};

//获取事务列表数据
const affairList = async (type, name, place, content, startTime, endTime) => {
    let params = {
        type: type,
        name: name,
        place: place,
        content: content,
        startTime: startTime,
        endTime: endTime
    }
    // console.log("before: ");
    // console.log(affairs.value);
    //console.log(params);
    let result = await getAffairs(params);
    // console.log("r: ");
    // console.log(result);

    //渲染视图
    affairs.value = result.data;
    // console.log("a: ");
    // console.log(affairs.value);
}
affairList();


// 获取指定日期的事件
const getEventsByDate = (date) => {
    // console.log(date);
    // console.log(affairs.value.filter(event => comp(event, date)));
    return affairs.value.filter(event => comp(event, date));
};

const comp = (event, date) => {
    const start = date + 'T' + '00:00:00';
    const end = date + 'T' + '23:59:59';
    //console.log(event);
    // console.log(Date.parse(event.endTime));
    // console.log(Date.parse(start));
    // console.log(Date.parse(event.startTime));
    // console.log(Date.parse(end));
    //console.log((Date.parse(event.endTime) >= Date.parse(start) && Date.parse(event.startTime) <= Date.parse(end)));
    return (Date.parse(event.endTime) >= Date.parse(start) && Date.parse(event.startTime) <= Date.parse(end));
}

const showTime=(time)=>{
    return time.split("T").join(" ");
}

const editEventDialogVisible = ref(false)

const editForm = reactive({
    type: "",
    name: "",
    place: "",
    content: "",
    startTime: "",
    endTime: ""
})

const editEvent = (event) => {
    editForm.type = event.type
    editForm.name = event.name
    editForm.place = event.place
    editForm.content = event.content
    editForm.startTime = event.startTime
    editForm.endTime = event.endTime
    editEventDialogVisible.value = true
}

const onEditSubmit = async (editForm) => {
    editForm.startTime = editForm.startTime.split(" ").join("T");
    editForm.endTime = editForm.endTime.split(" ").join("T");
    console.log(editForm)
}

const onDelete = async (event) => {
    console.log("删除日程id: ", event.id)
}


</script>

<style scoped>
.is-selected {
    color: #14b8a6;
}

.EventInCalendar {
    @apply 
    bg-teal-100 rounded-default p-1 my-1;
}

.type1 {
    @apply
    bg-cyan-200
    rounded-default p-1 my-1;
}
.type2 {
    @apply
    bg-amber-100
    rounded-default p-1 my-1;
}
.type3 {
    @apply
    bg-green-100
    rounded-default p-1 my-1;
}
.type4 {
    @apply
    bg-gray-200
    rounded-default p-1 my-1;
}
</style>

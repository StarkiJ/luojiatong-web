<template>
    <div id="DayView-Head" class="p-4 text-2xl">
        <el-icon size="25" style="vertical-align: middle">
            <List />
        </el-icon>
        <span style="vertical-align: middle"> 本日事务</span>
    </div>

    <el-scrollbar max-height="400px" style="max-width: 600px">
        <div id="TimeLine">
            <el-timeline style="max-width: 600px">
                <el-timeline-item placement="top" v-for="(event, index) in todayEvents" :key="index"
                    :timestamp="showTime(event.startTime)" @click.native="showEventDetail(event)">
                    <el-card style="max-width: 480px" :class="getCardClass(event.type)">
                        <el-row>
                            <el-col :span="8">
                                <div class="text-2xl font-bold p-2">
                                    {{ event.name }}
                                </div>
                            </el-col>
                            <el-col :span="16">
                                <div class='p-1'>
                                    <el-icon style="vertical-align: middle">
                                        <Clock />
                                    </el-icon>
                                    <span style="vertical-align: middle" class='p-2'>{{ showTime(event.startTime) }} -
                                        {{
                                            showTime(event.endTime) }}</span>
                                </div>
                                <div class='p-1'>
                                    <el-icon style="vertical-align: middle">
                                        <Location />
                                    </el-icon>
                                    <span style="vertical-align: middle" class='p-2'>{{ event.place }}</span>
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
import { ref, reactive } from 'vue';
import { DeleteAffair, UpdateAffair, getAffairs } from '@/api/affairs.js';
import { ElMessage } from 'element-plus'
//import { events } from './showEventDetail.js';


let todayEvents = ref([
    {
        id: 12,
        type: 3,
        name: "数学",
        place: "图",
        content: "学习",
        startTime: "2024-06-01T15:00:00",
        endTime: "2024-06-01T17:00:00"
    },
    {
        id: 4,
        type: 2,
        name: "羽毛球",
        place: "体育馆",
        content: null,
        startTime: "2024-06-01T18:00:00",
        endTime: "2024-06-01T19:00:00"
    },
])

const eventDetailVisible = ref(false);
const selectedEvent = ref(null);

// const today = new Date();
// const todayStr = ('0' + (today.getMonth() + 1)).slice(-2) + '-' + ('0' + today.getDate()).slice(-2);
// const todayEvents = events.filter(event => event.startTime === todayStr);

const getCurrentDate = () => {
    let now = new Date();
    const year = now.getFullYear();
    const month = (now.getMonth() + 1).toString().padStart(2, '0');
    const day = now.getDate().toString().padStart(2, '0');
    return year + "-" + month + "-" + day;
}
let today = getCurrentDate();
console.log(today);
const startTime = today + 'T' + '00:00:00';
const endTime = today + 'T' + '23:59:59';

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
            return '未知';
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
            return '';
    }
};

const affairList = async (type, name, place, content, startTime, endTime) => {
    let params = {
        type: type,
        name: name,
        place: place,
        content: content,
        startTime: startTime,
        endTime: endTime
    }
    // console.log(params);
    let result = await getAffairs(params);
    // console.log("result: ");
    // console.log(result);

    //渲染视图
    todayEvents.value = result.data;
}
affairList(null, null, null, null, startTime, endTime);

const showEventDetail = (event) => {
    selectedEvent.value = event;
    eventDetailVisible.value = true;
};

const showTime = (time) => {
    return time.split("T").join(" ");
}

const editEventDialogVisible = ref(false)

const editForm = reactive({
    id: 0,
    type: 0,
    name: "",
    place: "",
    content: "",
    startTime: "",
    endTime: ""
})

const editEvent = (event) => {
    editForm.id = event.id
    editForm.type = event.type.value
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

    //调用接口
    let result = await UpdateAffair(editForm);
    console.log(result)

    ElMessage.success(result.msg ? result.msg : '添加成功');
    //affairList(null, null, null, null, startTime, endTime);
    this.$router.go(0);
}

const onDelete = async (event) => {
    let ids = [];
    ids.push(event.id);
    console.log("删除日程id: ", ids)
    let result = await DeleteAffair(ids);
    console.log(result)

    ElMessage.success(result.msg ? result.msg : '删除成功');
    location.reload();
}

</script>


<style scoped>
.type1 {
    @apply bg-cyan-200;
}

.type2 {
    @apply bg-amber-100;
}

.type3 {
    @apply bg-green-100;
}

.type4 {
    @apply bg-gray-200;
}
</style>

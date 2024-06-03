<template>
    <el-menu
        default-active="2"
        class="el-menu-vertical-demo"
        :collapse="isCollapse"
        background-color="#ccfbf1"
        active-text-color="#14b8a6"
        @open="handleOpen"
        @close="handleClose">
        <el-menu-item index="1">
            <el-icon class="collapse-btn" @click="collapseNav">
                <Fold />
            </el-icon>
            <span style="vertical-align: middle">折叠</span>
        </el-menu-item>

        <el-sub-menu index="2">
            <template #title>
                <el-icon><Calendar /></el-icon>
                <span>日程管理</span>
            </template>
            <el-menu-item-group title="课程管理">
                <el-menu-item index="2-1">
                    <el-icon><School /></el-icon>
                    <span>导入课表</span>
                </el-menu-item>
                <el-menu-item index="2-2">
                    <el-icon><Plus /></el-icon>
                    <span>新增课程</span>
                </el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="待办事项">
                <el-menu-item index="2-3">
                    <el-icon><Plus /></el-icon>
                    <span @click="createNewEvent = true">
                        新建日程
                    </span>
                </el-menu-item>
            </el-menu-item-group>
        </el-sub-menu>

        <el-sub-menu index="3">
            <template #title>
                <el-icon><School /></el-icon>
                <span>场馆预约</span>
            </template>
            <el-menu-item-group title="场馆预约">
                <el-menu-item index="3-1">
                    <el-icon><Reading /></el-icon>
                    <span>图书馆</span>
                </el-menu-item>
                <el-menu-item index="3-2">
                    <el-icon><Basketball /></el-icon>
                    <span>体育馆</span>
                </el-menu-item>
            </el-menu-item-group>
        </el-sub-menu>

        <el-sub-menu index="4">
            <template #title>
                <el-icon><TrendCharts /></el-icon>
                <span>学习助手</span>
            </template>
            <el-menu-item-group title="学习助手">
                <el-menu-item index="4-1">
                    <el-icon><Monitor /></el-icon>
                    <span>成绩计算</span>
                </el-menu-item>
                <el-menu-item index="4-2">
                    <el-icon><Guide /></el-icon>
                    <span>查给分</span>
                </el-menu-item>
            </el-menu-item-group>
        </el-sub-menu>
        
    </el-menu>

    <!-- 新建日程 -->
    <el-dialog v-model="createNewEvent" title="新建日程" width="500">
        <el-form :model="form" label-width="auto" style="max-width: 480px">
            <el-form-item label="名称">
                <el-input v-model="form.name" />
            </el-form-item>

            <el-form-item label="时间">
                <el-col :span="11">
                    <el-date-picker v-model="form.startTime" type="datetime" placeholder="开始时间"
                        format="YYYY-MM-DD HH:mm:ss" value-format="YYYY-MM-DD HH:mm:ss" style="width: 100%" />
                </el-col>
                <el-col :span="2" class="text-center">
                    <span class="text-gray-500">-</span>
                </el-col>
                <el-col :span="11">
                    <el-date-picker v-model="form.endTime" type="datetime" placeholder="结束时间"
                        format="YYYY-MM-DD HH:mm:ss" value-format="YYYY-MM-DD HH:mm:ss" style="width: 100%" />
                </el-col>
            </el-form-item>

            <el-form-item label="类型">
                <el-select v-model="form.type" @change="$forceUpdate()">
                    <el-option label="课程" value="1" />
                    <el-option label="运动" value="2" />
                    <el-option label="图书馆" value="3" />
                    <el-option label="其他" value="4" />
                </el-select>
            </el-form-item>

            <el-form-item label="地点">
                <el-input v-model="form.place" />
            </el-form-item>

            <el-form-item label="备注">
                <el-input v-model="form.content" type="textarea" />
            </el-form-item>
        </el-form>

        <template #footer>
            <div class="dialog-footer">
                <el-button type="primary" @click="onSubmit(form)">Create</el-button>
                <el-button @click="createNewEvent = false">Cancel</el-button>
            </div>
        </template>
    </el-dialog>
</template>

<script setup>
    import { reactive, ref, toRefs, onMounted  } from 'vue'
    import { AddAffair } from '@/api/affairs';
    import { ElMessage } from 'element-plus';
    import * as ElementPlusIconsVue from '@element-plus/icons-vue'

    // 新建日程
    const createNewEvent = ref(false)

    //增加事务模型
    const form = reactive({
        type: 0,
        name: "",
        place: "",
        content: "",
        startTime: "",
        endTime: ""
    })

    const onSubmit = async (form) => {
        form.startTime = form.startTime.split(" ").join("T");
        form.endTime= form.endTime.split(" ").join("T");
        //console.log(form)
        //调用接口
        let result = await AddAffair(form);
        //console.log(result)

        ElMessage.success(result.msg ? result.msg : '添加成功');
        location.reload();
    }

    // 处理菜单折叠
    const isCollapse = ref(true)
    const collapseNav = () => {
        isCollapse.value = !isCollapse.value;
    }

    const handleOpen = (key, keyPath) => {
    console.log(key, keyPath)
    }
    const handleClose = (key, keyPath) => {
    console.log(key, keyPath)
    }
</script>

<style scoped>
    .el-menu-vertical-demo:not(.el-menu--collapse) {
        width: 200px;
        min-height: 100%;
    }
    
    .collapse-btn {
        font-size: 24px;
        margin-right: 10px;
        color: #545c64;
        padding-top: 6px;
        vertical-align: middle;
    }
</style>
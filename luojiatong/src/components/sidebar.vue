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
                    <!-- 折叠状态下点这个会有问题 -->
                    <el-icon><Plus /></el-icon>
                    <createNewEvent />
                    <!-- <span>新建日程</span> -->
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
</template>

<script setup>
    import { reactive, ref, toRefs, onMounted  } from 'vue'
    import createNewEvent from '../components/createNewEvent.vue'
    import * as ElementPlusIconsVue from '@element-plus/icons-vue'

    // 菜单部分
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
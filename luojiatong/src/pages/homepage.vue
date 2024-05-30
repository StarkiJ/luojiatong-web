<template>
  <div class="common-layout">
    <el-header class="homepage-header">
        <div>
            <span>珞珈通</span>
        </div>
    </el-header>
    <el-container>
        <!-- 侧边栏 -->
        <Sidebar />
        <el-main>
            <el-row :gutter="10" class="homepage-main">
                <el-col :lg="8" class="left">
                    <!-- 左侧内容：待办清单/本日日程 -->   
                    <DayView />
                </el-col>
                <el-col :lg="16" :md="12" class="bg-light-100">
                    <!-- 右侧内容：月历 -->
                    <MonthView />
                </el-col>
                
            </el-row>
        </el-main>
    </el-container>
  </div>
  <!-- 路由占位符 -->
  <router-view></router-view>
</template>

<script setup>
    import { reactive, ref, toRefs, onMounted  } from 'vue'
    import * as ElementPlusIconsVue from '@element-plus/icons-vue'
    import { ElMessage, ElMessageBox } from "element-plus"
    import DayView from '../components/dayview.vue'
    import MonthView from '../components/monthview.vue'
    import Sidebar from '../components/sidebar.vue'

    document.title = '珞珈通-主页'

</script>

<style scoped>
    .homepage-header{
        @apply 
        flex
        bg-teal-500
        text-light-50
        font-bold
        text-4xl
        items-center
        ;
    }
    .homepage-main {
        @apply
        bg-light-100
        min-h-screen
        ;
    }
    
</style>
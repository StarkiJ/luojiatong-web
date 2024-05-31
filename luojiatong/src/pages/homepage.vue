<template>
    <div class="common-layout">
      <el-header class="homepage-header">
          <div>
              <span>珞珈通</span>
          </div>
      </el-header>
      <el-container class="main-container">
          <!-- 侧边栏 -->
          <Sidebar class="sidebar"/>
          <el-main>
              <el-row :gutter="10" class="homepage-main">
                  <el-col :xl="8" :lg="16" :md="12" class="left">
                      <!-- 左侧内容：待办清单/本日日程 -->   
                      <DayView />
                  </el-col>
                  <el-col :xl="16" :lg="8" :md="12" class="bg-light-100">
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
  .common-layout {
      height: 100vh;
      width: 100vw;
      display: flex;
      flex-direction: column;
  }
  
  .homepage-header {
      @apply 
      flex
      bg-teal-500
      text-light-50
      font-bold
      text-4xl
      items-center;
      width: 100%;
  }
  
  .main-container {
      flex: 1;
      display: flex;
  }
  
  .sidebar {
      height: 100%; /* 确保侧边栏填充整个高度 */
      background-color: #ccfbf1;
  }
  
  .homepage-main {
      @apply
      bg-light-100
      flex-1;
  }
  
  .el-container {
      @apply
      flex-1;
      display: flex;
  }
  
  .el-main {
      @apply
      flex-1;
      overflow: auto;
  }
  </style>
  
import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import WindiCSS from 'vite-plugin-windicss'

import path from 'node:path'

// https://vitejs.dev/config/
export default defineConfig({
  // base: 'D:/WorkSpace/luojiatong-web/luojiatong/dist',
  base: "./",
  plugins: [
    vue(),
    WindiCSS(),
  ],
  resolve: {
    alias: {
      "~":path.resolve(__dirname, "src"), // src
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server:{
    proxy:{
      '/api':{//获取路径中包含了/api的请求
          target:'http://localhost:8080',//后台服务所在的源
          changeOrigin:true,//修改源
          rewrite:(path)=>path.replace(/^\/api/,'')///api替换为''
      }
    }
  }
})

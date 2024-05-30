<template>
    <el-row class="login-container">
        <el-col :lg="16" :md="12" class="left">
            <div>
                <div>珞珈通</div>
                <div>智慧珞珈Lite</div>
            </div>
        </el-col>
        <el-col :lg="8" class="right">
            <div class="title">
                    欢迎回来
            </div>
            <div>
                <el-form ref="formRef" model="form" label-width="auto" style="max-width: 600px">
                    <el-form-item label="账号" prop="username">
                        <el-input 
                            v-model="form.username" 
                            placeholder='请输入用户名'>
                            <template #prefix>
                                <el-icon><User /></el-icon>
                            </template>
                        </el-input>
                    </el-form-item>
                    <el-form-item label="密码" prop="password">
                        <el-input 
                            v-model="form.password"
                            type="password" 
                            placeholder='请输入密码'
                            show-password>
                            <template #prefix>
                                <el-icon><Lock /></el-icon>
                            </template>
                        </el-input>
                    </el-form-item>
                </el-form>
            </div>
            <div>
                <el-button class="bg-teal-500" type="primary" @click="onSubmit">Login</el-button>
            </div>
        </el-col>

    </el-row>
</template>

<script setup>
    import { reactive, ref } from 'vue'
    // import { User } from '@element-plus/icons-vue'
    import * as ElementPlusIconsVue from '@element-plus/icons-vue'

    document.title = '珞珈通-登录'

    const form = reactive({
    username: '',
    password: '',
    })

    const formRef = ref(null) // 变成响应式的

    const onSubmit = () => {
        formRef.value.validate((valid)=>{
            if(!valid){
                return false
            }
            console.log('验证通过')
        })
    }

    const rules = {
        username:[
            { 
                required: true,
                message: '用户名不能为空',
                trigger: 'blur' 
            },
            { 
                min: 3,
                max: 5, 
                message: '用户名长度必须为3-5个字符', 
                trigger: 'blur' 
            },
        ],
        password:[
            {   
                required: true,
                message: '请输入密码',
                trigger: 'blur' 
            },
        ],
    }

</script>

<style scope>
.login-container{
    @apply min-h-screen bg-teal-500;
}

.login-container .left, .login-container .right{
    @apply flex items-center justify-center flex-col;
}
.left>div>div:first-child{
    @apply font-bold text-5xl text-light-50 mb-4;
}
.left>div>div:last-child{
    @apply text-light-50;
}

.login-container .right{
    @apply  bg-light-100 flex items-center justify-center flex-col;
}
.right .title{
    @apply font-bold text-3xl mb-8;
}


</style>
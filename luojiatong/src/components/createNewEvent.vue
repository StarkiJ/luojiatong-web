<template>

    <span @click="createNewEvent = true">
        新建日程
    </span>  

    <el-dialog v-model="createNewEvent" title="新建日程" width="500">
        <el-form :model="form"
            label-width="auto" 
            style="max-width: 480px"
        >
            <el-form-item label="名称">
                <el-input v-model="form.name" />
            </el-form-item>
            
            <el-form-item label="时间">
                <el-col :span="11">
                    <el-date-picker
                    v-model="form.startTime"
                    type="datetime"
                    placeholder="开始时间"
                    style="width: 100%"
                    />
                </el-col>
                <el-col :span="2" class="text-center">
                    <span class="text-gray-500">-</span>
                </el-col>
                <el-col :span="11">
                    <el-date-picker
                    v-model="form.endTime"
                    type="datetime"
                    placeholder="结束时间"
                    style="width: 100%"
                    />
                </el-col>
            </el-form-item>

            <el-form-item label="类型">
                <el-select v-model="form.type">
                    <el-option label="课程" value="课程" />
                    <el-option label="运动" value="运动" />
                    <el-option label="图书馆" value="图书馆" />
                    <el-option label="其他" value="其他" />
                </el-select>
            </el-form-item>

            <el-form-item label="地点">
                <el-input v-model="form.location" />
            </el-form-item>
            
            <el-form-item label="备注">
                <el-input v-model="form.desc" type="textarea" />
            </el-form-item>
        </el-form>

        <template #footer>
            <div class="dialog-footer">
                <el-button type="primary" @click="onSubmit">Create</el-button>
                <el-button @click="createNewEvent = false">Cancel</el-button>
            </div>
        </template>
    </el-dialog>

</template>

<script setup>
    import { ref, reactive } from 'vue'

    const createNewEvent = ref(false)

    const form = reactive({
        name: '',
        startTime: '',
        endTime: '',
        location: '',
        desc: '',
    })

    const onSubmit = () => {
        console.log('submit!')
    }

</script>
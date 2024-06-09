import request from '@/utils/request.js'


//测试hello
export const hello = () => {
    //const tokenStore = useTokenStore();
    //在pinia中定义的响应式数据,都不需要.value
    //return request.get('/category',{headers:{'Authorization':tokenStore.token}})
    return request.get('/affairs/hello')
}

//事务条件查询
export const getAffairs = (params) => {
    //const tokenStore = useTokenStore();
    //在pinia中定义的响应式数据,都不需要.value
    //return request.get('/category',{headers:{'Authorization':tokenStore.token}})
    return request.get('/affairs', { params: params })
}

//事务添加
export const AddAffair = (affair) => {
    return request.post('/affairs', affair)
}

//事务修改
export const UpdateAffair = (affair) => {
    return request.put('/affairs', affair)
}

//事务删除
export const DeleteAffair = (ids) => {
    return request.delete('/affairs/' + ids)
}

//课程删除
export const DeleteCourse = (names) => {
    return request.delete('/affairs/course/' + names)
}

//课程更新
export const UpdateCourse = (names) => {
    return request.get('/affairs/course')
}
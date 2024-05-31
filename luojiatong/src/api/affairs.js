import request from '@/utils/request.js'


//测试hello
export const hello = () => {
    //const tokenStore = useTokenStore();
    //在pinia中定义的响应式数据,都不需要.value
    //return request.get('/category',{headers:{'Authorization':tokenStore.token}})
    return request.get('/affairs/hello')
}

//事务条件查询
export const getAffairs = (affair) => {
    //const tokenStore = useTokenStore();
    //在pinia中定义的响应式数据,都不需要.value
    //return request.get('/category',{headers:{'Authorization':tokenStore.token}})
    return request.get('/affairs', affair)
}

//事务添加
export const AddAffair = (affair) => {
    return request.post('/affairs', affair)
}

//事务修改
export const articleCategoryUpdateService = (categoryData) => {
    return request.put('/affairs', categoryData)
}

//事务删除
export const articleCategoryDeleteService = (id) => {
    return request.delete('/affairs?id=' + id)
}
function $2(tagName){
    // 返回节点数组
    var elems =  document.getElementsByTagName(tagName);
    return elems;
}

function $(tagName){
    // 函数接收字符字符串参数,表示标签名
    // 获取元素节点,不能用标签名直接获取,用get方法获取属性值
    var elem =  document.getElementsByTagName(tagName)[0];
    return elem;
}
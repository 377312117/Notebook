/*轮播图
获取所有的图片标签
每隔一秒切换()
    变更下标,取图片元素,控制显示和隐藏
    var imgs;
    setInterval()
    function (){
        imgIndex ++;
        imageIndex对应的元素时显示的,其他的隐藏
        下标越界判断
    }
2.做轮播图的下标
    显示在图片上方
*/
// 图片轮播
$(function(){
    var imgIndex=0;//图片下标
    var timeId; //保存定时器id
    setInterval(autoPlay,1000);  //开启定时器
    // 定时器方法,每隔一秒执行一次
    function  autoPlay(){
    // 获取图片,根据下标显示或者隐藏
    // 隐藏当前下标对应的图片
        $('.banner img').eq(imgIndex).css('display','none');
        // 更新下标防止越界,先自增再做越界处理
        imgIndex = ++imgIndex == $('.banner img').length ? 0 : imgIndex;
        // 显示下一张图片
        $('.banner img').eq(imgIndex).css('display','block');
        // 所有图标索引更改为默认颜色
        $('.imgNav li').each(function(){
            // 遍历数组,对每个元素修改背景颜色
            // this指代当前对象
            $(this).css('background','grey');
        });
        // 切换下标,更改背景颜色
        $('.imgNav li').eq(imgIndex).css('background','red');
        // $('.imgNav li').eq(imgIndex-1).css('background','grey');
    };
    
    $('.banner').mouseover(function(){
        clearInterval(timeId);
    });

    $('.banner').mouseout(function(){
        timeId=setInterval(autoPlay,1000);
    });
    // 鼠标点击下标切换图片
    $('.imgNav li').each(function(){
        // 遍历li元素,为每个元素添加点击事件
        $(this).click(function(){
            // 点击切换时,停止定时器
            clearInterval(timeId);
            // 被点击的li元素背景为红色,其他li为灰色
            $(this).css('background','red').siblings().css('background','grey');
            var index = $(this).index();
            $(".banner img").eq(index).css('display','block').siblings().css('display','none');
            imgIndex=index;
            // 点击切换完成后开启定时器
            timeId=setInterval(autoPlay,1000);
        });
    });
});
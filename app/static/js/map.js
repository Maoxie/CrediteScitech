/**
 * Created by yzt on 2017/9/23.
 */

// 百度地图API功能
let scale = 18;
let map = new BMap.Map("allmap");
let point = new BMap.Point(116.328243,39.982622);
let marker = new BMap.Marker(point);  // 创建标注
map.addOverlay(marker);              // 将标注添加到地图中
map.centerAndZoom(point, scale);
map.enableScrollWheelZoom();				// 启用滚轮放大缩小
map.disableDoubleClickZoom();				// 禁止双击放大
map.addOverlay(marker);						// 添加一个小圆点
let opts = {
  width : 200,     // 信息窗口宽度
  height: 100,     // 信息窗口高度
  title : "启信信息科技有限公司" , // 信息窗口标题
  enableMessage:true,//设置允许信息窗发送短息
  message:"海淀黄庄地铁站旁，北京海诚公证处对面"
};
let infoWindow = new BMap.InfoWindow("海淀黄庄地铁站旁，北京海诚公证处对面", opts);  // 创建信息窗口对象
marker.addEventListener("click", function(){
    map.openInfoWindow(infoWindow,point); //开启信息窗口
});

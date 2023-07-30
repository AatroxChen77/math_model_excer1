# math_model_excer1
数学建模第一次磨合练习：出租车供求匹配与补贴方案

```
math_model_excer1                                                 //
├─ .git                                                           //
│  ├─ COMMIT_EDITMSG                                              //
│  ├─ config                                                      //
│  ├─ description                                                 //
│  ├─ FETCH_HEAD                                                  //
│  ├─ fsmonitor--daemon                                           //
│  │  └─ cookies                                                  //
│  ├─ HEAD                                                        //
│  ├─ hooks                                                       //
│  │  ├─ applypatch-msg.sample                                    //
│  │  ├─ commit-msg.sample                                        //
│  │  ├─ fsmonitor-watchman.sample                                //
│  │  ├─ post-update.sample                                       //
│  │  ├─ pre-applypatch.sample                                    //
│  │  ├─ pre-commit.sample                                        //
│  │  ├─ pre-merge-commit.sample                                  //
│  │  ├─ pre-push.sample                                          //
│  │  ├─ pre-rebase.sample                                        //
│  │  ├─ pre-receive.sample                                       //
│  │  ├─ prepare-commit-msg.sample                                //
│  │  ├─ push-to-checkout.sample                                  //
│  │  └─ update.sample                                            //
│  ├─ index                                                       //
│  ├─ info                                                        //
│  │  └─ exclude                                                  //
│  ├─ logs                                                        //
│  │  ├─ HEAD                                                     //
│  │  └─ refs                                                     //
│  │     ├─ heads                                                 //
│  │     │  ├─ main                                               //
│  │     │  └─ test                                               //
│  │     ├─ remotes                                               //
│  │     │  └─ origin                                             //
│  │     │     ├─ HEAD                                            //
│  │     │     └─ main                                            //
│  │     └─ stash                                                 //
│  ├─ objects                                                     //
│  │  ├─ 02                                                       //
│  │  │  └─ 922bd1b75e9ed0f91a5f8896547ecce7c51bd3                //
│  │  ├─ 24                                                       //
│  │  │  └─ e9ea2f0961ec611ce6b4158a6be93014f368ce                //
│  │  ├─ 2a                                                       //
│  │  │  ├─ 39208b1de4b749a8ae9bbbf11ce8b5697afde7                //
│  │  │  └─ f001ae308f06c01403c420b6ccdf369a16a988                //
│  │  ├─ 2b                                                       //
│  │  │  ├─ 141d359db56595278d4015519c4232f0048294                //
│  │  │  └─ 95b0126a49efac9ea2d045b16a93653187f22e                //
│  │  ├─ 30                                                       //
│  │  │  └─ 22770bd4f08c595f2335b4e2c226c704b85985                //
│  │  ├─ 36                                                       //
│  │  │  └─ d73e89a19e9146bcb3bb96bf6197a08c2dc012                //
│  │  ├─ 37                                                       //
│  │  │  └─ 6dc8f5de0a40f23c6c3f8aaa11ade8f9c7042e                //
│  │  ├─ 3e                                                       //
│  │  │  └─ 416fc905c4cd045610dbda742a2073e9b4003c                //
│  │  ├─ 45                                                       //
│  │  │  └─ 9cd6934c39fe73b0b8bf9ccd1b8c1a06637221                //
│  │  ├─ 48                                                       //
│  │  │  └─ 97627a93b10b36f8af82843aff9635f646a917                //
│  │  ├─ 4f                                                       //
│  │  │  └─ af59e1999baa416fdbf46d80b2c77e970d927a                //
│  │  ├─ 51                                                       //
│  │  │  └─ 5c3bad15b917ea79acb386ef2af4a32f6acc55                //
│  │  ├─ 5b                                                       //
│  │  │  └─ 6af76737307e6e6f477cdd406e0aa648d57880                //
│  │  ├─ 5e                                                       //
│  │  │  └─ 76c4d8f4a33370ea5eb44cf64611964e7d833f                //
│  │  ├─ 70                                                       //
│  │  │  └─ ba4e34d4208e37b4b06bfbcd93e78d799e5950                //
│  │  ├─ 86                                                       //
│  │  │  └─ df1c36111fd7b88da67e8755651e4196863f2c                //
│  │  ├─ 8a                                                       //
│  │  │  └─ ef08ffaf8fd97d8f8b7f3973d895ad6924e9d4                //
│  │  ├─ 8b                                                       //
│  │  │  └─ 7c1c8c49c258c1c445009744c388f40c6fa20d                //
│  │  ├─ 9a                                                       //
│  │  │  └─ 29a9158d28ebf1ea43b21169ff8d28a2415eab                //
│  │  ├─ 9c                                                       //
│  │  │  └─ ab1177d6ca3b52bd7315315d1007679d839874                //
│  │  ├─ 9d                                                       //
│  │  │  └─ e9c771d99d4ec0b2d30c20721a99cfe2fadf8a                //
│  │  ├─ a3                                                       //
│  │  │  └─ d93080413be94382e207bab4c43043733e7c8a                //
│  │  ├─ b0                                                       //
│  │  │  └─ b1b5c2f1db07c9741189f194d615c1ea7530d2                //
│  │  ├─ c0                                                       //
│  │  │  └─ 019a11a7e804d9087488e3c73b9ab52d8158dd                //
│  │  ├─ c1                                                       //
│  │  │  └─ 61919ab67fc4fcd2b01cf0991a65bdae6c636e                //
│  │  ├─ ce                                                       //
│  │  │  └─ 2ed65e9ad6584e4aa257155dfd25dbf1ff9a36                //
│  │  ├─ d8                                                       //
│  │  │  └─ ca0c1aa22da9479d4b2e56ac3f865198eaa721                //
│  │  ├─ da                                                       //
│  │  │  └─ 55ebed00ec4cd51eb170e410c96a7e2e6c989e                //
│  │  ├─ f3                                                       //
│  │  │  └─ fbf24f20be41e76d570e5fa07f6b763232c9a1                //
│  │  ├─ fd                                                       //
│  │  │  └─ 619ba87afa6937db7210dd9cc0c8c61e39ff07                //
│  │  ├─ ff                                                       //
│  │  │  └─ 55e54e3ff17187d914812608428c94eadcd919                //
│  │  ├─ info                                                     //
│  │  └─ pack                                                     //
│  │     ├─ pack-de728d1e5b36743ea2c7a73e7e2f3ea793f918a2.idx     //
│  │     └─ pack-de728d1e5b36743ea2c7a73e7e2f3ea793f918a2.pack    //
│  ├─ ORIG_HEAD                                                   //
│  ├─ packed-refs                                                 //
│  └─ refs                                                        //
│     ├─ heads                                                    //
│     │  ├─ main                                                  //
│     │  └─ test                                                  //
│     ├─ remotes                                                  //
│     │  └─ origin                                                //
│     │     ├─ HEAD                                               //
│     │     └─ main                                               //
│     ├─ stash                                                    //
│     └─ tags                                                     //
├─ .gitignore                                                     //
├─ GPS_data                                                       //
│  ├─ all_txt_data                                                //
│  │  ├─ 20140803_train.txt                                       //
│  │  ├─ 交通赛数据_上                                                  //
│  │  │  ├─ 20140804_train.txt                                    //
│  │  │  ├─ 20140805_train.txt                                    //
│  │  │  ├─ 20140806_train.txt                                    //
│  │  │  ├─ 20140808_train.txt                                    //
│  │  │  ├─ 20140809_train.txt                                    //
│  │  │  ├─ 20140810_train.txt                                    //
│  │  │  ├─ 20140811_train.txt                                    //
│  │  │  ├─ 20140812_train.txt                                    //
│  │  │  ├─ 20140814_train.txt                                    //
│  │  │  └─ 20140815_train.txt                                    //
│  │  ├─ 交通赛数据_上.7z                                               //
│  │  ├─ 交通赛数据_下.7z                                               //
│  │  └─ 请替换-交通赛数据_下.7z-中的同名文件1117.7z                             //
│  ├─ concur.py                                                   //
│  ├─ data_process.ipynb                                          //
│  ├─ df_selected.pkl                                             //
│  └─ trip_df.csv                                                 //
├─ README.md                                                      //
└─ shape                                                          //
   ├─ Chengdu_shp                                                 //
   │  ├─ chengdu                                                  //
   │  │  ├─ chengdu.dbf                                           //
   │  │  ├─ chengdu.prj                                           //
   │  │  ├─ chengdu.sbn                                           //
   │  │  ├─ chengdu.sbx                                           //
   │  │  ├─ chengdu.shp                                           //
   │  │  ├─ chengdu.shp.xml                                       //
   │  │  └─ chengdu.shx                                           //
   │  └─ chengdu_city                                             //
   │     ├─ 九级路_polyline.dbf                                      //
   │     ├─ 九级路_polyline.prj                                      //
   │     ├─ 九级路_polyline.sbn                                      //
   │     ├─ 九级路_polyline.sbx                                      //
   │     ├─ 九级路_polyline.shp                                      //
   │     ├─ 九级路_polyline.shp.xml                                  //
   │     ├─ 九级路_polyline.shx                                      //
   │     ├─ 乡镇_point.dbf                                          //
   │     ├─ 乡镇_point.prj                                          //
   │     ├─ 乡镇_point.sbn                                          //
   │     ├─ 乡镇_point.sbx                                          //
   │     ├─ 乡镇_point.shp                                          //
   │     ├─ 乡镇_point.shp.xml                                      //
   │     ├─ 乡镇_point.shx                                          //
   │     ├─ 乡镇村道2_polyline.dbf                                    //
   │     ├─ 乡镇村道2_polyline.prj                                    //
   │     ├─ 乡镇村道2_polyline.sbn                                    //
   │     ├─ 乡镇村道2_polyline.sbx                                    //
   │     ├─ 乡镇村道2_polyline.shp                                    //
   │     ├─ 乡镇村道2_polyline.shp.xml                                //
   │     ├─ 乡镇村道2_polyline.shx                                    //
   │     ├─ 乡镇村道_polyline.dbf                                     //
   │     ├─ 乡镇村道_polyline.prj                                     //
   │     ├─ 乡镇村道_polyline.sbn                                     //
   │     ├─ 乡镇村道_polyline.sbx                                     //
   │     ├─ 乡镇村道_polyline.shp                                     //
   │     ├─ 乡镇村道_polyline.shp.xml                                 //
   │     ├─ 乡镇村道_polyline.shx                                     //
   │     ├─ 交通出行_point.dbf                                        //
   │     ├─ 交通出行_point.prj                                        //
   │     ├─ 交通出行_point.sbn                                        //
   │     ├─ 交通出行_point.sbx                                        //
   │     ├─ 交通出行_point.shp                                        //
   │     ├─ 交通出行_point.shp.xml                                    //
   │     ├─ 交通出行_point.shx                                        //
   │     ├─ 休闲娱乐_point.dbf                                        //
   │     ├─ 休闲娱乐_point.prj                                        //
   │     ├─ 休闲娱乐_point.sbn                                        //
   │     ├─ 休闲娱乐_point.sbx                                        //
   │     ├─ 休闲娱乐_point.shp                                        //
   │     ├─ 休闲娱乐_point.shp.xml                                    //
   │     ├─ 休闲娱乐_point.shx                                        //
   │     ├─ 住宿_point.dbf                                          //
   │     ├─ 住宿_point.prj                                          //
   │     ├─ 住宿_point.sbn                                          //
   │     ├─ 住宿_point.sbx                                          //
   │     ├─ 住宿_point.shp                                          //
   │     ├─ 住宿_point.shp.xml                                      //
   │     ├─ 住宿_point.shx                                          //
   │     ├─ 停车场_point.dbf                                         //
   │     ├─ 停车场_point.prj                                         //
   │     ├─ 停车场_point.sbn                                         //
   │     ├─ 停车场_point.sbx                                         //
   │     ├─ 停车场_point.shp                                         //
   │     ├─ 停车场_point.shp.xml                                     //
   │     ├─ 停车场_point.shx                                         //
   │     ├─ 公安交警_point.dbf                                        //
   │     ├─ 公安交警_point.prj                                        //
   │     ├─ 公安交警_point.sbn                                        //
   │     ├─ 公安交警_point.sbx                                        //
   │     ├─ 公安交警_point.shp                                        //
   │     ├─ 公安交警_point.shp.xml                                    //
   │     ├─ 公安交警_point.shx                                        //
   │     ├─ 兴趣区界_region.dbf                                       //
   │     ├─ 兴趣区界_region.prj                                       //
   │     ├─ 兴趣区界_region.sbn                                       //
   │     ├─ 兴趣区界_region.sbx                                       //
   │     ├─ 兴趣区界_region.shp                                       //
   │     ├─ 兴趣区界_region.shp.xml                                   //
   │     ├─ 兴趣区界_region.shx                                       //
   │     ├─ 其他_point.dbf                                          //
   │     ├─ 其他_point.prj                                          //
   │     ├─ 其他_point.sbn                                          //
   │     ├─ 其他_point.sbx                                          //
   │     ├─ 其他_point.shp                                          //
   │     ├─ 其他_point.shp.xml                                      //
   │     ├─ 其他_point.shx                                          //
   │     ├─ 其他设施2_point.dbf                                       //
   │     ├─ 其他设施2_point.prj                                       //
   │     ├─ 其他设施2_point.sbn                                       //
   │     ├─ 其他设施2_point.sbx                                       //
   │     ├─ 其他设施2_point.shp                                       //
   │     ├─ 其他设施2_point.shp.xml                                   //
   │     ├─ 其他设施2_point.shx                                       //
   │     ├─ 其他设施3_point.dbf                                       //
   │     ├─ 其他设施3_point.prj                                       //
   │     ├─ 其他设施3_point.sbn                                       //
   │     ├─ 其他设施3_point.sbx                                       //
   │     ├─ 其他设施3_point.shp                                       //
   │     ├─ 其他设施3_point.shp.xml                                   //
   │     ├─ 其他设施3_point.shx                                       //
   │     ├─ 其他设施4_point.dbf                                       //
   │     ├─ 其他设施4_point.prj                                       //
   │     ├─ 其他设施4_point.sbn                                       //
   │     ├─ 其他设施4_point.sbx                                       //
   │     ├─ 其他设施4_point.shp                                       //
   │     ├─ 其他设施4_point.shp.xml                                   //
   │     ├─ 其他设施4_point.shx                                       //
   │     ├─ 其他设施_point.dbf                                        //
   │     ├─ 其他设施_point.prj                                        //
   │     ├─ 其他设施_point.sbn                                        //
   │     ├─ 其他设施_point.sbx                                        //
   │     ├─ 其他设施_point.shp                                        //
   │     ├─ 其他设施_point.shp.xml                                    //
   │     ├─ 其他设施_point.shx                                        //
   │     ├─ 其它道路2_polyline.dbf                                    //
   │     ├─ 其它道路2_polyline.prj                                    //
   │     ├─ 其它道路2_polyline.sbn                                    //
   │     ├─ 其它道路2_polyline.sbx                                    //
   │     ├─ 其它道路2_polyline.shp                                    //
   │     ├─ 其它道路2_polyline.shp.xml                                //
   │     ├─ 其它道路2_polyline.shx                                    //
   │     ├─ 其它道路_polyline.dbf                                     //
   │     ├─ 其它道路_polyline.prj                                     //
   │     ├─ 其它道路_polyline.sbn                                     //
   │     ├─ 其它道路_polyline.sbx                                     //
   │     ├─ 其它道路_polyline.shp                                     //
   │     ├─ 其它道路_polyline.shp.xml                                 //
   │     ├─ 其它道路_polyline.shx                                     //
   │     ├─ 功能区_region.dbf                                        //
   │     ├─ 功能区_region.prj                                        //
   │     ├─ 功能区_region.sbn                                        //
   │     ├─ 功能区_region.sbx                                        //
   │     ├─ 功能区_region.shp                                        //
   │     ├─ 功能区_region.shp.xml                                    //
   │     ├─ 功能区_region.shx                                        //
   │     ├─ 加油站_point.dbf                                         //
   │     ├─ 加油站_point.prj                                         //
   │     ├─ 加油站_point.sbn                                         //
   │     ├─ 加油站_point.sbx                                         //
   │     ├─ 加油站_point.shp                                         //
   │     ├─ 加油站_point.shp.xml                                     //
   │     ├─ 加油站_point.shx                                         //
   │     ├─ 医疗服务_point.dbf                                        //
   │     ├─ 医疗服务_point.prj                                        //
   │     ├─ 医疗服务_point.sbn                                        //
   │     ├─ 医疗服务_point.sbx                                        //
   │     ├─ 医疗服务_point.shp                                        //
   │     ├─ 医疗服务_point.shp.xml                                    //
   │     ├─ 医疗服务_point.shx                                        //
   │     ├─ 县_point.dbf                                           //
   │     ├─ 县_point.prj                                           //
   │     ├─ 县_point.sbn                                           //
   │     ├─ 县_point.sbx                                           //
   │     ├─ 县_point.shp                                           //
   │     ├─ 县_point.shp.xml                                       //
   │     ├─ 县_point.shx                                           //
   │     ├─ 县界_region.dbf                                         //
   │     ├─ 县界_region.prj                                         //
   │     ├─ 县界_region.sbn                                         //
   │     ├─ 县界_region.sbx                                         //
   │     ├─ 县界_region.shp                                         //
   │     ├─ 县界_region.shp.xml                                     //
   │     ├─ 县界_region.shx                                         //
   │     ├─ 县道_polyline.dbf                                       //
   │     ├─ 县道_polyline.prj                                       //
   │     ├─ 县道_polyline.sbn                                       //
   │     ├─ 县道_polyline.sbx                                       //
   │     ├─ 县道_polyline.shp                                       //
   │     ├─ 县道_polyline.shp.xml                                   //
   │     ├─ 县道_polyline.shx                                       //
   │     ├─ 国道_polyline.dbf                                       //
   │     ├─ 国道_polyline.prj                                       //
   │     ├─ 国道_polyline.sbn                                       //
   │     ├─ 国道_polyline.sbx                                       //
   │     ├─ 国道_polyline.shp                                       //
   │     ├─ 国道_polyline.shp.xml                                   //
   │     ├─ 国道_polyline.shx                                       //
   │     ├─ 地级市_point.dbf                                         //
   │     ├─ 地级市_point.prj                                         //
   │     ├─ 地级市_point.sbn                                         //
   │     ├─ 地级市_point.sbx                                         //
   │     ├─ 地级市_point.shp                                         //
   │     ├─ 地级市_point.shp.xml                                     //
   │     ├─ 地级市_point.shx                                         //
   │     ├─ 地铁_polyline.dbf                                       //
   │     ├─ 地铁_polyline.prj                                       //
   │     ├─ 地铁_polyline.sbn                                       //
   │     ├─ 地铁_polyline.sbx                                       //
   │     ├─ 地铁_polyline.shp                                       //
   │     ├─ 地铁_polyline.shp.xml                                   //
   │     ├─ 地铁_polyline.shx                                       //
   │     ├─ 城市快速路_polyline.dbf                                    //
   │     ├─ 城市快速路_polyline.prj                                    //
   │     ├─ 城市快速路_polyline.sbn                                    //
   │     ├─ 城市快速路_polyline.sbx                                    //
   │     ├─ 城市快速路_polyline.shp                                    //
   │     ├─ 城市快速路_polyline.shp.xml                                //
   │     ├─ 城市快速路_polyline.shx                                    //
   │     ├─ 大厦_point.dbf                                          //
   │     ├─ 大厦_point.prj                                          //
   │     ├─ 大厦_point.sbn                                          //
   │     ├─ 大厦_point.sbx                                          //
   │     ├─ 大厦_point.shp                                          //
   │     ├─ 大厦_point.shp.xml                                      //
   │     ├─ 大厦_point.shx                                          //
   │     ├─ 岛屿_region.dbf                                         //
   │     ├─ 岛屿_region.prj                                         //
   │     ├─ 岛屿_region.sbn                                         //
   │     ├─ 岛屿_region.sbx                                         //
   │     ├─ 岛屿_region.shp                                         //
   │     ├─ 岛屿_region.shp.xml                                     //
   │     ├─ 岛屿_region.shx                                         //
   │     ├─ 市界_region.dbf                                         //
   │     ├─ 市界_region.prj                                         //
   │     ├─ 市界_region.sbn                                         //
   │     ├─ 市界_region.sbx                                         //
   │     ├─ 市界_region.shp                                         //
   │     ├─ 市界_region.shp.xml                                     //
   │     ├─ 市界_region.shx                                         //
   │     ├─ 建成区界_region.dbf                                       //
   │     ├─ 建成区界_region.prj                                       //
   │     ├─ 建成区界_region.sbn                                       //
   │     ├─ 建成区界_region.sbx                                       //
   │     ├─ 建成区界_region.shp                                       //
   │     ├─ 建成区界_region.shp.xml                                   //
   │     ├─ 建成区界_region.shx                                       //
   │     ├─ 收费站_point.dbf                                         //
   │     ├─ 收费站_point.prj                                         //
   │     ├─ 收费站_point.sbn                                         //
   │     ├─ 收费站_point.sbx                                         //
   │     ├─ 收费站_point.shp                                         //
   │     ├─ 收费站_point.shp.xml                                     //
   │     ├─ 收费站_point.shx                                         //
   │     ├─ 政府机关_point.dbf                                        //
   │     ├─ 政府机关_point.prj                                        //
   │     ├─ 政府机关_point.sbn                                        //
   │     ├─ 政府机关_point.sbx                                        //
   │     ├─ 政府机关_point.shp                                        //
   │     ├─ 政府机关_point.shp.xml                                    //
   │     ├─ 政府机关_point.shx                                        //
   │     ├─ 旅游_point.dbf                                          //
   │     ├─ 旅游_point.prj                                          //
   │     ├─ 旅游_point.sbn                                          //
   │     ├─ 旅游_point.sbx                                          //
   │     ├─ 旅游_point.shp                                          //
   │     ├─ 旅游_point.shp.xml                                      //
   │     ├─ 旅游_point.shx                                          //
   │     ├─ 机场_point.dbf                                          //
   │     ├─ 机场_point.prj                                          //
   │     ├─ 机场_point.sbn                                          //
   │     ├─ 机场_point.sbx                                          //
   │     ├─ 机场_point.shp                                          //
   │     ├─ 机场_point.shp.xml                                      //
   │     ├─ 机场_point.shx                                          //
   │     ├─ 村2_point.dbf                                          //
   │     ├─ 村2_point.prj                                          //
   │     ├─ 村2_point.sbn                                          //
   │     ├─ 村2_point.sbx                                          //
   │     ├─ 村2_point.shp                                          //
   │     ├─ 村2_point.shp.xml                                      //
   │     ├─ 村2_point.shx                                          //
   │     ├─ 村3_point.dbf                                          //
   │     ├─ 村3_point.prj                                          //
   │     ├─ 村3_point.sbn                                          //
   │     ├─ 村3_point.sbx                                          //
   │     ├─ 村3_point.shp                                          //
   │     ├─ 村3_point.shp.xml                                      //
   │     ├─ 村3_point.shx                                          //
   │     ├─ 村4_point.dbf                                          //
   │     ├─ 村4_point.prj                                          //
   │     ├─ 村4_point.sbn                                          //
   │     ├─ 村4_point.sbx                                          //
   │     ├─ 村4_point.shp                                          //
   │     ├─ 村4_point.shp.xml                                      //
   │     ├─ 村4_point.shx                                          //
   │     ├─ 村_point.dbf                                           //
   │     ├─ 村_point.prj                                           //
   │     ├─ 村_point.sbn                                           //
   │     ├─ 村_point.sbx                                           //
   │     ├─ 村_point.shp                                           //
   │     ├─ 村_point.shp.xml                                       //
   │     ├─ 村_point.shx                                           //
   │     ├─ 水系_region.dbf                                         //
   │     ├─ 水系_region.prj                                         //
   │     ├─ 水系_region.sbn                                         //
   │     ├─ 水系_region.sbx                                         //
   │     ├─ 水系_region.shp                                         //
   │     ├─ 水系_region.shp.xml                                     //
   │     ├─ 水系_region.shx                                         //
   │     ├─ 汽车服务_point.dbf                                        //
   │     ├─ 汽车服务_point.prj                                        //
   │     ├─ 汽车服务_point.sbn                                        //
   │     ├─ 汽车服务_point.sbx                                        //
   │     ├─ 汽车服务_point.shp                                        //
   │     ├─ 汽车服务_point.shp.xml                                    //
   │     ├─ 汽车服务_point.shx                                        //
   │     ├─ 汽车站_point.dbf                                         //
   │     ├─ 汽车站_point.prj                                         //
   │     ├─ 汽车站_point.sbn                                         //
   │     ├─ 汽车站_point.sbx                                         //
   │     ├─ 汽车站_point.shp                                         //
   │     ├─ 汽车站_point.shp.xml                                     //
   │     ├─ 汽车站_point.shx                                         //
   │     ├─ 火车站_point.dbf                                         //
   │     ├─ 火车站_point.prj                                         //
   │     ├─ 火车站_point.sbn                                         //
   │     ├─ 火车站_point.sbx                                         //
   │     ├─ 火车站_point.shp                                         //
   │     ├─ 火车站_point.shp.xml                                     //
   │     ├─ 火车站_point.shx                                         //
   │     ├─ 省会_point.dbf                                          //
   │     ├─ 省会_point.prj                                          //
   │     ├─ 省会_point.sbn                                          //
   │     ├─ 省会_point.sbx                                          //
   │     ├─ 省会_point.shp                                          //
   │     ├─ 省会_point.shp.xml                                      //
   │     ├─ 省会_point.shx                                          //
   │     ├─ 省界_region.dbf                                         //
   │     ├─ 省界_region.prj                                         //
   │     ├─ 省界_region.sbn                                         //
   │     ├─ 省界_region.sbx                                         //
   │     ├─ 省界_region.shp                                         //
   │     ├─ 省界_region.shp.xml                                     //
   │     ├─ 省界_region.shx                                         //
   │     ├─ 省道_polyline.dbf                                       //
   │     ├─ 省道_polyline.prj                                       //
   │     ├─ 省道_polyline.sbn                                       //
   │     ├─ 省道_polyline.sbx                                       //
   │     ├─ 省道_polyline.shp                                       //
   │     ├─ 省道_polyline.shp.xml                                   //
   │     ├─ 省道_polyline.shx                                       //
   │     ├─ 科研教育_point.dbf                                        //
   │     ├─ 科研教育_point.prj                                        //
   │     ├─ 科研教育_point.sbn                                        //
   │     ├─ 科研教育_point.sbx                                        //
   │     ├─ 科研教育_point.shp                                        //
   │     ├─ 科研教育_point.shp.xml                                    //
   │     ├─ 科研教育_point.shx                                        //
   │     ├─ 绿地_region.dbf                                         //
   │     ├─ 绿地_region.prj                                         //
   │     ├─ 绿地_region.sbn                                         //
   │     ├─ 绿地_region.sbx                                         //
   │     ├─ 绿地_region.shp                                         //
   │     ├─ 绿地_region.shp.xml                                     //
   │     ├─ 绿地_region.shx                                         //
   │     ├─ 行人道路_polyline.dbf                                     //
   │     ├─ 行人道路_polyline.prj                                     //
   │     ├─ 行人道路_polyline.sbn                                     //
   │     ├─ 行人道路_polyline.sbx                                     //
   │     ├─ 行人道路_polyline.shp                                     //
   │     ├─ 行人道路_polyline.shp.xml                                 //
   │     ├─ 行人道路_polyline.shx                                     //
   │     ├─ 购物2_point.dbf                                         //
   │     ├─ 购物2_point.prj                                         //
   │     ├─ 购物2_point.sbn                                         //
   │     ├─ 购物2_point.sbx                                         //
   │     ├─ 购物2_point.shp                                         //
   │     ├─ 购物2_point.shp.xml                                     //
   │     ├─ 购物2_point.shx                                         //
   │     ├─ 购物3_point.dbf                                         //
   │     ├─ 购物3_point.prj                                         //
   │     ├─ 购物3_point.sbn                                         //
   │     ├─ 购物3_point.sbx                                         //
   │     ├─ 购物3_point.shp                                         //
   │     ├─ 购物3_point.shp.xml                                     //
   │     ├─ 购物3_point.shx                                         //
   │     ├─ 购物_point.dbf                                          //
   │     ├─ 购物_point.prj                                          //
   │     ├─ 购物_point.sbn                                          //
   │     ├─ 购物_point.sbx                                          //
   │     ├─ 购物_point.shp                                          //
   │     ├─ 购物_point.shp.xml                                      //
   │     ├─ 购物_point.shx                                          //
   │     ├─ 轮渡_polyline.dbf                                       //
   │     ├─ 轮渡_polyline.prj                                       //
   │     ├─ 轮渡_polyline.sbn                                       //
   │     ├─ 轮渡_polyline.sbx                                       //
   │     ├─ 轮渡_polyline.shp                                       //
   │     ├─ 轮渡_polyline.shp.xml                                   //
   │     ├─ 轮渡_polyline.shx                                       //
   │     ├─ 金融服务_point.dbf                                        //
   │     ├─ 金融服务_point.prj                                        //
   │     ├─ 金融服务_point.sbn                                        //
   │     ├─ 金融服务_point.sbx                                        //
   │     ├─ 金融服务_point.shp                                        //
   │     ├─ 金融服务_point.shp.xml                                    //
   │     ├─ 金融服务_point.shx                                        //
   │     ├─ 铁路_polyline.dbf                                       //
   │     ├─ 铁路_polyline.prj                                       //
   │     ├─ 铁路_polyline.sbn                                       //
   │     ├─ 铁路_polyline.sbx                                       //
   │     ├─ 铁路_polyline.shp                                       //
   │     ├─ 铁路_polyline.shp.xml                                   //
   │     ├─ 铁路_polyline.shx                                       //
   │     ├─ 餐饮_point.dbf                                          //
   │     ├─ 餐饮_point.prj                                          //
   │     ├─ 餐饮_point.sbn                                          //
   │     ├─ 餐饮_point.sbx                                          //
   │     ├─ 餐饮_point.shp                                          //
   │     ├─ 餐饮_point.shp.xml                                      //
   │     ├─ 餐饮_point.shx                                          //
   │     ├─ 高速_polyline.dbf                                       //
   │     ├─ 高速_polyline.prj                                       //
   │     ├─ 高速_polyline.sbn                                       //
   │     ├─ 高速_polyline.sbx                                       //
   │     ├─ 高速_polyline.shp                                       //
   │     ├─ 高速_polyline.shp.xml                                   //
   │     ├─ 高速_polyline.shx                                       //
   │     ├─ 高速服务区_point.dbf                                       //
   │     ├─ 高速服务区_point.prj                                       //
   │     ├─ 高速服务区_point.sbn                                       //
   │     ├─ 高速服务区_point.sbx                                       //
   │     ├─ 高速服务区_point.shp                                       //
   │     ├─ 高速服务区_point.shp.xml                                   //
   │     └─ 高速服务区_point.shx                                       //
   └─ shape.ipynb                                                 //

```
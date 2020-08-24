from django.db import models

# Create your models here.


class Device(models.Model):
    device_name = models.CharField(max_length=255, verbose_name="设备名称")
    device_mgmt_ip = models.CharField(max_length=255, verbose_name="管理地址")
    device_type = models.CharField(max_length=64, verbose_name="设备类型")
    os_version = models.CharField(max_length=255, verbose_name="设备OS版本")
    device_brand_model = models.CharField(max_length=64, verbose_name="设备品牌")
    device_mode = models.CharField(max_length=127, verbose_name="设备型号")
    networking_mode = models.CharField(max_length=127, verbose_name="组网方式")
    cluster_status = models.CharField(max_length=32, verbose_name="集群状态")
    status = models.CharField(max_length=32, verbose_name="设备状态")
    device_area = models.CharField(max_length=127, verbose_name="所属区域")
    is_hide = models.BooleanField(default=False, verbose_name="是否参与路径计算")
    placement = models.CharField(max_length=512, verbose_name="物理位置")
    device_capability = models.CharField(max_length=32, verbose_name="容量（条数）")
    description = models.TextField(verbose_name="描述")
    is_delete = models.BooleanField(default=False, verbose_name="删除标志")
    is_nanotube = models.BooleanField(default=False, verbose_name="纳管标志")
    # organization = models.ForeignKey("organization", on_delete=models.CASCADE, verbose_name="所属组织")
    device_esn = models.CharField(max_length=64, verbose_name="设备esn")
    device_assets = models.CharField(max_length=64, verbose_name="资产编号")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        db_table = "device"
        verbose_name = '设备表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.device_name


class Password(models.Model):
    username = models.CharField(max_length=64, verbose_name="用户名")
    password = models.CharField(max_length=64, verbose_name="密码")
    device = models.ForeignKey("device", on_delete=models.CASCADE, verbose_name="设备id")
    connect_way = models.CharField(max_length=64, verbose_name="连接方式")
    port = models.CharField(max_length=32, verbose_name="端口")
    timeout = models.IntegerField(verbose_name="超时时间（秒）")
    type = models.CharField(max_length=64, verbose_name="账户类型")
    remark = models.TextField(verbose_name="备注")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        db_table = "password"
        verbose_name = '设备访问凭证'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username




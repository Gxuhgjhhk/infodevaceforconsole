from py4j.java_gateway import JavaGateway

def get_detailed_phone_info_with_py4j():
    gateway = JavaGateway()

    Build = gateway.jvm.android.os.Build
    SystemProperties = gateway.jvm.android.os.SystemProperties
    Context = gateway.jvm.android.content.Context
    BatteryManager = gateway.jvm.android.os.BatteryManager
    activity = gateway.jvm.org.kivy.android.PythonActivity.mActivity
    context = activity.getApplicationContext()
    total_memory = SystemProperties.getLong("ro.product.ram", 0)
    battery_manager = context.getSystemService(Context.BATTERY_SERVICE)
    battery_info = battery_manager.getIntProperty(BatteryManager.BATTERY_PROPERTY_CAPACITY)

    detailed_info = {
        'brand': str(Build.BRAND),
        'model': str(Build.MODEL),
        'version': str(Build.VERSION.RELEASE),
        'total_memory': total_memory,
        'battery_level': battery_info
    }
    print(detailed_info)
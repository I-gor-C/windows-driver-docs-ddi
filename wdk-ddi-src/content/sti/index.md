---
UID : NA:sti
ms.assetid : 68cc0060-fd37-3ec3-a689-419b81682f45
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# sti.h header



sti.h contains the following programming interfaces:







## Structures
| Title | Description |
| ---- |:---- |
| [_ERROR_INFOW](ns-sti-_error_infow.md) | The STI_ERROR_INFO structure is used as a parameter for the IStiDevice::GetLastErrorInfo and IStiUSD::GetLastErrorInfo methods. It is also used as a member of the STI_DIAG structure. |
| [_STI_DEV_CAPS](ns-sti-_sti_dev_caps.md) | The STI_DEV_CAPS structure is used as a parameter to the IStiDevice::GetCapabilities method. It is also a member of the STI_DEVICE_INFORMATION and STI_WIA_DEVICE_INFORMATION structures. |
| [_STI_DEVICE_INFORMATIONW](ns-sti-_sti_device_informationw.md) | The STI_DEVICE_INFORMATION structure is used as an output parameter for the IStillImage::GetDeviceList and IStillImage::GetDeviceInfo functions. It is used as an input parameter for IStillImage::SetupDeviceParameters. |
| [_STI_DEVICE_STATUS](ns-sti-_sti_device_status.md) | The STI_DEVICE_STATUS structure is used as a parameter to the IStiDevice::GetStatus and IStiUSD::GetStatus methods. |
| [_STI_DIAG](ns-sti-_sti_diag.md) | The STI_DIAG structure is used as a parameter to the IStiDevice::Diagnostic and IStiUSD::Diagnostic methods. |
| [_STI_WIA_DEVICE_INFORMATIONW](ns-sti-_sti_wia_device_informationw.md) | The STI_WIA_DEVICE_INFORMATION structure contains device information. |
| [_STINOTIFY](ns-sti-_stinotify.md) | The STINOTIFY structure is used as a parameter to the IStillImage::LaunchApplicationForDevice, IStiDevice::GetLastNotificationData, and IStiUSD::GetNotificationData methods. |
| [_STISUBSCRIBE](ns-sti-_stisubscribe.md) | The STISUBSCRIBE structure is used as a parameter for the IStiDevice::Subscribe method. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_STI_DEVICE_MJ_TYPE](ne-sti-_sti_device_mj_type.md) | The STI_DEVICE_TYPE type identifies the device type of a still image device.The DWORD is divided into a HIWORD containing the major device type, and a LOWORD containing a vendor-defined subtype. |
# Sti.h header


This header is used by Imaging devices. For more information, see
- [Imaging devices](../_image/index.md)

Sti.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [IStiDevice::DeviceReset method](nf-sti-istidevice-devicereset.md) | The IStiDevice |
| [IStiDevice::Diagnostic method](nf-sti-istidevice-diagnostic.md) | The IStiDevice |
| [IStiDevice::Escape method](nf-sti-istidevice-escape.md) | The IStiDevice |
| [IStiDevice::GetCapabilities method](nf-sti-istidevice-getcapabilities.md) | The IStiDevice |
| [IStiDevice::GetLastError method](nf-sti-istidevice-getlasterror.md) | The IStiDevice |
| [IStiDevice::GetLastErrorInfo method](nf-sti-istidevice-getlasterrorinfo.md) | The IStiDevice |
| [IStiDevice::GetLastNotificationData method](nf-sti-istidevice-getlastnotificationdata.md) | The IStiDevice |
| [IStiDevice::GetStatus method](nf-sti-istidevice-getstatus.md) | The IStiDevice |
| [IStiDevice::Initialize method](nf-sti-istidevice-initialize.md) | The IStiDevice |
| [IStiDevice::LockDevice method](nf-sti-istidevice-lockdevice.md) | The IStiDevice |
| [IStiDevice::RawReadCommand method](nf-sti-istidevice-rawreadcommand.md) | The IStiDevice |
| [IStiDevice::RawReadData method](nf-sti-istidevice-rawreaddata.md) | The IStiDevice |
| [IStiDevice::RawWriteCommand method](nf-sti-istidevice-rawwritecommand.md) | The IStiDevice |
| [IStiDevice::RawWriteData method](nf-sti-istidevice-rawwritedata.md) | The IStiDevice |
| [IStiDevice::Release method](nf-sti-istidevice-release.md) | The IStiDevice |
| [IStiDevice::Subscribe method](nf-sti-istidevice-subscribe.md) | The IStiDevice |
| [IStiDevice::UnLockDevice method](nf-sti-istidevice-unlockdevice.md) | The IStiDevice |
| [IStiDevice::UnSubscribe method](nf-sti-istidevice-unsubscribe.md) | The IStiDevice |

## Structures

| Title   | Description   |
| ---- |:---- |
| [STINOTIFY structure](ns-sti--stinotify.md) | The STINOTIFY structure is used as a parameter to the IStillImage |
| [STISUBSCRIBE structure](ns-sti--stisubscribe.md) | The STISUBSCRIBE structure is used as a parameter for the IStiDevice |
| [STI_DEVICE_STATUS structure](ns-sti--sti-device-status.md) | The STI_DEVICE_STATUS structure is used as a parameter to the IStiDevice |
| [STI_DEV_CAPS structure](ns-sti--sti-dev-caps.md) | The STI_DEV_CAPS structure is used as a parameter to the IStiDevice |
| [STI_DIAG structure](ns-sti--sti-diag.md) | The STI_DIAG structure is used as a parameter to the IStiDevice |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [STI_DEVICE_MJ_TYPE enumeration](ne-sti--sti-device-mj-type.md) | The STI_DEVICE_TYPE type identifies the device type of a still image device.The DWORD is divided into a HIWORD containing the major device type, and a LOWORD containing a vendor-defined subtype. |

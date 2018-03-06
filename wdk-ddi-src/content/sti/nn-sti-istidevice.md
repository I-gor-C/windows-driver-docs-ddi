---
UID: NN:sti.IStiDevice
title: IStiDevice
author: windows-driver-content
description: This section describes the methods defined for the IStiDevice COM Interface. Method prototypes are contained in Sti.h.
old-location: image\istidevice_interface_methods.htm
old-project: image
ms.assetid: 86ce412e-007b-4ea9-9c09-766eee543852
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IStiDevice, IStiDevice interface [Imaging Devices], IStiDevice interface [Imaging Devices], described, image.istidevice_interface_methods, sti/IStiDevice, stifnc_ef9e9c06-e918-462c-92c0-f4b1605a0847.xml
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: sti.h
req.include-header: 
req.target-type: Desktop
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: sti.h
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	sti.h
api_name:
-	IStiDevice
product: Windows
targetos: Windows
req.typenames: STI_DEVICE_MJ_TYPE, STI_DEVICE_MJ_TYPE
req.product: Windows 10 or later.
---

# IStiDevice interface

This section describes the methods defined for the <a href="https://msdn.microsoft.com/b026fb74-9ce6-4d4e-8a5b-402731904064">IStiDevice COM Interface</a>. Method prototypes are contained in <i>Sti.h</i>.

## Methods

<p>The <b>IStiDevice</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IStiDevice::DeviceReset](nf-sti-istidevice-devicereset.md) | The IStiDevice::DeviceReset method resets a still image device to a known state. |
| [IStiDevice::Diagnostic](nf-sti-istidevice-diagnostic.md) | The IStiDevice::Diagnostic method executes diagnostic tests on a still image device. |
| [IStiDevice::Escape](nf-sti-istidevice-escape.md) | The IStiDevice::Escape method sends a request for a vendor-specific I/O operation to a still image device. |
| [IStiDevice::GetCapabilities](nf-sti-istidevice-getcapabilities.md) | The IStiDevice::GetCapabilities method returns a still image device's capabilities. |
| [IStiDevice::GetLastError](nf-sti-istidevice-getlasterror.md) | The IStiDevice::GetLastError method returns the last known error associated with a still image device. |
| [IStiDevice::GetLastErrorInfo](nf-sti-istidevice-getlasterrorinfo.md) | The IStiDevice::GetLastErrorInfo method returns information about the last known error associated with a still image device. |
| [IStiDevice::GetLastNotificationData](nf-sti-istidevice-getlastnotificationdata.md) | The IStiDevice::GetLastNotificationData method returns a description of the most recent event that occurred on a still image device. |
| [IStiDevice::GetStatus](nf-sti-istidevice-getstatus.md) | The IStiDevice::GetStatus method returns a still image device's status information. |
| [IStiDevice::Initialize](nf-sti-istidevice-initialize.md) | The IStiDevice::Initialize method initializes an instance of the COM object that defines the IStiDevice interface. This method is for internal use only. |
| [IStiDevice::LockDevice](nf-sti-istidevice-lockdevice.md) | The IStiDevice::LockDevice method locks a device for exclusive use by the caller. |
| [IStiDevice::RawReadCommand](nf-sti-istidevice-rawreadcommand.md) | The IStiDevice::RawReadCommand method reads command information from a still image device. |
| [IStiDevice::RawReadData](nf-sti-istidevice-rawreaddata.md) | The IStiDevice::RawReadData method reads data from a still image device. |
| [IStiDevice::RawWriteCommand](nf-sti-istidevice-rawwritecommand.md) | The IStiDevice::RawWriteCommand method sends command information to a still image device. |
| [IStiDevice::RawWriteData](nf-sti-istidevice-rawwritedata.md) | The IStiDevice::RawWriteData method writes data to a still image device. |
| [IStiDevice::Release](nf-sti-istidevice-release.md) | The IStiDevice::Release method closes the instance of the COM object that was created by a previous call to IStillImage::CreateDevice, and removes access to the object's interface. |
| [IStiDevice::Subscribe](nf-sti-istidevice-subscribe.md) | The IStiDevice::Subscribe method registers the caller to receive notifications of device events. |
| [IStiDevice::UnLockDevice](nf-sti-istidevice-unlockdevice.md) | The IStiDevice::UnLockDevice method unlocks a device that was locked by a previous call to IStiDevice::LockDevice. |
| [IStiDevice::UnSubscribe](nf-sti-istidevice-unsubscribe.md) | The IStiDevice::UnSubscribe method removes the caller from the list of applications registered to receive notification of device events. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Desktop |
| **Header** | sti.h |
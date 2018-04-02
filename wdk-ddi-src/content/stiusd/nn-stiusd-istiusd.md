---
UID: NN:stiusd.IStiUSD
title: IStiUSD
author: windows-driver-content
description: This section describes the methods defined for the IStiUSD COM Interface. Method prototypes are contained in Stiusd.h.
old-location: image\istiusd_interface_methods.htm
old-project: image
ms.assetid: 62740263-5bbb-48e1-be3d-9ee9cb37d6b9
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: IStiUSD, IStiUSD interface [Imaging Devices], IStiUSD interface [Imaging Devices], described, image.istiusd_interface_methods, stifnc_2fa7c229-f4c5-455e-ba93-019c5b84dd79.xml, stiusd/IStiUSD
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: stiusd.h
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
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	stiusd.h
api_name:
-	IStiUSD
product: Windows
targetos: Windows
req.typenames: STI_WIA_DEVICE_INFORMATIONW, *PSTI_WIA_DEVICE_INFORMATIONW
req.product: Windows 10 or later.
---

# IStiUSD interface

This section describes the methods defined for the <a href="https://msdn.microsoft.com/2f805955-8c66-4c9e-839e-c8a98c6637a8">IStiUSD COM Interface</a>. Method prototypes are contained in <i>Stiusd.h</i>.

## Methods

<p>The <b>IStiUSD</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IStiUSD::DeviceReset](nf-stiusd-istiusd-devicereset.md) | A still image minidriver's IStiUSD::DeviceReset method resets a still image device to a known, initialized state. |
| [IStiUSD::Diagnostic](nf-stiusd-istiusd-diagnostic.md) | A still image minidriver's IStiUSD::Diagnostic method runs diagnostic tests on a still image device. |
| [IStiUSD::Escape](nf-stiusd-istiusd-escape.md) | A still image minidriver's IStiUSD::Escape method performs a vendor-specific I/O operation on a still image device. |
| [IStiUSD::GetCapabilities](nf-stiusd-istiusd-getcapabilities.md) | A still image minidriver's IStiUSD::GetCapabilities method returns a still image device's capabilities. |
| [IStiUSD::GetLastError](nf-stiusd-istiusd-getlasterror.md) | The IStiUSD::GetLastError method returns the last known error associated with a still image device. |
| [IStiUSD::GetLastErrorInfo](nf-stiusd-istiusd-getlasterrorinfo.md) | A still image minidriver's IStiUSD::GetLastErrorInfo method returns information about the last known error associated with a still image device. |
| [IStiUSD::GetNotificationData](nf-stiusd-istiusd-getnotificationdata.md) | A still image minidriver's IStiUSD::GetNotificationData method returns a description of the most recent event that occurred on a still image device. |
| [IStiUSD::GetStatus](nf-stiusd-istiusd-getstatus.md) | A still image minidriver's IStiUSD::GetStatus method returns the status of a still image device. |
| [IStiUSD::Initialize](nf-stiusd-istiusd-initialize.md) | A still image minidriver's IStiUSD::Initialize method initializes an instance of the COM object that defines the IStiUSD interface. |
| [IStiUSD::LockDevice](nf-stiusd-istiusd-lockdevice.md) | A still image minidriver's IStiUSD::LockDevice method locks a device for exclusive use by the caller. |
| [IStiUSD::RawReadCommand](nf-stiusd-istiusd-rawreadcommand.md) | A still image minidriver's IStiUSD::RawReadCommand method reads command information from a still image device. |
| [IStiUSD::RawReadData](nf-stiusd-istiusd-rawreaddata.md) | A still image minidriver's IStiUSD::RawReadData method reads data from a still image device. |
| [IStiUSD::RawWriteCommand](nf-stiusd-istiusd-rawwritecommand.md) | A still image minidriver's IStiDevice::RawWriteCommand method sends command information to a still image device. |
| [IStiUSD::RawWriteData](nf-stiusd-istiusd-rawwritedata.md) | A still image minidriver's IStiUSD::RawWriteData method writes data to a still image device. |
| [IStiUSD::SetNotificationHandle](nf-stiusd-istiusd-setnotificationhandle.md) | A still image minidriver's IStiUSD::SetNotificationHandle method specifies an event handle that the minidriver should use to inform the caller of device events. |
| [IStiUSD::UnLockDevice](nf-stiusd-istiusd-unlockdevice.md) | A still image minidriver's IStiUSD::UnLockDevice method unlocks a device that was locked by a previous call to IStiUSD::LockDevice. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Desktop |
| **Header** | stiusd.h |
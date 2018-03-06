---
UID: NN:stiusd.IStiDeviceControl
title: IStiDeviceControl
author: windows-driver-content
description: This section describes the methods defined for the IStiDeviceControl COM Interface. Method prototypes are contained in Stiusd.h.
old-location: image\istidevicecontrol_interface_methods.htm
old-project: image
ms.assetid: de58597a-d10a-45b3-bf75-539e5cd00535
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: IStiDeviceControl, IStiDeviceControl interface [Imaging Devices], IStiDeviceControl interface [Imaging Devices], described, image.istidevicecontrol_interface_methods, stifnc_532906f7-46b9-4874-8099-6be551e77711.xml, stiusd/IStiDeviceControl
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
req.lib: stiusd.h
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
-	IStiDeviceControl
product: Windows
targetos: Windows
req.typenames: STI_WIA_DEVICE_INFORMATIONW, *PSTI_WIA_DEVICE_INFORMATIONW
req.product: Windows 10 or later.
---

# IStiDeviceControl interface

This section describes the methods defined for the <a href="https://msdn.microsoft.com/6d98f5d7-c471-4abb-8e69-dbac3d336c2f">IStiDeviceControl COM Interface</a>. Method prototypes are contained in <i>Stiusd.h</i>.

## Methods

<p>The <b>IStiDeviceControl</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IStiDeviceControl::AddRef](nf-stiusd-istidevicecontrol-addref.md) | The IStiDeviceControl::AddRef method increments the reference count for the IStiDeviceControl interface. |
| [IStiDeviceControl::GetMyDeviceHandle](nf-stiusd-istidevicecontrol-getmydevicehandle.md) | This topic describes the GetMyDeviceHandle method. |
| [IStiDeviceControl::GetMyDeviceOpenMode](nf-stiusd-istidevicecontrol-getmydeviceopenmode.md) | The IStiDeviceControl::GetMyDeviceOpenMode method allows a still image minidriver to obtain the transfer mode that an application specified when it created an instance of a still image device. |
| [IStiDeviceControl::GetMyDevicePortName](nf-stiusd-istidevicecontrol-getmydeviceportname.md) | The IStiDeviceControl::GetMyDevicePortName method allows a user-mode still image minidriver to obtain a device's port name. |
| [IStiDeviceControl::RawDeviceControl](nf-stiusd-istidevicecontrol-rawdevicecontrol.md) | This topic describes the RawDeviceControl method. |
| [IStiDeviceControl::Release](nf-stiusd-istidevicecontrol-release.md) | The IStiDeviceControl::Release method closes the instance of the COM object that was created when a minidriver client called IStiUSD::Initialize. |
| [IStiDeviceControl::WriteToErrorLog](nf-stiusd-istidevicecontrol-writetoerrorlog.md) | The IStiDeviceControl::WriteToErrorLog method allows a user-mode still image minidriver to write a message into the still image error log. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Desktop |
| **Header** | stiusd.h |
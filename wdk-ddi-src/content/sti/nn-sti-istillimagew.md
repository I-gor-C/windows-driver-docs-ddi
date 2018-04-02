---
UID: NN:sti.IStillImageW
title: IStillImageW
author: windows-driver-content
description: This section describes the methods defined for the IStillImage COM Interface. Method prototypes are contained in Sti.h.
old-location: image\istillimage_interface_methods.htm
old-project: image
ms.assetid: a9ceee48-cbb5-4448-83b4-9c19fe89fcb9
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: IStillImageW, IStillImageW interface [Imaging Devices], IStillImageW interface [Imaging Devices], described, image.istillimage_interface_methods, sti/IStillImageW, stifnc_a737fc11-5690-49a8-b64e-82b27bb55e52.xml
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
req.lib: 
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
-	IStillImageW
product:
- Windows
targetos: Windows
req.typenames: STI_DEVICE_MJ_TYPE, STI_DEVICE_MJ_TYPE
req.product: Windows 10 or later.
---

# IStillImageW interface

This section describes the methods defined for the <a href="https://msdn.microsoft.com/eb60a3fd-e7e2-4d3c-973e-af8cb3c3c511">IStillImage COM Interface</a>. Method prototypes are contained in <i>S</i><i>ti.h</i>.

## Methods

<p>The <b>IStillImageW</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IStillImageW::CreateDevice](nf-sti-istillimagew-createdevice.md) | The IStillImage::CreateDevice method creates an instance of the COM object that defines the IStiDevice COM Interface, and returns a pointer to the interface. |
| [IStillImageW::EnableHwNotifications](nf-sti-istillimagew-enablehwnotifications.md) | The IStillImage::EnableHwNotifications method requests the still image event monitor to enable or disable the notification of applications when Still Image Device Events occur for a specified device. |
| [IStillImageW::GetDeviceInfo](nf-sti-istillimagew-getdeviceinfo.md) | The IStillImage::GetDeviceInfo method returns hardware characteristics for a specified still image device. |
| [IStillImageW::GetDeviceList](nf-sti-istillimagew-getdevicelist.md) | The IStillImage::GetDeviceList method returns hardware characteristics for all installed still image devices. |
| [IStillImageW::GetDeviceValue](nf-sti-istillimagew-getdevicevalue.md) | The IStillImage::GetDeviceValue method returns registry information associated with a specified still image device. |
| [IStillImageW::GetHwNotificationState](nf-sti-istillimagew-gethwnotificationstate.md) | The IStillImage::GetHwNotificationState method indicates whether applications will be notified when Still Image Device Events occur on a specified device. |
| [IStillImageW::GetSTILaunchInformation](nf-sti-istillimagew-getstilaunchinformation.md) | The IStillImage::GetSTILaunchInformation method returns the reason the calling still image application was started, if the still image event monitor started it. |
| [IStillImageW::Initialize](nf-sti-istillimagew-initialize.md) | The IStillImage::Initialize method initializes an instance of the COM object that defines the IStillImage COM interface. This method is for internal system use only. |
| [IStillImageW::LaunchApplicationForDevice](nf-sti-istillimagew-launchapplicationfordevice.md) | The IStillImage::LaunchApplicationForDevice method starts a specified application for a specified still image device. |
| [IStillImageW::RegisterLaunchApplication](nf-sti-istillimagew-registerlaunchapplication.md) | The IStillImage::RegisterLaunchApplication method adds an application to the still image event monitor's list of push-model aware applications. |
| [IStillImageW::Release](nf-sti-istillimagew-release.md) | The IStillImage::Release method closes the instance of the COM object that was created by a previous call to IStillImage::StiCreateInstance, and removes access to the object's interface. |
| [IStillImageW::SetDeviceValue](nf-sti-istillimagew-setdevicevalue.md) | The IStillImage::SetDeviceValue method sets registry information for a specified still image device. |
| [IStillImageW::SetupDeviceParameters](nf-sti-istillimagew-setupdeviceparameters.md) | The IStillImage::SetupDeviceParameters method allows clients of the IStillImage COM interface to modify a still image device's stored characteristics, if the device's bus type is unknown. |
| [IStillImageW::UnregisterLaunchApplication](nf-sti-istillimagew-unregisterlaunchapplication.md) | The IStillImage::UnregisterLaunchApplication method removes an application from the still image event monitor's list of push-model aware applications. |
| [IStillImageW::WriteToErrorLog](nf-sti-istillimagew-writetoerrorlog.md) | The IStillImage::WriteToErrorLog method writes a message to the still image error log. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Windows 8 Windows 8 |
| **Target Platform** | Desktop |
| **Header** | sti.h |
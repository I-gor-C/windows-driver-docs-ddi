---
UID: NN:portcls.IPortClsNotifications
title: IPortClsNotifications
author: windows-driver-content
description: An interface implemented by ports to provide notification helpers to miniports to support audio module communication.
old-location: audio\iportclsnotifications.htm
old-project: audio
ms.assetid: 03F65E4E-C942-4748-8D3E-938A6AC51B2A
ms.author: windowsdriverdev
ms.date: 2/26/2018
ms.keywords: IPortClsNotifications, IPortClsNotifications interface [Audio Devices], IPortClsNotifications interface [Audio Devices], described, audio.iportclsnotifications, portcls/IPortClsNotifications
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 10, version 1703 and later versions of Windows.
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
req.lib: Portcls.lib
req.dll: 
req.irql: PASSIVE_LEVEL
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	COM
api_location:
-	portcls.h
api_name:
-	IPortClsNotifications
product: Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---

# IPortClsNotifications interface

An interface implemented by ports to provide
 notification helpers to miniports to support audio module communication.

For more information about audio modules, 
 see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/audio/implementing-audio-module-communication">Implementing Audio Module Discovery</a>. 
 

The miniport audio driver will call into their port to create and send the notification.

## Methods

<p>The <b>IPortClsNotifications</b> interface has these methods.</p>

| Method | Description |
| ---- |:---- |
| [IPortClsNotifications::AllocNotificationBuffer](nf-portcls-iportclsnotifications-allocnotificationbuffer.md) | Allocates a buffer of the specified size, in the specified memory pool, for use in sending notifications, to allow for communications between audio modules and UWP apps. |
| [IPortClsNotifications::FreeNotificationBuffer](nf-portcls-iportclsnotifications-freenotificationbuffer.md) | Frees a previously allocated IPortClsNotifications buffer. The buffer is used in sending notifications, to allow for communications between audio modules and UWP apps. |
| [IPortClsNotifications::SendNotification](nf-portcls-iportclsnotifications-sendnotification.md) | Sends a notification to the listening UWP apps, to allow for communications between audio modules and UWP apps. |


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 10, version 1703 and later versions of Windows. Available in Windows 10, version 1703 and later versions of Windows. |
| **Target Platform** | Windows |
| **Header** | portcls.h |
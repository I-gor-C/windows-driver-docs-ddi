---
UID: NF:portcls.IPortClsNotifications.FreeNotificationBuffer
title: IPortClsNotifications::FreeNotificationBuffer method
author: windows-driver-content
description: Frees a previously allocated IPortClsNotifications buffer. The buffer is used in sending notifications, to allow for communications between audio modules and UWP apps.
old-location: audio\iportclsnotifications_freenotification.htm
old-project: audio
ms.assetid: 93EC2651-3C52-4810-9F7A-A81BC7DA20AF
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: FreeNotificationBuffer method [Audio Devices], FreeNotificationBuffer method [Audio Devices], IPortClsNotifications interface, FreeNotificationBuffer,IPortClsNotifications.FreeNotificationBuffer, IPortClsNotifications, IPortClsNotifications interface [Audio Devices], FreeNotificationBuffer method, IPortClsNotifications::FreeNotificationBuffer, audio.iportclsnotifications_freenotification, portcls/IPortClsNotifications::FreeNotificationBuffer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
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
-	Portcls.lib
-	Portcls.dll
api_name:
-	IPortClsNotifications.FreeNotificationBuffer
product: Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---


# FreeNotificationBuffer method
Frees a previously allocated IPortClsNotifications buffer. The buffer is used in sending notifications, to allow for communications between audio modules and UWP apps. 

For more information about audio modules, see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/audio/implementing-audio-module-communication">Implementing Audio Module Discovery</a>.

## Syntax

````
NTSTATUS  FreeNotificationBuffer(
  [in] PPCNOTIFICATION NotificationBuffer
);
````

## Parameters

`NotificationBuffer`

The address of the notification buffer returned in the <a href="https://msdn.microsoft.com/23DBA3D8-FC27-4F5D-9F1C-A22B6C2856D2">IPortClsNotifications::AllocNotificationBuffer</a> call.


## Return Value

This function returns void.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 10, version 1703 and later versions of Windows.  |
| **Target Platform** | Universal |
| **Header** | portcls.h (include Portcls.h) |
| **Library** | Portcls.lib |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="..\portcls\nn-portcls-iportclsnotifications.md">IPortClsNotifications</a>
---
UID: NF:portcls.IPortClsNotifications.SendNotification
title: IPortClsNotifications::SendNotification method
author: windows-driver-content
description: Sends a notification to the listening UWP apps, to allow for communications between audio modules and UWP apps.
old-location: audio\iportclsnotifications_sendnotification.htm
old-project: audio
ms.assetid: 0683C30D-0AAD-4859-BA30-908FA747CC35
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: IPortClsNotifications, IPortClsNotifications interface [Audio Devices], SendNotification method, IPortClsNotifications::SendNotification, SendNotification method [Audio Devices], SendNotification method [Audio Devices], IPortClsNotifications interface, SendNotification,IPortClsNotifications.SendNotification, audio.iportclsnotifications_sendnotification, portcls/IPortClsNotifications::SendNotification
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
-	IPortClsNotifications.SendNotification
product:
- Windows
targetos: Windows
req.typenames: PC_EXIT_LATENCY, *PPC_EXIT_LATENCY
---


# IPortClsNotifications::SendNotification method
Sends a notification to the listening UWP apps, to allow for communications between audio modules and UWP apps.

## Syntax

```
void SendNotification(
  const GUID             *NotificationId,
  PPCNOTIFICATION_BUFFER NotificationBuffer
);
```

## Parameters

`NotificationId`

KSNOTIFICATIONID_AudioModule

`NotificationBuffer`




## Return Value

This function returns void.

## Remarks

Pointer to the PCNOTIFICATION structure to send to Audio Module clients.

The expected format of the payload is a <a href="https://msdn.microsoft.com/92A9462C-0E8C-4012-9374-3437BB220502">KSAUDIOMODULE_NOTIFICATION</a> structure. The miniport driver can optionally send additional information immediately following the <b>KSAUDIOMODULE_NOTIFICATION</b> structure that will be untouched and sent to the Audio Module clients.



For more information about audio modules, see <a href="https://msdn.microsoft.com/en-us/windows/hardware/drivers/audio/implementing-audio-module-communication">Implementing Audio Module Discovery</a>.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows 10, version 1703 and later versions of Windows.  |
| **Target Platform** | Universal |
| **Header** | portcls.h (include Portcls.h) |
| **Library** | Portcls.lib |
| **IRQL** | PASSIVE_LEVEL |

## See Also

<a href="https://msdn.microsoft.com/03F65E4E-C942-4748-8D3E-938A6AC51B2A">IPortClsNotifications</a>
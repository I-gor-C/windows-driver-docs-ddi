---
UID: NC:hdaudio.PUNREGISTER_NOTIFICATION_EVENT
title: PUNREGISTER_NOTIFICATION_EVENT
author: windows-driver-content
description: The UnregisterNotificationEvent routine deletes the registration of an event that was previously registered by a call to RegisterNotificationEvent.The function pointer type for an UnregisterNotificationEvent routine is defined as follows.
old-location: audio\unregisternotificationevent.htm
old-project: audio
ms.assetid: 525e2dd9-68e1-468d-895e-d9f57372d619
ms.author: windowsdriverdev
ms.date: 3/19/2018
ms.keywords: PUNREGISTER_NOTIFICATION_EVENT, UnregisterNotificationEvent, UnregisterNotificationEvent callback function [Audio Devices], aud-prop2_3f7488ae-5744-422e-871f-54dc2fd63bc2.xml, audio.unregisternotificationevent, hdaudio/UnregisterNotificationEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: hdaudio.h
req.include-header: Hdaudio.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows.
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
req.irql: PASSIVE_LEVEL.
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	UserDefined
api_location:
-	Hdaudio.h
api_name:
-	UnregisterNotificationEvent
product: Windows
targetos: Windows
req.typenames: SM_SetRNIDMgmtInfo_OUT, *PSM_SetRNIDMgmtInfo_OUT
---


# PUNREGISTER_NOTIFICATION_EVENT callback function
The <i>UnregisterNotificationEvent</i> routine deletes the registration of an event that was previously registered by a call to <a href="https://msdn.microsoft.com/44702d79-80ac-411f-ae47-bf60b9cb541d">RegisterNotificationEvent</a>.

The function pointer type for an <i>UnregisterNotificationEvent</i> routine is defined as follows.

## Syntax

```
PUNREGISTER_NOTIFICATION_EVENT PunregisterNotificationEvent;

NTSTATUS PunregisterNotificationEvent(
  PVOID _context,
  HANDLE Handle,
  PKEVENT NotificationEvent
)
{...}
```

## Parameters

`_context`

Specifies the context value from the Context member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff536418">HDAUDIO_BUS_INTERFACE_V2</a> structure.

`Handle`

Handle that identifies the DMA engine. This handle value was obtained from a previous call to <a href="https://msdn.microsoft.com/038e52be-04db-41c2-aa19-85bc4eb8bc57">AllocateCaptureDmaEngine</a> or <a href="https://msdn.microsoft.com/fb2a64ca-7e8e-4352-86c6-b9500e535c75">AllocateRenderDmaEngine</a>.

`NotificationEvent`

A pointer to a kernel event that was previously registered for DMA progress notification with a call to <a href="https://msdn.microsoft.com/44702d79-80ac-411f-ae47-bf60b9cb541d">RegisterNotificationEvent</a>.


## Return Value

<i>UnregisterNotificationEvent</i> returns STATUS_SUCCESS if the call successfully unregisters the notification event. Otherwise, the routine returns STATUS_INVALID_PARAMETER to indicate that the specified tag is not valid.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Windows Vista and later versions of Windows.  |
| **Target Platform** | Desktop |
| **Header** | hdaudio.h (include Hdaudio.h) |
| **IRQL** | PASSIVE_LEVEL. |

## See Also

<a href="https://msdn.microsoft.com/038e52be-04db-41c2-aa19-85bc4eb8bc57">AllocateCaptureDmaEngine</a>



<a href="https://msdn.microsoft.com/fb2a64ca-7e8e-4352-86c6-b9500e535c75">AllocateRenderDmaEngine</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff536418">HDAUDIO_BUS_INTERFACE_V2</a>



<a href="https://msdn.microsoft.com/44702d79-80ac-411f-ae47-bf60b9cb541d">RegisterNotificationEvent</a>
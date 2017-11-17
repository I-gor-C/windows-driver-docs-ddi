---
UID: NC.wlanihv.DOT11EXT_SEND_NOTIFICATION
title: DOT11EXT_SEND_NOTIFICATION
author: windows-driver-content
description: 
ms.assetid: a66c2ae8-6452-43ce-9376-5ca2ad8755b7
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wlanihv.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# DOT11EXT_SEND_NOTIFICATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_SEND_NOTIFICATION Dot11extSendNotification; 

// Definition

DWORD Dot11extSendNotification 
(
	HANDLE hDot11SvcHandle
	PL2_NOTIFICATION_DATA pNotificationData
)
{...}

DOT11EXT_SEND_NOTIFICATION 


```

## -parameters

### -param hDot11SvcHandle: 
### -param pNotificationData: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
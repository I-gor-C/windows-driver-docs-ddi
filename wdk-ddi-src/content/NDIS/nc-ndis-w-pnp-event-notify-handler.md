---
UID: NC.ndis.W_PNP_EVENT_NOTIFY_HANDLER
title: W_PNP_EVENT_NOTIFY_HANDLER
author: windows-driver-content
description: 
ms.assetid: 82148071-7ed1-41ba-9d76-6dcad562a448
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndis.h
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

# W_PNP_EVENT_NOTIFY_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

W_PNP_EVENT_NOTIFY_HANDLER WPnpEventNotifyHandler; 

// Definition

VOID WPnpEventNotifyHandler 
(
	NDIS_HANDLE MiniportAdapterContext
	NDIS_DEVICE_PNP_EVENT DevicePnPEvent
	PVOID InformationBuffer
	ULONG InformationBufferLength
)
{...}

W_PNP_EVENT_NOTIFY_HANDLER 


```

## -parameters

### -param MiniportAdapterContext: 
### -param DevicePnPEvent: 
### -param InformationBuffer: 
### -param InformationBufferLength: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.mfgphone.MFGPHONE_SIMLINEEVENT_NOTIFY_CALLBACK
title: MFGPHONE_SIMLINEEVENT_NOTIFY_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 407aeade-18a4-420a-817c-b0d2ec7cb58d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mfgphone.h
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

# MFGPHONE_SIMLINEEVENT_NOTIFY_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

MFGPHONE_SIMLINEEVENT_NOTIFY_CALLBACK MfgphoneSimlineeventNotifyCallback; 

// Definition

VOID MfgphoneSimlineeventNotifyCallback 
(
	UINT SimSlot
	MFGPHONE_SIMLINEEVENT SimLineEvent
	PVOID Context
)
{...}

MFGPHONE_SIMLINEEVENT_NOTIFY_CALLBACK 


```

## -parameters

### -param SimSlot: 
### -param SimLineEvent: 
### -param Context: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
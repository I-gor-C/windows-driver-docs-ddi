---
UID: NC.fwpsk.FWPS_CALLOUT_BOOTTIME_CALLOUT_DELETE_NOTIFY_FN0
title: FWPS_CALLOUT_BOOTTIME_CALLOUT_DELETE_NOTIFY_FN0
author: windows-driver-content
description: 
ms.assetid: ac246524-254f-4bd3-8f57-42c4b4993551
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: fwpsk.h
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

# FWPS_CALLOUT_BOOTTIME_CALLOUT_DELETE_NOTIFY_FN0 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

FWPS_CALLOUT_BOOTTIME_CALLOUT_DELETE_NOTIFY_FN0 FwpsCalloutBoottimeCalloutDeleteNotifyFn0; 

// Definition

void FwpsCalloutBoottimeCalloutDeleteNotifyFn0 
(
	UINT32 calloutId
)
{...}

FWPS_CALLOUT_BOOTTIME_CALLOUT_DELETE_NOTIFY_FN0 


```

## -parameters

### -param calloutId: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
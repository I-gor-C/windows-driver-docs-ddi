---
UID: NC.fwpsk.FWPS_CALLOUT_NOTIFY_FN3
title: FWPS_CALLOUT_NOTIFY_FN3
author: windows-driver-content
description: 
ms.assetid: 93a0b9af-d778-4f9f-ba2a-8a98b773cee3
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

# FWPS_CALLOUT_NOTIFY_FN3 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

FWPS_CALLOUT_NOTIFY_FN3 FwpsCalloutNotifyFn3; 

// Definition

NTSTATUS FwpsCalloutNotifyFn3 
(
	FWPS_CALLOUT_NOTIFY_TYPE notifyType
	 const GUID *filterKey
	FWPS_FILTER3 *filter
)
{...}

FWPS_CALLOUT_NOTIFY_FN3 


```

## -parameters

### -param notifyType: 
### -param *filterKey: 
### -param *filter: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
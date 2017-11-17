---
UID: NC.wdm.FWMI_NOTIFICATION_CALLBACK
title: FWMI_NOTIFICATION_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 8f446e0e-1155-4f37-863b-a1edb9ffb713
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# FWMI_NOTIFICATION_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

FWMI_NOTIFICATION_CALLBACK FwmiNotificationCallback; 

// Definition

_IRQL_requires_same_ VOID FwmiNotificationCallback 
(
	PVOID Wnode
	PVOID Context
)
{...}

FWMI_NOTIFICATION_CALLBACK WMI_NOTIFICATION_CALLBACK


```

## -parameters

### -param Wnode: 
### -param Context: 



## -returns

Returns _IRQL_requires_same_ VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
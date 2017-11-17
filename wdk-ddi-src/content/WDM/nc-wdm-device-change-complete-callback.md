---
UID: NC.wdm.DEVICE_CHANGE_COMPLETE_CALLBACK
title: DEVICE_CHANGE_COMPLETE_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 29622999-7335-49da-90f7-634b4c1e80b5
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

# DEVICE_CHANGE_COMPLETE_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DEVICE_CHANGE_COMPLETE_CALLBACK DeviceChangeCompleteCallback; 

// Definition

_IRQL_requires_same_ VOID DeviceChangeCompleteCallback 
(
	PVOID Context
)
{...}

DEVICE_CHANGE_COMPLETE_CALLBACK PDEVICE_CHANGE_COMPLETE_CALLBACK


```

## -parameters

### -param Context: 



## -returns

Returns _IRQL_requires_same_ VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
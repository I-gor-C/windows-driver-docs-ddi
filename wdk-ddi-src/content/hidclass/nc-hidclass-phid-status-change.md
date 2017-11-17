---
UID: NC.hidclass.PHID_STATUS_CHANGE
title: PHID_STATUS_CHANGE
author: windows-driver-content
description: 
ms.assetid: 3f37b7b2-4d92-4ed5-af74-5b1fc6fb46c1
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hidclass.h
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

# PHID_STATUS_CHANGE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHID_STATUS_CHANGE PhidStatusChange; 

// Definition

VOID PhidStatusChange 
(
	PVOID Context
	DeviceObjectState State
)
{...}

PHID_STATUS_CHANGE 


```

## -parameters

### -param Context: 
### -param State: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
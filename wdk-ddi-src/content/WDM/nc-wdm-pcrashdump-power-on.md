---
UID: NC.wdm.PCRASHDUMP_POWER_ON
title: PCRASHDUMP_POWER_ON
author: windows-driver-content
description: 
ms.assetid: dc1236cd-452d-4df7-9d8a-cb7c4375988c
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

# PCRASHDUMP_POWER_ON callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCRASHDUMP_POWER_ON PcrashdumpPowerOn; 

// Definition

NTSTATUS PcrashdumpPowerOn 
(
	PVOID Context
)
{...}

PCRASHDUMP_POWER_ON 


```

## -parameters

### -param Context: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
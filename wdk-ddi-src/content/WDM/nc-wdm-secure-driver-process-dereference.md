---
UID: NC.wdm.SECURE_DRIVER_PROCESS_DEREFERENCE
title: SECURE_DRIVER_PROCESS_DEREFERENCE
author: windows-driver-content
description: 
ms.assetid: cf369c5b-df80-49e7-af94-a306cd657ccb
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

# SECURE_DRIVER_PROCESS_DEREFERENCE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

SECURE_DRIVER_PROCESS_DEREFERENCE SecureDriverProcessDereference; 

// Definition

VOID SecureDriverProcessDereference 
(
	PVOID InterfaceContext
	PEPROCESS Process
)
{...}

SECURE_DRIVER_PROCESS_DEREFERENCE PSECURE_DRIVER_PROCESS_DEREFERENCE


```

## -parameters

### -param InterfaceContext: 
### -param Process: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
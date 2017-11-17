---
UID: NC.wdm.SECURE_DRIVER_PROCESS_REFERENCE
title: SECURE_DRIVER_PROCESS_REFERENCE
author: windows-driver-content
description: 
ms.assetid: 66cdc60f-c569-4c9d-ae06-8d315bc42b70
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

# SECURE_DRIVER_PROCESS_REFERENCE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

SECURE_DRIVER_PROCESS_REFERENCE SecureDriverProcessReference; 

// Definition

PEPROCESS SecureDriverProcessReference 
(
	PVOID InterfaceContext
)
{...}

SECURE_DRIVER_PROCESS_REFERENCE PSECURE_DRIVER_PROCESS_REFERENCE


```

## -parameters

### -param InterfaceContext: 



## -returns

Returns PEPROCESS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
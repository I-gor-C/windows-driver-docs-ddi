---
UID: NC.classpnp.PCLASS_SCAN_FOR_SPECIAL_HANDLER
title: PCLASS_SCAN_FOR_SPECIAL_HANDLER
author: windows-driver-content
description: 
ms.assetid: a4ea5b64-8f5e-4144-95b0-b69aa688ea07
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: classpnp.h
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

# PCLASS_SCAN_FOR_SPECIAL_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_SCAN_FOR_SPECIAL_HANDLER PclassScanForSpecialHandler; 

// Definition

VOID PclassScanForSpecialHandler 
(
	PFUNCTIONAL_DEVICE_EXTENSION FdoExtension
	ULONG_PTR Data
)
{...}

PCLASS_SCAN_FOR_SPECIAL_HANDLER 


```

## -parameters

### -param FdoExtension: 
### -param Data: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
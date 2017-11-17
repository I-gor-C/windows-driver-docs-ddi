---
UID: NC.wdm.PREPLACE_UNLOAD
title: PREPLACE_UNLOAD
author: windows-driver-content
description: 
ms.assetid: 8f02761e-465d-452f-a08d-63a1933d2e3a
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

# PREPLACE_UNLOAD callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PREPLACE_UNLOAD PreplaceUnload; 

// Definition

VOID PreplaceUnload 
(
	 VOID
)
{...}

PREPLACE_UNLOAD 


```

## -parameters

### -param VOID: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.d3dkmthk.PDXGK_GRAPHICSPOWER_UNREGISTER
title: PDXGK_GRAPHICSPOWER_UNREGISTER
author: windows-driver-content
description: 
ms.assetid: 887e55d0-d914-4871-86db-f91fd96150d6
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dkmthk.h
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

# PDXGK_GRAPHICSPOWER_UNREGISTER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PDXGK_GRAPHICSPOWER_UNREGISTER PdxgkGraphicspowerUnregister; 

// Definition

NTSTATUS PdxgkGraphicspowerUnregister 
(
	PVOID DeviceHandle
	PVOID PrivateHandle
)
{...}

PDXGK_GRAPHICSPOWER_UNREGISTER 


```

## -parameters

### -param DeviceHandle: 
### -param PrivateHandle: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.ks.PFNKSINTERSECTHANDLER
title: PFNKSINTERSECTHANDLER
author: windows-driver-content
description: 
ms.assetid: 3103e1dd-c0e3-4fd9-98f8-c8f63ed44c91
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSINTERSECTHANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSINTERSECTHANDLER Pfnksintersecthandler; 

// Definition

NTSTATUS Pfnksintersecthandler 
(
	PIRP Irp
	PKSP_PIN Pin
	PKSDATARANGE DataRange
	PVOID Data
)
{...}

PFNKSINTERSECTHANDLER 


```

## -parameters

### -param Irp: 
### -param Pin: 
### -param DataRange: 
### -param Data: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.ks.PFNKSHANDLER
title: PFNKSHANDLER
author: windows-driver-content
description: 
ms.assetid: b51109f9-0e69-4eca-b5a0-063ee5abbe4c
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

# PFNKSHANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSHANDLER Pfnkshandler; 

// Definition

NTSTATUS Pfnkshandler 
(
	PIRP Irp
	PKSIDENTIFIER Request
	PVOID Data
)
{...}

PFNKSHANDLER 


```

## -parameters

### -param Irp: 
### -param Request: 
### -param Data: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.ndis.BIND_HANDLER
title: BIND_HANDLER
author: windows-driver-content
description: 
ms.assetid: 2d13fa41-b42d-48d9-92af-2ea83291cc9f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndis.h
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

# BIND_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

BIND_HANDLER BindHandler; 

// Definition

VOID BindHandler 
(
	PNDIS_STATUS Status
	NDIS_HANDLE BindContext
	PNDIS_STRING DeviceName
	PVOID SystemSpecific1
	PVOID SystemSpecific2
)
{...}

BIND_HANDLER 


```

## -parameters

### -param Status: 
### -param BindContext: 
### -param DeviceName: 
### -param SystemSpecific1: 
### -param SystemSpecific2: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
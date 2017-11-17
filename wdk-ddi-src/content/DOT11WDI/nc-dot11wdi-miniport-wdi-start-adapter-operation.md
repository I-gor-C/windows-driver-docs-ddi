---
UID: NC.dot11wdi.MINIPORT_WDI_START_ADAPTER_OPERATION
title: MINIPORT_WDI_START_ADAPTER_OPERATION
author: windows-driver-content
description: 
ms.assetid: d5c4cdd1-2983-458f-949c-3a49f46cf93f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dot11wdi.h
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

# MINIPORT_WDI_START_ADAPTER_OPERATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

MINIPORT_WDI_START_ADAPTER_OPERATION MiniportWdiStartAdapterOperation; 

// Definition

NDIS_STATUS MiniportWdiStartAdapterOperation 
(
	NDIS_HANDLE MiniportAdapterContext
)
{...}

MINIPORT_WDI_START_ADAPTER_OPERATION 


```

## -parameters

### -param MiniportAdapterContext: 



## -returns

Returns NDIS_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
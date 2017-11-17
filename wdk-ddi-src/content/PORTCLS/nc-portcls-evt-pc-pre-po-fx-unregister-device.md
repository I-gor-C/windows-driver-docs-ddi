---
UID: NC.portcls.EVT_PC_PRE_PO_FX_UNREGISTER_DEVICE
title: EVT_PC_PRE_PO_FX_UNREGISTER_DEVICE
author: windows-driver-content
description: 
ms.assetid: 6ed0a1fa-dc95-42bd-945d-9b66c58dfe6b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: portcls.h
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

# EVT_PC_PRE_PO_FX_UNREGISTER_DEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_PC_PRE_PO_FX_UNREGISTER_DEVICE EvtPcPrePoFxUnregisterDevice; 

// Definition

VOID EvtPcPrePoFxUnregisterDevice 
(
	PVOID PoFxDeviceContext
	POHANDLE PoHandle
)
{...}

EVT_PC_PRE_PO_FX_UNREGISTER_DEVICE PFN_PC_PRE_PO_FX_UNREGISTER_DEVICE


```

## -parameters

### -param PoFxDeviceContext: 
### -param PoHandle: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
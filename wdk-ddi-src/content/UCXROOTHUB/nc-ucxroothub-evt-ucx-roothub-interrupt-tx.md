---
UID: NC.ucxroothub.EVT_UCX_ROOTHUB_INTERRUPT_TX
title: EVT_UCX_ROOTHUB_INTERRUPT_TX
author: windows-driver-content
description: 
ms.assetid: 869ba210-a3f4-488d-a9df-4a0bef867490
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxroothub.h
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

# EVT_UCX_ROOTHUB_INTERRUPT_TX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UCX_ROOTHUB_INTERRUPT_TX EvtUcxRoothubInterruptTx; 

// Definition

VOID EvtUcxRoothubInterruptTx 
(
	UCXROOTHUB UcxRootHub
	WDFREQUEST Request
)
{...}

EVT_UCX_ROOTHUB_INTERRUPT_TX PFN_UCX_ROOTHUB_INTERRUPT_TX


```

## -parameters

### -param UcxRootHub: 
### -param Request: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
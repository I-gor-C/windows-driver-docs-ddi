---
UID: NC.tdikrnl.ProviderPnPPowerComplete
title: ProviderPnPPowerComplete
author: windows-driver-content
description: 
ms.assetid: f496639b-1061-4136-a58a-3b68e53f8339
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: tdikrnl.h
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

# ProviderPnPPowerComplete callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ProviderPnPPowerComplete Providerpnppowercomplete; 

// Definition

VOID Providerpnppowercomplete 
(
	PNET_PNP_EVENT NetEvent
	NTSTATUS ProviderStatus
)
{...}

ProviderPnPPowerComplete 


```

## -parameters

### -param NetEvent: 
### -param ProviderStatus: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
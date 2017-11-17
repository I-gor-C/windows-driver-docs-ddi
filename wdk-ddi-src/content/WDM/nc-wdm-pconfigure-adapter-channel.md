---
UID: NC.wdm.PCONFIGURE_ADAPTER_CHANNEL
title: PCONFIGURE_ADAPTER_CHANNEL
author: windows-driver-content
description: 
ms.assetid: 49500a3d-451e-4603-abc9-b828bb530425
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

# PCONFIGURE_ADAPTER_CHANNEL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCONFIGURE_ADAPTER_CHANNEL PconfigureAdapterChannel; 

// Definition

NTSTATUS PconfigureAdapterChannel 
(
	PDMA_ADAPTER DmaAdapter
	ULONG FunctionNumber
	PVOID Context
)
{...}

PCONFIGURE_ADAPTER_CHANNEL 


```

## -parameters

### -param DmaAdapter: 
### -param FunctionNumber: 
### -param Context: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
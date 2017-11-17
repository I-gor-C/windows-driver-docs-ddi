---
UID: NC.wdm.PCANCEL_ADAPTER_CHANNEL
title: PCANCEL_ADAPTER_CHANNEL
author: windows-driver-content
description: 
ms.assetid: 2bb650f6-4944-47d3-aa7a-7f4760cc2bec
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

# PCANCEL_ADAPTER_CHANNEL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCANCEL_ADAPTER_CHANNEL PcancelAdapterChannel; 

// Definition

BOOLEAN PcancelAdapterChannel 
(
	PDMA_ADAPTER DmaAdapter
	PDEVICE_OBJECT DeviceObject
	PVOID DmaTransferContext
)
{...}

PCANCEL_ADAPTER_CHANNEL 


```

## -parameters

### -param DmaAdapter: 
### -param DeviceObject: 
### -param DmaTransferContext: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
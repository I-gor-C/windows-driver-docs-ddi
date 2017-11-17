---
UID: NC.wdm.PFLUSH_ADAPTER_BUFFERS
title: PFLUSH_ADAPTER_BUFFERS
author: windows-driver-content
description: 
ms.assetid: 55ed0c6c-c4e9-42ae-826a-6c7594263fda
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

# PFLUSH_ADAPTER_BUFFERS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFLUSH_ADAPTER_BUFFERS PflushAdapterBuffers; 

// Definition

BOOLEAN PflushAdapterBuffers 
(
	PDMA_ADAPTER DmaAdapter
	PMDL Mdl
	PVOID MapRegisterBase
	PVOID CurrentVa
	ULONG Length
	BOOLEAN WriteToDevice
)
{...}

PFLUSH_ADAPTER_BUFFERS 


```

## -parameters

### -param DmaAdapter: 
### -param Mdl: 
### -param MapRegisterBase: 
### -param CurrentVa: 
### -param Length: 
### -param WriteToDevice: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
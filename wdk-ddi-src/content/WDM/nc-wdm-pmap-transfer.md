---
UID: NC.wdm.PMAP_TRANSFER
title: PMAP_TRANSFER
author: windows-driver-content
description: 
ms.assetid: 55917207-1d86-4565-90ae-bc49e7f3f3db
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

# PMAP_TRANSFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMAP_TRANSFER PmapTransfer; 

// Definition

PHYSICAL_ADDRESS PmapTransfer 
(
	PDMA_ADAPTER DmaAdapter
	PMDL Mdl
	PVOID MapRegisterBase
	PVOID CurrentVa
	PULONG Length
	BOOLEAN WriteToDevice
)
{...}

PMAP_TRANSFER 


```

## -parameters

### -param DmaAdapter: 
### -param Mdl: 
### -param MapRegisterBase: 
### -param CurrentVa: 
### -param Length: 
### -param WriteToDevice: 



## -returns

Returns PHYSICAL_ADDRESS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.wdm.PCANCEL_MAPPED_TRANSFER
title: PCANCEL_MAPPED_TRANSFER
author: windows-driver-content
description: 
ms.assetid: 977b4f84-1ee0-4529-bbe8-6630f05a256a
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

# PCANCEL_MAPPED_TRANSFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCANCEL_MAPPED_TRANSFER PcancelMappedTransfer; 

// Definition

NTSTATUS PcancelMappedTransfer 
(
	PDMA_ADAPTER DmaAdapter
	PVOID DmaTransferContext
)
{...}

PCANCEL_MAPPED_TRANSFER 


```

## -parameters

### -param DmaAdapter: 
### -param DmaTransferContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
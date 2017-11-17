---
UID: NC.wdm.PFLUSH_ADAPTER_BUFFERS_EX
title: PFLUSH_ADAPTER_BUFFERS_EX
author: windows-driver-content
description: 
ms.assetid: 4f59a8ef-38a9-40db-9dbc-8603728478a5
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

# PFLUSH_ADAPTER_BUFFERS_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFLUSH_ADAPTER_BUFFERS_EX PflushAdapterBuffersEx; 

// Definition

NTSTATUS PflushAdapterBuffersEx 
(
	PDMA_ADAPTER DmaAdapter
	PMDL Mdl
	PVOID MapRegisterBase
	ULONGLONG Offset
	ULONG Length
	BOOLEAN WriteToDevice
)
{...}

PFLUSH_ADAPTER_BUFFERS_EX 


```

## -parameters

### -param DmaAdapter: 
### -param Mdl: 
### -param MapRegisterBase: 
### -param Offset: 
### -param Length: 
### -param WriteToDevice: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
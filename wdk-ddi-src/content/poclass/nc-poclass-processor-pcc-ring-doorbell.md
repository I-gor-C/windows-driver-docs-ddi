---
UID: NC.poclass.PROCESSOR_PCC_RING_DOORBELL
title: PROCESSOR_PCC_RING_DOORBELL
author: windows-driver-content
description: 
ms.assetid: b9f1b4d1-2aa3-4ac6-a268-de628b75c998
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: poclass.h
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

# PROCESSOR_PCC_RING_DOORBELL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PROCESSOR_PCC_RING_DOORBELL ProcessorPccRingDoorbell; 

// Definition

NTSTATUS ProcessorPccRingDoorbell 
(
	UCHAR Command
	PPROCESSOR_PCC_DOORBELL_CALLBACK Callback
	ULONG_PTR Context
)
{...}

PROCESSOR_PCC_RING_DOORBELL 


```

## -parameters

### -param Command: 
### -param Callback: 
### -param Context: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
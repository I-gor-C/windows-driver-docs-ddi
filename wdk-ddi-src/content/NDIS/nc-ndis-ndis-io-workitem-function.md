---
UID: NC.ndis.NDIS_IO_WORKITEM_FUNCTION
title: NDIS_IO_WORKITEM_FUNCTION
author: windows-driver-content
description: 
ms.assetid: 5ab2b195-f416-4a50-b4cb-8fa9724dba27
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ndis.h
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

# NDIS_IO_WORKITEM_FUNCTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NDIS_IO_WORKITEM_FUNCTION NdisIoWorkitemFunction; 

// Definition

VOID NdisIoWorkitemFunction 
(
	PVOID WorkItemContext
	NDIS_HANDLE NdisIoWorkItemHandle
)
{...}

NDIS_IO_WORKITEM_FUNCTION PNDIS_IO_WORKITEM_FUNCTION


```

## -parameters

### -param WorkItemContext: 
### -param NdisIoWorkItemHandle: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
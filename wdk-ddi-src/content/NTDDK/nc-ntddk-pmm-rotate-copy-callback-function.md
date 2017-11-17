---
UID: NC.ntddk.PMM_ROTATE_COPY_CALLBACK_FUNCTION
title: PMM_ROTATE_COPY_CALLBACK_FUNCTION
author: windows-driver-content
description: 
ms.assetid: 0a92e336-91f9-47d3-b582-72d0571ff7e9
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# PMM_ROTATE_COPY_CALLBACK_FUNCTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMM_ROTATE_COPY_CALLBACK_FUNCTION PmmRotateCopyCallbackFunction; 

// Definition

NTSTATUS PmmRotateCopyCallbackFunction 
(
	PMDL DestinationMdl
	PMDL SourceMdl
	PVOID Context
)
{...}

PMM_ROTATE_COPY_CALLBACK_FUNCTION 


```

## -parameters

### -param DestinationMdl: 
### -param SourceMdl: 
### -param Context: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
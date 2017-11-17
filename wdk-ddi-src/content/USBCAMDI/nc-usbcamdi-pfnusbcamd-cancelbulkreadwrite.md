---
UID: NC.usbcamdi.PFNUSBCAMD_CancelBulkReadWrite
title: PFNUSBCAMD_CancelBulkReadWrite
author: windows-driver-content
description: 
ms.assetid: 586fe694-311a-4506-a114-a76606fcf9eb
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: usbcamdi.h
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

# PFNUSBCAMD_CancelBulkReadWrite callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNUSBCAMD_CancelBulkReadWrite PfnusbcamdCancelbulkreadwrite; 

// Definition

NTSTATUS PfnusbcamdCancelbulkreadwrite 
(
	PVOID DeviceContext
	ULONG PipeIndex
)
{...}

PFNUSBCAMD_CancelBulkReadWrite 


```

## -parameters

### -param DeviceContext: 
### -param PipeIndex: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
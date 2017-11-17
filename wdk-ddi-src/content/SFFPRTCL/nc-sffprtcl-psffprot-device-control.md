---
UID: NC.sffprtcl.PSFFPROT_DEVICE_CONTROL
title: PSFFPROT_DEVICE_CONTROL
author: windows-driver-content
description: 
ms.assetid: 01f689f1-bbc3-4de3-965c-b7f46a2c5712
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sffprtcl.h
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

# PSFFPROT_DEVICE_CONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSFFPROT_DEVICE_CONTROL PsffprotDeviceControl; 

// Definition

NTSTATUS PsffprotDeviceControl 
(
	IN PVOID Context
	IN SFFPROT_DCTYPE Type
	IN PVOID Buffer
	IN ULONG Length
	OUT PULONG LengthReturned
)
{...}

PSFFPROT_DEVICE_CONTROL 


```

## -parameters

### -param Context: 
### -param Type: 
### -param Buffer: 
### -param Length: 
### -param LengthReturned: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
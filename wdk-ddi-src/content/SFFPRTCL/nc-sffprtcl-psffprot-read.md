---
UID: NC.sffprtcl.PSFFPROT_READ
title: PSFFPROT_READ
author: windows-driver-content
description: 
ms.assetid: c3f983f1-ede4-4ce5-a47c-5a14ecb47ba4
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

# PSFFPROT_READ callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSFFPROT_READ PsffprotRead; 

// Definition

NTSTATUS PsffprotRead 
(
	IN PVOID Context
	IN PMDL Mdl
	IN ULONGLONG Offset
	IN ULONG Length
	OUT PULONG LengthReturned
)
{...}

PSFFPROT_READ 


```

## -parameters

### -param Context: 
### -param Mdl: 
### -param Offset: 
### -param Length: 
### -param LengthReturned: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
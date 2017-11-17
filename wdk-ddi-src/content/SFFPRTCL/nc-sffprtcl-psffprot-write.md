---
UID: NC.sffprtcl.PSFFPROT_WRITE
title: PSFFPROT_WRITE
author: windows-driver-content
description: 
ms.assetid: b941ace0-8589-4fe5-ad23-11e7acf9299c
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

# PSFFPROT_WRITE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSFFPROT_WRITE PsffprotWrite; 

// Definition

NTSTATUS PsffprotWrite 
(
	IN PVOID Context
	IN PMDL Mdl
	IN ULONGLONG Offset
	IN ULONG Length
	OUT PULONG LengthReturned
)
{...}

PSFFPROT_WRITE 


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
---
UID: NC.sffprtcl.PSFFPROT_TRIM
title: PSFFPROT_TRIM
author: windows-driver-content
description: 
ms.assetid: d56e24de-c3cc-41af-a470-78f1ae2e5773
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

# PSFFPROT_TRIM callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSFFPROT_TRIM PsffprotTrim; 

// Definition

NTSTATUS PsffprotTrim 
(
	IN PVOID Context
	IN PVOID DataSetRanges
	IN ULONG DataSetRangesCount
)
{...}

PSFFPROT_TRIM 


```

## -parameters

### -param Context: 
### -param DataSetRanges: 
### -param DataSetRangesCount: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
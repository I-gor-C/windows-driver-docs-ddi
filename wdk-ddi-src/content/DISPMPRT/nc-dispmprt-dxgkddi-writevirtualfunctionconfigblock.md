---
UID: NC.dispmprt.DXGKDDI_WRITEVIRTUALFUNCTIONCONFIGBLOCK
title: DXGKDDI_WRITEVIRTUALFUNCTIONCONFIGBLOCK
author: windows-driver-content
description: 
ms.assetid: 444cc373-0b6e-4fc3-a053-c585dc61656e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dispmprt.h
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

# DXGKDDI_WRITEVIRTUALFUNCTIONCONFIGBLOCK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_WRITEVIRTUALFUNCTIONCONFIGBLOCK DxgkddiWritevirtualfunctionconfigblock; 

// Definition

NTSTATUS DxgkddiWritevirtualfunctionconfigblock 
(
	HANDLE Context
	DXGKARG_WRITEVIRTUALFUNCTIONCONFIGBLOCK * pArgs
)
{...}

DXGKDDI_WRITEVIRTUALFUNCTIONCONFIGBLOCK PDXGKDDI_WRITEVIRTUALFUNCTIONCONFIGBLOCK


```

## -parameters

### -param Context: 
### -param pArgs: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
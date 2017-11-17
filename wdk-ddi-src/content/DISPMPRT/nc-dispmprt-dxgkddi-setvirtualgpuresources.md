---
UID: NC.dispmprt.DXGKDDI_SETVIRTUALGPURESOURCES
title: DXGKDDI_SETVIRTUALGPURESOURCES
author: windows-driver-content
description: 
ms.assetid: 69d53594-b139-4002-8b1b-ff0ae216c060
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

# DXGKDDI_SETVIRTUALGPURESOURCES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_SETVIRTUALGPURESOURCES DxgkddiSetvirtualgpuresources; 

// Definition

NTSTATUS DxgkddiSetvirtualgpuresources 
(
	HANDLE Context
	DXGKARG_SETVIRTUALGPURESOURCES * pArgs
)
{...}

DXGKDDI_SETVIRTUALGPURESOURCES PDXGKDDI_SETVIRTUALGPURESOURCES


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
---
UID: NC.iddcx.PFN_IDDCXGETVERSION
title: *PFN_IDDCXGETVERSION
author: windows-driver-content
description: 
ms.assetid: 40c4b8db-c3eb-43dc-b1b5-3f508a5df567
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: iddcx.h
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

# *PFN_IDDCXGETVERSION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_IDDCXGETVERSION *PfnIddcxgetversion; 

// Definition

NTSTATUS *PfnIddcxgetversion 
(
	PIDD_DRIVER_GLOBALS DriverGlobals
	IDARG_OUT_GETVERSION *pOutArgs
)
{...}

*PFN_IDDCXGETVERSION 


```

## -parameters

### -param DriverGlobals: 
### -param *pOutArgs: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
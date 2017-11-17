---
UID: NC.iddcx.PFN_IDDCXADAPTERUPDATEMAXDISPLAYPIPELINERATE
title: *PFN_IDDCXADAPTERUPDATEMAXDISPLAYPIPELINERATE
author: windows-driver-content
description: 
ms.assetid: 3000f56a-4afe-4a5b-b7c9-1d84b9a7fa9a
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

# *PFN_IDDCXADAPTERUPDATEMAXDISPLAYPIPELINERATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_IDDCXADAPTERUPDATEMAXDISPLAYPIPELINERATE *PfnIddcxadapterupdatemaxdisplaypipelinerate; 

// Definition

NTSTATUS *PfnIddcxadapterupdatemaxdisplaypipelinerate 
(
	PIDD_DRIVER_GLOBALS DriverGlobals
	IDDCX_ADAPTER hOsAdapterContext
	CONST IDARG_IN_MAXDISPLAYPIPELINERATE *pInArgs
)
{...}

*PFN_IDDCXADAPTERUPDATEMAXDISPLAYPIPELINERATE 


```

## -parameters

### -param DriverGlobals: 
### -param hOsAdapterContext: 
### -param *pInArgs: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
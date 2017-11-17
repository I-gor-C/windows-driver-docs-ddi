---
UID: NC.iddcx.PFN_IDDCXREPORTCRITICALERROR
title: *PFN_IDDCXREPORTCRITICALERROR
author: windows-driver-content
description: 
ms.assetid: 24ea7f83-ba3f-4173-a338-9f55b570f5dc
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

# *PFN_IDDCXREPORTCRITICALERROR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_IDDCXREPORTCRITICALERROR *PfnIddcxreportcriticalerror; 

// Definition

NTSTATUS *PfnIddcxreportcriticalerror 
(
	PIDD_DRIVER_GLOBALS DriverGlobals
	IDDCX_ADAPTER AdapterObject
	IDARG_IN_REPORTCRITICALERROR *pInArgs
)
{...}

*PFN_IDDCXREPORTCRITICALERROR 


```

## -parameters

### -param DriverGlobals: 
### -param AdapterObject: 
### -param *pInArgs: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
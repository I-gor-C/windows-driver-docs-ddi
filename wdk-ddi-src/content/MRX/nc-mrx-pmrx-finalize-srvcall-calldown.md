---
UID: NC.mrx.PMRX_FINALIZE_SRVCALL_CALLDOWN
title: PMRX_FINALIZE_SRVCALL_CALLDOWN
author: windows-driver-content
description: 
ms.assetid: 4749f5f2-2941-4d02-acea-54c6526253b2
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mrx.h
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

# PMRX_FINALIZE_SRVCALL_CALLDOWN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_FINALIZE_SRVCALL_CALLDOWN PmrxFinalizeSrvcallCalldown; 

// Definition

NTSTATUS PmrxFinalizeSrvcallCalldown 
(
	IN OUT PMRX_SRV_CALL SrvCall
	IN BOOLEAN Force
)
{...}

PMRX_FINALIZE_SRVCALL_CALLDOWN 


```

## -parameters

### -param SrvCall: 
### -param Force: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
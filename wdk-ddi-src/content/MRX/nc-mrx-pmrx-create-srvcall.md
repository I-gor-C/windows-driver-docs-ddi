---
UID: NC.mrx.PMRX_CREATE_SRVCALL
title: PMRX_CREATE_SRVCALL
author: windows-driver-content
description: 
ms.assetid: 22a93d63-5370-41c0-a720-f74839d3d77c
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

# PMRX_CREATE_SRVCALL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_CREATE_SRVCALL PmrxCreateSrvcall; 

// Definition

NTSTATUS PmrxCreateSrvcall 
(
	IN OUT PMRX_SRV_CALL SrvCall
	IN OUT PMRX_SRVCALL_CALLBACK_CONTEXT SrvCallCallBackContext
)
{...}

PMRX_CREATE_SRVCALL 


```

## -parameters

### -param SrvCall: 
### -param SrvCallCallBackContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
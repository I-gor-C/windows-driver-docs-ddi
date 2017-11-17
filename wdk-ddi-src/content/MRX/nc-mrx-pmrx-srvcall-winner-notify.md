---
UID: NC.mrx.PMRX_SRVCALL_WINNER_NOTIFY
title: PMRX_SRVCALL_WINNER_NOTIFY
author: windows-driver-content
description: 
ms.assetid: 012f7920-45fb-4fc2-b3e3-451465aa7b80
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

# PMRX_SRVCALL_WINNER_NOTIFY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_SRVCALL_WINNER_NOTIFY PmrxSrvcallWinnerNotify; 

// Definition

NTSTATUS PmrxSrvcallWinnerNotify 
(
	IN OUT PMRX_SRV_CALL SrvCall
	IN BOOLEAN ThisMinirdrIsTheWinner
	IN OUT PVOID RecommunicateContext
)
{...}

PMRX_SRVCALL_WINNER_NOTIFY 


```

## -parameters

### -param SrvCall: 
### -param ThisMinirdrIsTheWinner: 
### -param RecommunicateContext: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
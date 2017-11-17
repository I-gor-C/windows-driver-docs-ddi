---
UID: NC.dsm.DSM_BROADCAST_SRB
title: DSM_BROADCAST_SRB
author: windows-driver-content
description: 
ms.assetid: a74a4fbc-ce70-41c5-970e-6fbab993ab19
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dsm.h
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

# DSM_BROADCAST_SRB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_BROADCAST_SRB DsmBroadcastSrb; 

// Definition

NTSTATUS DsmBroadcastSrb 
(
	IN PVOID DsmContext
	IN PDSM_IDS DsmIds
	IN PIRP Irp
	IN PSCSI_REQUEST_BLOCK Srb
	IN PKEVENT Event
)
{...}

DSM_BROADCAST_SRB 


```

## -parameters

### -param DsmContext: 
### -param DsmIds: 
### -param Irp: 
### -param Srb: 
### -param Event: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
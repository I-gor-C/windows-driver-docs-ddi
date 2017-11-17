---
UID: NC.dsm.DSM_SRB_DEVICE_CONTROL
title: DSM_SRB_DEVICE_CONTROL
author: windows-driver-content
description: 
ms.assetid: 9c8cb57d-5d90-4cb1-97dd-394003bfbf20
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

# DSM_SRB_DEVICE_CONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DSM_SRB_DEVICE_CONTROL DsmSrbDeviceControl; 

// Definition

NTSTATUS DsmSrbDeviceControl 
(
	IN PVOID DsmContext
	IN PDSM_IDS DsmIds
	IN PIRP Irp
	IN PSCSI_REQUEST_BLOCK Srb
	IN PKEVENT Event
)
{...}

DSM_SRB_DEVICE_CONTROL 


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
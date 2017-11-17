---
UID: NC.wsk.PFN_WSK_INSPECT_COMPLETE
title: PFN_WSK_INSPECT_COMPLETE
author: windows-driver-content
description: 
ms.assetid: 83568d05-b0ec-4cd0-8a1c-b1264dc0c363
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wsk.h
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

# PFN_WSK_INSPECT_COMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WSK_INSPECT_COMPLETE PfnWskInspectComplete; 

// Definition

NTSTATUS PfnWskInspectComplete 
(
	PWSK_SOCKET ListenSocket
	PWSK_INSPECT_ID InspectID
	WSK_INSPECT_ACTION Action
	PIRP Irp
)
{...}

PFN_WSK_INSPECT_COMPLETE 


```

## -parameters

### -param ListenSocket: 
### -param InspectID: 
### -param Action: 
### -param Irp: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
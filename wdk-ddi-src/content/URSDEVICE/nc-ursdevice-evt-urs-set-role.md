---
UID: NC.ursdevice.EVT_URS_SET_ROLE
title: EVT_URS_SET_ROLE
author: windows-driver-content
description: 
ms.assetid: 0c9558a5-05a4-4780-8780-03a91f6729da
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ursdevice.h
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

# EVT_URS_SET_ROLE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_URS_SET_ROLE EvtUrsSetRole; 

// Definition

NTSTATUS EvtUrsSetRole 
(
	WDFDEVICE Device
	URS_ROLE Role
)
{...}

EVT_URS_SET_ROLE PFN_URS_SET_ROLE


```

## -parameters

### -param Device: 
### -param Role: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
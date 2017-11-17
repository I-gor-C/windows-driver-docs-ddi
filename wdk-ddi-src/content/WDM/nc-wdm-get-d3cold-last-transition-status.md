---
UID: NC.wdm.GET_D3COLD_LAST_TRANSITION_STATUS
title: GET_D3COLD_LAST_TRANSITION_STATUS
author: windows-driver-content
description: 
ms.assetid: 90c6b6fa-fb56-41ed-ba8b-f4b5aaa7c953
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# GET_D3COLD_LAST_TRANSITION_STATUS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

GET_D3COLD_LAST_TRANSITION_STATUS GetD3coldLastTransitionStatus; 

// Definition

VOID GetD3coldLastTransitionStatus 
(
	PVOID Context
	PD3COLD_LAST_TRANSITION_STATUS LastTransitionStatus
)
{...}

GET_D3COLD_LAST_TRANSITION_STATUS PGET_D3COLD_LAST_TRANSITION_STATUS


```

## -parameters

### -param Context: 
### -param LastTransitionStatus: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
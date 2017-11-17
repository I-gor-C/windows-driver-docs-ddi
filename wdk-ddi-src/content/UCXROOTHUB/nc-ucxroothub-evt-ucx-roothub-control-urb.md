---
UID: NC.ucxroothub.EVT_UCX_ROOTHUB_CONTROL_URB
title: EVT_UCX_ROOTHUB_CONTROL_URB
author: windows-driver-content
description: 
ms.assetid: 097aca88-0399-42b3-98cc-c23d86362839
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxroothub.h
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

# EVT_UCX_ROOTHUB_CONTROL_URB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UCX_ROOTHUB_CONTROL_URB EvtUcxRoothubControlUrb; 

// Definition

VOID EvtUcxRoothubControlUrb 
(
	UCXROOTHUB UcxRootHub
	WDFREQUEST Request
)
{...}

EVT_UCX_ROOTHUB_CONTROL_URB PFN_UCX_ROOTHUB_CONTROL_URB


```

## -parameters

### -param UcxRootHub: 
### -param Request: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
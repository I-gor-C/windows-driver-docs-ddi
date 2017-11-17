---
UID: NC.ucxroothub.EVT_UCX_ROOTHUB_GET_30PORT_INFO
title: EVT_UCX_ROOTHUB_GET_30PORT_INFO
author: windows-driver-content
description: 
ms.assetid: 6932315b-7ad1-4e77-9ddc-57a60e541791
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

# EVT_UCX_ROOTHUB_GET_30PORT_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_UCX_ROOTHUB_GET_30PORT_INFO EvtUcxRoothubGet30PortInfo; 

// Definition

VOID EvtUcxRoothubGet30PortInfo 
(
	UCXROOTHUB UcxRootHub
	WDFREQUEST Request
)
{...}

EVT_UCX_ROOTHUB_GET_30PORT_INFO PFN_UCX_ROOTHUB_GET_30PORT_INFO


```

## -parameters

### -param UcxRootHub: 
### -param Request: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.strmini.PHW_RECEIVE_STREAM_DATA_SRB
title: PHW_RECEIVE_STREAM_DATA_SRB
author: windows-driver-content
description: 
ms.assetid: 7f5eea0d-06e9-4681-9dda-e8efab301f0d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: strmini.h
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

# PHW_RECEIVE_STREAM_DATA_SRB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHW_RECEIVE_STREAM_DATA_SRB PhwReceiveStreamDataSrb; 

// Definition

VOID PhwReceiveStreamDataSrb 
(
	IN _HW_STREAM_REQUEST_BLOCK *SRB
)
{...}

PHW_RECEIVE_STREAM_DATA_SRB 


```

## -parameters

### -param *SRB: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
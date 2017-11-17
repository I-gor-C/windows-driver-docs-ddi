---
UID: NC.d3dkmthk.PFND3DKMT_TRIMNOTIFICATIONCALLBACK
title: PFND3DKMT_TRIMNOTIFICATIONCALLBACK
author: windows-driver-content
description: 
ms.assetid: 47a015d3-20e3-410d-a2a1-bbb20a6fde99
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dkmthk.h
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

# PFND3DKMT_TRIMNOTIFICATIONCALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_TRIMNOTIFICATIONCALLBACK Pfnd3dkmtTrimnotificationcallback; 

// Definition

VOID Pfnd3dkmtTrimnotificationcallback 
(
	D3DKMT_TRIMNOTIFICATION *
)
{...}

PFND3DKMT_TRIMNOTIFICATIONCALLBACK 


```

## -parameters

### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
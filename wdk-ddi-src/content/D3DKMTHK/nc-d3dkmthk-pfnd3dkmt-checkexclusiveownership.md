---
UID: NC.d3dkmthk.PFND3DKMT_CHECKEXCLUSIVEOWNERSHIP
title: PFND3DKMT_CHECKEXCLUSIVEOWNERSHIP
author: windows-driver-content
description: 
ms.assetid: 399e95de-bbc9-4d9b-823a-0677cc2042af
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

# PFND3DKMT_CHECKEXCLUSIVEOWNERSHIP callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_CHECKEXCLUSIVEOWNERSHIP Pfnd3dkmtCheckexclusiveownership; 

// Definition

BOOLEAN Pfnd3dkmtCheckexclusiveownership 
(
	 
)
{...}

PFND3DKMT_CHECKEXCLUSIVEOWNERSHIP 


```

## -parameters

### -param : 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
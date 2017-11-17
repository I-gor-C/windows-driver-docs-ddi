---
UID: NC.61883.PCIP_VALIDATE_ROUTINE
title: PCIP_VALIDATE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: a9683e5e-4c33-4a12-add9-7340258819ed
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: 61883.h
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

# PCIP_VALIDATE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCIP_VALIDATE_ROUTINE PcipValidateRoutine; 

// Definition

ULONG PcipValidateRoutine 
(
	PCIP_VALIDATE_INFO ValidateInfo
)
{...}

PCIP_VALIDATE_ROUTINE 


```

## -parameters

### -param ValidateInfo: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
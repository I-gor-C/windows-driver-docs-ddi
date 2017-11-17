---
UID: NC.d3dkmthk.PFND3DKMT_BUDGETCHANGENOTIFICATIONCALLBACK
title: PFND3DKMT_BUDGETCHANGENOTIFICATIONCALLBACK
author: windows-driver-content
description: 
ms.assetid: d2328211-07b1-49a7-8822-34fdf79c952c
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

# PFND3DKMT_BUDGETCHANGENOTIFICATIONCALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFND3DKMT_BUDGETCHANGENOTIFICATIONCALLBACK Pfnd3dkmtBudgetchangenotificationcallback; 

// Definition

VOID Pfnd3dkmtBudgetchangenotificationcallback 
(
	D3DKMT_BUDGETCHANGENOTIFICATION *
)
{...}

PFND3DKMT_BUDGETCHANGENOTIFICATIONCALLBACK 


```

## -parameters

### -param *: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
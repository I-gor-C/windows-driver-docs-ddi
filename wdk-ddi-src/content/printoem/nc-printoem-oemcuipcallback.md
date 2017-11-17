---
UID: NC.printoem.OEMCUIPCALLBACK
title: OEMCUIPCALLBACK
author: windows-driver-content
description: 
ms.assetid: a3b04b02-e6e1-4611-ae6d-5bb56262af28
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: printoem.h
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

# OEMCUIPCALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

OEMCUIPCALLBACK Oemcuipcallback; 

// Definition

LONG Oemcuipcallback 
(
	 PCPSUICBPARAM
	 POEMCUIPPARAM
)
{...}

OEMCUIPCALLBACK 


```

## -parameters

### -param PCPSUICBPARAM: 
### -param POEMCUIPPARAM: 



## -returns

Returns LONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
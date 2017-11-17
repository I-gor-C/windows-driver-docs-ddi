---
UID: NC.ntddk.PHAL_RESET_DISPLAY_PARAMETERS
title: PHAL_RESET_DISPLAY_PARAMETERS
author: windows-driver-content
description: 
ms.assetid: 8072750b-bca5-4cd8-aaaa-b158932ace72
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# PHAL_RESET_DISPLAY_PARAMETERS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PHAL_RESET_DISPLAY_PARAMETERS PhalResetDisplayParameters; 

// Definition

BOOLEAN PhalResetDisplayParameters 
(
	ULONG Columns
	ULONG Rows
)
{...}

PHAL_RESET_DISPLAY_PARAMETERS 


```

## -parameters

### -param Columns: 
### -param Rows: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
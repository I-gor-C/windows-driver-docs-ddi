---
UID: NC.wdm.NMI_CALLBACK
title: NMI_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 3b4c860b-d478-40bb-b120-3023c822454a
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

# NMI_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

NMI_CALLBACK NmiCallback; 

// Definition

_IRQL_requires_same_ BOOLEAN NmiCallback 
(
	PVOID Context
	BOOLEAN Handled
)
{...}

NMI_CALLBACK PNMI_CALLBACK


```

## -parameters

### -param Context: 
### -param Handled: 



## -returns

Returns _IRQL_requires_same_ BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
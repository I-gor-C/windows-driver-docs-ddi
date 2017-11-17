---
UID: NC.dispmprt.DXGKDDI_CONTROL_ETW_LOGGING
title: DXGKDDI_CONTROL_ETW_LOGGING
author: windows-driver-content
description: 
ms.assetid: 1614c415-2138-48cc-b659-d62a4f87dfce
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dispmprt.h
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

# DXGKDDI_CONTROL_ETW_LOGGING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_CONTROL_ETW_LOGGING DxgkddiControlEtwLogging; 

// Definition

VOID DxgkddiControlEtwLogging 
(
	IN_BOOLEAN Enable
	IN_ULONG Flags
	IN_UCHAR Level
)
{...}

DXGKDDI_CONTROL_ETW_LOGGING PDXGKDDI_CONTROL_ETW_LOGGING


```

## -parameters

### -param Enable: 
### -param Flags: 
### -param Level: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
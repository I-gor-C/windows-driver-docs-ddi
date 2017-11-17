---
UID: NC.dispmprt.DXGKDDI_GETVENDORANDDEVICE
title: DXGKDDI_GETVENDORANDDEVICE
author: windows-driver-content
description: 
ms.assetid: 3bab878a-ee34-4654-8304-abce55cb4664
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

# DXGKDDI_GETVENDORANDDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DXGKDDI_GETVENDORANDDEVICE DxgkddiGetvendoranddevice; 

// Definition

VOID DxgkddiGetvendoranddevice 
(
	HANDLE Context
	DXGKARG_GETVENDORANDDEVICE * pArgs
)
{...}

DXGKDDI_GETVENDORANDDEVICE PDXGKDDI_GETVENDORANDDEVICE


```

## -parameters

### -param Context: 
### -param pArgs: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
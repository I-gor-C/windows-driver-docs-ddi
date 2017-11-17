---
UID: NC.mrx.PMRX_NETROOT_CALLBACK
title: PMRX_NETROOT_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 09b0fa4f-cbed-4a62-8c21-5e6685c6d52c
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: mrx.h
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

# PMRX_NETROOT_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PMRX_NETROOT_CALLBACK PmrxNetrootCallback; 

// Definition

VOID PmrxNetrootCallback 
(
	IN OUT PMRX_CREATENETROOT_CONTEXT CreateContext
)
{...}

PMRX_NETROOT_CALLBACK 


```

## -parameters

### -param CreateContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
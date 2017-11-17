---
UID: NC.ntifs.INIT_SECURITY_INTERFACE_W
title: INIT_SECURITY_INTERFACE_W
author: windows-driver-content
description: 
ms.assetid: 9347d367-1a47-48b1-adf1-a7f3dd51ae14
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntifs.h
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

# INIT_SECURITY_INTERFACE_W callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

INIT_SECURITY_INTERFACE_W InitSecurityInterfaceW; 

// Definition

PSecurityFunctionTableW InitSecurityInterfaceW 
(
	void 
)
{...}

INIT_SECURITY_INTERFACE_W 


```

## -parameters

### -param : 



## -returns

Returns PSecurityFunctionTableW that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
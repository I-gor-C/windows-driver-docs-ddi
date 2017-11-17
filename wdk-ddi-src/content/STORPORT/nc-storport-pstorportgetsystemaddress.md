---
UID: NC.storport.PStorPortGetSystemAddress
title: PStorPortGetSystemAddress
author: windows-driver-content
description: 
ms.assetid: 58429109-720f-49d1-95a9-2dbbe216383f
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: storport.h
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

# PStorPortGetSystemAddress callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PStorPortGetSystemAddress Pstorportgetsystemaddress; 

// Definition

PVOID Pstorportgetsystemaddress 
(
	PSCSI_REQUEST_BLOCK Srb
)
{...}

PStorPortGetSystemAddress 


```

## -parameters

### -param Srb: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
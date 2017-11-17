---
UID: NC.hdcpumdddi.PFN_START_AKE
title: PFN_START_AKE
author: windows-driver-content
description: 
ms.assetid: ad97dff8-21ed-4a48-b318-a7ceaa5382b6
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: hdcpumdddi.h
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

# PFN_START_AKE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_START_AKE PfnStartAke; 

// Definition

VOID PfnStartAke 
(
	PVOID pDriverContext
)
{...}

PFN_START_AKE 


```

## -parameters

### -param pDriverContext: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
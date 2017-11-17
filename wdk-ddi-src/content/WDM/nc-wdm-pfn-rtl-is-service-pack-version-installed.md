---
UID: NC.wdm.PFN_RTL_IS_SERVICE_PACK_VERSION_INSTALLED
title: PFN_RTL_IS_SERVICE_PACK_VERSION_INSTALLED
author: windows-driver-content
description: 
ms.assetid: d5f22f82-eb2a-43ff-8e7f-b0f2d7013076
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

# PFN_RTL_IS_SERVICE_PACK_VERSION_INSTALLED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_RTL_IS_SERVICE_PACK_VERSION_INSTALLED PfnRtlIsServicePackVersionInstalled; 

// Definition

BOOLEAN PfnRtlIsServicePackVersionInstalled 
(
	ULONG Version
)
{...}

PFN_RTL_IS_SERVICE_PACK_VERSION_INSTALLED 


```

## -parameters

### -param Version: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
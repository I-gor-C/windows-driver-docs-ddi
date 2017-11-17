---
UID: NC.wdfinstaller.PFN_WDFPREDEVICEREMOVE
title: PFN_WDFPREDEVICEREMOVE
author: windows-driver-content
description: 
ms.assetid: 8cb30355-bc65-4698-b2f8-748471d0adff
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfinstaller.h
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

# PFN_WDFPREDEVICEREMOVE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPREDEVICEREMOVE PfnWdfpredeviceremove; 

// Definition

ULONG PfnWdfpredeviceremove 
(
	LPCWSTR InfPath
	LPCWSTR InfSectionName
)
{...}

PFN_WDFPREDEVICEREMOVE 


```

## -parameters

### -param InfPath: 
### -param InfSectionName: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
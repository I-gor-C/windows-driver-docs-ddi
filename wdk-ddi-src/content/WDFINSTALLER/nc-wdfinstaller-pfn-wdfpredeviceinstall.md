---
UID: NC.wdfinstaller.PFN_WDFPREDEVICEINSTALL
title: PFN_WDFPREDEVICEINSTALL
author: windows-driver-content
description: 
ms.assetid: d8050f8c-0165-46f8-8858-5a8a52ef7950
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

# PFN_WDFPREDEVICEINSTALL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPREDEVICEINSTALL PfnWdfpredeviceinstall; 

// Definition

ULONG PfnWdfpredeviceinstall 
(
	LPCWSTR InfPath
	LPCWSTR InfSectionName
)
{...}

PFN_WDFPREDEVICEINSTALL 


```

## -parameters

### -param InfPath: 
### -param InfSectionName: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
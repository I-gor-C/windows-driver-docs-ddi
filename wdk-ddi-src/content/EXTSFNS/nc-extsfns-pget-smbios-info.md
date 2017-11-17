---
UID: NC.extsfns.PGET_SMBIOS_INFO
title: PGET_SMBIOS_INFO
author: windows-driver-content
description: 
ms.assetid: 1ff0c9a7-0db8-4ca2-8930-67fb42c96576
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# PGET_SMBIOS_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_SMBIOS_INFO PgetSmbiosInfo; 

// Definition

HRESULT PgetSmbiosInfo 
(
	IN PDEBUG_CLIENT Client
	OUT PDEBUG_SMBIOS_INFO pSmbiosInfo
)
{...}

PGET_SMBIOS_INFO 


```

## -parameters

### -param Client: 
### -param pSmbiosInfo: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
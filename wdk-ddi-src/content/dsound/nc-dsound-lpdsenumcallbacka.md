---
UID: NC.dsound.LPDSENUMCALLBACKA
title: LPDSENUMCALLBACKA
author: windows-driver-content
description: 
ms.assetid: 7f27759f-0ab7-459c-8ff1-e91dda24a1fc
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dsound.h
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

# LPDSENUMCALLBACKA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPDSENUMCALLBACKA Lpdsenumcallbacka; 

// Definition

BOOL Lpdsenumcallbacka 
(
	 LPGUID
	 LPCSTR
	 LPCSTR
	 LPVOID
)
{...}

LPDSENUMCALLBACKA 


```

## -parameters

### -param LPGUID: 
### -param LPCSTR: 
### -param LPCSTR: 
### -param LPVOID: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
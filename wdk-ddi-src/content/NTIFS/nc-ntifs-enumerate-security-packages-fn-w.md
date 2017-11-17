---
UID: NC.ntifs.ENUMERATE_SECURITY_PACKAGES_FN_W
title: ENUMERATE_SECURITY_PACKAGES_FN_W
author: windows-driver-content
description: 
ms.assetid: f494aab6-50bd-4352-82db-7fbc345bdf26
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

# ENUMERATE_SECURITY_PACKAGES_FN_W callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ENUMERATE_SECURITY_PACKAGES_FN_W EnumerateSecurityPackagesFnW; 

// Definition

SECURITY_STATUS EnumerateSecurityPackagesFnW 
(
	unsigned long *
	PSecPkgInfoW *
)
{...}

ENUMERATE_SECURITY_PACKAGES_FN_W 


```

## -parameters

### -param *: 
### -param *: 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.ntifs.REVERT_SECURITY_CONTEXT_FN
title: REVERT_SECURITY_CONTEXT_FN
author: windows-driver-content
description: 
ms.assetid: 731fc062-91a6-4c1c-9cd1-0b85e07e2109
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

# REVERT_SECURITY_CONTEXT_FN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

REVERT_SECURITY_CONTEXT_FN RevertSecurityContextFn; 

// Definition

SECURITY_STATUS RevertSecurityContextFn 
(
	PCtxtHandle 
)
{...}

REVERT_SECURITY_CONTEXT_FN 


```

## -parameters

### -param : 



## -returns

Returns SECURITY_STATUS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
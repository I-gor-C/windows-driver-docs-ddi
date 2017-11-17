---
UID: NC.bthsdpddi.PCREATENODEALTERNATIVE
title: PCREATENODEALTERNATIVE
author: windows-driver-content
description: 
ms.assetid: 966e21f9-a969-47d0-b4b9-cfbb61aa92a1
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: bthsdpddi.h
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

# PCREATENODEALTERNATIVE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODEALTERNATIVE Pcreatenodealternative; 

// Definition

PSDP_NODE Pcreatenodealternative 
(
	ULONG tag
)
{...}

PCREATENODEALTERNATIVE 


```

## -parameters

### -param tag: 



## -returns

Returns PSDP_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
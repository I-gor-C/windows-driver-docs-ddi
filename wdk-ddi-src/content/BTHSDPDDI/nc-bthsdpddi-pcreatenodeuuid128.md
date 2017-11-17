---
UID: NC.bthsdpddi.PCREATENODEUUID128
title: PCREATENODEUUID128
author: windows-driver-content
description: 
ms.assetid: 1f8751dc-0604-47cd-b113-37c21fc9a9f7
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

# PCREATENODEUUID128 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCREATENODEUUID128 Pcreatenodeuuid128; 

// Definition

PSDP_NODE Pcreatenodeuuid128 
(
	const GUID *pUuidVal
	ULONG tag
)
{...}

PCREATENODEUUID128 


```

## -parameters

### -param *pUuidVal: 
### -param tag: 



## -returns

Returns PSDP_NODE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
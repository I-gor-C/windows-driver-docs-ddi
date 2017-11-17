---
UID: NC.compstui.PFNPROPSHEETUI
title: PFNPROPSHEETUI
author: windows-driver-content
description: 
ms.assetid: 0c222b63-88e5-4e33-9d6b-f9c702c8715e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: compstui.h
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

# PFNPROPSHEETUI callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNPROPSHEETUI Pfnpropsheetui; 

// Definition

LONG Pfnpropsheetui 
(
	PPROPSHEETUI_INFO pPSUIInfo
	LPARAM lParam
)
{...}

PFNPROPSHEETUI 


```

## -parameters

### -param pPSUIInfo: 
### -param lParam: 



## -returns

Returns LONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
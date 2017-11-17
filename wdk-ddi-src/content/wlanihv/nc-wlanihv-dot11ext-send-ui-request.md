---
UID: NC.wlanihv.DOT11EXT_SEND_UI_REQUEST
title: DOT11EXT_SEND_UI_REQUEST
author: windows-driver-content
description: 
ms.assetid: e1aee64d-f9eb-4b4f-9b5f-648cd3b81727
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wlanihv.h
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

# DOT11EXT_SEND_UI_REQUEST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

DOT11EXT_SEND_UI_REQUEST Dot11extSendUiRequest; 

// Definition

DWORD Dot11extSendUiRequest 
(
	HANDLE hDot11SvcHandle
	PDOT11EXT_IHV_UI_REQUEST pIhvUIRequest
)
{...}

DOT11EXT_SEND_UI_REQUEST 


```

## -parameters

### -param hDot11SvcHandle: 
### -param pIhvUIRequest: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
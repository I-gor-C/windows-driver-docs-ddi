---
UID: NC.extsfns.EXT_XML_DATA
title: EXT_XML_DATA
author: windows-driver-content
description: 
ms.assetid: 495b534b-9bf6-49e5-b58e-26bc58c451d2
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

# EXT_XML_DATA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXT_XML_DATA ExtXmlData; 

// Definition

HRESULT ExtXmlData 
(
	PDEBUG_CLIENT4 Client
	PEXT_CAB_XML_DATA pXmpData
)
{...}

EXT_XML_DATA 


```

## -parameters

### -param Client: 
### -param pXmpData: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
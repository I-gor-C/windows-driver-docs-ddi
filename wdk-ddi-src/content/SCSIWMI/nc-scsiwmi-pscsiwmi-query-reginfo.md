---
UID: NC.scsiwmi.PSCSIWMI_QUERY_REGINFO
title: PSCSIWMI_QUERY_REGINFO
author: windows-driver-content
description: 
ms.assetid: ad123069-bb9c-4e9a-a5ef-c69dd25544b4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: scsiwmi.h
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

# PSCSIWMI_QUERY_REGINFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSCSIWMI_QUERY_REGINFO PscsiwmiQueryReginfo; 

// Definition

UCHAR PscsiwmiQueryReginfo 
(
	PVOID DeviceContext
	PSCSIWMI_REQUEST_CONTEXT RequestContext
	PWSTR *MofResourceName
)
{...}

PSCSIWMI_QUERY_REGINFO 


```

## -parameters

### -param DeviceContext: 
### -param RequestContext: 
### -param *MofResourceName: 



## -returns

Returns UCHAR that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
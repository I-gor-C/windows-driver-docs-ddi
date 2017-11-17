---
UID: NC.ufxclient.UFX_FDO_INIT
title: UFX_FDO_INIT
author: windows-driver-content
description: 
ms.assetid: c30a9e80-08cc-439a-bdf2-4eab8bbbe28a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ufxclient.h
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

# UFX_FDO_INIT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

UFX_FDO_INIT UfxFdoInit; 

// Definition

NTSTATUS UfxFdoInit 
(
	PUFX_GLOBALS 
	WDFDRIVER 
	PWDFDEVICE_INIT 
	PWDF_OBJECT_ATTRIBUTES 
)
{...}

UFX_FDO_INIT PFN_UFX_FDO_INIT


```

## -parameters

### -param : 
### -param : 
### -param : 
### -param : 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
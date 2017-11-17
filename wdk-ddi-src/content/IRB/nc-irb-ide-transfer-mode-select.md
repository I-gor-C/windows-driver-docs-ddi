---
UID: NC.irb.IDE_TRANSFER_MODE_SELECT
title: IDE_TRANSFER_MODE_SELECT
author: windows-driver-content
description: 
ms.assetid: 19969b7d-f665-4e68-bd06-fe7bc0e92fb8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: irb.h
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

# IDE_TRANSFER_MODE_SELECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

IDE_TRANSFER_MODE_SELECT IdeTransferModeSelect; 

// Definition

BOOLEAN IdeTransferModeSelect 
(
	PVOID ControllerExtension
	PIDE_TRANSFER_MODE_PARAMETERS TransferModeSelect
)
{...}

IDE_TRANSFER_MODE_SELECT 


```

## -parameters

### -param ControllerExtension: 
### -param TransferModeSelect: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
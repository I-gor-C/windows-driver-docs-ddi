---
UID: NC.wdm.PPCI_EXPRESS_ROOT_PORT_WRITE_CONFIG_SPACE
title: PPCI_EXPRESS_ROOT_PORT_WRITE_CONFIG_SPACE
author: windows-driver-content
description: 
ms.assetid: 185097f5-6aed-42de-9ff6-17b90877611b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
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

# PPCI_EXPRESS_ROOT_PORT_WRITE_CONFIG_SPACE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PPCI_EXPRESS_ROOT_PORT_WRITE_CONFIG_SPACE PpciExpressRootPortWriteConfigSpace; 

// Definition

ULONG PpciExpressRootPortWriteConfigSpace 
(
	PVOID Context
	PVOID Buffer
	ULONG Offset
	ULONG Length
)
{...}

PPCI_EXPRESS_ROOT_PORT_WRITE_CONFIG_SPACE 


```

## -parameters

### -param Context: 
### -param Buffer: 
### -param Offset: 
### -param Length: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
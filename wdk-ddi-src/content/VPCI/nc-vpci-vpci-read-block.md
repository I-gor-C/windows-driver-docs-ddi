---
UID: NC.vpci.VPCI_READ_BLOCK
title: VPCI_READ_BLOCK
author: windows-driver-content
description: 
ms.assetid: e1dc501c-edda-42ce-aecf-725b49daf72a
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: vpci.h
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

# VPCI_READ_BLOCK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

VPCI_READ_BLOCK VpciReadBlock; 

// Definition

NTSTATUS VpciReadBlock 
(
	PVOID Context
	ULONG BlockId
	PVOID Buffer
	ULONG Length
)
{...}

VPCI_READ_BLOCK PVPCI_READ_BLOCK


```

## -parameters

### -param Context: 
### -param BlockId: 
### -param Buffer: 
### -param Length: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.wdm.ENABLE_VIRTUALIZATION
title: ENABLE_VIRTUALIZATION
author: windows-driver-content
description: 
ms.assetid: 3d0d13c1-1be8-46f8-ad8c-dbb6cd0a1074
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

# ENABLE_VIRTUALIZATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

ENABLE_VIRTUALIZATION EnableVirtualization; 

// Definition

NTSTATUS EnableVirtualization 
(
	PVOID Context
	UINT16 NumVFs
	BOOLEAN EnableVfMigration
	BOOLEAN EnableMigrationInterrupt
	BOOLEAN EnableVirtualization
)
{...}

ENABLE_VIRTUALIZATION PENABLE_VIRTUALIZATION


```

## -parameters

### -param Context: 
### -param NumVFs: 
### -param EnableVfMigration: 
### -param EnableMigrationInterrupt: 
### -param EnableVirtualization: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
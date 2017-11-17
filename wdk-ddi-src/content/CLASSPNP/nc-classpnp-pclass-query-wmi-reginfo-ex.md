---
UID: NC.classpnp.PCLASS_QUERY_WMI_REGINFO_EX
title: PCLASS_QUERY_WMI_REGINFO_EX
author: windows-driver-content
description: 
ms.assetid: 5ada0854-9b22-4051-9d6d-d23269556e4e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: classpnp.h
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

# PCLASS_QUERY_WMI_REGINFO_EX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_QUERY_WMI_REGINFO_EX PclassQueryWmiReginfoEx; 

// Definition

NTSTATUS PclassQueryWmiReginfoEx 
(
	PDEVICE_OBJECT DeviceObject
	ULONG *RegFlags
	PUNICODE_STRING Name
	PUNICODE_STRING MofResouceName
)
{...}

PCLASS_QUERY_WMI_REGINFO_EX 


```

## -parameters

### -param DeviceObject: 
### -param *RegFlags: 
### -param Name: 
### -param MofResouceName: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
---
UID: NC.classpnp.PCLASS_QUERY_WMI_REGINFO
title: PCLASS_QUERY_WMI_REGINFO
author: windows-driver-content
description: 
ms.assetid: 6438e09d-ceac-4cbb-bbee-ca0e4c32c35f
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

# PCLASS_QUERY_WMI_REGINFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PCLASS_QUERY_WMI_REGINFO PclassQueryWmiReginfo; 

// Definition

NTSTATUS PclassQueryWmiReginfo 
(
	PDEVICE_OBJECT DeviceObject
	ULONG *RegFlags
	PUNICODE_STRING Name
)
{...}

PCLASS_QUERY_WMI_REGINFO 


```

## -parameters

### -param DeviceObject: 
### -param *RegFlags: 
### -param Name: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also
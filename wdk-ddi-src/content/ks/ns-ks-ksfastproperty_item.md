---
UID: NS:ks.KSFASTPROPERTY_ITEM
title: KSFASTPROPERTY_ITEM
author: windows-driver-content
description: The KSFASTPROPERTY_ITEM structure is used with items for fast I/O dispatching.
old-location: stream\ksfastproperty_item.htm
old-project: stream
ms.assetid: 8a39b7cb-cd05-4fb8-9e50-7425e689a36f
ms.author: windowsdriverdev
ms.date: 2/23/2018
ms.keywords: "*PKSFASTPROPERTY_ITEM, KSFASTPROPERTY_ITEM, KSFASTPROPERTY_ITEM structure [Streaming Media Devices], PKSFASTPROPERTY_ITEM, PKSFASTPROPERTY_ITEM structure pointer [Streaming Media Devices], ks-struct_dddb648f-ea8a-436a-b948-397364fe2db6.xml, ks/KSFASTPROPERTY_ITEM, ks/PKSFASTPROPERTY_ITEM, stream.ksfastproperty_item"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ks.h
api_name:
-	KSFASTPROPERTY_ITEM
product: Windows
targetos: Windows
req.typenames: KSFASTPROPERTY_ITEM, *PKSFASTPROPERTY_ITEM
---

# KSFASTPROPERTY_ITEM structure
The KSFASTPROPERTY_ITEM structure is used with items for fast I/O dispatching.

## Syntax
```
typedef struct KSFASTPROPERTY_ITEM {
  ULONG PropertyId;
  union {
    PFNKSFASTHANDLER GetPropertyHandler;
    BOOLEAN          GetSupported;
  };
  union {
    PFNKSFASTHANDLER SetPropertyHandler;
    BOOLEAN          SetSupported;
  };
  ULONG Reserved;
}  *PKSFASTPROPERTY_ITEM;
```

## Members


`PropertyId`

Specifies the identifier of the specific property within the set.

`Reserved`

Reserved and set to zero.


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ks.h (include Ks.h) |

## See Also

<a href="https://msdn.microsoft.com/library/windows/hardware/ff567173">KStrFastHandler</a>
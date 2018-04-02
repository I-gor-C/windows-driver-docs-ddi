---
UID: NS:ntddrilapitypes.RILRADIOSTATEITEM
title: RILRADIOSTATEITEM
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilradiostateitem.htm
old-project: netvista
ms.assetid: 152e3b52-44e4-4ed7-bfc3-38d0c65725fd
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*LPRILRADIOSTATEITEM, RILRADIOSTATEITEM, RILRADIOSTATEITEM structure [Network Drivers Starting with Windows Vista], netvista.rilradiostateitem, ntddrilapitypes/RILRADIOSTATEITEM"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddrilapitypes.h
req.include-header: Rilapitypes.h
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
-	ntddrilapitypes.h
api_name:
-	RILRADIOSTATEITEM
product: Windows
targetos: Windows
req.typenames: RILRADIOSTATEITEM, *LPRILRADIOSTATEITEM
---

# RILRADIOSTATEITEM structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef struct RILRADIOSTATEITEM {
  DWORD                 dwItemId;
  RILRADIOSTATEITEMFLAG dwItemFlag;
  DWORD                 dwItemAttributes;
  union {
    BYTE         byteArray[64];
    int          intArray[16];
    int          intVal;
    unsigned int uintArray[16];
    unsigned int uintVal;
    WCHAR        wszVal[32];
  } itemValueUnion;
  RILITEMVALUEUNION     RILITEMVALUEUNION;
  WCHAR                 wszFriendlyName[32];
  WCHAR                 wszItemValueOptions[256];
}  *LPRILRADIOSTATEITEM;
```

## Members


`dwItemId`



`dwItemFlag`



`dwItemAttributes`



`itemValueUnion`



`RILITEMVALUEUNION`



`wszFriendlyName`



`wszItemValueOptions`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | ntddrilapitypes.h (include Rilapitypes.h) |
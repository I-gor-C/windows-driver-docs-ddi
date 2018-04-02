---
UID: NS:rilapitypes.RILDISPLAYINFO
title: RILDISPLAYINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rildisplayinfo.htm
old-project: netvista
ms.assetid: 6c28e50c-a76a-4a7c-af29-6e58bcfe3f3b
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*LPRILDISPLAYINFO, RILDISPLAYINFO, RILDISPLAYINFO structure [Network Drivers Starting with Windows Vista], netvista.rildisplayinfo, ntddrilapitypes/RILDISPLAYINFO"
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: rilapitypes.h
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
-	RILDISPLAYINFO
product: Windows
targetos: Windows
req.typenames: RILDISPLAYINFO, *LPRILDISPLAYINFO
req.product: Windows 10 or later.
---

# RILDISPLAYINFO structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef struct RILDISPLAYINFO {
  DWORD              cbSize;
  DWORD              dwParams;
  DWORD              dwExecutor;
  RILDISPLAYINFOTYPE dwType;
  RILDISPLAYINFOTAG  dwTag;
  DWORD              dwMessageSize;
  BYTE               pbMessage[1];
} *LPRILDISPLAYINFO, RILDISPLAYINFO;
```

## Members


`cbSize`



`dwParams`



`dwExecutor`



`dwType`



`dwTag`



`dwMessageSize`



`pbMessage`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |
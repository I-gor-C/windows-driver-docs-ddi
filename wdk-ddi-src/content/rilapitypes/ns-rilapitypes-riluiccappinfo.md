---
UID: NS:rilapitypes.RILUICCAPPINFO
title: RILUICCAPPINFO
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\riluiccappinfo.htm
old-project: netvista
ms.assetid: b3a688fe-928c-458e-ac47-59a9ae61bc5e
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: "*LPRILUICCAPPINFO, RILUICCAPPINFO, RILUICCAPPINFO structure [Network Drivers Starting with Windows Vista], netvista.riluiccappinfo, ntddrilapitypes/RILUICCAPPINFO"
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
-	RILUICCAPPINFO
product: Windows
targetos: Windows
req.typenames: RILUICCAPPINFO, *LPRILUICCAPPINFO
req.product: Windows 10 or later.
---

# RILUICCAPPINFO structure
This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.

## Syntax
```
typedef struct RILUICCAPPINFO {
  DWORD          cbSize;
  DWORD          dwParams;
  HUICCAPP       hUiccApp;
  RILUICCAPPTYPE dwUiccAppType;
  DWORD          dwAppIdLength;
  BYTE           bAppId[32];
  DWORD          dwAppNameLength;
  char           cszAppName[256];
  DWORD          dwNumPins;
  BYTE           bPinRef[8];
}  *LPRILUICCAPPINFO;
```

## Members


`cbSize`



`dwParams`



`hUiccApp`



`dwUiccAppType`



`dwAppIdLength`



`bAppId`



`dwAppNameLength`



`cszAppName`



`dwNumPins`



`bPinRef`




## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Header** | rilapitypes.h (include Rilapitypes.h) |
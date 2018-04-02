---
UID: NF:wiamdef.wiasGetItemType
title: wiasGetItemType function
author: windows-driver-content
description: The wiasGetItemType function indicates the item type.
old-location: image\wiasgetitemtype.htm
old-project: image
ms.assetid: 9659d669-ccf3-423a-9c81-12232a978d07
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: image.wiasgetitemtype, wiamdef/wiasGetItemType, wiasFncs_634f945c-e60b-4668-b1a7-19b398a86e7c.xml, wiasGetItemType, wiasGetItemType function [Imaging Devices]
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiamdef.h
req.include-header: Wiamdef.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.
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
req.lib: Wiaservc.lib
req.dll: Wiaservc.dll
req.irql: 
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	DllExport
api_location:
-	Wiaservc.dll
api_name:
-	wiasGetItemType
product:
- Windows
targetos: Windows
req.typenames: DEVICEDIALOGDATA2, *LPDEVICEDIALOGDATA2, *PDEVICEDIALOGDATA2
req.product: Windows 10 or later.
---


# wiasGetItemType function
The <b>wiasGetItemType </b>function indicates the item type.

## Syntax

```
HRESULT wiasGetItemType(
  BYTE *pWiasContext,
  LONG *plType
);
```

## Parameters

`pWiasContext`

Pointer to a WIA item context.

`plType`

TBD


## Return Value

On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Windows SDK documentation).


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | wiamdef.h (include Wiamdef.h) |
| **Library** | Wiaservc.lib |
| **DLL** | Wiaservc.dll |
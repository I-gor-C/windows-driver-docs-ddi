---
UID: NF:wiamdef.wiasReadPropGuid
title: wiasReadPropGuid function
author: windows-driver-content
description: The wiasReadPropGuid function retrieves a GUID property value from a WIA item.
old-location: image\wiasreadpropguid.htm
old-project: image
ms.assetid: 287bf42b-253a-4d1a-8879-c3ab89b6743a
ms.author: windowsdriverdev
ms.date: 2/27/2018
ms.keywords: image.wiasreadpropguid, wiamdef/wiasReadPropGuid, wiasFncs_80e78a38-5f47-4bd3-b071-62eebc65fd6f.xml, wiasReadPropGuid, wiasReadPropGuid function [Imaging Devices]
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
-	wiasReadPropGuid
product: Windows
targetos: Windows
req.typenames: DEVICEDIALOGDATA2, *LPDEVICEDIALOGDATA2, *PDEVICEDIALOGDATA2
req.product: Windows 10 or later.
---


# wiasReadPropGuid function
The <b>wiasReadPropGuid </b>function retrieves a GUID property value from a WIA item.

## Syntax

````
HRESULT _stdcall wiasReadPropGuid(
  _In_      BYTE   *pWiasContext,
            PROPID propid,
  _Out_     GUID   *pgVal,
  _Out_opt_ GUID   *pgValOld,
            BOOL   bMustExist
);
````

## Parameters

`pWiasContext`

Pointer to a WIA item context.

`propid`

Specifies the property identifier.

`pguidVal`

TBD

`pguidValOld`

TBD

`bMustExist`

Indicates whether the property must exist. If set to <b>TRUE</b>, the property must exist; if set to <b>FALSE</b>, the property does not have to exist.


## Return Value

On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Microsoft Windows SDK documentation).


## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.  |
| **Target Platform** | Desktop |
| **Header** | wiamdef.h (include Wiamdef.h) |
| **Library** | Wiaservc.lib |
| **DLL** | Wiaservc.dll |

## See Also

<a href="..\wiamdef\nf-wiamdef-wiaswritepropguid.md">wiasWritePropGuid</a>



<a href="..\wiamdef\nf-wiamdef-wiasreadpropfloat.md">wiasReadPropFloat</a>



<a href="..\wiamdef\nf-wiamdef-wiasreadpropstr.md">wiasReadPropStr</a>



<a href="..\wiamdef\nf-wiamdef-wiasreadpropbin.md">wiasReadPropBin</a>



<a href="..\wiamdef\nf-wiamdef-wiasreadproplong.md">wiasReadPropLong</a>
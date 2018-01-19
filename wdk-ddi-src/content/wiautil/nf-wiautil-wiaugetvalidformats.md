---
UID : NF:wiautil.wiauGetValidFormats
title : wiauGetValidFormats function
author : windows-driver-content
description : The wiauGetValidFormats function calls the IWiaMiniDrv::drvGetWiaFormatInfo method and makes a list of valid formats, using a specified tymed value.
old-location : image\wiaugetvalidformats.htm
old-project : image
ms.assetid : 8bf1d76a-2e5b-4e9a-85fc-187fea72d38c
ms.author : windowsdriverdev
ms.date : 1/17/2018
ms.keywords : wiauGetValidFormats
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : wiautil.h
req.include-header : Wiautil.h
req.target-type : Desktop
req.target-min-winverclnt : Available in Windows XP and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : wiauGetValidFormats
req.alt-loc : wiautil.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : SKIP_AMOUNT
req.product : Windows 10 or later.
---


# wiauGetValidFormats function
The <b>wiauGetValidFormats</b> function calls the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543986">IWiaMiniDrv::drvGetWiaFormatInfo</a> method and makes a list of valid formats, using a specified tymed value.

## Syntax

````
HRESULT _stdcall wiauGetValidFormats(
  _In_  IWiaMiniDrv *pDrv,
  _In_  BYTE        *pWiasContext,
        LONG        TymedValue,
  _Out_ int         *pNumFormats,
  _Out_ GUID        **ppFormatArray
);
````

## Parameters

`pDrv`

Points to the WIA minidriver object. This parameter should be set to <b>this</b>.

`pWiasContext`

Pointer to a WIA item context.

`TymedValue`

Specifies the tymed value to search for.

`pNumFormats`

Pointer to a memory location that receives the number of formats.

`ppFormatArray`

Pointer to a memory location that receives the address of the array of format GUIDs.


## Return Value

On success, the function returns S_OK. If the function fails, it returns a standard COM error.

## Remarks

The caller of this function is responsible for freeing the format array, using the <b>delete[]</b> operator.</p>

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Desktop |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | wiautil.h (include Wiautil.h) |
| **Library** |  |
| **IRQL** |  |
| **DDI compliance rules** |  |
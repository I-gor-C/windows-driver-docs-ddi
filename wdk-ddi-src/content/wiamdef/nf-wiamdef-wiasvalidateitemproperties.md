---
UID: NF.wiamdef.wiasValidateItemProperties
title: wiasValidateItemProperties
author: windows-driver-content
description: The wiasValidateItemProperties function validates a list of simple item properties against their current valid values.
old-location: image\wiasvalidateitemproperties.htm
ms.assetid: d7858b1b-88cf-4e75-a466-40afdcb01d9b
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: image
req.header: wiamdef.h
req.include-header: Wiamdef.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiasValidateItemProperties
req.alt-loc: Wiaservc.dll
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
ms.keywords: wiasValidateItemProperties
req.iface: 
req.product: Windows 10 or later.
---

# wiasValidateItemProperties function



## -description
<p>The <b>wiasValidateItemProperties </b>function validates a list of simple item properties against their current valid values.</p>


## -syntax

````
HRESULT _stdcall wiasValidateItemProperties(
  _In_       BYTE     *pWiasContext,
             ULONG    nPropSpec,
  _In_ const PROPSPEC *pPropSpec
);
````


## -parameters
<dl>

### -param <i>pWiasContext</i> [in]

<dd>
<p>Pointer to a WIA item context.</p>
</dd>

### -param <i>nPropSpec</i> 

<dd>
<p>Specifies the number of properties to validate.</p>
</dd>

### -param <i>pPropSpec</i> [in]

<dd>
<p>Pointer to the first element of an array of PROPSPEC structures indicating the properties to validate.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Microsoft Windows SDK documentation).</p>

## -remarks
<p>This function validates simple property values of the following types grouped by attribute.</p>

<p>WIA_PROP_FLAG</p>

<p>VT_UI1, VT_UI2, VT_UI4, VT_UI8, VT_I1, VT_I2, VT_I4</p>

<p>WIA_PROP_RANGE</p>

<p>VT_UI1, VT_UI2, VT_UI4, VT_UI8, VT_I1, VT_I2, VT_I4, VT_R4, VT_R8</p>

<p>WIA_PROP_LIST</p>

<p>VT_UI1, VT_UI2, VT_UI4, VT_UI8, VT_I1, VT_I2, VT_I4, VT_R4, VT_R8, VT_BSTR</p>

<p> </p>

<p>The PROPSPEC structure is defined in the Windows SDK documentation.</p>

<p>This function validates simple property values of the following types grouped by attribute.</p>

<p>WIA_PROP_FLAG</p>

<p>VT_UI1, VT_UI2, VT_UI4, VT_UI8, VT_I1, VT_I2, VT_I4</p>

<p>WIA_PROP_RANGE</p>

<p>VT_UI1, VT_UI2, VT_UI4, VT_UI8, VT_I1, VT_I2, VT_I4, VT_R4, VT_R8</p>

<p>WIA_PROP_LIST</p>

<p>VT_UI1, VT_UI2, VT_UI4, VT_UI8, VT_I1, VT_I2, VT_I4, VT_R4, VT_R8, VT_BSTR</p>

<p> </p>

<p>The PROPSPEC structure is defined in the Windows SDK documentation.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows Me and in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiamdef.h (include Wiamdef.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Wiaservc.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Wiaservc.dll</dt>
</dl>
</td>
</tr>
</table>
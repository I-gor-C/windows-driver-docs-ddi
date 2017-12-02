---
UID: NF.wiamdef.wiasGetPropertyAttributes
title: wiasGetPropertyAttributes
author: windows-driver-content
description: The wiasGetPropertyAttributes function retrieves the access flags and valid values for a set of properties.
old-location: image\wiasgetpropertyattributes.htm
old-project: image
ms.assetid: b12ff158-73e7-4fdf-b7b1-2969d161ed93
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: wiasGetPropertyAttributes
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
req.alt-api: wiasGetPropertyAttributes
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
req.iface: 
req.product: Windows 10 or later.
---

# wiasGetPropertyAttributes function



## -description
<p>The <b>wiasGetPropertyAttributes </b>function retrieves the access flags and valid values for a set of properties.</p>


## -syntax

````
HRESULT _stdcall wiasGetPropertyAttributes(
  _In_  BYTE        *pWiasContext,
        LONG        cPropSpec,
  _In_  PROPSPEC    *pPropSpec,
        ULONG       *pulAccessFlags,
  _Out_ PROPVARIANT *pPropVar
);
````


## -parameters
<dl>

### -param pWiasContext [in]

<dd>
<p>Pointer to a WIA item context.</p>
</dd>

### -param cPropSpec 

<dd>
<p>Specifies the number of properties.</p>
</dd>

### -param pPropSpec [in]

<dd>
<p>Pointer to a PROPSPEC structure (defined in the Microsoft Windows SDK documentation) indicating the properties for which to get valid values and access flags.</p>
</dd>

### -param pulAccessFlags 

<dd>
<p>Pointer to an array that contains the access flags for the properties.</p>
</dd>

### -param pPropVar [out]

<dd>
<p>Pointer to an array of PROPVARIANT structures (defined in the Microsoft Windows SDK documentation) that contains the valid values for the properties.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Windows SDK documentation).</p>

## -remarks
<p>This function fills each element of the <i>pPropVar </i>array with a PROPVARIANT structure that specifies the valid values for the corresponding property. Properties with the access rights flag WIA_PROP_NONE have no valid values for that property. The data type for the valid values of these properties is VT_EMPTY.</p>

<p>One or more of the WIA_PROP_Xxx property attributes and access flags can be returned in each element of the <i>pulAccessFlags</i> array. The property attribute constants are described in the Windows SDK documentation.</p>

<p>If the property has a range of valid values, the values can be determined through the <i>pPropVar </i>parameter upon completion of this function. The <i>pPropVar </i>parameter specifies an array of PROPVARIANT structures.</p>

<p>Valid integer and floating-point values in a range are accessed using the following index constants.</p>

<p>WIA_RANGE_MIN  </p>

<p>Minimum value</p>

<p>WIA_RANGE_NOM  </p>

<p>Nominal value</p>

<p>WIA_RANGE_MAX  </p>

<p>Maximum value</p>

<p>WIA_RANGE_STEP</p>

<p>Increment value</p>

<p>Valid list values are accessed using the following index constants.</p>

<p>WIA_LIST_COUNT</p>

<p>Count of valid list values, not counting the nominal value</p>

<p>WIA_LIST_NOM</p>

<p>WIA_LIST_VALUES</p>

<p>Index to first valid value</p>

<p>Valid bitwise flag values are accessed using the following index constants.</p>

<p>WIA_FLAG_NOM   </p>

<p>WIA_FLAG_VALUES</p>

<p>All valid flags are joined together by an OR operator</p>

<p>The PROPSPEC and PROPVARIANT structures are defined in the Microsoft Windows SDK documentation.</p>

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
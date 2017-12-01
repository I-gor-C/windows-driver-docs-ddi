---
UID: NF.wiamdef.wiasSetPropertyAttributes
title: wiasSetPropertyAttributes
author: windows-driver-content
description: The wiasSetPropertyAttributes function sets the access flags and valid values for a set of properties.
old-location: image\wiassetpropertyattributes.htm
old-project: image
ms.assetid: 210e69e7-b3b8-43b5-a0d3-f023c7256438
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: wiasSetPropertyAttributes
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
req.alt-api: wiasSetPropertyAttributes
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

# wiasSetPropertyAttributes function



## -description
<p>The <b>wiasSetPropertyAttributes </b>function sets the access flags and valid values for a set of properties.</p>


## -syntax

````
HRESULT _stdcall wiasSetPropertyAttributes(
  _In_  BYTE        *pWiasContext,
        LONG        cPropSpec,
  _In_  PROPSPEC    *pPropSpec,
  _In_  ULONG       *pulAccessFlags,
  _Out_ PROPVARIANT *pPropVar
);
````


## -parameters
<dl>

### -param <i>pWiasContext</i> [in]

<dd>
<p>Pointer to a WIA item context.</p>
</dd>

### -param <i>cPropSpec</i> 

<dd>
<p>Specifies the number of properties.</p>
</dd>

### -param <i>pPropSpec</i> [in]

<dd>
<p>Pointer to a PROPSPEC structure indicating the properties for which to set valid values and access flags.</p>
</dd>

### -param <i>pulAccessFlags</i> [in]

<dd>
<p>Pointer to an array that contains the access flags to be written.</p>
</dd>

### -param <i>pPropVar</i> [out]

<dd>
<p>Pointer to an array of PROPVARIANT structures that contains the valid values to be written.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Microsoft Windows SDK documentation).</p>

## -remarks
<p>Minidrivers should use the function <a href="..\wiamdef\nf-wiamdef-wiassetitempropattribs.md">wiasSetItemPropAttribs</a> to initialize groups of simple properties.</p>

<p>The minidriver can set the WIA_PROP_CACHEABLE flag on a property that does not change over time. By setting this flag on a property, the minidriver indicates that the WIA service can cache the property value. See the Windows SDK documentation for a list of all property attributes.</p>

<p>The PROPSPEC and PROPVARIANT structures are defined in the Windows SDK documentation.</p>

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

## -see-also
<dl>
<dt>
<a href="..\wiamdef\nf-wiamdef-wiassetitempropattribs.md">wiasSetItemPropAttribs</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiasSetPropertyAttributes function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

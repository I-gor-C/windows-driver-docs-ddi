---
UID: NF.wiamdef.wiasGetContextFromName
title: wiasGetContextFromName
author: windows-driver-content
description: The wiasGetContextFromName function retrieves the item context for an item name.
old-location: image\wiasgetcontextfromname.htm
old-project: image
ms.assetid: d15bf48e-132d-4f89-8f19-64f57deed500
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: wiasGetContextFromName
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
req.alt-api: wiasGetContextFromName
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

# wiasGetContextFromName function



## -description
<p>The <b>wiasGetContextFromName</b> function retrieves the item context for an item name.</p>


## -syntax

````
HRESULT _stdcall wiasGetContextFromName(
  _In_  BYTE *pWiasContext,
        LONG lFlags,
  _In_  BSTR bstrName,
  _Out_ BYTE **ppWiasContext
);
````


## -parameters
<dl>

### -param <i>pWiasContext</i> [in]

<dd>
<p>Pointer to a WIA item context.</p>
</dd>

### -param <i>lFlags</i> 

<dd>
<p>Reserved for system use and should be set to 0.</p>
</dd>

### -param <i>bstrName</i> [in]

<dd>
<p>Specifies the name of the context that is being searched for.</p>
</dd>

### -param <i>ppWiasContext</i> [out]

<dd>
<p>Pointer to a memory location that receives the address of the WIA item context.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Microsoft Windows SDK documentation).</p>

## -remarks
<p>This function searches for item contexts whose WIA_IPA_FULL_ITEM_NAME property matches <i>bstrName</i>. Note that this property is different from WIA_IPA_ITEM_NAME, which does not contain path information.</p>

<p>This function should be used by minidrivers when they need to move from one application item context to another, given the item's name. The names of the application items come from their corresponding driver items, which the minidriver creates and names. </p>

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
<a href="..\wiamdef\nf-wiamdef-wiasgetrootitem.md">wiasGetRootItem</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiasGetContextFromName function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.wiamdef.wiasCreateChildAppItem
title: wiasCreateChildAppItem
author: windows-driver-content
description: The wiasCreateChildAppItem function creates a new application item and inserts it as a child of the specified (parent) item. Note that this item will not have any properties in its property sets until the driver or application actually fills them in.
old-location: image\wiascreatechildappitem.htm
old-project: image
ms.assetid: 1dba59b0-5eac-4507-bd42-517a856aa864
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: wiasCreateChildAppItem
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
req.alt-api: wiasCreateChildAppItem
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

# wiasCreateChildAppItem function



## -description
<p>The <b>wiasCreateChildAppItem</b> function creates a new application item and inserts it as a child of the specified (parent) item. Note that this item will not have any properties in its property sets until the driver or application actually fills them in.</p>


## -syntax

````
HRESULT _stdcall wiasCreateChildAppItem(
  _In_  BYTE *pParentWiasContext,
        LONG lFlags,
  _In_  BSTR bstrItemName,
  _In_  BSTR bstrFullItemName,
  _Out_ BYTE **ppWiasChildContext
);
````


## -parameters
<dl>

### -param <i>pParentWiasContext</i> [in]

<dd>
<p>Pointer to the item context to which the child will be added.</p>
</dd>

### -param <i>lFlags</i> 

<dd>
<p>Is reserved for system use.  </p>
</dd>

### -param <i>bstrItemName</i> [in]

<dd>
<p>Specifies a string that contains the item name without path information.</p>
</dd>

### -param <i>bstrFullItemName</i> [in]

<dd>
<p>Specifies a string that contains the item name including path information.</p>
</dd>

### -param <i>ppWiasChildContext</i> [out]

<dd>
<p>Pointer to a memory location that receives the address of the newly created child item's context.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Microsoft Windows SDK documentation).</p>

## -remarks


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
<a href="..\wiamdef\nf-wiamdef-wiascreatedrvitem.md">wiasCreateDrvItem</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [image\image]:%20wiasCreateChildAppItem function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

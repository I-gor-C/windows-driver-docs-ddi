---
UID: NF.wiamdef.wiasGetChildrenContexts
title: wiasGetChildrenContexts
author: windows-driver-content
description: The wiasGetChildrenContexts function retrieves an array of item contexts belonging to the current item's children.
old-location: image\wiasgetchildrencontexts.htm
old-project: image
ms.assetid: a69216f4-1272-488f-8d06-8dc3b6a88452
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: wiasGetChildrenContexts
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
req.alt-api: wiasGetChildrenContexts
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

# wiasGetChildrenContexts function



## -description
<p>The <b>wiasGetChildrenContexts</b> function retrieves an array of item contexts belonging to the current item's children.</p>


## -syntax

````
HRESULT _stdcall wiasGetChildrenContexts(
  _In_  BYTE  *pParentContext,
  _Out_ ULONG *pulNumChildren,
  _Out_ BYTE  ***pppChildren
);
````


## -parameters
<dl>

### -param pParentContext [in]

<dd>
<p>Pointer to the parent item.</p>
</dd>

### -param pulNumChildren [out]

<dd>
<p>Pointer to a memory location that receives the number of children contexts.</p>
</dd>

### -param pppChildren [out]

<dd>
<p>Pointer to a memory location that points to an array whose elements are addresses of <b>IWiaItem</b> objects (described in the Microsoft Windows SDK documentation). Each <b>IWiaItem</b> object represents one child context.</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error or one of the WIA_ERROR_XXX errors (described in the Windows SDK documentation).</p>

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
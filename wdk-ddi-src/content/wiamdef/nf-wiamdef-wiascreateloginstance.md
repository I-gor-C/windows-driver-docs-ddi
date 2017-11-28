---
UID: NF.wiamdef.wiasCreateLogInstance
title: wiasCreateLogInstance
author: windows-driver-content
description: The wiasCreateLogInstance function creates an instance of a logging object.
old-location: image\wiascreateloginstance.htm
old-project: image
ms.assetid: 7a340187-51c5-4997-b4d0-5b89ea8e16c0
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: wiasCreateLogInstance
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
req.alt-api: wiasCreateLogInstance
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

# wiasCreateLogInstance function



## -description
<p>The <b>wiasCreateLogInstance</b> function creates an instance of a logging object.</p>


## -syntax

````
HRESULT _stdcall wiasCreateLogInstance(
  _In_  BYTE      *pModuleHandle,
  _Out_ IWiaLogEx **ppIWiaLogEx
);
````


## -parameters
<dl>

### -param <i>pModuleHandle</i> [in]

<dd>
<p>Pointer to the module handle, which is used to filter output.</p>
</dd>

### -param <i>ppIWiaLogEx</i> [out]

<dd>
<p>Pointer to a memory location that receives the address of the logging interface.</p>
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
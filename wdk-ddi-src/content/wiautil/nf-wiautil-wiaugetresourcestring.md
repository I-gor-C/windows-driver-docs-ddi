---
UID: NF.wiautil.wiauGetResourceString
title: wiauGetResourceString
author: windows-driver-content
description: The wiauGetResourceString function gets a resource string, storing it as a BSTR.
old-location: image\wiaugetresourcestring.htm
ms.assetid: b042702a-46ff-4ec9-8a92-af8516802e64
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: image
req.header: wiautil.h
req.include-header: Wiautil.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiauGetResourceString
req.alt-loc: wiautil.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
ms.keywords: wiauGetResourceString
req.iface: 
req.product: Windows 10 or later.
---

# wiauGetResourceString function



## -description
<p>The <b>wiauGetResourceString</b> function gets a resource string, storing it as a <b>BSTR</b>.</p>


## -syntax

````
HRESULT _stdcall wiauGetResourceString(
        HINSTANCE hInst,
        LONG      lResourceID,
  _Out_ BSTR      *pbstrStr
);
````


## -parameters
<dl>

### -param <i>hInst</i> 

<dd>
<p>Specifies the handle of the module instance.</p>
</dd>

### -param <i>lResourceID</i> 

<dd>
<p>Specifies the resource ID of the target BSTR value.</p>
</dd>

### -param <i>pbstrStr</i> [out]

<dd>
<p>Points to the memory location that receives the retrieved string. The caller of this function must free this string by calling <b>SysFreeString</b> (described in the Microsoft Windows SDK documentation).</p>
</dd>
</dl>

## -returns
<p>On success, the function returns S_OK. If the function fails, it returns a standard COM error.</p>

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
<p>Available in Windows XP and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wiautil.h (include Wiautil.h)</dt>
</dl>
</td>
</tr>
</table>
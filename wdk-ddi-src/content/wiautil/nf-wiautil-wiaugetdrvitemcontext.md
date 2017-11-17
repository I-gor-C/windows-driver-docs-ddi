---
UID: NF.wiautil.wiauGetDrvItemContext
title: wiauGetDrvItemContext
author: windows-driver-content
description: The wiauGetDrvItemContext function gets the driver item context, and optionally, the driver item.
old-location: image\wiaugetdrvitemcontext.htm
ms.assetid: 6d4b7a25-436f-4547-8969-66dd45fa46fd
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
req.alt-api: wiauGetDrvItemContext
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
ms.keywords: wiauGetDrvItemContext
req.iface: 
req.product: Windows 10 or later.
---

# wiauGetDrvItemContext function



## -description
<p>The <b>wiauGetDrvItemContext</b> function gets the driver item context, and optionally, the driver item.</p>


## -syntax

````
HRESULT _stdcall wiauGetDrvItemContext(
  _In_    BYTE                  *pWiasContext,
  _Inout_ VOID                  **ppItemCtx,
  _Inout_ IWiaDrvItem ppDrvItem **ppDrvItem
);
````


## -parameters
<dl>

### -param <i>pWiasContext</i> [in]

<dd>
<p>Pointer to a WIA item context.</p>
</dd>

### -param <i>ppItemCtx</i> [in, out]

<dd>
<p>Pointer to a memory location that receives a pointer to the driver item context.</p>
</dd>

### -param <i>ppDrvItem</i> [in, out]

<dd>
<p><i>Optional</i>. Pointer to a memory location that receives a pointer to a driver item. The default value of this parameter is <b>NULL</b>, which means that when this function returns, no change is made to this parameter.</p>
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
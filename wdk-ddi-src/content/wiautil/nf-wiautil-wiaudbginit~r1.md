---
UID: NF.wiautil.wiauDbgInit~r1
title: wiauDbgInit
author: windows-driver-content
description: The wiauDbgInit function initializes WIA debugging.
old-location: image\wiaudbginit.htm
old-project: image
ms.assetid: a9308d66-c8b0-4e0e-8203-e2b3f91b7e27
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: wiauDbgInit
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wiautil.h
req.include-header: Wiautil.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: wiauDbgInit
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
req.iface: 
req.product: Windows 10 or later.
---

# wiauDbgInit function



## -description
<p>The <b>wiauDbgInit</b> function initializes WIA debugging.</p>


## -syntax

````
void __stdcall wiauDbgInit(
  _In_opt_ HINSTANCE hInstance
);
````


## -parameters
<dl>

### -param <i>hInstance</i> [in, optional]

<dd>
<p>Is the handle to the DLL instance.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>If the <b>wiauDbgInit</b> function not called, all DLLs loaded by a process inherit the debug flags of that process. </p>

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
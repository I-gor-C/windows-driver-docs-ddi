---
UID: NF.poscx.PosCxIsPosApp
title: PosCxIsPosApp
author: windows-driver-content
description: PosCxIsPosApp checks if the open instance is associated with a point-of-service application.
old-location: pos\poscxisposapp.htm
ms.assetid: 890A0ACB-9717-4BF8-87B5-A6C1FAD661C2
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: pos
req.header: poscx.h
req.include-header: Poscx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PosCxIsPosApp
req.alt-loc: poscx.h
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
ms.keywords: PosCxIsPosApp
req.iface: 
req.product: Windows 10 or later.
---

# PosCxIsPosApp function



## -description
<p>PosCxIsPosApp checks if the open instance is associated with a point-of-service application.</p>


## -syntax

````
BOOLEAN PosCxIsPosApp(
  _In_ WDFDEVICE     device,
  _In_ WDFFILEOBJECT fileObject
);
````


## -parameters
<dl>

### -param <i>device</i> [in]

<dd>
<p>A handle to a framework device object that represents the device.</p>
</dd>

### -param <i>fileObject</i> [in]

<dd>
<p>A handle to a framework file object that identifies the caller, usually acquired with <a href="https://msdn.microsoft.com/library/windows/hardware/ff549963">WdfRequestGetFileObject</a>.</p>
</dd>
</dl>

## -returns
<p>Returns TRUE if <i>fileObject</i> is associated with a point-of-service application. Otherwise, returns FALSE.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Product</p>
</th>
<td width="70%">
<p>Windows 10 or later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Poscx.h (include Poscx.h)</dt>
</dl>
</td>
</tr>
</table>
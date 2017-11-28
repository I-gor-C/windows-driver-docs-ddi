---
UID: NF.poscx.PosCxMarkPosApp
title: PosCxMarkPosApp
author: windows-driver-content
description: PosCxMarkPosApp marks the open instance as associated or not associated with a point-of-service application.
old-location: pos\poscxmarkposapp.htm
old-project: pos
ms.assetid: 6BFFD014-E9DC-495C-9810-0D23BD93C41A
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PosCxMarkPosApp
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: poscx.h
req.include-header: Poscx.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PosCxMarkPosApp
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
req.iface: 
req.product: Windows 10 or later.
---

# PosCxMarkPosApp function



## -description
<p>PosCxMarkPosApp marks the open instance as associated or not associated with a point-of-service application.</p>
<p>This optional method provides value if the driver implements multiple device interfaces. It helps to  identify which interface is currently in use.</p>


## -syntax

````
NTSTATUS PosCxMarkPosApp(
  _In_ WDFDEVICE     device,
  _In_ WDFFILEOBJECT fileObject,
  _In_ BOOLEAN       isPosApp
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

### -param <i>isPosApp</i> [in]

<dd>
<p>Specifies if the open instance is associated with a point-of-service application. Set to TRUE if it is associated with a point-of-service application. Otherwise, set to FALSE.</p>
</dd>
</dl>

## -returns
<p>Possible return values are:</p>

<p> </p>

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
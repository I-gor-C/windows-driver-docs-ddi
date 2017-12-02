---
UID: NF.poscx.PosCxClose
title: PosCxClose
author: windows-driver-content
description: PosCxClose is called to delete an opened PosCx library instance. This function releases the device if the caller is the owner, and cancels pending requests. It should be called from the driver's EVT_WDF_FILE_CLOSE callback.
old-location: pos\poscxclose.htm
old-project: pos
ms.assetid: 90D097B9-EE7B-49FA-B0F7-6A255D140C06
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PosCxClose
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
req.alt-api: PosCxClose
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

# PosCxClose function



## -description
<p>      PosCxClose is called to delete an opened PosCx library instance. This function releases the device if the caller is the owner, 

      and cancels pending requests. It should be called from 

      the driver's <a href="..\wdfdevice\nc-wdfdevice-evt-wdf-file-close.md">EVT_WDF_FILE_CLOSE</a> callback.</p>


## -syntax

````
NTSTATUS PosCxClose(
  _In_ WDFDEVICE     device,
  _In_ WDFFILEOBJECT fileObject
);
````


## -parameters
<dl>

### -param device [in]

<dd>
<p>A handle to a framework device object that represents the device.</p>
</dd>

### -param fileObject [in]

<dd>
<p>      A handle to a framework file object that identifies the caller associated with the open instance.</p>
</dd>
</dl>

## -returns
<p>An appropriate NTSTATUS error code that indicates the close instance completion status.</p>

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
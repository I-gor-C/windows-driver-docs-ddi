---
UID: NF.wdfhwaccess.WDF_READ_REGISTER_UCHAR
title: WDF_READ_REGISTER_UCHAR
author: windows-driver-content
description: The WDF_READ_REGISTER_UCHAR function reads a byte from the specified register address.
old-location: wdf\wdf_read_register_uchar.htm
old-project: wdf
ms.assetid: C8633689-0900-42BB-9D0D-6F95CBA13A37
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WDF_READ_REGISTER_UCHAR
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: wdfhwaccess.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 2.0
req.alt-api: WDF_READ_REGISTER_UCHAR
req.alt-loc: Wdfhwaccess.h
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

# WDF_READ_REGISTER_UCHAR function



## -description
<p class="CCE_Message">[Applies to UMDF only]</p>
<p>The <b>WDF_READ_REGISTER_UCHAR</b> function reads a byte from the specified register address.</p>


## -syntax

````
UCHAR WDF_READ_REGISTER_UCHAR(
  _In_ WDFDEVICE Device,
  _In_ PUCHAR    Register
);
````


## -parameters
<dl>

### -param Device [in]

<dd>
<p>A handle to a framework device object.</p>
</dd>

### -param Register [in]

<dd>
<p>A pointer to the register address, which must be a mapped range in memory space.</p>
</dd>
</dl>

## -returns
<p><b>WDF_READ_REGISTER_UCHAR</b> returns the byte that is read from the specified port address.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum support</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wdfhwaccess.h</dt>
</dl>
</td>
</tr>
</table>
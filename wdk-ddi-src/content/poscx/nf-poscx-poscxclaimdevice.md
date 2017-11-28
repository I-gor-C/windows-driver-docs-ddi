---
UID: NF.poscx.PosCxClaimDevice
title: PosCxClaimDevice
author: windows-driver-content
description: PosCxClaimDevice is called to claim a device for exclusive use. The caller should call PosCxReleaseDevice when the device is no longer needed.
old-location: pos\poscxclaimdevice.htm
old-project: pos
ms.assetid: 16EB583C-FB61-4811-A691-3FBD159F8FD0
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: PosCxClaimDevice
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
req.alt-api: PosCxClaimDevice
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

# PosCxClaimDevice function



## -description
<p>PosCxClaimDevice is called to claim a device for exclusive use. 

The caller should call <a href="https://msdn.microsoft.com/library/windows/hardware/mt593132">PosCxReleaseDevice</a> when the device is no longer needed. 

      </p>
<p>If the device is already claimed, the caller must wait until access is granted.</p>


## -syntax

````
NTSTATUS PosCxClaimDevice(
  _In_ WDFDEVICE  device,
  _In_ WDFREQUEST request
);
````


## -parameters
<dl>

### -param <i>device</i> [in]

<dd>
<p>A handle to a framework device object that represents the device.</p>
</dd>

### -param <i>request</i> [in]

<dd>
<p>A handle to a framework request object that represents the request. This request must come from a WDF IO queue.</p>
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
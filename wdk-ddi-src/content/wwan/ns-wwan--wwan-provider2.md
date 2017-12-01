---
UID: NS.wwan._WWAN_PROVIDER2
title: WWAN_PROVIDER2
author: windows-driver-content
description: The WWAN_PROVIDER2 structure describes the details of a network provider.
old-location: netvista\wwan_provider2.htm
old-project: netvista
ms.assetid: 0B9352EE-C7CE-4F9D-9373-0096222295A4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WWAN_PROVIDER2, WWAN_PROVIDER2, *PWWAN_PROVIDER2
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Versions: Supported in Windows 8 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_PROVIDER2
req.alt-loc: wwan.h
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

# WWAN_PROVIDER2 structure



## -description
<p>The WWAN_PROVIDER2 structure describes the details of a network provider.</p>


## -syntax

````
typedef struct _WWAN_PROVIDER2 {
  WWAN_PROVIDER       Provider;
  WWAN_CELLULAR_CLASS WwanCellularClass;
  ULONG               Rssi;
  ULONG               ErrorRate;
} WWAN_PROVIDER2, *PWWAN_PROVIDER2;
````


## -struct-fields
<dl>

### -field <b>Provider</b>

<dd>
<p>A formatted WWAN_PROVIDER object that represents details about a network provider.</p>
</dd>

### -field <b>WwanCellularClass</b>

<dd>
<p>The cellular class that the provider uses.</p>
</dd>

### -field <b>Rssi</b>

<dd>
<p>A value that represents the strength of the wireless signal. Please refer to <a href="..\wwan\ns-wwan--wwan-signal-state.md">WWAN_SIGNAL_STATE</a> on the format of this member.</p>
</dd>

### -field <b>ErrorRate</b>

<dd>
<p>	A coded value that represents a percentage range of error rates. Please refer to <a href="..\wwan\ns-wwan--wwan-signal-state.md">WWAN_SIGNAL_STATE</a> on the format of this member.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Versions: Supported in Windows 8 and later versions of Windows.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h (include Wwan.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wwan\ns-wwan--wwan-signal-state.md">WWAN_SIGNAL_STATE</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-provider.md">WWAN_PROVIDER</a>
</dt>
<dt>
<a href="..\wwan\ne-wwan--wwan-cellular-class.md">WWAN_CELLULAR_CLASS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_PROVIDER2 structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

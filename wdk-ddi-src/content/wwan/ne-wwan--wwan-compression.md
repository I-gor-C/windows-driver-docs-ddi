---
UID: NE.wwan._WWAN_COMPRESSION
title: WWAN_COMPRESSION
author: windows-driver-content
description: The WWAN_COMPRESSION enumeration lists the different compression options that are supported by the MB device.
old-location: netvista\wwan_compression.htm
old-project: netvista
ms.assetid: a22bcf4e-f460-4f32-9e1e-4ae952fc87d0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_COMPRESSION
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

# WWAN_COMPRESSION enumeration



## -description
<p>The WWAN_COMPRESSION enumeration lists the different compression options that are supported by the MB
  device.</p>


## -syntax

````
typedef enum _WWAN_COMPRESSION { 
  WwanCompressionNone    = 0,
  WwanCompressionEnable,
  WwanCompressionMax
} WWAN_COMPRESSION, *PWWAN_COMPRESSION;
````


## -enum-fields
<dl>

### -field <a id="WwanCompressionNone"></a><a id="wwancompressionnone"></a><a id="WWANCOMPRESSIONNONE"></a><b>WwanCompressionNone</b>

<dd>
<p>No compression is applied.</p>
</dd>

### -field <a id="WwanCompressionEnable"></a><a id="wwancompressionenable"></a><a id="WWANCOMPRESSIONENABLE"></a><b>WwanCompressionEnable</b>

<dd>
<p>Enable header and data compression.</p>
</dd>

### -field <a id="WwanCompressionMax"></a><a id="wwancompressionmax"></a><a id="WWANCOMPRESSIONMAX"></a><b>WwanCompressionMax</b>

<dd>
<p>The total number of supported compression options.</p>
</dd>
</dl>

## -remarks
<p>This enumeration applies only to GSM devices. The MB Service specifies 
    <b>WwanCompressionNone</b> as the compression type for CDMA-based devices.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows 7 and later versions of Windows.</p>
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
<a href="..\wwan\ns-wwan--wwan-set-context-state.md">WWAN_SET_CONTEXT_STATE</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-context.md">WWAN_CONTEXT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_COMPRESSION enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

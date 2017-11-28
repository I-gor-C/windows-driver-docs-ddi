---
UID: NE.wwan._WWAN_PIN_MODE
title: WWAN_PIN_MODE
author: windows-driver-content
description: The WWAN_PIN_MODE enumeration lists the different states of a Personal Identification Number (PIN) type.
old-location: netvista\wwan_pin_mode.htm
old-project: netvista
ms.assetid: 55fa9dd4-370e-4f72-be40-4f14373cee27
ms.author: windowsdriverdev
ms.date: 11/22/2017
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
req.alt-api: WWAN_PIN_MODE
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

# WWAN_PIN_MODE enumeration



## -description
<p>The WWAN_PIN_MODE enumeration lists the different states of a Personal Identification Number (PIN)
  type.</p>


## -syntax

````
typedef enum _WWAN_PIN_MODE { 
  WwanPinModeNotSupported  = 0,
  WwanPinModeEnabled,
  WwanPinModeDisabled,
  WwanPinModeMax
} WWAN_PIN_MODE, *PWWAN_PIN_MODE;
````


## -enum-fields
<dl>

### -field <a id="WwanPinModeNotSupported"></a><a id="wwanpinmodenotsupported"></a><a id="WWANPINMODENOTSUPPORTED"></a><b>WwanPinModeNotSupported</b>

<dd>
<p>The PIN type is not supported.</p>
</dd>

### -field <a id="WwanPinModeEnabled"></a><a id="wwanpinmodeenabled"></a><a id="WWANPINMODEENABLED"></a><b>WwanPinModeEnabled</b>

<dd>
<p>The PIN type is supported and currently enabled.</p>
</dd>

### -field <a id="WwanPinModeDisabled"></a><a id="wwanpinmodedisabled"></a><a id="WWANPINMODEDISABLED"></a><b>WwanPinModeDisabled</b>

<dd>
<p>The PIN type is supported though currently disabled.</p>
</dd>

### -field <a id="WwanPinModeMax"></a><a id="wwanpinmodemax"></a><a id="WWANPINMODEMAX"></a><b>WwanPinModeMax</b>

<dd>
<p>The total number of supported PIN type states.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571214">WWAN_PIN_DESC</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_PIN_MODE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NE.wwan._WWAN_PIN_FORMAT
title: WWAN_PIN_FORMAT
author: windows-driver-content
description: The WWAN_PIN_FORMAT enumeration lists the different Personal Identification Number (PIN) formats that are supported by the MB device.
old-location: netvista\wwan_pin_format.htm
old-project: netvista
ms.assetid: ccc3934c-fed4-4f9d-ae2a-d5e96bdb1e46
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
req.alt-api: WWAN_PIN_FORMAT
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

# WWAN_PIN_FORMAT enumeration



## -description
<p>The WWAN_PIN_FORMAT enumeration lists the different Personal Identification Number (PIN) formats that
  are supported by the MB device.</p>


## -syntax

````
typedef enum _WWAN_PIN_FORMAT { 
  WwanPinFormatUnknown       = 0,
  WwanPinFormatNumeric,
  WwanPinFormatAlphaNumeric,
  WwanPinFormatMax
} WWAN_PIN_FORMAT, *PWWAN_PIN_FORMAT;
````


## -enum-fields
<dl>

### -field <a id="WwanPinFormatUnknown"></a><a id="wwanpinformatunknown"></a><a id="WWANPINFORMATUNKNOWN"></a><b>WwanPinFormatUnknown</b>

<dd>
<p>The format of PIN is not specified.</p>
</dd>

### -field <a id="WwanPinFormatNumeric"></a><a id="wwanpinformatnumeric"></a><a id="WWANPINFORMATNUMERIC"></a><b>WwanPinFormatNumeric</b>

<dd>
<p>The format of the PIN allows only the numerical characters 0 through 9.</p>
</dd>

### -field <a id="WwanPinFormatAlphaNumeric"></a><a id="wwanpinformatalphanumeric"></a><a id="WWANPINFORMATALPHANUMERIC"></a><b>WwanPinFormatAlphaNumeric</b>

<dd>
<p>The format of the PIN allows alphanumeric characters a through z (lowercase), A through Z
     (uppercase), 0 through 9 (numeric), the asterisk symbol (*), and the pound symbol (#).</p>
</dd>

### -field <a id="WwanPinFormatMax"></a><a id="wwanpinformatmax"></a><a id="WWANPINFORMATMAX"></a><b>WwanPinFormatMax</b>

<dd>
<p>The total number of supported PIN formats.</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_PIN_FORMAT enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

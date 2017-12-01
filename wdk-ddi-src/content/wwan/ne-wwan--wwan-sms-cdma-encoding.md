---
UID: NE.wwan._WWAN_SMS_CDMA_ENCODING
title: WWAN_SMS_CDMA_ENCODING
author: windows-driver-content
description: The WWAN_SMS_CDMA_ENCODING enumeration lists the different SMS CDMA encoding formats that are supported by the MB device.
old-location: netvista\wwan_sms_cdma_encoding.htm
old-project: netvista
ms.assetid: 1f632da2-36bb-491e-b445-5c320277a446
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
req.alt-api: WWAN_SMS_CDMA_ENCODING
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

# WWAN_SMS_CDMA_ENCODING enumeration



## -description
<p>The WWAN_SMS_CDMA_ENCODING enumeration lists the different SMS CDMA encoding formats that are
  supported by the MB device.</p>


## -syntax

````
typedef enum _WWAN_SMS_CDMA_ENCODING { 
  WwanSmsCdmaEncodingOctet        = 0,
  WwanSmsCdmaEncodingEpm,
  WwanSmsCdmaEncoding7BitAscii,
  WwanSmsCdmaEncodingIa5,
  WwanSmsCdmaEncodingUnicode,
  WwanSmsCdmaEncodingShiftJis,
  WwanSmsCdmaEncodingKorean,
  WwanSmsCdmaEncodingLatinHebrew,
  WwanSmsCdmaEncodingLatin,
  WwanSmsCdmaEncodingGsm7Bit,
  WwanSmsCdmaEncodingMax
} WWAN_SMS_CDMA_ENCODING, *PWWAN_SMS_CDMA_ENCODING;
````


## -enum-fields
<dl>

### -field <a id="WwanSmsCdmaEncodingOctet"></a><a id="wwansmscdmaencodingoctet"></a><a id="WWANSMSCDMAENCODINGOCTET"></a><b>WwanSmsCdmaEncodingOctet</b>

<dd>
<p>The message uses octet encoding.</p>
</dd>

### -field <a id="WwanSmsCdmaEncodingEpm"></a><a id="wwansmscdmaencodingepm"></a><a id="WWANSMSCDMAENCODINGEPM"></a><b>WwanSmsCdmaEncodingEpm</b>

<dd>
<p>The message uses EPM encoding.</p>
</dd>

### -field <a id="WwanSmsCdmaEncoding7BitAscii"></a><a id="wwansmscdmaencoding7bitascii"></a><a id="WWANSMSCDMAENCODING7BITASCII"></a><b>WwanSmsCdmaEncoding7BitAscii</b>

<dd>
<p>The message uses 7-bit ASCII encoding. The encoded message is represented in bytes per character.</p>
</dd>

### -field <a id="WwanSmsCdmaEncodingIa5"></a><a id="wwansmscdmaencodingia5"></a><a id="WWANSMSCDMAENCODINGIA5"></a><b>WwanSmsCdmaEncodingIa5</b>

<dd>
<p>The message uses IA5 encoding.</p>
</dd>

### -field <a id="WwanSmsCdmaEncodingUnicode"></a><a id="wwansmscdmaencodingunicode"></a><a id="WWANSMSCDMAENCODINGUNICODE"></a><b>WwanSmsCdmaEncodingUnicode</b>

<dd>
<p>The message uses Unicode encoding.</p>
</dd>

### -field <a id="WwanSmsCdmaEncodingShiftJis"></a><a id="wwansmscdmaencodingshiftjis"></a><a id="WWANSMSCDMAENCODINGSHIFTJIS"></a><b>WwanSmsCdmaEncodingShiftJis</b>

<dd>
<p>The message uses shifted JIS encoding.</p>
</dd>

### -field <a id="WwanSmsCdmaEncodingKorean"></a><a id="wwansmscdmaencodingkorean"></a><a id="WWANSMSCDMAENCODINGKOREAN"></a><b>WwanSmsCdmaEncodingKorean</b>

<dd>
<p>The message uses Korean encoding.</p>
</dd>

### -field <a id="WwanSmsCdmaEncodingLatinHebrew"></a><a id="wwansmscdmaencodinglatinhebrew"></a><a id="WWANSMSCDMAENCODINGLATINHEBREW"></a><b>WwanSmsCdmaEncodingLatinHebrew</b>

<dd>
<p>The message uses Latin Hebrew encoding.</p>
</dd>

### -field <a id="WwanSmsCdmaEncodingLatin"></a><a id="wwansmscdmaencodinglatin"></a><a id="WWANSMSCDMAENCODINGLATIN"></a><b>WwanSmsCdmaEncodingLatin</b>

<dd>
<p>The message uses Latin encoding.</p>
</dd>

### -field <a id="WwanSmsCdmaEncodingGsm7Bit"></a><a id="wwansmscdmaencodinggsm7bit"></a><a id="WWANSMSCDMAENCODINGGSM7BIT"></a><b>WwanSmsCdmaEncodingGsm7Bit</b>

<dd>
<p>The message uses 7-bit GSM encoding.</p>
</dd>

### -field <a id="WwanSmsCdmaEncodingMax"></a><a id="wwansmscdmaencodingmax"></a><a id="WWANSMSCDMAENCODINGMAX"></a><b>WwanSmsCdmaEncodingMax</b>

<dd>
<p>The total number of supported SMS CDMA encoding formats.</p>
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
<a href="..\wwan\ns-wwan--wwan-sms-cdma-record.md">WWAN_SMS_CDMA_RECORD</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-sms-send-cdma.md">WWAN_SMS_SEND_CDMA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SMS_CDMA_ENCODING enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

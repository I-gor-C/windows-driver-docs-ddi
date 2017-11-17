---
UID: NE.wwan._WWAN_SMS_FORMAT
title: WWAN_SMS_FORMAT
author: windows-driver-content
description: The WWAN_SMS_FORMAT enumeration lists different Short Message Service (SMS) formats.
old-location: netvista\wwan_sms_format.htm
ms.assetid: fb583ded-8292-4486-8e85-3d3039611d14
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_SMS_FORMAT
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
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
req.iface: 
req.product: Windows 10 or later.
---

# WWAN_SMS_FORMAT enumeration



## -description
<p>The WWAN_SMS_FORMAT enumeration lists different Short Message Service (SMS) formats.</p>


## -syntax

````
typedef enum _WWAN_SMS_FORMAT { 
  WwanSmsFormatPdu        = 0,
  WwanSmsFormatReserved0,
  WwanSmsFormatReserved1,
  WwanSmsFormatReserved2,
  WwanSmsFormatCdma,
  WwanSmsFormatMax
} WWAN_SMS_FORMAT, *PWWAN_SMS_FORMAT;
````


## -enum-fields
<dl>

### -field <a id="WwanSmsFormatPdu"></a><a id="wwansmsformatpdu"></a><a id="WWANSMSFORMATPDU"></a><b>WwanSmsFormatPdu</b>

<dd>
<p>SMS messages are in PDU format. For GSM-based devices, messages are hexadecimal strings that
     represent messages in PDU format as defined in the 3GPP TS 27.005 and 3GPP TS 23.040 specifications. For
     CDMA-based devices messages are byte arrays that represent messages as defined in section 3.4.2.1 SMS
     Point-to-Point Message in 3GPP2 specification C.S0015-A "Short Message Service (SMS) for Wideband Spread
     Spectrum Systems".</p>
</dd>

### -field <a id="WwanSmsFormatReserved0"></a><a id="wwansmsformatreserved0"></a><a id="WWANSMSFORMATRESERVED0"></a><b>WwanSmsFormatReserved0</b>

<dd>
<p>This value is reserved for future use. Do not use.</p>
</dd>

### -field <a id="WwanSmsFormatReserved1"></a><a id="wwansmsformatreserved1"></a><a id="WWANSMSFORMATRESERVED1"></a><b>WwanSmsFormatReserved1</b>

<dd>
<p>This value is reserved for future use. Do not use.</p>
</dd>

### -field <a id="WwanSmsFormatReserved2"></a><a id="wwansmsformatreserved2"></a><a id="WWANSMSFORMATRESERVED2"></a><b>WwanSmsFormatReserved2</b>

<dd>
<p>This value is reserved for future use. Do not use.</p>
</dd>

### -field <a id="WwanSmsFormatCdma"></a><a id="wwansmsformatcdma"></a><a id="WWANSMSFORMATCDMA"></a><b>WwanSmsFormatCdma</b>

<dd>
<p>The message is in text format. For more information, see 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571243">WWAN_SMS_CDMA_RECORD</a> and 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff571251">WWAN_SMS_SEND_CDMA</a>. This value applies
     only to CDMA-based devices.</p>
</dd>

### -field <a id="WwanSmsFormatMax"></a><a id="wwansmsformatmax"></a><a id="WWANSMSFORMATMAX"></a><b>WwanSmsFormatMax</b>

<dd>
<p>This value is reserved. Do not use.</p>
</dd>
</dl>

## -remarks
<p>CDMA-based devices support only 
    <b>WwanSmsFormatCdma</b>. The 
    <b>WwanSmsFormatCdma</b> format is not applicable for GSM-based devices.</p>

<p>CDMA-based devices support only 
    <b>WwanSmsFormatCdma</b>. The 
    <b>WwanSmsFormatCdma</b> format is not applicable for GSM-based devices.</p>

<p>CDMA-based devices support only 
    <b>WwanSmsFormatCdma</b>. The 
    <b>WwanSmsFormatCdma</b> format is not applicable for GSM-based devices.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571238">WWAN_SET_SMS_CONFIGURATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571244">WWAN_SMS_CONFIGURATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571249">WWAN_SMS_READ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571250">WWAN_SMS_SEND</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571243">WWAN_SMS_CDMA_RECORD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571251">WWAN_SMS_SEND_CDMA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SMS_FORMAT enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

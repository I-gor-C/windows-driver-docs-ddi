---
UID: NE.wwan._WWAN_SMS_FORMAT
title: WWAN_SMS_FORMAT
author: windows-driver-content
description: The WWAN_SMS_FORMAT enumeration lists different Short Message Service (SMS) formats.
old-location: netvista\wwan_sms_format.htm
old-project: netvista
ms.assetid: fb583ded-8292-4486-8e85-3d3039611d14
ms.author: windowsdriverdev
ms.date: 11/30/2017
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

### -field WwanSmsFormatPdu

<dd>
<p>SMS messages are in PDU format. For GSM-based devices, messages are hexadecimal strings that
     represent messages in PDU format as defined in the 3GPP TS 27.005 and 3GPP TS 23.040 specifications. For
     CDMA-based devices messages are byte arrays that represent messages as defined in section 3.4.2.1 SMS
     Point-to-Point Message in 3GPP2 specification C.S0015-A "Short Message Service (SMS) for Wideband Spread
     Spectrum Systems".</p>
</dd>

### -field WwanSmsFormatReserved0

<dd>
<p>This value is reserved for future use. Do not use.</p>
</dd>

### -field WwanSmsFormatReserved1

<dd>
<p>This value is reserved for future use. Do not use.</p>
</dd>

### -field WwanSmsFormatReserved2

<dd>
<p>This value is reserved for future use. Do not use.</p>
</dd>

### -field WwanSmsFormatCdma

<dd>
<p>The message is in text format. For more information, see 
     <a href="..\wwan\ns-wwan--wwan-sms-cdma-record.md">WWAN_SMS_CDMA_RECORD</a> and 
     <a href="..\wwan\ns-wwan--wwan-sms-send-cdma.md">WWAN_SMS_SEND_CDMA</a>. This value applies
     only to CDMA-based devices.</p>
</dd>

### -field WwanSmsFormatMax

<dd>
<p>This value is reserved. Do not use.</p>
</dd>
</dl>

## -remarks
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
<a href="..\wwan\ns-wwan--wwan-set-sms-configuration.md">WWAN_SET_SMS_CONFIGURATION</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-sms-configuration.md">WWAN_SMS_CONFIGURATION</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-sms-read.md">WWAN_SMS_READ</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-sms-send.md">WWAN_SMS_SEND</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-sms-cdma-record.md">WWAN_SMS_CDMA_RECORD</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-sms-send-cdma.md">WWAN_SMS_SEND_CDMA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SMS_FORMAT enumeration%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

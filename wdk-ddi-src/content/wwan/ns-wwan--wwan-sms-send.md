---
UID: NS.wwan._WWAN_SMS_SEND
title: WWAN_SMS_SEND
author: windows-driver-content
description: The WWAN_SMS_SEND structure represents an SMS text message to send.
old-location: netvista\wwan_sms_send.htm
old-project: netvista
ms.assetid: 2d2e5d13-56ca-452c-86fd-4a48b11d53ab
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: WWAN_SMS_SEND, WWAN_SMS_SEND, *PWWAN_SMS_SEND
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: wwan.h
req.include-header: Wwan.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows 7 and later versions of Windows.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_SMS_SEND
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

# WWAN_SMS_SEND structure



## -description
<p>The WWAN_SMS_SEND structure represents an SMS text message to send.</p>


## -syntax

````
typedef struct _WWAN_SMS_SEND {
  WWAN_SMS_FORMAT SmsFormat;
  union {
    WWAN_SMS_SEND_PDU  Pdu;
    WWAN_SMS_SEND_CDMA Cdma;
  } u;
} WWAN_SMS_SEND, *PWWAN_SMS_SEND;
````


## -struct-fields
<dl>

### -field SmsFormat

<dd>
<p>The format of the SMS text message.</p>
</dd>

### -field u

<dd>
<p>Container union for the different SMS formats.</p>
<dl>

### -field Pdu

<dd>
<p>Short message data types to be used depending on the value of 
      <b>SmsFormat</b> as shown in the following table.
      </p>
<table>
<tr>
<th>SmsFormat</th>
<th>Member to use</th>
</tr>
<tr>
<td>
<p>WwanSmsFormatPdu</p>
</td>
<td>
<p>Pdu</p>
</td>
</tr>
<tr>
<td>
<p>WwanSmsFormatCdma</p>
</td>
<td>
<p>Cdma</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Cdma

<dd>
<p>Short message data types to be used depending on the value of 
      <b>SmsFormat</b> as shown in the following table.
      </p>
<table>
<tr>
<th>SmsFormat</th>
<th>Member to use</th>
</tr>
<tr>
<td>
<p>WwanSmsFormatPdu</p>
</td>
<td>
<p>Pdu</p>
</td>
</tr>
<tr>
<td>
<p>WwanSmsFormatCdma</p>
</td>
<td>
<p>Cdma</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>
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
<a href="..\wwan\ns-wwan--wwan-sms-send-pdu.md">WWAN_SMS_SEND_PDU</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-sms-send-cdma.md">WWAN_SMS_SEND_CDMA</a>
</dt>
<dt>
<a href="..\ndiswwan\ns-ndiswwan--ndis-wwan-sms-send.md">NDIS_WWAN_SMS_SEND</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SMS_SEND structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

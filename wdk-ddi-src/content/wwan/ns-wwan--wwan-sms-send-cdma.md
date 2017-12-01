---
UID: NS.wwan._WWAN_SMS_SEND_CDMA
title: WWAN_SMS_SEND_CDMA
author: windows-driver-content
description: The WWAN_SMS_SEND_CDMA structure represents a CDMA-based SMS text message to send.
old-location: netvista\wwan_sms_send_cdma.htm
old-project: netvista
ms.assetid: e05b7391-7852-45c7-aed0-36c95b4e475b
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: WWAN_SMS_SEND_CDMA, WWAN_SMS_SEND_CDMA, *PWWAN_SMS_SEND_CDMA
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
req.alt-api: WWAN_SMS_SEND_CDMA
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

# WWAN_SMS_SEND_CDMA structure



## -description
<p>The WWAN_SMS_SEND_CDMA structure represents a CDMA-based SMS text message to send.</p>


## -syntax

````
typedef struct _WWAN_SMS_SEND_CDMA {
  WWAN_SMS_CDMA_ENCODING EncodingId;
  WWAN_SMS_CDMA_LANG     LanguageId;
  CHAR                   Address[WWAN_SMS_CDMA_ADDR_MAX_LEN];
  USHORT                 SizeInBytes;
  BYTE                   SizeInCharacters;
  BYTE                   EncodedMsg[WWAN_SMS_CDMA_MAX_BUF_LEN];
} WWAN_SMS_SEND_CDMA, *PWWAN_SMS_SEND_CDMA;
````


## -struct-fields
<dl>

### -field <b>EncodingId</b>

<dd>
<p>The encoding that is used in the CDMA message. 
     <b>EncodedMsg</b> message should be interpreted based on the value of this member.</p>
</dd>

### -field <b>LanguageId</b>

<dd>
<p>The language used in CDMA message. This is an indicator of the language used in SMS message and
     may be set to 
     <b>WwanSmsCdmaLangUnknown</b>, if the language is not known.</p>
</dd>

### -field <b>Address</b>

<dd>
<p>A NULL-terminated string with a maximum length of 15 digits that represents a mobile number. The
     number can be in any of the following formats:
     </p>
<ul>
<li>
<p>"+ &lt;International Country Code&gt; &lt;Mobile Number&gt;\0"</p>
</li>
<li>
<p>"&lt;Mobile Number&gt;\0"</p>
</li>
</ul>
<p>If 
     <b>MsgStatus</b> is 
     <i>WwanMsgStatusDraft</i> or 
     <i>WwanMsgStatusSent</i>, miniport drivers should specify the receiver's mobile number in the previous
     members. Otherwise, if 
     <b>MsgStatus</b> is 
     <i>WwanMsgStatusNew</i> or 
     <i>WwanMsgStatusOld</i>, miniport drivers should specify the sender's mobile number.</p>
</dd>

### -field <b>SizeInBytes</b>

<dd>
<p>The size, in bytes, of 
     <b>EncodedMsg</b> . The encoded message can have a maximum length of WWAN_SMS_CDMA_MAX_BUF_LEN. Miniport
     drivers must specify a value for this member for all encoding types.</p>
</dd>

### -field <b>SizeInCharacters</b>

<dd>
<p>Size of 
     <b>EncodedMsg</b> in number of characters represented by the encoded data. Miniport drivers should
     specify 0 for this member when 
     <b>EncodingId</b> is set to 
     <i>WwanSmsCdmaEncodingShiftJis</i> or 
     <i>WwanSmsCdmaEncodingKorean</i>.</p>
</dd>

### -field <b>EncodedMsg</b>

<dd>
<p>The encoded content that represents the CDMA-based SMS text message.</p>
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
<a href="..\wwan\ne-wwan--wwan-sms-cdma-encoding.md">WWAN_SMS_CDMA_ENCODING</a>
</dt>
<dt>
<a href="..\wwan\ne-wwan--wwan-sms-cdma-lang.md">WWAN_SMS_CDMA_LANG</a>
</dt>
<dt>
<a href="..\wwan\ns-wwan--wwan-sms-send.md">WWAN_SMS_SEND</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SMS_SEND_CDMA structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

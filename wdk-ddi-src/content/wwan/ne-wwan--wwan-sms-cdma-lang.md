---
UID: NE.wwan._WWAN_SMS_CDMA_LANG
title: WWAN_SMS_CDMA_LANG
author: windows-driver-content
description: The WWAN_SMS_CDMA_LANG enumeration lists the different SMS CDMA languages that are supported by the MB device.
old-location: netvista\wwan_sms_cdma_lang.htm
old-project: netvista
ms.assetid: 5294ce07-a4eb-4c21-88f1-04889dfbc1a1
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
req.alt-api: WWAN_SMS_CDMA_LANG
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

# WWAN_SMS_CDMA_LANG enumeration



## -description
<p>The WWAN_SMS_CDMA_LANG enumeration lists the different SMS CDMA languages that are supported by the
  MB device.</p>


## -syntax

````
typedef enum _WWAN_SMS_CDMA_LANG { 
  WwanSmsCdmaLangUnknown   = 0,
  WwanSmsCdmaLangEnglish,
  WwanSmsCdmaLangFrench,
  WwanSmsCdmaLangSpanish,
  WwanSmsCdmaLangJapanese,
  WwanSmsCdmaLangKorean,
  WwanSmsCdmaLangChinese,
  WwanSmsCdmaLangHebrew,
  WwanSmsCdmaLangMax
} WWAN_SMS_CDMA_LANG, *PWWAN_SMS_CDMA_LANG;
````


## -enum-fields
<dl>

### -field <a id="WwanSmsCdmaLangUnknown"></a><a id="wwansmscdmalangunknown"></a><a id="WWANSMSCDMALANGUNKNOWN"></a><b>WwanSmsCdmaLangUnknown</b>

<dd>
<p>The message language is unknown.</p>
</dd>

### -field <a id="WwanSmsCdmaLangEnglish"></a><a id="wwansmscdmalangenglish"></a><a id="WWANSMSCDMALANGENGLISH"></a><b>WwanSmsCdmaLangEnglish</b>

<dd>
<p>The message is in English.</p>
</dd>

### -field <a id="WwanSmsCdmaLangFrench"></a><a id="wwansmscdmalangfrench"></a><a id="WWANSMSCDMALANGFRENCH"></a><b>WwanSmsCdmaLangFrench</b>

<dd>
<p>The message is in French.</p>
</dd>

### -field <a id="WwanSmsCdmaLangSpanish"></a><a id="wwansmscdmalangspanish"></a><a id="WWANSMSCDMALANGSPANISH"></a><b>WwanSmsCdmaLangSpanish</b>

<dd>
<p>The message is in Spanish.</p>
</dd>

### -field <a id="WwanSmsCdmaLangJapanese"></a><a id="wwansmscdmalangjapanese"></a><a id="WWANSMSCDMALANGJAPANESE"></a><b>WwanSmsCdmaLangJapanese</b>

<dd>
<p>The message is in Japanese.</p>
</dd>

### -field <a id="WwanSmsCdmaLangKorean"></a><a id="wwansmscdmalangkorean"></a><a id="WWANSMSCDMALANGKOREAN"></a><b>WwanSmsCdmaLangKorean</b>

<dd>
<p>The message is in Korean.</p>
</dd>

### -field <a id="WwanSmsCdmaLangChinese"></a><a id="wwansmscdmalangchinese"></a><a id="WWANSMSCDMALANGCHINESE"></a><b>WwanSmsCdmaLangChinese</b>

<dd>
<p>The message is in Chinese.</p>
</dd>

### -field <a id="WwanSmsCdmaLangHebrew"></a><a id="wwansmscdmalanghebrew"></a><a id="WWANSMSCDMALANGHEBREW"></a><b>WwanSmsCdmaLangHebrew</b>

<dd>
<p>The message is in Hebrew.</p>
</dd>

### -field <a id="WwanSmsCdmaLangMax"></a><a id="wwansmscdmalangmax"></a><a id="WWANSMSCDMALANGMAX"></a><b>WwanSmsCdmaLangMax</b>

<dd>
<p>The total number of supported SMS CDMA languages.</p>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SMS_CDMA_LANG enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

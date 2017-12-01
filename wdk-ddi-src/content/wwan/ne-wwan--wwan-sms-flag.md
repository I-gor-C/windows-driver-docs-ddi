---
UID: NE.wwan._WWAN_SMS_FLAG
title: WWAN_SMS_FLAG
author: windows-driver-content
description: The WWAN_SMS_FLAG enumeration lists different flags to filter SMS text messages.
old-location: netvista\wwan_sms_flag.htm
old-project: netvista
ms.assetid: 6620d6c8-2b8a-440e-acf4-fb08570b13bf
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
req.alt-api: WWAN_SMS_FLAG
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

# WWAN_SMS_FLAG enumeration



## -description
<p>The WWAN_SMS_FLAG enumeration lists different flags to filter SMS text messages.</p>


## -syntax

````
typedef enum _WWAN_SMS_FLAG { 
  WwanSmsFlagAll    = 0,
  WwanSmsFlagIndex,
  WwanSmsFlagNew,
  WwanSmsFlagOld,
  WwanSmsFlagSent,
  WwanSmsFlagDraft,
  WwanSmsFlagMax
} WWAN_SMS_FLAG, *PWWAN_SMS_FLAG;
````


## -enum-fields
<dl>

### -field <a id="WwanSmsFlagAll"></a><a id="wwansmsflagall"></a><a id="WWANSMSFLAGALL"></a><b>WwanSmsFlagAll</b>

<dd>
<p>No filter is set.</p>
</dd>

### -field <a id="WwanSmsFlagIndex"></a><a id="wwansmsflagindex"></a><a id="WWANSMSFLAGINDEX"></a><b>WwanSmsFlagIndex</b>

<dd>
<p>Filter based on the value of an index.</p>
</dd>

### -field <a id="WwanSmsFlagNew"></a><a id="wwansmsflagnew"></a><a id="WWANSMSFLAGNEW"></a><b>WwanSmsFlagNew</b>

<dd>
<p>Filter for new (unread) messages.</p>
</dd>

### -field <a id="WwanSmsFlagOld"></a><a id="wwansmsflagold"></a><a id="WWANSMSFLAGOLD"></a><b>WwanSmsFlagOld</b>

<dd>
<p>Filter for old (read) messages.</p>
</dd>

### -field <a id="WwanSmsFlagSent"></a><a id="wwansmsflagsent"></a><a id="WWANSMSFLAGSENT"></a><b>WwanSmsFlagSent</b>

<dd>
<p>Filter for sent messages.</p>
</dd>

### -field <a id="WwanSmsFlagDraft"></a><a id="wwansmsflagdraft"></a><a id="WWANSMSFLAGDRAFT"></a><b>WwanSmsFlagDraft</b>

<dd>
<p>Filter for draft messages.</p>
</dd>

### -field <a id="WwanSmsFlagMax"></a><a id="wwansmsflagmax"></a><a id="WWANSMSFLAGMAX"></a><b>WwanSmsFlagMax</b>

<dd>
<p>The total number of filter flags.</p>
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
<a href="..\wwan\ns-wwan--wwan-sms-filter.md">WWAN_SMS_FILTER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_SMS_FLAG enumeration%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

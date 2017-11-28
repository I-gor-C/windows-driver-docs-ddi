---
UID: NE.wwan._WWAN_MSG_STATUS
title: WWAN_MSG_STATUS
author: windows-driver-content
description: The WWAN_MSG_STATUS enumeration lists different SMS message statuses.
old-location: netvista\wwan_msg_status.htm
old-project: netvista
ms.assetid: 60eb0494-fcc6-4546-a13a-b6d1dcf165e6
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
req.alt-api: WWAN_MSG_STATUS
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

# WWAN_MSG_STATUS enumeration



## -description
<p>The WWAN_MSG_STATUS enumeration lists different SMS message statuses.</p>


## -syntax

````
typedef enum _WWAN_MSG_STATUS { 
  WwanMsgStatusNew    = 0,
  WwanMsgStatusOld,
  WwanMsgStatusDraft,
  WwanMsgStatusSent,
  WwanMsgStatusMax
} WWAN_MSG_STATUS, *PWWAN_MSG_STATUS;
````


## -enum-fields
<dl>

### -field <a id="WwanMsgStatusNew"></a><a id="wwanmsgstatusnew"></a><a id="WWANMSGSTATUSNEW"></a><b>WwanMsgStatusNew</b>

<dd>
<p>The message is new or unread.</p>
</dd>

### -field <a id="WwanMsgStatusOld"></a><a id="wwanmsgstatusold"></a><a id="WWANMSGSTATUSOLD"></a><b>WwanMsgStatusOld</b>

<dd>
<p>The message is old and is read.</p>
</dd>

### -field <a id="WwanMsgStatusDraft"></a><a id="wwanmsgstatusdraft"></a><a id="WWANMSGSTATUSDRAFT"></a><b>WwanMsgStatusDraft</b>

<dd>
<p>The message is unsent and stored in the device.</p>
</dd>

### -field <a id="WwanMsgStatusSent"></a><a id="wwanmsgstatussent"></a><a id="WWANMSGSTATUSSENT"></a><b>WwanMsgStatusSent</b>

<dd>
<p>The message has already been sent.</p>
</dd>

### -field <a id="WwanMsgStatusMax"></a><a id="wwanmsgstatusmax"></a><a id="WWANMSGSTATUSMAX"></a><b>WwanMsgStatusMax</b>

<dd>
<p>The total number of supported SMS message statuses.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571243">WWAN_SMS_CDMA_RECORD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571248">WWAN_SMS_PDU_RECORD</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_MSG_STATUS enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

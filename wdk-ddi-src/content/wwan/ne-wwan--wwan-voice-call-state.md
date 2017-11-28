---
UID: NE.wwan._WWAN_VOICE_CALL_STATE
title: WWAN_VOICE_CALL_STATE
author: windows-driver-content
description: The WWAN_VOICE_CALL_STATE enumeration lists the different voice call states that are supported by the MB device.
old-location: netvista\wwan_voice_call_state.htm
old-project: netvista
ms.assetid: 50b85fc0-b84a-4c1d-9d7b-4b91150f8e76
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
req.alt-api: WWAN_VOICE_CALL_STATE
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

# WWAN_VOICE_CALL_STATE enumeration



## -description
<p>The WWAN_VOICE_CALL_STATE enumeration lists the different voice call states that are supported by the
  MB device.</p>


## -syntax

````
typedef enum _WWAN_VOICE_CALL_STATE { 
  WwanVoiceCallStateNone        = 0,
  WwanVoiceCallStateInProgress,
  WwanVoiceCallStateHangUp,
  WwanVoiceCallStateMaximum
} WWAN_VOICE_CALL_STATE, *PWWAN_VOICE_CALL_STATE;
````


## -enum-fields
<dl>

### -field <a id="WwanVoiceCallStateNone"></a><a id="wwanvoicecallstatenone"></a><a id="WWANVOICECALLSTATENONE"></a><b>WwanVoiceCallStateNone</b>

<dd>
<p>The device does not support voice calls, or there is no voice call currently in progress.</p>
</dd>

### -field <a id="WwanVoiceCallStateInProgress"></a><a id="wwanvoicecallstateinprogress"></a><a id="WWANVOICECALLSTATEINPROGRESS"></a><b>WwanVoiceCallStateInProgress</b>

<dd>
<p>A voice call is currently in progress. This value applies only to devices whose voice class is 
     <b>WwanVoiceClassSeparateVoiceData</b>.</p>
</dd>

### -field <a id="WwanVoiceCallStateHangUp"></a><a id="wwanvoicecallstatehangup"></a><a id="WWANVOICECALLSTATEHANGUP"></a><b>WwanVoiceCallStateHangUp</b>

<dd>
<p>A voice call is completed. This value applies only to devices whose voice class is 
     <b>WwanVoiceClassSeparateVoiceData</b>.</p>
</dd>

### -field <a id="WwanVoiceCallStateMaximum"></a><a id="wwanvoicecallstatemaximum"></a><a id="WWANVOICECALLSTATEMAXIMUM"></a><b>WwanVoiceCallStateMaximum</b>

<dd>
<p>The total number of supported voice call states.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff571202">WWAN_CONTEXT_STATE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_VOICE_CALL_STATE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

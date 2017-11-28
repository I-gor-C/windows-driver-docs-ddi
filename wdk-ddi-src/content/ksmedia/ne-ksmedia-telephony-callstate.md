---
UID: NE.ksmedia.TELEPHONY_CALLSTATE
title: TELEPHONY_CALLSTATE
author: windows-driver-content
description: The TELEPHONY_CALLSTATE enumeration defines constants that specify the state of a phone call.
old-location: audio\telephony_callstate.htm
old-project: audio
ms.assetid: 8191418A-7139-4BF4-9869-F21AA54EA8B3
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PKSIDEFAULTCLOCK, KSIDEFAULTCLOCK, *PKSIDEFAULTCLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10,Windows 10 Mobile
req.target-min-winversvr: None supported
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: TELEPHONY_CALLSTATE
req.alt-loc: ksmedia.h
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
---

# TELEPHONY_CALLSTATE enumeration



## -description
<p>The <b>TELEPHONY_CALLSTATE</b> enumeration defines constants that specify the state of a phone call.</p>


## -syntax

````
typedef enum  { 
  TELEPHONY_CALLSTATE_DISABLED            = 0,
  TELEPHONY_CALLSTATE_ENABLED             = 1,
  TELEPHONY_CALLSTATE_HOLD                = 2,
  TELEPHONY_CALLSTATE_PROVIDERTRANSITION  = 3
} TELEPHONY_CALLSTATE;
````


## -enum-fields
<dl>

### -field <a id="TELEPHONY_CALLSTATE_DISABLED"></a><a id="telephony_callstate_disabled"></a><b>TELEPHONY_CALLSTATE_DISABLED</b>

<dd>
<p>Specifies that the phone call is disabled.</p>
</dd>

### -field <a id="TELEPHONY_CALLSTATE_ENABLED"></a><a id="telephony_callstate_enabled"></a><b>TELEPHONY_CALLSTATE_ENABLED</b>

<dd>
<p>Specifies that the phone call is enabled. This constant is set in a number of situations. For example, it will be set by the audio driver when the provider change operation is <b>TELEPHONY_PROVIDERCHANGEOP_END</b> and when <b>TELEPHONY_CALLCONTROLOP_ENABLE</b> is received.</p>
</dd>

### -field <a id="TELEPHONY_CALLSTATE_HOLD"></a><a id="telephony_callstate_hold"></a><b>TELEPHONY_CALLSTATE_HOLD</b>

<dd>
<p>Specifies that the phone call is on hold.</p>
</dd>

### -field <a id="TELEPHONY_CALLSTATE_PROVIDERTRANSITION"></a><a id="telephony_callstate_providertransition"></a><b>TELEPHONY_CALLSTATE_PROVIDERTRANSITION</b>

<dd>
<p>Specifies that the phone call is disabled. This constant is set by the audio driver when the provider change operation is <b>TELEPHONY_PROVIDERCHANGEOP_BEGIN</b>.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Client</p>
</th>
<td width="70%">
<p>Windows 10 Mobile</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ksmedia.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt169884">KSTELEPHONY_CALLINFO</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt169898">TELEPHONY_PROVIDERCHANGEOP</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20TELEPHONY_CALLSTATE enumeration%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NE.wwan._WWAN_USSD_EVENT_TYPE
title: WWAN_USSD_EVENT_TYPE
author: windows-driver-content
description: The WWAN_USSD_EVENT_TYPE enumeration lists the different types of Unstructured Supplementary Service Data (USSD) events.
old-location: netvista\wwan_ussd_event_type.htm
old-project: netvista
ms.assetid: CEBC8A75-03E9-4E2A-9092-2FA3005371FE
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: WUDF_WORKITEM_CONFIG, WUDF_WORKITEM_CONFIG, *PWUDF_WORKITEM_CONFIG
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: wwan.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with  Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: WWAN_USSD_EVENT_TYPE
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

# WWAN_USSD_EVENT_TYPE enumeration



## -description
<p>The WWAN_USSD_EVENT_TYPE enumeration lists the different types of Unstructured Supplementary Service Data (USSD) events.</p>


## -syntax

````
typedef enum _WWAN_USSD_EVENT_TYPE { 
  WwanUssdEventNoActionRequired       = 0,
  WwanUssdEventActionRequired         = 1,
  WwanUssdEventTerminated             = 2,
  WwanUssdEventOtherLocalClient       = 3,
  WwanUssdEventOperationNotSupported  = 4,
  WwanUssdEventNetworkTimeOut         = 5
} WWAN_USSD_EVENT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="WwanUssdEventNoActionRequired"></a><a id="wwanussdeventnoactionrequired"></a><a id="WWANUSSDEVENTNOACTIONREQUIRED"></a><b>WwanUssdEventNoActionRequired</b>

<dd>
<p>Indicates no further action is required or information needed.</p>
</dd>

### -field <a id="WwanUssdEventActionRequired"></a><a id="wwanussdeventactionrequired"></a><a id="WWANUSSDEVENTACTIONREQUIRED"></a><b>WwanUssdEventActionRequired</b>

<dd>
<p>Indicates the USSD session is still open and further information is needed, such as additional USSD strings.</p>
</dd>

### -field <a id="WwanUssdEventTerminated"></a><a id="wwanussdeventterminated"></a><a id="WWANUSSDEVENTTERMINATED"></a><b>WwanUssdEventTerminated</b>

<dd>
<p>Indicates the USSD session has been terminated.</p>
</dd>

### -field <a id="WwanUssdEventOtherLocalClient"></a><a id="wwanussdeventotherlocalclient"></a><a id="WWANUSSDEVENTOTHERLOCALCLIENT"></a><b>WwanUssdEventOtherLocalClient</b>

<dd>
<p>Indicates an active USSD session already exists and that a new session cannot be established until the active session terminates. This includes sessions that are invisible to the MB stack such as a USSD session termination in the Subscriber Identity Module (SIM).</p>
</dd>

### -field <a id="WwanUssdEventOperationNotSupported"></a><a id="wwanussdeventoperationnotsupported"></a><a id="WWANUSSDEVENTOPERATIONNOTSUPPORTED"></a><b>WwanUssdEventOperationNotSupported</b>

<dd>
<p>Indicates that the previous request is not supported by the miniport driver or MB device.</p>
</dd>

### -field <a id="WwanUssdEventNetworkTimeOut"></a><a id="wwanussdeventnetworktimeout"></a><a id="WWANUSSDEVENTNETWORKTIMEOUT"></a><b>WwanUssdEventNetworkTimeOut</b>

<dd>
<p>Indicates that the USSD session was closed due to a session time-out either locally or by the network. The miniport driver or MB device is responsible for timing out an inactive USSD session after an implementation-specific time-out.</p>
</dd>
</dl>

## -remarks
<p>Network-initiated USSD events use <i>WwanUssdEventActionRequired</i> to indicate when further information is needed after an MB device initiated operation. <i>WwanUssdEventActionRequired</i> events also indicate that the session is still open. All other events indicate that the existing USSD session has been closed.</p>

<p><i>WwanUssdEventNoActionRequired</i> and <i>WwanUssdEventActionRequired</i> are the only events that require a non-empty USSD string to accompany them with a string length from 1 to 160 bytes. All other events must set the USSD string length to 0 to indicate that the string is empty.</p>

<p>The value of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh464136">WWAN_USSD_EVENT</a><b>SessionState</b> member is ignored if no string is present.</p>

<p>Network-initiated USSD events use <i>WwanUssdEventActionRequired</i> to indicate when further information is needed after an MB device initiated operation. <i>WwanUssdEventActionRequired</i> events also indicate that the session is still open. All other events indicate that the existing USSD session has been closed.</p>

<p><i>WwanUssdEventNoActionRequired</i> and <i>WwanUssdEventActionRequired</i> are the only events that require a non-empty USSD string to accompany them with a string length from 1 to 160 bytes. All other events must set the USSD string length to 0 to indicate that the string is empty.</p>

<p>The value of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh464136">WWAN_USSD_EVENT</a><b>SessionState</b> member is ignored if no string is present.</p>

<p>Network-initiated USSD events use <i>WwanUssdEventActionRequired</i> to indicate when further information is needed after an MB device initiated operation. <i>WwanUssdEventActionRequired</i> events also indicate that the session is still open. All other events indicate that the existing USSD session has been closed.</p>

<p><i>WwanUssdEventNoActionRequired</i> and <i>WwanUssdEventActionRequired</i> are the only events that require a non-empty USSD string to accompany them with a string length from 1 to 160 bytes. All other events must set the USSD string length to 0 to indicate that the string is empty.</p>

<p>The value of the <a href="https://msdn.microsoft.com/library/windows/hardware/hh464136">WWAN_USSD_EVENT</a><b>SessionState</b> member is ignored if no string is present.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported starting with  Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Wwan.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh464136">WWAN_USSD_EVENT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20WWAN_USSD_EVENT_TYPE enumeration%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NS.ksmedia._tagKSTELEPHONY_CALLINFO
title: tagKSTELEPHONY_CALLINFO
author: windows-driver-content
description: The KSTELEPHONY_CALLINFO structure specifies the type and state of a phone call for the KSPROPERTY_TELEPHONY_CALLINFO property.
old-location: audio\kstelephony_callinfo.htm
old-project: audio
ms.assetid: B5B89AAC-169B-42B0-8FC8-AB436EFC3579
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: tagKSTELEPHONY_CALLINFO, KSTELEPHONY_CALLINFO, *PKSTELEPHONY_CALLINFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10,Windows 10 Mobile
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSTELEPHONY_CALLINFO
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

# tagKSTELEPHONY_CALLINFO structure



## -description
<p>The <b>KSTELEPHONY_CALLINFO</b> structure specifies the type and state of a phone call for the <a href="https://msdn.microsoft.com/library/windows/hardware/mt169873">KSPROPERTY_TELEPHONY_CALLINFO</a> property.</p>


## -syntax

````
typedef struct _tagKSTELEPHONY_CALLINFO {
  TELEPHONY_CALLTYPE  CallType;
  TELEPHONY_CALLSTATE CallState;
} KSTELEPHONY_CALLINFO, *PKSTELEPHONY_CALLINFO;
````


## -struct-fields
<dl>

### -field <b>CallType</b>

<dd>
<p>Specifies the type of phone call (circuit-switched, LTE packet-switched, or WLAN packet-switched).</p>
</dd>

### -field <b>CallState</b>

<dd>
<p>Specifies the state of the phone call.</p>
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
<p>Windows Server 2016</p>
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
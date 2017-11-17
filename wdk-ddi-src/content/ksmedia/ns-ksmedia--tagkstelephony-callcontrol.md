---
UID: NS.ksmedia._tagKSTELEPHONY_CALLCONTROL
title: tagKSTELEPHONY_CALLCONTROL
author: windows-driver-content
description: The KSTELEPHONY_CALLCONTROL structure specifies the phone call type and control operation to use for the KSPROPERTY_TELEPHONY_CALLCONTROL property.
old-location: audio\kstelephony_callcontrol.htm
ms.assetid: 44CA5D9D-EF6E-4681-93EB-B803638896F9
ms.author: windowsdriverdev
ms.date: 10/30/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: audio
req.header: ksmedia.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10,Windows 10 Mobile
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSTELEPHONY_CALLCONTROL
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
ms.keywords: tagKSTELEPHONY_CALLCONTROL, KSTELEPHONY_CALLCONTROL, *PKSTELEPHONY_CALLCONTROL
req.iface: 
---

# tagKSTELEPHONY_CALLCONTROL structure



## -description
<p>The <b>KSTELEPHONY_CALLCONTROL</b> structure specifies the phone call type and control operation to use for the <a href="https://msdn.microsoft.com/library/windows/hardware/mt169871">KSPROPERTY_TELEPHONY_CALLCONTROL</a> property.</p>


## -syntax

````
typedef struct _tagKSTELEPHONY_CALLCONTROL {
  TELEPHONY_CALLTYPE      CallType;
  TELEPHONY_CALLCONTROLOP CallControlOp;
} KSTELEPHONY_CALLCONTROL, *PKSTELEPHONY_CALLCONTROL;
````


## -struct-fields
<dl>

### -field <b>CallType</b>

<dd>
<p>Specifies the type of phone call (circuit-switched, LTE packet-switched, or WLAN packet-switched).</p>
</dd>

### -field <b>CallControlOp</b>

<dd>
<p>Specifies the call control operation (enable or disable).</p>
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
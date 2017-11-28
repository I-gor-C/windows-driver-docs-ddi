---
UID: NE.ntddrilapitypes.RILMANAGECALLPARAMSCOMMAND
title: RILMANAGECALLPARAMSCOMMAND
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmanagecallparamscommand.htm
old-project: netvista
ms.assetid: d0344812-811e-47f6-a03b-bb753cce912a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: TUPLE_REQUEST, TUPLE_REQUEST, *PTUPLE_REQUEST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddrilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILMANAGECALLPARAMSCOMMAND
req.alt-loc: ntddrilapitypes.h
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

# RILMANAGECALLPARAMSCOMMAND enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.</p>


## -syntax

````
typedef enum _RILMANAGECALLPARAMSCOMMAND { 
  RIL_CALLCMD_RELEASECALL,
  RIL_CALLCMD_HOLDACTIVE_ACCEPTHELD,
  RIL_CALLCMD_HOLDALLBUTONE,
  RIL_CALLCMD_ADDHELDTOCONF,
  RIL_CALLCMD_ADDHELDTOCONF_DISCONNECT,
  RIL_CALLCMD_RELEASEPROCEEDING,
  RIL_CALLCMD_RELEASEALLCALLS,
  RIL_CALLCMD_RELEASEHELDCONFCALL,
  RIL_CALLCMD_ACCEPTINCOMINGCALL,
  RIL_CALLCMD_OFFERMEDIA,
  RIL_CALLCMD_ANSWERMEDIAOFFER,
  RIL_CALLCMD_BLINDCALLTRANSFER,
  RIL_CALLCMD_ASSUREDCALLTRANSFER,
  RIL_CALLCMD_CONSULTATIVECALLTRANSFER,
  RIL_CALLCMD_RTT,
  RIL_CALLCMD_MAX
} RILMANAGECALLPARAMSCOMMAND;
````


## -enum-fields
<dl>

### -field <a id="RIL_CALLCMD_RELEASECALL"></a><a id="ril_callcmd_releasecall"></a><b>RIL_CALLCMD_RELEASECALL</b>

<dd></dd>

### -field <a id="RIL_CALLCMD_HOLDACTIVE_ACCEPTHELD"></a><a id="ril_callcmd_holdactive_acceptheld"></a><b>RIL_CALLCMD_HOLDACTIVE_ACCEPTHELD</b>

<dd></dd>

### -field <a id="RIL_CALLCMD_HOLDALLBUTONE"></a><a id="ril_callcmd_holdallbutone"></a><b>RIL_CALLCMD_HOLDALLBUTONE</b>

<dd></dd>

### -field <a id="RIL_CALLCMD_ADDHELDTOCONF"></a><a id="ril_callcmd_addheldtoconf"></a><b>RIL_CALLCMD_ADDHELDTOCONF</b>

<dd></dd>

### -field <a id="RIL_CALLCMD_ADDHELDTOCONF_DISCONNECT"></a><a id="ril_callcmd_addheldtoconf_disconnect"></a><b>RIL_CALLCMD_ADDHELDTOCONF_DISCONNECT</b>

<dd></dd>

### -field <a id="RIL_CALLCMD_RELEASEPROCEEDING"></a><a id="ril_callcmd_releaseproceeding"></a><b>RIL_CALLCMD_RELEASEPROCEEDING</b>

<dd></dd>

### -field <a id="RIL_CALLCMD_RELEASEALLCALLS"></a><a id="ril_callcmd_releaseallcalls"></a><b>RIL_CALLCMD_RELEASEALLCALLS</b>

<dd></dd>

### -field <a id="RIL_CALLCMD_RELEASEHELDCONFCALL"></a><a id="ril_callcmd_releaseheldconfcall"></a><b>RIL_CALLCMD_RELEASEHELDCONFCALL</b>

<dd></dd>

### -field <a id="RIL_CALLCMD_ACCEPTINCOMINGCALL"></a><a id="ril_callcmd_acceptincomingcall"></a><b>RIL_CALLCMD_ACCEPTINCOMINGCALL</b>

<dd></dd>

### -field <a id="RIL_CALLCMD_OFFERMEDIA"></a><a id="ril_callcmd_offermedia"></a><b>RIL_CALLCMD_OFFERMEDIA</b>

<dd></dd>

### -field <a id="RIL_CALLCMD_ANSWERMEDIAOFFER"></a><a id="ril_callcmd_answermediaoffer"></a><b>RIL_CALLCMD_ANSWERMEDIAOFFER</b>

<dd></dd>

### -field <a id="RIL_CALLCMD_BLINDCALLTRANSFER"></a><a id="ril_callcmd_blindcalltransfer"></a><b>RIL_CALLCMD_BLINDCALLTRANSFER</b>

<dd></dd>

### -field <a id="RIL_CALLCMD_ASSUREDCALLTRANSFER"></a><a id="ril_callcmd_assuredcalltransfer"></a><b>RIL_CALLCMD_ASSUREDCALLTRANSFER</b>

<dd></dd>

### -field <a id="RIL_CALLCMD_CONSULTATIVECALLTRANSFER"></a><a id="ril_callcmd_consultativecalltransfer"></a><b>RIL_CALLCMD_CONSULTATIVECALLTRANSFER</b>

<dd></dd>

### -field <a id="RIL_CALLCMD_RTT"></a><a id="ril_callcmd_rtt"></a><b>RIL_CALLCMD_RTT</b>

<dd></dd>

### -field <a id="RIL_CALLCMD_MAX"></a><a id="ril_callcmd_max"></a><b>RIL_CALLCMD_MAX</b>

<dd></dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddrilapitypes.h</dt>
</dl>
</td>
</tr>
</table>
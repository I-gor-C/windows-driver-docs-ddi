---
UID: NE.rilapitypes.RILMANAGECALLPARAMSCOMMAND
title: RILMANAGECALLPARAMSCOMMAND
author: windows-driver-content
description: This topic supports the Windows driver infrastructure and is not intended to be used directly from your code.
old-location: netvista\rilmanagecallparamscommand_2.htm
old-project: netvista
ms.assetid: 0749f3fb-261c-4b98-961f-f2720100b8e6
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: RIL_WritePhonebookEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: rilapitypes.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RILMANAGECALLPARAMSCOMMAND
req.alt-loc: rilapitypes.h
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

# RILMANAGECALLPARAMSCOMMAND enumeration



## -description
<p>This topic supports the Windows driver infrastructure and is not intended to be used directly from your code. </p>


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

### -field RIL_CALLCMD_RELEASECALL

<dd></dd>

### -field RIL_CALLCMD_HOLDACTIVE_ACCEPTHELD

<dd></dd>

### -field RIL_CALLCMD_HOLDALLBUTONE

<dd></dd>

### -field RIL_CALLCMD_ADDHELDTOCONF

<dd></dd>

### -field RIL_CALLCMD_ADDHELDTOCONF_DISCONNECT

<dd></dd>

### -field RIL_CALLCMD_RELEASEPROCEEDING

<dd></dd>

### -field RIL_CALLCMD_RELEASEALLCALLS

<dd></dd>

### -field RIL_CALLCMD_RELEASEHELDCONFCALL

<dd></dd>

### -field RIL_CALLCMD_ACCEPTINCOMINGCALL

<dd></dd>

### -field RIL_CALLCMD_OFFERMEDIA

<dd></dd>

### -field RIL_CALLCMD_ANSWERMEDIAOFFER

<dd></dd>

### -field RIL_CALLCMD_BLINDCALLTRANSFER

<dd></dd>

### -field RIL_CALLCMD_ASSUREDCALLTRANSFER

<dd></dd>

### -field RIL_CALLCMD_CONSULTATIVECALLTRANSFER

<dd></dd>

### -field RIL_CALLCMD_RTT

<dd></dd>

### -field RIL_CALLCMD_MAX

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
<dt>Rilapitypes.h</dt>
</dl>
</td>
</tr>
</table>
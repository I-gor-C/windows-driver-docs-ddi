---
UID: NS.ntddk._POWER_THROTTLING_PROCESS_STATE
title: POWER_THROTTLING_PROCESS_STATE
author: windows-driver-content
description: Stores the throttling policies and how to apply them to a target process when that process is subject to power management.
old-location: kernel\power_throttling_process_state.htm
ms.assetid: f22be66a-1f1c-4999-a99e-9a8575313239
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: POWER_THROTTLING_PROCESS_STATE
req.alt-loc: Ntddk.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: POWER_THROTTLING_PROCESS_STATE, POWER_THROTTLING_PROCESS_STATE, *PPOWER_THROTTLING_PROCESS_STATE
req.iface: 
---

# POWER_THROTTLING_PROCESS_STATE structure



## -description
<p>Stores the throttling policies and how to apply them to a target process when that process is subject to power management.</p>


## -syntax

````
typedef struct _POWER_THROTTLING_PROCESS_STATE {
  ULONG  Version;
  ULONG  ControlMask;
  ULONG  StateMask;
} POWER_THROTTLING_PROCESS_STATE, POWER_THROTTLING_PROCESS_STATE;
````


## -struct-fields
<dl>

### -field <b>Version</b>

<dd>
<p>The version of this structure. Set to PROCESS_POWER_THROTTLING_CURRENT_VERSION.</p>
</dd>

### -field <b>ControlMask</b>

<dd>
<p>Flags that enable the caller to take control of the power throttling mechanism.</p>
<ul>
<li>PROCESS_POWER_THROTTLING_EXECUTION_SPEED: Manages the execution speed of the process.</li>
</ul>
</dd>

### -field <b>StateMask</b>

<dd>
<p>Flags that manage the power throttling mechanism on/off state.</p>
<ul>
<li>PROCESS_POWER_THROTTLING_EXECUTION_SPEED: Manages the execution speed of the process.</li>
</ul>
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
<p>Windows 10, version 1709</p>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddk.h</dt>
</dl>
</td>
</tr>
</table>
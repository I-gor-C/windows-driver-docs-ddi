---
UID: NS.pepfx._PEP_COORDINATED_IDLE_STATE
title: PEP_COORDINATED_IDLE_STATE
author: windows-driver-content
description: The PEP_COORIDNATED_IDLE_STATE structure describes a coordinated idle state to the OS.
old-location: kernel\pep_coordinated_idle_state.htm
ms.assetid: 0B3B53F8-2D1E-430B-9C51-E35465899811
ms.author: windowsdriverdev
ms.date: 11/2/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: kernel
req.header: pepfx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Supported starting with Windows 10.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PEP_COORDINATED_IDLE_STATE
req.alt-loc: pepfx.h
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
ms.keywords: PEP_COORDINATED_IDLE_STATE, PEP_COORDINATED_IDLE_STATE, *PPEP_COORDINATED_IDLE_STATE
req.iface: 
---

# PEP_COORDINATED_IDLE_STATE structure



## -description
<p>The <b>PEP_COORIDNATED_IDLE_STATE</b> structure describes a coordinated idle state to the OS.</p>


## -syntax

````
typedef struct _PEP_COORDINATED_IDLE_STATE {
  ULONG Latency;
  ULONG BreakEvenDuration;
  ULONG DependencyCount;
  ULONG MaximumDependencySize;
} PEP_COORDINATED_IDLE_STATE, *PPEP_COORDINATED_IDLE_STATE;
````


## -struct-fields
<dl>

### -field <b>Latency</b>

<dd>
<p>The latency of waking from this idle state, in 100ns units.</p>
</dd>

### -field <b>BreakEvenDuration</b>

<dd>
<p>Supplies the minimum time the state must be entered to amortize the cost of entering/exiting the state. Idle durations longer than this period should save power when compared to entering a lighter state for the same period.</p>
</dd>

### -field <b>DependencyCount</b>

<dd>
<p>Supplies the number of dependencies this coordinated state has on other coordinated states or on processors.</p>
</dd>

### -field <b>MaximumDependencySize</b>

<dd>
<p>Supplies the maximum size of a single dependency.</p>
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
<p>Supported starting with Windows 10.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Pepfx.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/mt186776">PEP_NOTIFY_PPM_QUERY_COORDINATED_STATES notification</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/0B3B53F8-2D1E-430B-9C51-E35465899811">PEP_COORDINATED_IDLE_STATE structure</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PEP_COORDINATED_IDLE_STATE structure%20 RELEASE:%20(11/2/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

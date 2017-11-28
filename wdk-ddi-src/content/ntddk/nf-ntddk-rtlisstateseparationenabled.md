---
UID: NF.ntddk.RtlIsStateSeparationEnabled
title: RtlIsStateSeparationEnabled
author: windows-driver-content
description: Checks if the SKU for the current context supports multiple sessions.
old-location: kernel\rtlisstateseparationenabled.htm
old-project: kernel
ms.assetid: 7c28a82c-e039-4045-94cd-b47a45d15e28
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: RtlIsStateSeparationEnabled
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntddk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RtlIsStateSeparationEnabled
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe (kernel mode)
req.irql: PASSIVE_LEVEL
req.iface: 
---

# RtlIsStateSeparationEnabled function



## -description
<p>
			
            Checks if the SKU for the current context supports multiple
    sessions.
</p>


## -syntax

````
 BOOLEAN  RtlIsStateSeparationEnabled(
   VOID 
);
````


## -parameters


## -returns
<p> TRUE indicates state separation enabled;

    FALSE otherwise.</p>

<p> TRUE indicates state separation enabled;

    FALSE otherwise.</p>

<p> TRUE indicates state separation enabled;

    FALSE otherwise.</p>

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
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe (kernel mode)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>
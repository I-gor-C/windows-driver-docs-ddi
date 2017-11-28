---
UID: NF.fltkernel.FltRemoveOpenReparseEntry
title: FltRemoveOpenReparseEntry
author: windows-driver-content
description: This routine removes an OPEN_REPARSE_LIST_ENTRY structure (added by FltAddOpenReparseEntry) from a create operation.
old-location: ifsk\fltremoveopenreparseentry.htm
old-project: ifsk
ms.assetid: FD8C3A32-E578-47E9-9B2A-E1809D62F7B8
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltRemoveOpenReparseEntry
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1607
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltAddOpenReparseEntry
req.alt-loc: fltKernel.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _IRQL_requires_max_(APC_LEVEL)
req.iface: 
---

# FltRemoveOpenReparseEntry function



## -description
<p>This routine removes an <a href="..\ntifs\ns-ntifs--open-reparse-list-entry.md">OPEN_REPARSE_LIST_ENTRY</a> structure (added by <a href="https://msdn.microsoft.com/library/windows/hardware/mt734255">FltAddOpenReparseEntry</a>) from a create operation.</p>
<p>
<div class="alert"><b>Important</b>  <i>OpenReparseEntry</i> must be an entry added by <a href="https://msdn.microsoft.com/library/windows/hardware/mt734255">FltAddOpenReparseEntry</a>. All other entries are not valid.</div>
<div> </div>
</p>


## -syntax

````
void FltAddOpenReparseEntry(
  _In_ PFLT_FILTER              Filter,
  _In_ PFLT_CALLBACK_DATA       Data,
  _In_ POPEN_REPARSE_LIST_ENTRY OpenReparseEntry
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>The filter to dereference.</p>
</dd>

### -param <i>Data</i> [in]

<dd>
<p>The create operation to remove open reparse information
                       from.</p>
</dd>

### -param <i>OpenReparseEntry</i> [in]

<dd>
<p>The open reparse information to remove, of type <a href="..\ntifs\ns-ntifs--open-reparse-list-entry.md">OPEN_REPARSE_LIST_ENTRY</a>.</p>
</dd>
</dl>

## -returns
<p>This routine does not return a value.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1607</p>
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
<dt>FltKernel.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>_IRQL_requires_max_(APC_LEVEL)</p>
</td>
</tr>
</table>
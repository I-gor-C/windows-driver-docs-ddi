---
UID: NF.fltkernel.FltFreeOpenReparseList
title: FltFreeOpenReparseList
author: windows-driver-content
description: This routine deallocates any information copied into a create operation by a previous call to FltCopyOpenReparseList.
old-location: ifsk\fltfreeopenreparselist.htm
old-project: ifsk
ms.assetid: 78FA1585-F834-48E4-BB15-78BA5563F9D0
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FltFreeOpenReparseList
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

# FltFreeOpenReparseList function



## -description
<p>This routine deallocates any information copied into a create operation by
    a previous call to <a href="..\fltkernel\nf-fltkernel-fltcopyopenreparselist.md">FltCopyOpenReparseList</a>.  </p>


## -syntax

````
void FltAddOpenReparseEntry(
  _In_ PFLT_FILTER Filter,
  _In_ PECP_LIST   EcpList
);
````


## -parameters
<dl>

### -param Filter [in]

<dd>
<p>The filter to dereference.</p>
</dd>

### -param EcpList [in]

<dd>
<p>The ECP list whose open reparse information should
                       be deallocated.</p>
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
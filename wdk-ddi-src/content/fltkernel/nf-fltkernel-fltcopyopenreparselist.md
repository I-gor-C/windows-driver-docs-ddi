---
UID: NF.fltkernel.FltCopyOpenReparseList
title: FltCopyOpenReparseList
author: windows-driver-content
description: This routine copies any open reparse information from a previous create into a new ECP list that can be used to issue a second create.
old-location: ifsk\fltcopyopenreparselist.htm
old-project: ifsk
ms.assetid: 07C39363-559A-4B55-850E-052BA78E869D
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltCopyOpenReparseList
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

# FltCopyOpenReparseList function



## -description
<p>This routine copies any open reparse information from a previous create into
    a new ECP list that can be used to issue a second create.</p>


## -syntax

````
NTSTATUS FltAddOpenReparseEntry(
  _In_    PFLT_FILTER        Filter,
  _In_    PFLT_CALLBACK_DATA Data,
  _Inout_ PECP_LIST          EcpList
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p>The filter to reference.</p>
</dd>

### -param <i>Data</i> [in]

<dd>
<p>The create operation from which open reparse
                       information should be copied.</p>
</dd>

### -param <i>EcpList</i> [in, out]

<dd>
<p>A new ECP list to copy open reparse information
                       to.</p>
</dd>
</dl>

## -returns
<p>The following NT status codes are returned.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER_2</b></dt>
</dl><p>Status code if <i>Data</i> is not a create operation. This is an error code.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The operation completed successfully.</p>

<p> </p>

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

## -see-also
<dl>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltfreeopenreparselist.md">FltFreeOpenReparseList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltCopyOpenReparseList routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

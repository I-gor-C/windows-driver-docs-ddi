---
UID: NF.fltkernel.FltAddOpenReparseEntry
title: FltAddOpenReparseEntry
author: windows-driver-content
description: This routine adds a caller allocated open reparse structure, OPEN_REPARSE_LIST_ENTRY, into a create operation.
old-location: ifsk\fltaddopenreparseentry.htm
ms.assetid: D58AB46A-0D87-45B5-8C58-E99ED0F906D2
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
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
ms.keywords: FltAddOpenReparseEntry
req.iface: 
---

# FltAddOpenReparseEntry function



## -description
<p>This routine adds a caller allocated open reparse structure, <a href="https://msdn.microsoft.com/A6D28F60-FA38-45EA-9E3C-D2E6F899333E">OPEN_REPARSE_LIST_ENTRY</a>,  into a create operation.</p>


## -syntax

````
NTSTATUS FltAddOpenReparseEntry(
  _In_ PFLT_FILTER              Filter,
  _In_ PFLT_CALLBACK_DATA       Data,
  _In_ POPEN_REPARSE_LIST_ENTRY OpenReparseEntry
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
<p>The create operation to attach open reparse information to.</p>
</dd>

### -param <i>OpenReparseEntry</i> [in]

<dd>
<p>The open reparse information to add, of type <a href="https://msdn.microsoft.com/A6D28F60-FA38-45EA-9E3C-D2E6F899333E">OPEN_REPARSE_LIST_ENTRY</a>.</p>
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
<p>This routine adds an ECP list and/or ECP as needed.  <i>Filter</i> is referenced
    for the lifetime of the open reparse entry structure, not the ECP itself,
    which is conceptually independent of any specific filter.</p>

<p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/mt734261">FltRemoveOpenReparseEntry</a> to remove the open reparse structure from the create operation.</p>

<p>This routine adds an ECP list and/or ECP as needed.  <i>Filter</i> is referenced
    for the lifetime of the open reparse entry structure, not the ECP itself,
    which is conceptually independent of any specific filter.</p>

<p>Use <a href="https://msdn.microsoft.com/library/windows/hardware/mt734261">FltRemoveOpenReparseEntry</a> to remove the open reparse structure from the create operation.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/mt734261">FltRemoveOpenReparseEntry</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltAddOpenReparseEntry routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

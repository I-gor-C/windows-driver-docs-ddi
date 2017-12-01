---
UID: NF.fltkernel.FltRegisterForDataScan
title: FltRegisterForDataScan
author: windows-driver-content
description: The FltRegisterForDataScan routine enables data scanning for the volume attached to the minifilter instance.
old-location: ifsk\fltregisterfordatascan.htm
old-project: ifsk
ms.assetid: E603975A-B927-475A-9DEA-2D01C1249819
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltRegisterForDataScan
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: The FltRegisterForDataScan routine is available starting with   Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltRegisterForDataScan
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: Fltmgr.sys
req.irql: <= APC_LEVEL
req.iface: 
---

# FltRegisterForDataScan function



## -description
<p>The <b>FltRegisterForDataScan</b> routine enables data scanning for the volume attached to the minifilter instance.</p>


## -syntax

````
NTSTATUS FltRegisterForDataScan(
  _In_ PFLT_INSTANCE Instance
);
````


## -parameters
<dl>

### -param <i>Instance</i> [in]

<dd>
<p>An opaque instance pointer for the minifilter driver instance to register for data scanning.</p>
</dd>
</dl>

## -returns
<p><b>FltRegisterForDataScan</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as one of the following. </p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>The filter manager does not support data scans for the volume attached to this instance.</p>

<p> </p>

## -remarks
<p>If <b>STATUS_NOT_SUPPORTED</b> is returned by <b>FltRegisterForDataScan</b>, a minifilter can still create sections for data scanning using <a href="..\ntifs\nf-ntifs-fsrtlcreatesectionfordatascan.md">FsRtlCreateSectionForDataScan</a>. However, section access is not synchronized and conflict resolution is left to the minifilter driver.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>The <b>FltRegisterForDataScan</b> routine is available starting with   Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include Fltkernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>FltMgr.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= APC_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltallocatecontext.md">FltAllocateContext</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltclosesectionfordatascan.md">FltCloseSectionForDataScan</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltcreatesectionfordatascan.md">FltCreateSectionForDataScan</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-fsrtlcreatesectionfordatascan.md">FsRtlCreateSectionForDataScan</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltRegisterForDataScan routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

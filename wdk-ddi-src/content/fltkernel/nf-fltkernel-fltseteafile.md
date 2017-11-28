---
UID: NF.fltkernel.FltSetEaFile
title: FltSetEaFile
author: windows-driver-content
description: FltSetEaFile sets extended-attribute (EA) values for a file.
old-location: ifsk\fltseteafile.htm
old-project: ifsk
ms.assetid: 06427ef2-43e9-46c1-92e5-ab1b6146cc43
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltSetEaFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP3, Windows Server 2003 SP1, and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltSetEaFile
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# FltSetEaFile function



## -description
<p><b>FltSetEaFile</b> sets extended-attribute (EA) values for a file. </p>


## -syntax

````
NTSTATUS FltSetEaFile(
  _In_ PFLT_INSTANCE Instance,
  _In_ PFILE_OBJECT  FileObject,
  _In_ PVOID         EaBuffer,
  _In_ ULONG         Length
);
````


## -parameters
<dl>

### -param <i>Instance</i> [in]

<dd>
<p>Opaque instance pointer for the minifilter driver instance that the SetEa operation is to be sent to. The instance must be attached to the volume where the file resides. </p>
</dd>

### -param <i>FileObject</i> [in]

<dd>
<p>File object pointer for the file. </p>
</dd>

### -param <i>EaBuffer</i> [in]

<dd>
<p>Pointer to a caller-supplied, <a href="https://msdn.microsoft.com/library/windows/hardware/ff545793">FILE_FULL_EA_INFORMATION</a>-structured input buffer that contains the extended attribute (EA) values to be set. </p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Length, in bytes, of the buffer that the <i>EaBuffer</i> parameter points to. </p>
</dd>
</dl>

## -returns
<p><b>FltSetEaFile</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following: </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>The instance or volume is being torn down. This is an error code. </p>

<p> </p>

## -remarks


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
<p>Available in Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP3, Windows Server 2003 SP1, and later versions of the Windows operating system.</p>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545793">FILE_FULL_EA_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543435">FltQueryEaFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548252">IoCheckEaBufferValidity</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltSetEaFile function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

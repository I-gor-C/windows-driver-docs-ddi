---
UID: NF.fltkernel.FltIsDirectory
title: FltIsDirectory
author: windows-driver-content
description: A minifilter driver calls the FltIsDirectory routine to determine whether a given file object represents a directory.
old-location: ifsk\fltisdirectory.htm
ms.assetid: a9343e09-0b7b-4ed8-9b30-63ee0b38d13d
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: This routine is available on Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Microsoft Windows Server 2003 SP1, and later.  Note that this routine is not available on Windows 2000 SP4 or earlier.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltIsDirectory
req.alt-loc: fltmgr.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Fltmgr.lib
req.dll: Fltmgr.sys
req.irql: <= APC_LEVEL
ms.keywords: FltIsDirectory
req.iface: 
---

# FltIsDirectory function



## -description
<p>A minifilter driver calls the <b>FltIsDirectory</b> routine to determine whether a given file object represents a directory. </p>


## -syntax

````
NTSTATUS FltIsDirectory(
  _In_  PFILE_OBJECT  FileObject,
  _In_  PFLT_INSTANCE Instance,
  _Out_ PBOOLEAN      IsDirectory
);
````


## -parameters
<dl>

### -param <i>FileObject</i> [in]

<dd>
<p>Pointer to an already opened file object. </p>
</dd>

### -param <i>Instance</i> [in]

<dd>
<p>Opaque instance pointer for the instance associated with this file object. </p>
</dd>

### -param <i>IsDirectory</i> [out]

<dd>
<p>Pointer to a caller-supplied Boolean variable. On return, this variable receives <b>TRUE</b> if the file object represents a directory, <b>FALSE</b> otherwise. </p>
</dd>
</dl>

## -returns
<p><b>FltIsDirectory</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value, such as the following: </p><dl>
<dt><b>STATUS_NOT_SUPPORTED</b></dt>
</dl><p>This error code is returned if the file system does not support stream contexts.  Note that starting with Windows Vista, <a href="https://msdn.microsoft.com/library/windows/hardware/ff543318">FltIsDirectory</a> will return directory information even for file systems that do not support stream contexts.  </p>

<p> </p>

## -remarks
<p><b>FltIsDirectory</b> retrieves the desired information from the filter manager's internal stream context manager. The filter manager caches this information for future queries on this stream.</p>

<p><b>FltIsDirectory</b> retrieves the desired information from the filter manager's internal stream context manager. The filter manager caches this information for future queries on this stream.</p>

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
<p>This routine is available on Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP2, Microsoft Windows Server 2003 SP1, and later.  Note that this routine is not available on Windows 2000 SP4 or earlier.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Fltkernel.h (include FltKernel.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Fltmgr.lib</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547285">FsRtlSupportsPerStreamContexts</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltIsDirectory routine%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

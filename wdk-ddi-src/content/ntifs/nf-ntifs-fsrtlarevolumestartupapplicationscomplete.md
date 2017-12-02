---
UID: NF.ntifs.FsRtlAreVolumeStartupApplicationsComplete
title: FsRtlAreVolumeStartupApplicationsComplete
author: windows-driver-content
description: The FsRtlAreVolumeStartupApplicationsComplete function determines whether volume startup applications have completed processing.
old-location: ifsk\fsrtlarevolumestartupapplicationscomplete.htm
old-project: ifsk
ms.assetid: a6ee1b04-7f62-452c-92b7-7325278bcd17
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlAreVolumeStartupApplicationsComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Fltkernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Windows Vista and later versions of Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlAreVolumeStartupApplicationsComplete
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: <= APC_LEVEL
req.iface: 
---

# FsRtlAreVolumeStartupApplicationsComplete function



## -description
<p>The <b>FsRtlAreVolumeStartupApplicationsComplete</b> function determines whether volume startup applications have completed processing.</p>


## -syntax

````
BOOLEAN FsRtlAreVolumeStartupApplicationsComplete(void);
````


## -parameters


## -returns
<p><b>FsRtlAreVolumeStartupApplicationsComplete</b> returns <b>TRUE</b> if all volume startup applications for the system have completed their startup processing, <b>FALSE</b> otherwise.</p>

<p><b>FsRtlAreVolumeStartupApplicationsComplete</b> returns <b>TRUE</b> if all volume startup applications for the system have completed their startup processing, <b>FALSE</b> otherwise.</p>

<p><b>FsRtlAreVolumeStartupApplicationsComplete</b> returns <b>TRUE</b> if all volume startup applications for the system have completed their startup processing, <b>FALSE</b> otherwise.</p>

## -remarks
<p>The <b>FsRtlAreVolumeStartupApplicationsComplete</b> function returns <b>TRUE</b> if session manager (Smss.exe) has completed running all startup applications for the system volume(s), <b>FALSE</b> otherwise.</p>

<p>You can use this information to modify the behavior of file system drivers.  For example, a file system driver can adversely affect Autochk.exe if the driver starts its processing before Autochck.exe has fully completed.  If <b>FsRtlAreVolumeStartupApplicationsComplete</b> returns <b>TRUE</b>, Autochk.exe is guaranteed to have fully completed.</p>

<p>To retrieve information about the volume that a minifilter instance is attached to, see <a href="..\fltkernel\nf-fltkernel-fltqueryvolumeinformation.md">FltQueryVolumeInformation</a>. </p>

<p>To retrieve information about the volume associated with a given file, directory, or storage device, see <a href="..\fltkernel\nf-fltkernel-fltqueryvolumeinformation.md">FltQueryVolumeInformation</a>. </p>

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
<p>Available in Windows Vista and later versions of Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Fltkernel.h or Ntifs.h)</dt>
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
<dt>NtosKrnl.exe</dt>
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
<a href="..\fltkernel\nf-fltkernel-fltqueryvolumeinformation.md">FltQueryVolumeInformation</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-zwqueryvolumeinformationfile.md">ZwQueryVolumeInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlAreVolumeStartupApplicationsComplete function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

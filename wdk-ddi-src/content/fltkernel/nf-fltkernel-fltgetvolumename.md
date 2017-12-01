---
UID: NF.fltkernel.FltGetVolumeName
title: FltGetVolumeName
author: windows-driver-content
description: The FltGetVolumeName routine gets the volume name for a given volume.
old-location: ifsk\fltgetvolumename.htm
old-project: ifsk
ms.assetid: 50815b33-d417-4499-9423-f65697396200
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltGetVolumeName
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: FltKernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltGetVolumeName
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

# FltGetVolumeName function



## -description
<p>The <b>FltGetVolumeName</b> routine gets the volume name for a given volume. </p>


## -syntax

````
NTSTATUS FltGetVolumeName(
  _In_        PFLT_VOLUME     Volume,
  _Inout_opt_ PUNICODE_STRING VolumeName,
  _Out_opt_   PULONG          BufferSizeNeeded
);
````


## -parameters
<dl>

### -param <i>Volume</i> [in]

<dd>
<p>An opaque pointer for the volume. </p>
</dd>

### -param <i>VolumeName</i> [in, out, optional]

<dd>
<p>A pointer to a caller-allocated <a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a> structure that contains the volume's non-persistent device object name (for example, "\Device\HarddiskVolume1") when STATUS_SUCCESS is returned.  Be aware that pool for the <b>Buffer</b> member of this structure is caller-allocated also. This parameter is optional and can be <b>NULL</b>. However, <i>VolumeName</i> must be non-<b>NULL</b> if <i>BufferSizeNeeded</i> is <b>NULL</b>.</p>
</dd>

### -param <i>BufferSizeNeeded</i> [out, optional]

<dd>
<p>A pointer to a caller-allocated variable that receives the size, in bytes, of the requested volume name.   If <b>FltGetVolumeName</b> returns STATUS_BUFFER_TOO_SMALL, <i>BufferSizeNeeded</i> receives the size of the buffer (pointed to by the <b>Buffer</b> member of the UNICODE_STRING structure) that is required for this routine to succeed.</p>
<p><i>BufferSizeNeeded</i> is optional and can be <b>NULL</b>. However, <i>BufferSizeNeeded</i> must be non-<b>NULL</b> if <i>VolumeName</i> is <b>NULL</b>.</p>
</dd>
</dl>

## -returns
<p><b>FltGetVolumeName</b> returns one of the following NTSTATUS values:</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The UNICODE_STRING structure, pointed to by <i>VolumeName</i>, contains the name of the volume in the <b>Buffer</b> member for the structure and the length of the name, in bytes, in the <b>Length</b> member.</p><dl>
<dt><b>STATUS_BUFFER_TOO_SMALL</b></dt>
</dl><p>The <b>Buffer</b> member of the UNICODE_STRING structure, pointed to by <i>VolumeName</i>, is too small (as indicated by its <b>MaximumLength</b> member) to contain the entire volume name.  This is an error code.</p><dl>
<dt><b>STATUS_INVALID_PARAMETER</b></dt>
</dl><p><i>VolumeName</i> and <i>BufferSizeNeeded</i> are both <b>NULL</b>. This is an error code. </p>

<p> </p>

## -remarks
<p>For this routine to succeed, the <b>Buffer</b> member of the UNICODE_STRING structure (pointed to by <i>VolumeName</i>) must be large enough, as indicated by its <b>MaximumLength</b> member, to contain the entire volume name string.  The following pseudocode shows one possible method to successfully acquire a volume name:</p>

<p>Allocate <code>VolumeNameSize</code> bytes of pool for <b>Buffer</b> and set <b>MaximumLength</b> to <code>VolumeNameSize</code>.</p>

<p><code>VolumeNameStruct.Buffer</code> contains the Unicode volume name string, which is <code>VolumeNameStruct.Length</code> bytes in length.</p>

<p>To get the volume GUID name for a given volume, call <a href="..\fltkernel\nf-fltkernel-fltgetvolumeguidname.md">FltGetVolumeGuidName</a>. </p>

<p>To get an opaque volume pointer for a volume with a given name, call <a href="..\fltkernel\nf-fltkernel-fltgetvolumefromname.md">FltGetVolumeFromName</a>. </p>

<p>For more information about how to name a volume, see <a href="NULL">Supporting Mount Manager Requests in a Storage Class Driver</a>. </p>

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
<a href="ifsk.filtergetdosname">FilterGetDosName</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetvolumefromname.md">FltGetVolumeFromName</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltgetvolumeguidname.md">FltGetVolumeGuidName</a>
</dt>
<dt>
<a href="..\wudfwdm\ns-wudfwdm--unicode-string.md">UNICODE_STRING</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltGetVolumeName routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

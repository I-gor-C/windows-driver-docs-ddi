---
UID: NF.fltkernel.FltQueryEaFile
title: FltQueryEaFile
author: windows-driver-content
description: FltQueryEaFile returns information about extended-attribute (EA) values for a file.
old-location: ifsk\fltqueryeafile.htm
ms.assetid: 3981ab65-2d21-4188-88dc-04eb7aff0869
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows 2000 Update Rollup 1 for SP4, Windows XP SP3, Windows Server 2003 SP1, and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltQueryEaFile
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
ms.keywords: FltQueryEaFile
req.iface: 
---

# FltQueryEaFile function



## -description
<p><b>FltQueryEaFile</b> returns information about extended-attribute (EA) values for a file. </p>


## -syntax

````
NTSTATUS FltQueryEaFile(
  _In_      PFLT_INSTANCE Instance,
  _In_      PFILE_OBJECT  FileObject,
  _Out_     PVOID         ReturnedEaData,
  _In_      ULONG         Length,
  _In_      BOOLEAN       ReturnSingleEntry,
  _In_opt_  PVOID         EaList,
  _In_      ULONG         EaListLength,
  _In_opt_  PULONG        EaIndex,
  _In_      BOOLEAN       RestartScan,
  _Out_opt_ PULONG        LengthReturned
);
````


## -parameters
<dl>

### -param <i>Instance</i> [in]

<dd>
<p>Opaque instance pointer for the minifilter driver instance that the <i>QueryEa</i> operation is to be sent to. The instance must be attached to the volume where the file resides. </p>
</dd>

### -param <i>FileObject</i> [in]

<dd>
<p>File object pointer for the file. </p>
</dd>

### -param <i>ReturnedEaData</i> [out]

<dd>
<p>Pointer to a caller-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff545793">FILE_FULL_EA_INFORMATION</a>-structured input buffer where the extended attribute values are to be returned. </p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Length, in bytes, of the buffer that the <i>ReturnedEaData</i> parameter points to. </p>
</dd>

### -param <i>ReturnSingleEntry</i> [in]

<dd>
<p>Set to <b>TRUE</b> if <b>FltQueryEaFile</b> should return only the first entry that is found. </p>
</dd>

### -param <i>EaList</i> [in, optional]

<dd>
<p>Pointer to a caller-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff540295">FILE_GET_EA_INFORMATION</a>-structured input buffer specifying the extended attributes to be queried. This parameter is optional and can be <b>NULL</b>. </p>
</dd>

### -param <i>EaListLength</i> [in]

<dd>
<p>Length, in bytes, of the buffer that the <i>EaList</i> parameter points to. </p>
</dd>

### -param <i>EaIndex</i> [in, optional]

<dd>
<p>Index of the entry at which to begin scanning the file's extended-attribute list. This parameter is ignored if the <i>EaList</i> parameter points to a nonempty list. This parameter is optional and can be <b>NULL</b>. </p>
</dd>

### -param <i>RestartScan</i> [in]

<dd>
<p>Set to <b>TRUE</b> if <b>FltQueryEaFile</b> should begin the scan at the first entry in the file's extended-attribute list. If this parameter is not set to <b>TRUE</b>, the scan is resumed from a previous call to <b>FltQueryEaFile</b>. </p>
</dd>

### -param <i>LengthReturned</i> [out, optional]

<dd>
<p>Pointer to a caller-allocated variable that receives the size, in bytes, of the information returned in the <i>ReturnedEaData</i> buffer. This parameter is optional and can be <b>NULL</b>. </p>
</dd>
</dl>

## -returns
<p><b>FltQueryEaFile</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following: </p><dl>
<dt><b>STATUS_EAS_NOT_SUPPORTED</b></dt>
</dl><p>The file system does not support extended attributes. This is an error code. </p><dl>
<dt><b>STATUS_FLT_DELETING_OBJECT</b></dt>
</dl><p>The instance or volume is being torn down. This is an error code. </p><dl>
<dt><b>STATUS_INSUFFICIENT_RESOURCES</b></dt>
</dl><p><b>FltQueryEaFile</b> encountered a pool allocation failure. This is an error code. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540295">FILE_GET_EA_INFORMATION</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff544500">FltSetEaFile</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548252">IoCheckEaBufferValidity</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltQueryEaFile function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

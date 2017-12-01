---
UID: NF.ntifs.ZwSetEaFile
title: ZwSetEaFile
author: windows-driver-content
description: The ZwSetEaFile routine sets extended-attribute (EA) values for a file.
old-location: kernel\zwseteafile.htm
old-project: kernel
ms.assetid: e791900a-06a8-4c8b-8ca8-c4e73d94f609
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: ZwSetEaFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: FltKernel.h, Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows 2000   and later versions of the Windows operating system.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ZwSetEaFile
req.alt-loc: NtosKrnl.exe
req.ddi-compliance: PowerIrpDDis, HwStorPortProhibitedDDIs
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: NtosKrnl.lib
req.dll: NtosKrnl.exe
req.irql: PASSIVE_LEVEL
req.iface: 
---

# ZwSetEaFile function



## -description
<p>The <b>ZwSetEaFile</b> routine sets extended-attribute (EA) values for a file.</p>


## -syntax

````
NTSTATUS ZwSetEaFile(
  _In_  HANDLE           FileHandle,
  _Out_ PIO_STATUS_BLOCK IoStatusBlock,
  _In_  PVOID            Buffer,
  _In_  ULONG            Length
);
````


## -parameters
<dl>

### -param <i>FileHandle</i> [in]

<dd>
<p>The handle for the file on which the operation is to be performed.</p>
</dd>

### -param <i>IoStatusBlock</i> [out]

<dd>
<p>A pointer to an <a href="..\wdm\ns-wdm--io-status-block.md">IO_STATUS_BLOCK</a> structure that receives the final completion status and other information about the requested operation.</p>
</dd>

### -param <i>Buffer</i> [in]

<dd>
<p>A pointer to a caller-supplied, <a href="..\wdm\ns-wdm--file-full-ea-information.md">FILE_FULL_EA_INFORMATION</a>-structured input buffer that contains the extended attribute values to be set. </p>
</dd>

### -param <i>Length</i> [in]

<dd>
<p>Length, in bytes, of the buffer that the <i>Buffer</i> parameter points to.</p>
</dd>
</dl>

## -returns
<p><b>ZwSetEaFile</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following:</p><dl>
<dt>STATUS_EA_LIST_INCONSISTENT</dt>
</dl><p>The EaList parameter is not formatted correctly. This is an error code.</p>

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
<p>Available in Microsoft Windows 2000   and later versions of the Windows operating system.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\ns-wdm--file-full-ea-information.md">FILE_FULL_EA_INFORMATION</a>
</dt>
<dt>
<a href="..\ntifs\nf-ntifs-zwqueryeafile.md">ZwQueryEaFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwSetEaFile routine%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

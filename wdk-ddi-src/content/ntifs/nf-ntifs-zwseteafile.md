---
UID: NF.ntifs.ZwSetEaFile
title: ZwSetEaFile function
author: windows-driver-content
description: The ZwSetEaFile routine sets extended-attribute (EA) values for a file.
old-location: kernel\zwseteafile.htm
old-project: kernel
ms.assetid: e791900a-06a8-4c8b-8ca8-c4e73d94f609
ms.author: windowsdriverdev
ms.date: 12/7/2017
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
---

# ZwSetEaFile function



## -description
The <b>ZwSetEaFile</b> routine sets extended-attribute (EA) values for a file.



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

### -param FileHandle [in]

The handle for the file on which the operation is to be performed.


### -param IoStatusBlock [out]

A pointer to an <a href="kernel.io_status_block">IO_STATUS_BLOCK</a> structure that receives the final completion status and other information about the requested operation.


### -param Buffer [in]

A pointer to a caller-supplied, <a href="kernel.file_full_ea_information">FILE_FULL_EA_INFORMATION</a>-structured input buffer that contains the extended attribute values to be set. 


### -param Length [in]

Length, in bytes, of the buffer that the <i>Buffer</i> parameter points to.


## -returns
<b>ZwSetEaFile</b> returns STATUS_SUCCESS or an appropriate NTSTATUS value such as the following:
<dl>
<dt>STATUS_EA_LIST_INCONSISTENT</dt>
</dl>The EaList parameter is not formatted correctly. This is an error code.

 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available in Microsoft Windows 2000   and later versions of the Windows operating system.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include FltKernel.h or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
DLL

</th>
<td width="70%">
<dl>
<dt>NtosKrnl.exe</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_powerirpddis">PowerIrpDDis</a>, <a href="devtest.storport_hwstorportprohibitedddis">HwStorPortProhibitedDDIs</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.file_full_ea_information">FILE_FULL_EA_INFORMATION</a>
</dt>
<dt>
<a href="kernel.zwqueryeafile">ZwQueryEaFile</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20ZwSetEaFile routine%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


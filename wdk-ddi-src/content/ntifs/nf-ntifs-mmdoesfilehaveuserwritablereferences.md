---
UID: NF.ntifs.MmDoesFileHaveUserWritableReferences
title: MmDoesFileHaveUserWritableReferences function
author: windows-driver-content
description: The MmDoesFileHaveUserWritableReferences function returns the number of writable references for a file object.
old-location: ifsk\mmdoesfilehaveuserwritablereferences.htm
old-project: ifsk
ms.assetid: b88afd6e-3a0a-471e-a874-db8fc3175d61
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: MmDoesFileHaveUserWritableReferences
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
req.alt-api: MmDoesFileHaveUserWritableReferences
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
---

# MmDoesFileHaveUserWritableReferences function



## -description
The <b>MmDoesFileHaveUserWritableReferences </b>function returns the number of writable references for a file object.



## -syntax

````
ULONG MmDoesFileHaveUserWritableReferences(
  _In_ PSECTION_OBJECT_POINTERS SectionPointer
);
````


## -parameters

### -param SectionPointer [in]

Pointer to a <a href="kernel.section_object_pointers">SECTION_OBJECT_POINTERS</a> structure that contains the file object's section object pointers.  This parameter is required and cannot be <b>NULL</b>.


## -returns
<b>MmDoesFileHaveUserWritableReferences </b>returns the number of writable references for the file object associated with the <i>SectionPointer </i>parameter.


## -remarks
<b>MmDoesFileHaveUserWritableReferences</b> returns the number of writable references for the file object that is associated with the <i>SectionPointer </i>parameter.  This return value is the sum of the following numbers:

 The number of writable file handles for the associated file object.

 The number of writable sections for the associated file object.

 The number of writable views for the associated file object.

 The number of outstanding <a href="kernel.mdl">MDL</a>s, which are mapping regions for the associated file object.

For transactional file systems, you can use this function to determine if a given transaction is referencing a file object that can change.  If so, the transaction must be rolled back because <a href="https://msdn.microsoft.com/b558ace9-b416-4572-ac94-58a083c9d33b">atomicity</a> cannot be guaranteed.

Prior to calling <b>MmDoesFileHaveUserWritableReferences</b>, transactional file systems must check and intercept the creation of file objects that specify write access.  Specifically, prior to starting a transaction, transactional file systems must ensure that there are no writable file objects that currently exist for the given file in the transaction.  While the transaction is ongoing, transactional file systems must fail the requests to create file objects with write access for the transacted files.

For more information about transactions, see <a href="https://msdn.microsoft.com/b558ace9-b416-4572-ac94-58a083c9d33b">Kernel Transaction Manager Design Guide</a> and <a href="kernel.kernel_transaction_manager__ktm__routines">Kernel Transaction Manager Routines</a>.

For more information about file objects, see <a href="kernel.file_object">FILE_OBJECT</a>.


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
Available in Windows Vista and later versions of Windows operating systems.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Fltkernel.h or Ntifs.h)</dt>
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
&lt;= APC_LEVEL

</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.file_object">FILE_OBJECT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MmDoesFileHaveUserWritableReferences function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>


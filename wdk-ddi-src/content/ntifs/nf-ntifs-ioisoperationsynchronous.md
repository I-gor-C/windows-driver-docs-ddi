---
UID: NF.ntifs.IoIsOperationSynchronous
title: IoIsOperationSynchronous
author: windows-driver-content
description: The IoIsOperationSynchronous routine determines whether a given IRP represents a synchronous or asynchronous I/O request.
old-location: ifsk\ioisoperationsynchronous.htm
old-project: ifsk
ms.assetid: b233dfab-6a99-4f2f-930e-cafd01dc4bb5
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IoIsOperationSynchronous
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IoIsOperationSynchronous
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
req.irql: Any level
req.iface: 
---

# IoIsOperationSynchronous function



## -description
<p>The <b>IoIsOperationSynchronous</b> routine determines whether a given IRP represents a synchronous or asynchronous I/O request. </p>


## -syntax

````
BOOLEAN IoIsOperationSynchronous(
  _In_ PIRP Irp
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>Pointer to the IRP for the operation. </p>
</dd>
</dl>

## -returns
<p><b>IoIsOperationSynchronous</b> returns <b>TRUE</b> if the operation is synchronous, otherwise <b>FALSE</b>. </p>

## -remarks
<p><b>IoIsOperationSynchronous</b> determines whether a given IRP requests a synchronous or asynchronous I/O operation, according to the following conditions: </p>

<p>If the IRP requests asynchronous paging I/O, the operation is asynchronous, even if one of the other conditions is true. </p>

<p>If the IRP requests synchronous paging I/O, the operation is synchronous. </p>

<p>If the file object was opened for synchronous I/O, the operation is synchronous. </p>

<p>If the IRP_SYNCHRONOUS_API flag is set in the IRP, the operation is synchronous. This flag is set for operations, such as <a href="..\wdm\nf-wdm-zwqueryinformationfile.md">ZwQueryInformationFile</a> and <a href="..\wdm\nf-wdm-zwsetinformationfile.md">ZwSetInformationFile</a>, that are always synchronous, even when performed on a file object that was opened for asynchronous I/O. </p>

<p>If none of the above conditions is true, the operation is asynchronous. </p>

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
<dt>Ntifs.h (include Ntifs.h)</dt>
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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\wdm\nf-wdm-iobuildsynchronousfsdrequest.md">IoBuildSynchronousFsdRequest</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-iocreatefile.md">IoCreateFile</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-iocreatefileex.md">IoCreateFileEx</a>
</dt>
<dt>
<a href="..\ntddk\nf-ntddk-iocreatefilespecifydeviceobjecthint.md">IoCreateFileSpecifyDeviceObjectHint</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--irp.md">IRP</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwcreatefile.md">ZwCreateFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwqueryinformationfile.md">ZwQueryInformationFile</a>
</dt>
<dt>
<a href="..\wdm\nf-wdm-zwsetinformationfile.md">ZwSetInformationFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20IoIsOperationSynchronous routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

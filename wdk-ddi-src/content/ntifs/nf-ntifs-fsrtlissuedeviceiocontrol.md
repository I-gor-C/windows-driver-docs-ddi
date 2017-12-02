---
UID: NF.ntifs.FsRtlIssueDeviceIoControl
title: FsRtlIssueDeviceIoControl
author: windows-driver-content
description: The FsRtlIssueDeviceIoControl routine sends a synchronous device I/O control request to a target device object.
old-location: ifsk\fsrtlissuedeviceiocontrol.htm
old-project: ifsk
ms.assetid: 3BB31389-EB1B-4443-9FCF-70B420D71126
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: FsRtlIssueDeviceIoControl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Universal
req.target-min-winverclnt: Available starting with Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FsRtlIssueDeviceIoControl
req.alt-loc: ntoskrnl.lib,ntoskrnl.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ntoskrnl.lib
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
---

# FsRtlIssueDeviceIoControl function



## -description
<p>The <b>FsRtlIssueDeviceIoControl</b> routine sends a synchronous device I/O control request to a target device object.</p>


## -syntax

````
NTSTATUS FsRtlIssueDeviceIoControl(
  _In_      PDEVICE_OBJECT DeviceObject,
  _In_      ULONG          IoCtl,
  _In_      ULONG          IrpFlags,
  _In_opt_  ULONG          InputBuffer,
  _In_      ULONG          InputBufferLength,
  _Out_opt_ ULONG          OutputBuffer,
  _In_      ULONG          OutputBufferLength,
  _In_      PULONG_PTR     IosbInformation
);
````


## -parameters
<dl>

### -param DeviceObject [in]

<dd>
<p>The target device object.</p>
</dd>

### -param IoCtl [in]

<dd>
<p>The IOCTL control code to issue.</p>
</dd>

### -param IrpFlags [in]

<dd>
<p>The desired IRP flags to set for IOCTL request.</p>
</dd>

### -param InputBuffer [in, optional]

<dd>
<p>An optional buffer containing the input data for the request.</p>
</dd>

### -param InputBufferLength [in]

<dd>
<p>The length, in bytes, of the input data in <i>InputBuffer</i>.</p>
</dd>

### -param OutputBuffer [out, optional]

<dd>
<p>An optional caller-supplied output buffer for returned data.</p>
</dd>

### -param OutputBufferLength [in]

<dd>
<p>The length, in bytes, of the output data buffer at <i>OutputBuffer</i>.</p>
</dd>

### -param IosbInformation [in]

<dd>
<p>A pointer to a <b>ULONG</b> status value to receive the information field value set in the I/O status block at completion of the request.</p>
</dd>
</dl>

## -returns
<p><b>FsRtlIssueDeviceIoControl</b> returns <b>STATUS_SUCCESS</b> or an another <b>NTSTATUS</b> value returned in the status block from the I/O operation.</p>

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
<p>Available starting with Windows 8.</p>
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
<dt>Ntoskrnl.lib</dt>
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
<a href="..\fltkernel\nf-fltkernel-fltdeviceiocontrolfile.md">FltDeviceIoControlFile</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FsRtlIssueDeviceIoControl routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

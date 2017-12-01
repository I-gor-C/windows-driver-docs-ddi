---
UID: NF.mrx.RxFsdDispatch
title: RxFsdDispatch
author: windows-driver-content
description: RxFsdDispatch implements the file system driver (FSD) dispatch for RDBSS to process an I/O request packet (IRP).
old-location: ifsk\rxfsddispatch.htm
old-project: ifsk
ms.assetid: 92b9b22a-0fe7-4c95-a4fc-5f5f5558b4cf
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxFsdDispatch
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: mrx.h
req.include-header: Mrx.h, Rxstruc.h, Struchdr.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxFsdDispatch
req.alt-loc: mrx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
---

# RxFsdDispatch function



## -description
<p><b>RxFsdDispatch</b> implements the file system driver (FSD) dispatch for RDBSS to process an I/O request packet (IRP). A pointer to this routine is copied over the device driver dispatch table for the network mini-redirector driver by the <b>RxDriverEntry</b> routine when RDBSS is initialized. </p>


## -syntax

````
NTSTATUS RxFsdDispatch(
  _In_ PRDBSS_DEVICE_OBJECT RxDeviceObject,
  _In_ PIRP                 Irp
);
````


## -parameters
<dl>

### -param <i>RxDeviceObject</i> [in]

<dd>
<p>A pointer to the RDBSS device object for this network mini-redirector.</p>
</dd>

### -param <i>Irp</i> [in]

<dd>
<p>A pointer to the I/O request packet being processed.</p>
</dd>
</dl>

## -returns
<p><b>RxFsdDispatch</b> returns one of the following values: </p><dl>
<dt><b>STATUS_INVALID_DEVICE_REQUEST</b></dt>
</dl><p>A request was made on an invalid device object. For example, this error is returned if a file system object is passed as the <i>RxDeviceObject</i> parameter. This status value indicates failure.</p><dl>
<dt><b>STATUS_OBJECT_NAME_INVALID</b></dt>
</dl><p>An invalid request was made to create a named pipe or a mailslot (the <b>MajorFunction</b> member of the <i>Irp</i> was IRP_MJ_CREATE_MAILSLOT or IRP_MJ_CREATE_NAMED_PIPE). This status value indicates failure.</p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>An asynchronous request was made and the status of the request is pending.</p><dl>
<dt><b>STATUS_SUCCESS</b></dt>
</dl><p>The <b>RxFsdDispatch</b> routine call was successful.</p>

<p> </p>

## -remarks
<p><b>RxFsdDispatch</b> is called by RDBSS to process an I/O request packet (IRP). These IRPs are normally received by RDBSS in response to a user-mode application requesting operations on a file. It is also possible for another kernel driver to issue such an IRP. </p>

<p>A pointer to <b>RxFsdDispatch</b> routine is copied over the driver dispatch table for a network mini-redirector driver when the <b>RxDriverEntry</b> routine is called to initialize RDBSS. </p>

<p>Internally, RDBSS maintains two dispatch vectors:</p>

<p>A common dispatch vector for most operations.</p>

<p>A private dispatch vector for file device FCB operations.</p>

<p>If the IRP is an IRP_MJ_CREATE request, then <b>RxFsdDispatch</b> will use a common dispatch vector. If the IRP is for an operation on an FCB of a file object, <b>RxFsdDispatch</b> will check if a private dispatch vector should be used. Otherwise a common dispatch vector will be used to process the IRP. </p>

<p><b>RxFsdDispatch</b> calls internal routines to process the standard IRPs most of which result in a call to one of the callback routines implemented by the network mini-redirector driver. </p>

<p>A few IRPs are treated as special and handled internally by RDBSS. For example, the IRP_MJ_SYSTEM_CONTROL is used internally if WMI is enabled. IRP_MJ_CREATE_MAILSLOT or IRP_MJ_CREATE_NAMED_PIPE requests are treated specially and rejected (a STATUS_OBJECT_NAME_INVALID error is returned). </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Mrx.h (include Mrx.h, Rxstruc.h, or Struchdr.h)</dt>
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
<a href="..\rxprocs\nf-rxprocs-rxdriverentry.md">RxDriverEntry</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxFsdDispatch routine%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.fltkernel.FltCurrentBatchOplock
title: FltCurrentBatchOplock
author: windows-driver-content
description: A minifilter driver calls FltCurrentBatchOplock to determine whether there are any batch or filter opportunistic locks (oplocks) on a file.
old-location: ifsk\fltcurrentbatchoplock.htm
old-project: ifsk
ms.assetid: 00eb27ee-2c6d-47c7-b3a6-63a6a7aac2fb
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: FltCurrentBatchOplock
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fltkernel.h
req.include-header: Fltkernel.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FltCurrentBatchOplock
req.alt-loc: FltMgr.lib,FltMgr.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: FltMgr.lib
req.dll: 
req.irql: <= APC_LEVEL
req.iface: 
---

# FltCurrentBatchOplock function



## -description
<p>A minifilter driver calls <b>FltCurrentBatchOplock</b> to determine whether there are any batch or filter opportunistic locks (oplocks) on a file. </p>


## -syntax

````
BOOLEAN FltCurrentBatchOplock(
  _In_ POPLOCK Oplock
);
````


## -parameters
<dl>

### -param <i>Oplock</i> [in]

<dd>
<p>Opaque oplock pointer for the file. This pointer must have been initialized by a previous call to <a href="..\fltkernel\nf-fltkernel-fltinitializeoplock.md">FltInitializeOplock</a>. </p>
</dd>
</dl>

## -returns
<p><b>FltCurrentBatchOplock</b> returns <b>TRUE</b> if there are current outstanding batch or filter oplocks; <b>FALSE</b> otherwise. </p>

## -remarks
<p><b>FltCurrentBatchOplock</b> returns <b>FALSE</b> if no batch or filter opportunistic locks are currently held. </p>

<p>For detailed information about opportunistic locks, see the Microsoft Windows SDK documentation. </p>

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
<a href="..\fltkernel\nf-fltkernel-fltcheckoplock.md">FltCheckOplock</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltinitializeoplock.md">FltInitializeOplock</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltoplockfsctrl.md">FltOplockFsctrl</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltoplockisfastiopossible.md">FltOplockIsFastIoPossible</a>
</dt>
<dt>
<a href="..\fltkernel\nf-fltkernel-fltuninitializeoplock.md">FltUninitializeOplock</a>
</dt>
<dt>
<a href="ifsk.fsctl_opbatch_ack_close_pending">FSCTL_OPBATCH_ACK_CLOSE_PENDING</a>
</dt>
<dt>
<a href="ifsk.fsctl_oplock_break_ack_no_2">FSCTL_OPLOCK_BREAK_ACK_NO_2</a>
</dt>
<dt>
<a href="ifsk.fsctl_oplock_break_acknowledge">FSCTL_OPLOCK_BREAK_ACKNOWLEDGE</a>
</dt>
<dt>
<a href="ifsk.fsctl_oplock_break_notify">FSCTL_OPLOCK_BREAK_NOTIFY</a>
</dt>
<dt>
<a href="ifsk.fsctl_request_batch_oplock">FSCTL_REQUEST_BATCH_OPLOCK</a>
</dt>
<dt>
<a href="ifsk.fsctl_request_filter_oplock">FSCTL_REQUEST_FILTER_OPLOCK</a>
</dt>
<dt>
<a href="ifsk.fsctl_request_oplock_level_1">FSCTL_REQUEST_OPLOCK_LEVEL_1</a>
</dt>
<dt>
<a href="ifsk.fsctl_request_oplock_level_2">FSCTL_REQUEST_OPLOCK_LEVEL_2</a>
</dt>
<dt>
<a href="ifsk.fsrtlcurrentbatchoplock">FsRtlCurrentBatchOplock</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20FltCurrentBatchOplock function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NF.mrx.RxStopMinirdr
title: RxStopMinirdr
author: windows-driver-content
description: RxStopMinirdr is called to stop a network mini-redirector that has previously been started.
old-location: ifsk\rxstopminirdr.htm
old-project: ifsk
ms.assetid: 059d2a99-f4da-45f1-8d91-0e57930595d2
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxStopMinirdr
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: mrx.h
req.include-header: Mrx.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxStopMinirdr
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

# RxStopMinirdr function



## -description
<p><b>RxStopMinirdr</b> is called to stop a network mini-redirector that has previously been started. As part of <b>RxStopMinirdr</b>, RDBSS will also de-register the network mini-redirector driver as a universal naming convention (UNC) provider with the Multiple UNC Provider (MUP) if the driver indicates support for UNC names.</p>


## -syntax

````
NTSTATUS RxStopMinirdr(
  _In_  PRX_CONTEXT RxContext,
  _Out_ PBOOLEAN    PostToFsp
);
````


## -parameters
<dl>

### -param <i>RxContext</i> [in]

<dd>
<p>A pointer to the RX_CONTEXT structure to use to get the device object and determine if this is a file system process. </p>
</dd>

### -param <i>PostToFsp</i> [out]

<dd>
<p>A pointer to a logical value that is set to <b>TRUE</b> on return if the request must be posted for later processing by the file system process. </p>
</dd>
</dl>

## -returns
<p><b>RxStopMinirdr</b> returns STATUS_SUCCESS if the stop sequence was successful or one of the following error values: </p><dl>
<dt><b>STATUS_PENDING</b></dt>
</dl><p>The stop sequence for RDBSS and network mini-redirectors must be completed in the context of the file system process. If the call to <b>RxStopMinirdr</b> comes from a different process (a user-mode request, for example), then the request will be posted for later processing and STATUS_PENDING will be returned. This error can also be returned if certain internal RDBSS locks cannot be acquired without waiting.</p><dl>
<dt><b>STATUS_REDIRECTOR_HAS_OPEN_HANDLES</b></dt>
</dl><p>The network mini-redirector has open handles and cannot be stopped at this time. </p><dl>
<dt><b>STATUS_REDIRECTOR_STOPPED</b></dt>
</dl><p>The network mini-redirector was already stopped. </p>

<p> </p>

## -remarks
<p>When a stop request is issued to RDBSS, there may be ongoing requests in the RDBSS. Some of the requests can be canceled while the remaining requests need to be processed to completion.</p>

<p>There are a number of strategies that can be employed to close down the RDBSS. Currently, the most conservative approach is employed. The cancellation of those operations that can be canceled and the stop operation is held back until the remaining requests run through to completion.</p>

<p>The RDBSS <b>RxStopMinirdr </b>is usually called as a result of an FSCTL or IOCTL request from a user-mode application or service to stop the network mini-redirector, although this call could also be made from the network mini-redirector or as part of shutdown processing by the operating system. </p>

<p>Once a call to <b>RxStopMinirdr</b> is issued, the only operations allowed by RDBSS and passed to the network mini-redirector are rerquests for the following I/O request packets:</p>

<p>IRP_MJ_CLEANUP</p>

<p>IRP_MJ_CLOSE</p>

<p>The stop sequence for RDBSS and the network mini-redirector must be completed in the context of the file system process. If the call to <b>RxStopMinirdr</b> comes from a different process (a user-mode request, for example), then the request must be posted for later processing and STATUS_PENDING will be returned. In this case, the effective user ID (the logon ID) of the caller is saved in the <b>FsdUid</b> member of the <i>RxContext</i> parameter. In addition, If certain internal RDBSS locks cannot be obtained without waiting, STATUS_PENDING is returned and <i>PostToFsp</i> is set to <b>TRUE</b>. When STATUS_PENDING is returned, then <b>RxStopMinirdr</b> will be posted for later processing by a file system process and completed. </p>

<p>If a network mini-redirector indicates support for UNC when registering with RDBSS (the <i>Controls</i> parameter to <b>RxRegisterMinirdr</b>), then <b>RxStopMinirdr</b> will try to de-register the <i>DeviceName</i> of the network mini-redirector as a UNC provider with MUP (calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545865">FsRtlDeregisterUncProvider</a> on behalf of the network mini-redirector). <b>RxStopMinirdr</b> also de-registers the file system with the I/O manager (calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548552">IoUnregisterFileSystem</a>) on behalf of the network mini-redirector).</p>

<p>The <b>RxStopMinirdr</b> routine then calls the network mini-redirector <b>MrxStop</b> callback routine if this routine is implemented. If there are no active FCBs remaining, STATUS_SUCCESS is returned. If there are some remaining active FCBs, STATUS_REDIRECTOR_HAS_OPEN_HANDLES is returned. In either case, the RDBSS dispatcher for the redrector is spun down and the internal state of the network mini-redirector in RDBSS is set to RDBSS_STARTABLE. </p>

<p>When a stop request is issued to RDBSS, there may be ongoing requests in the RDBSS. Some of the requests can be canceled while the remaining requests need to be processed to completion.</p>

<p>There are a number of strategies that can be employed to close down the RDBSS. Currently, the most conservative approach is employed. The cancellation of those operations that can be canceled and the stop operation is held back until the remaining requests run through to completion.</p>

<p>The RDBSS <b>RxStopMinirdr </b>is usually called as a result of an FSCTL or IOCTL request from a user-mode application or service to stop the network mini-redirector, although this call could also be made from the network mini-redirector or as part of shutdown processing by the operating system. </p>

<p>Once a call to <b>RxStopMinirdr</b> is issued, the only operations allowed by RDBSS and passed to the network mini-redirector are rerquests for the following I/O request packets:</p>

<p>IRP_MJ_CLEANUP</p>

<p>IRP_MJ_CLOSE</p>

<p>The stop sequence for RDBSS and the network mini-redirector must be completed in the context of the file system process. If the call to <b>RxStopMinirdr</b> comes from a different process (a user-mode request, for example), then the request must be posted for later processing and STATUS_PENDING will be returned. In this case, the effective user ID (the logon ID) of the caller is saved in the <b>FsdUid</b> member of the <i>RxContext</i> parameter. In addition, If certain internal RDBSS locks cannot be obtained without waiting, STATUS_PENDING is returned and <i>PostToFsp</i> is set to <b>TRUE</b>. When STATUS_PENDING is returned, then <b>RxStopMinirdr</b> will be posted for later processing by a file system process and completed. </p>

<p>If a network mini-redirector indicates support for UNC when registering with RDBSS (the <i>Controls</i> parameter to <b>RxRegisterMinirdr</b>), then <b>RxStopMinirdr</b> will try to de-register the <i>DeviceName</i> of the network mini-redirector as a UNC provider with MUP (calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff545865">FsRtlDeregisterUncProvider</a> on behalf of the network mini-redirector). <b>RxStopMinirdr</b> also de-registers the file system with the I/O manager (calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff548552">IoUnregisterFileSystem</a>) on behalf of the network mini-redirector).</p>

<p>The <b>RxStopMinirdr</b> routine then calls the network mini-redirector <b>MrxStop</b> callback routine if this routine is implemented. If there are no active FCBs remaining, STATUS_SUCCESS is returned. If there are some remaining active FCBs, STATUS_REDIRECTOR_HAS_OPEN_HANDLES is returned. In either case, the RDBSS dispatcher for the redrector is spun down and the internal state of the network mini-redirector in RDBSS is set to RDBSS_STARTABLE. </p>

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
<dt>Mrx.h (include Mrx.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545865">FsRtlDeregisterUncProvider</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548552">IoUnregisterFileSystem</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554693">RxRegisterMinirdr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554736">RxStartMiniRdr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554662">RxpUnregisterMinirdr</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554744">RxUnregisterMinirdr</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxStopMinirdr function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

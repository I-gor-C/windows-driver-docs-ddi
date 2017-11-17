---
UID: NF.rxprocs.RxChangeBufferingState
title: RxChangeBufferingState
author: windows-driver-content
description: RxChangeBufferingState is called to process a buffering state change request.
old-location: ifsk\rxchangebufferingstate.htm
ms.assetid: 83e181cd-bbec-4142-8d97-4f67285b6bb4
ms.author: windowsdriverdev
ms.date: 10/26/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: ifsk
req.header: rxprocs.h
req.include-header: Rxprocs.h, Struchdr.h, Fcb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxChangeBufferingState
req.alt-loc: rxprocs.h
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
ms.keywords: RxChangeBufferingState
req.iface: 
req.product: Windows 10 or later.
---

# RxChangeBufferingState function



## -description
<p><b>RxChangeBufferingState</b> is called to process a buffering state change request.</p>


## -syntax

````
NTSTATUS RxChangeBufferingState(
   PSRV_OPEN SrvOpen,
   PVOID     Context,
   BOOLEAN   ComputeNewState
);
````


## -parameters
<dl>

### -param <i>SrvOpen</i> 

<dd>
<p>A pointer to the SRV_OPEN data structure to be changed.</p>
</dd>

### -param <i>Context</i> 

<dd>
<p>A pointer to the context parameter for use by the network mini-redirector callback. </p>
</dd>

### -param <i>ComputeNewState</i> 

<dd>
<p>The value that indicates if the new buffering state is to be computed. When this value is set to <b>TRUE</b>, the new buffering state is determined by calling the network mini-redirector to compute the new buffering state. When this value is <b>FALSE</b>, the new buffering state is determined by the <i>BufferingFlags</i> member of the passed in <i>SrvOpen</i> structure.</p>
</dd>
</dl>

## -returns
<p><b>RxChangeBufferingState</b> always returns STATUS_SUCCESS whether this routine was successful or if an error occurs. If an error occurs, the buffering state is changed so that no buffering is enabled.</p>

## -remarks
<p>If local buffering is disabled for this FCB (FCB_STATE_DISABLE_LOCAL_BUFFERING is set in the FcbState structure member of the FCB), this will disable local buffering independent of the open mode on the FCB and any default buffering options. When FCB_STATE_DISABLE_LOCAL_BUFFERING is set, the new buffering state set by <b>RxChangeBufferingState</b> will be to disable all buffering.</p>

<p>If <i>ComputeNewState</i> is <b>TRUE</b>, then the <b>MRxComputeNewBufferingState</b> routine exported by the network mini-redirector is called to compute the new buffering state to use.</p>

<p>If the FCB is acquired exclusively and <i>ComputeNewState</i> is <b>FALSE</b>. then <b>RxChangeBufferingState</b> will set the following buffering state options:</p>

<p>FCB_STATE_WRITECACHING_ENABLED</p>

<p>FCB_STATE_FILESIZECACHEING_ENABLED</p>

<p>FCB_STATE_FILETIMECACHEING_ENABLED</p>

<p>FCB_STATE_WRITEBUFFERING_ENABLED</p>

<p>FCB_STATE_LOCK_BUFFERING_ENABLED</p>

<p>FCB_STATE_READBUFFERING_ENABLED</p>

<p>FCB_STATE_READCACHING_ENABLED</p>

<p>To acquire the FCB exclusively requires that the FCB must not be opened with any of the following values:</p>

<p>ShareAccess.SharedRead</p>

<p>ShareAccess.SharedWrite</p>

<p>ShareAccess.SharedDelete</p>

<p>RDBSS does not currently use a number of possible buffering options, so these options are ignored internally by RDBSS when they are set off using <b>RxChangeBufferingState</b>. These ignored buffering options include the following:</p>

<p>FCB_STATE_WRITEBUFFERING_ENABLED</p>

<p>FCB_STATE_READBUFFERING_ENABLED</p>

<p>FCB_STATE_OPENSHARING_ENABLED</p>

<p>FCB_STATE_COLLAPSING_ENABLED</p>

<p>FCB_STATE_FILESIZECACHEING_ENABLED</p>

<p>FCB_STATE_FILETIMECACHEING_ENABLED</p>

<p>If the FCB_STATE_WRITECACHING_ENABLED buffering state is changed to off, any FCB in the system cache is flushed. </p>

<p>On exit from <b>RxChangeBufferingState</b>, there is no change in resource ownership. </p>

<p>If local buffering is disabled for this FCB (FCB_STATE_DISABLE_LOCAL_BUFFERING is set in the FcbState structure member of the FCB), this will disable local buffering independent of the open mode on the FCB and any default buffering options. When FCB_STATE_DISABLE_LOCAL_BUFFERING is set, the new buffering state set by <b>RxChangeBufferingState</b> will be to disable all buffering.</p>

<p>If <i>ComputeNewState</i> is <b>TRUE</b>, then the <b>MRxComputeNewBufferingState</b> routine exported by the network mini-redirector is called to compute the new buffering state to use.</p>

<p>If the FCB is acquired exclusively and <i>ComputeNewState</i> is <b>FALSE</b>. then <b>RxChangeBufferingState</b> will set the following buffering state options:</p>

<p>FCB_STATE_WRITECACHING_ENABLED</p>

<p>FCB_STATE_FILESIZECACHEING_ENABLED</p>

<p>FCB_STATE_FILETIMECACHEING_ENABLED</p>

<p>FCB_STATE_WRITEBUFFERING_ENABLED</p>

<p>FCB_STATE_LOCK_BUFFERING_ENABLED</p>

<p>FCB_STATE_READBUFFERING_ENABLED</p>

<p>FCB_STATE_READCACHING_ENABLED</p>

<p>To acquire the FCB exclusively requires that the FCB must not be opened with any of the following values:</p>

<p>ShareAccess.SharedRead</p>

<p>ShareAccess.SharedWrite</p>

<p>ShareAccess.SharedDelete</p>

<p>RDBSS does not currently use a number of possible buffering options, so these options are ignored internally by RDBSS when they are set off using <b>RxChangeBufferingState</b>. These ignored buffering options include the following:</p>

<p>FCB_STATE_WRITEBUFFERING_ENABLED</p>

<p>FCB_STATE_READBUFFERING_ENABLED</p>

<p>FCB_STATE_OPENSHARING_ENABLED</p>

<p>FCB_STATE_COLLAPSING_ENABLED</p>

<p>FCB_STATE_FILESIZECACHEING_ENABLED</p>

<p>FCB_STATE_FILETIMECACHEING_ENABLED</p>

<p>If the FCB_STATE_WRITECACHING_ENABLED buffering state is changed to off, any FCB in the system cache is flushed. </p>

<p>On exit from <b>RxChangeBufferingState</b>, there is no change in resource ownership. </p>

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
<dt>Rxprocs.h (include Rxprocs.h, Struchdr.h, or Fcb.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554485">RxIndicateChangeOfBufferingState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554490">RxIndicateChangeOfBufferingStateForSrvOpen</a>
</dt>
<dt>
<a href="ifsk.the_srv_open_structure">The SRV_OPEN Structure</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxChangeBufferingState function%20 RELEASE:%20(10/26/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

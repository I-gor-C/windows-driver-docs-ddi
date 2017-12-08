---
UID: NC.mrx.PMRX_CALLDOWN_CTX
title: PMRX_CALLDOWN_CTX
author: windows-driver-content
description: TheMRxStart routine is called by RDBSS to start the network mini-redirector.
old-location: ifsk\mrxstart.htm
old-project: ifsk
ms.assetid: b5985fc4-dd1a-455d-b2ad-3dc2dfec2e6e
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: SetDSMCounters_IN, SetDSMCounters_IN, *PSetDSMCounters_IN
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: mrx.h
req.include-header: Mrx.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MRxStart
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
req.irql: 
req.iface: 
---

# PMRX_CALLDOWN_CTX callback



## -description
<p>The<i>MRxStart</i> routine is called by <a href="ifsk.the_rdbss_driver_and_library">RDBSS</a> to start the network mini-redirector.</p>


## -prototype

````
PMRX_CALLDOWN_CTX MRxStart;

NTSTATUS MRxStart(
  _Inout_ PRX_CONTEXT          RxContext,
  _Inout_ PRDBSS_DEVICE_OBJECT RxDeviceObject
)
{ ... }
````


## -parameters
<dl>

### -param RxContext [in, out]

<dd>
<p>A pointer to the RX_CONTEXT structure. This parameter contains the IRP that requested the network mini-redirector to start. </p>
</dd>

### -param RxDeviceObject [in, out]

<dd>
<p>A pointer to the RDBSS_DEVICE_OBJECT structure for this network mini-redirector. </p>
</dd>
</dl>

## -returns
<p><i>MRxStart</i> returns STATUS_SUCCESS on success or an appropriate NTSTATUS value, such as one of the following: </p><dl>
<dt><b>STATUS_REDIRECTOR_STARTED</b></dt>
</dl><p>The network mini-redirector was already started.</p><dl>
<dt><b>STATUS_UNSUCCESSFUL</b></dt>
</dl><p>The network mini-redirector was unable to start successfully.</p>

<p> </p>

## -remarks
<p><i>MRxStart</i> completes the initialization of the network mini-redirector from the RDBSS perspective. Note that this is different from the initialization done in the <b>DriverEntry</b> routine. Any initialization that depends on RDBSS should be done as part of this routine while the initialization that is independent of RDBSS should be done in the <b>DriverEntry</b> routine.</p>

<p>Before calling <i>MRxStart</i>, RDBSS modifies the following members in the RX_CONTEXT structure pointed to by the <i>RxContext</i> parameter:</p>

<p>The <b>MajorFunction</b> member is set to the major function of the IRP. </p>

<p>The <b>LowIoContext.ParamsFor.FsCtl.FsControlCode</b> member is set to the FSCTL code for the IRP if this was an FSTCL request used to start the network mini-redirector. </p>

<p><i>MRxStart</i> is called by RDBSS from the <a href="..\mrx\nf-mrx-rxstartminirdr.md">RxStartMinirdr</a> routine. Before calling <i>MRxStart</i>, RDBSS will register <i>RxDeviceObject</i> of the network mini-redirector as a file system. RDBSS will also register the network mini-redirector as a UNC provider if the network mini-redirector indicates support for UNC names.</p>

<p>If <i>MRxStart</i> returns STATUS_SUCCESS, then the routine was successful. Any other return value indicates that an error occurred in the startup sequence. </p>

<p>If <i>MRxStart</i> returns STATUS_SUCCESS, RDBSS sets the state of RDBSS to RDBSS_STARTED. This state is stored in the <b>StartStopContext.State</b> member of the RDBSS_DEVICE_OBJECT structure pointed to by <i>RxDeviceObject</i>.</p>

<p>A network mini-redirector would normally maintain an internal variable indicating whether the network mini-redirector is started. For example, a network mini-redirector might track when it is stopped, started, and when a start operation or stop operation is in progress. </p>

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
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.mrxdevfcbxxxcontrolfile">MRxDevFcbXXXControlFile</a>
</dt>
<dt>
<a href="ifsk.mrxstop">MRxStop</a>
</dt>
<dt>
<a href="..\mrx\nf-mrx-rxstartminirdr.md">RxStartMinirdr</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20MRxStart routine%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

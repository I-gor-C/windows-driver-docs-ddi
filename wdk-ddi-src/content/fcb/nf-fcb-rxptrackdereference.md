---
UID: NF.fcb.RxpTrackDereference
title: RxpTrackDereference
author: windows-driver-content
description: RxpTrackDereference is used in checked builds to track requests to dereference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures in checked builds. A log of these dereference requests can be accessed by the logging system and WMI.
old-location: ifsk\rxptrackdereference.htm
old-project: ifsk
ms.assetid: eaff92d2-d866-4096-8528-0672255ced60
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: RxpTrackDereference
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: fcb.h
req.include-header: Fcb.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: RxpTrackDereference
req.alt-loc: fcb.h
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

# RxpTrackDereference function



## -description
<p><b>RxpTrackDereference</b> is used in checked builds to track requests to dereference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures in checked builds. A log of these dereference requests can be accessed by the logging system and WMI. </p>


## -syntax

````
BOOLEAN RxpTrackDereference(
  _In_ ULONG TraceType,
  _In_ PCSTR FileName,
  _In_ ULONG Line,
  _In_ PVOID pInstance
);
````


## -parameters
<dl>

### -param <i>TraceType</i> [in]

<dd>
<p>The value that determines which dereference request type is tracked. This value can be one of the following macros defined in <i>fcb.h</i>:</p>
<p></p>
<dl>

### -param <a id="RDBSS_REF_TRACK_SRVCALL"></a><a id="rdbss_ref_track_srvcall"></a>RDBSS_REF_TRACK_SRVCALL

<dd>
<p>A dereference request on a SRV_CALL structure.</p>
</dd>

### -param <a id="RDBSS_REF_TRACK_NETROOT"></a><a id="rdbss_ref_track_netroot"></a>RDBSS_REF_TRACK_NETROOT

<dd>
<p>A dereference request on a NET_ROOT structure.</p>
</dd>

### -param <a id="RDBSS_REF_TRACK_VNETROOT"></a><a id="rdbss_ref_track_vnetroot"></a>RDBSS_REF_TRACK_VNETROOT

<dd>
<p>A dereference request on a V_NET_ROOT structure.</p>
</dd>

### -param <a id="RDBSS_REF_TRACK_NETFOBX"></a><a id="rdbss_ref_track_netfobx"></a>RDBSS_REF_TRACK_NETFOBX

<dd>
<p>A dereference request on an FOBX structure.</p>
</dd>

### -param <a id="RDBSS_REF_TRACK_NETFCB"></a><a id="rdbss_ref_track_netfcb"></a>RDBSS_REF_TRACK_NETFCB

<dd>
<p>A dereference request on an FCB structure.</p>
</dd>

### -param <a id="RDBSS_REF_TRACK_SRVOPEN"></a><a id="rdbss_ref_track_srvopen"></a>RDBSS_REF_TRACK_SRVOPEN

<dd>
<p>A dereference request on a SRV_OPEN structure.</p>
</dd>
</dl>
</dd>

### -param <i>FileName</i> [in]

<dd>
<p>The name of the source file where this routine was called.</p>
</dd>

### -param <i>Line</i> [in]

<dd>
<p>The line number in the source file where this routine was called.</p>
</dd>

### -param <i>pInstance</i> [in]

<dd>
<p>A pointer to the structure to be dereferenced.</p>
</dd>
</dl>

## -returns
<p><b>RxpTrackDereference</b> always returns <b>TRUE</b> on checked builds. </p>

## -remarks
<p>In checked builds, <b>RxpTrackDereference</b> is used to track requests to dereference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures. For retail builds, this function does nothing.</p>

<p>If WMI is enabled, a log of the dereference requests is sent as a WMI event to user-mode WMI components that have requested notification. The deference request is also logged to the RDBSS logging system by calling the <b>_RxLog</b> routine to record an I/O error log entry if logging is enabled. </p>

<p>Note that this routine does not actually dereference the structure passed (decrement the reference count on the structure).</p>

<p>A number of macros are defined in <i>fcb.h</i> for debugging that are the preferred way to call this routine. These macros provide a wrapper around the <b>RxReference</b> or <b>RxDereference</b> routines used for file structure management operations on SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures. These macros first call the corresponding <b>RxpTrackDereference</b> routine to log diagnostic information about the request before calling the corresponding <b>RxDereference</b> routine.</p>

<p>In checked builds, <b>RxpTrackDereference</b> is used to track requests to dereference SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures. For retail builds, this function does nothing.</p>

<p>If WMI is enabled, a log of the dereference requests is sent as a WMI event to user-mode WMI components that have requested notification. The deference request is also logged to the RDBSS logging system by calling the <b>_RxLog</b> routine to record an I/O error log entry if logging is enabled. </p>

<p>Note that this routine does not actually dereference the structure passed (decrement the reference count on the structure).</p>

<p>A number of macros are defined in <i>fcb.h</i> for debugging that are the preferred way to call this routine. These macros provide a wrapper around the <b>RxReference</b> or <b>RxDereference</b> routines used for file structure management operations on SRV_CALL, NET_ROOT, V_NET_ROOT, FOBX, FCB, and SRV_OPEN structures. These macros first call the corresponding <b>RxpTrackDereference</b> routine to log diagnostic information about the request before calling the corresponding <b>RxDereference</b> routine.</p>

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
<dt>Fcb.h (include Fcb.h)</dt>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff553384">RxAssert</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554385">RxDbgBreakPoint</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554388">RxDereference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554688">RxReference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff554659">RxpTrackReference</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff557368">_RxLog</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20RxpTrackDereference function%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

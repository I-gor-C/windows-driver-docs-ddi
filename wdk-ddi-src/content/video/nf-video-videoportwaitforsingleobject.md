---
UID: NF.video.VideoPortWaitForSingleObject
title: VideoPortWaitForSingleObject
author: windows-driver-content
description: The VideoPortWaitForSingleObject function puts the current thread into a wait state until the given dispatch object is set to the signaled state, or (optionally) until the wait times out.
old-location: display\videoportwaitforsingleobject.htm
old-project: display
ms.assetid: 574aa79e-c8ef-44de-8d0b-a550698a32e0
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: VideoPortWaitForSingleObject
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: video.h
req.include-header: Video.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Windows XP and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: VideoPortWaitForSingleObject
req.alt-loc: Videoprt.sys
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Videoprt.lib
req.dll: Videoprt.sys
req.irql: <= DISPATCH_LEVEL (see Remarks section)
req.iface: 
req.product: Windows 10 or later.
---

# VideoPortWaitForSingleObject function



## -description
<p>The <b>VideoPortWaitForSingleObject</b> function puts the current thread into a wait state until the given dispatch object is set to the signaled state, or (optionally) until the wait times out.</p>


## -syntax

````
VP_STATUS VideoPortWaitForSingleObject(
  _In_ PVOID          HwDeviceExtension,
  _In_ PVOID          Object,
  _In_ PLARGE_INTEGER Timeout
);
````


## -parameters
<dl>

### -param <i>HwDeviceExtension</i> [in]

<dd>
<p>Pointer to the miniport driver's device extension.</p>
</dd>

### -param <i>Object</i> [in]

<dd>
<p>Pointer to the event object.</p>
</dd>

### -param <i>Timeout</i> [in]

<dd>
<p>(Optional) Pointer to a time-out value that specifies the absolute or relative time at which the wait is to be completed. A negative value specifies a wait interval relative to the current time. The value should be expressed in units of 100 nanoseconds. Absolute expiration times track any changes in the system time; relative expiration times are not affected by system time changes.</p>
</dd>
</dl>

## -returns
<p><b>VideoPortWaitForSingleObject</b> returns one of the following values:</p><dl>
<dt><b>ERROR_INVALID_PARAMETER</b></dt>
</dl><p>One of the parameters is invalid or the call attempted to wait for a mapped user event.</p><dl>
<dt><b>NO_ERROR</b></dt>
</dl><p>The event object specified in the <i>pObject</i> parameter satisfied the wait.</p><dl>
<dt><b>WAIT_TIMEOUT</b></dt>
</dl><p>A time-out occurred before the event object was set to the signaled state. This value can be returned when the specified set of wait conditions cannot be immediately met and <i>Timeout</i> is set to zero.</p>

<p> </p>

## -remarks
<p>The miniport driver should not attempt to wait for a mapped user event.</p>

<p>Callers of <b>VideoPortWaitForSingleObject</b> must be running at IRQL &lt;= DISPATCH_LEVEL. Usually, the caller will be running at IRQL = PASSIVE_LEVEL and in a nonarbitrary thread context. A call to this function while running at IRQL = DISPATCH_LEVEL is valid if and only if the caller specifies a <i>Timeout</i> value of zero. That is, a miniport driver must not wait for a nonzero interval at IRQL = DISPATCH_LEVEL.</p>

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
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows XP and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Video.h (include Video.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>DLL</p>
</th>
<td width="70%">
<dl>
<dt>Videoprt.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL (see Remarks section)</p>
</td>
</tr>
</table>
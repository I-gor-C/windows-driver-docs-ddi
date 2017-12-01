---
UID: NS.ks._KSPIN_DISPATCH~r1
title: KSPIN_DISPATCH
author: windows-driver-content
description: The KSPIN_DISPATCH structure describes the callbacks for which clients can register in order to receive notification of pin events.
old-location: stream\kspin_dispatch.htm
old-project: stream
ms.assetid: 6c4aea1f-e788-49c7-91c0-831c87c6fd39
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KSPIN_DISPATCH,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPIN_DISPATCH
req.alt-loc: ks.h
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

# KSPIN_DISPATCH structure



## -description
<p>The KSPIN_DISPATCH structure describes the callbacks for which clients can register in order to receive notification of pin events.</p>


## -syntax

````
typedef struct _KSPIN_DISPATCH {
  PFNKSPINIRP                Create;
  PFNKSPINIRP                Close;
  PFNKSPIN                   Process;
  PFNKSPINVOID               Reset;
  PFNKSPINSETDATAFORMAT      SetDataFormat;
  PFNKSPINSETDEVICESTATE     SetDeviceState;
  PFNKSPIN                   Connect;
  PFNKSPINVOID               Disconnect;
  const KSCLOCK_DISPATCH     *Clock;
  const KSALLOCATOR_DISPATCH *Allocator;
} KSPIN_DISPATCH, *PKSPIN_DISPATCH;
````


## -struct-fields
<dl>

### -field <b>Create</b>

<dd>
<p>A pointer to a minidriver-supplied <a href="stream.avstrminipincreate">AVStrMiniPinCreate</a> callback routine. Optional. Can be <b>NULL</b>.</p>
</dd>

### -field <b>Close</b>

<dd>
<p>A pointer to a minidriver-supplied <a href="stream.avstrminipinclose">AVStrMiniPinClose</a> callback routine. Optional. Can be <b>NULL</b>.</p>
</dd>

### -field <b>Process</b>

<dd>
<p>A pointer to a minidriver-supplied <a href="stream.avstrminipinprocess">AVStrMiniPinProcess</a> callback routine. Optional. Can be <b>NULL</b>.</p>
</dd>

### -field <b>Reset</b>

<dd>
<p>A pointer to a minidriver-supplied <a href="stream.avstrminipinreset">AVStrMiniPinReset</a> callback routine. Optional. Can be <b>NULL</b>.</p>
</dd>

### -field <b>SetDataFormat</b>

<dd>
<p>A pointer to a minidriver-supplied <a href="stream.avstrminipinsetdataformat">AVStrMiniPinSetDataFormat</a> callback routine. Optional. Can be <b>NULL</b>.</p>
</dd>

### -field <b>SetDeviceState</b>

<dd>
<p>A pointer to a minidriver-supplied <a href="stream.avstrminipinsetdevicestate">AVStrMiniPinSetDeviceState</a> callback routine. Optional. Can be <b>NULL</b>.</p>
</dd>

### -field <b>Connect</b>

<dd>
<p>A pointer to a minidriver-supplied <a href="stream.avstrminipinconnect">AVStrMiniPinConnect</a> callback routine. Optional. Can be <b>NULL</b>.</p>
</dd>

### -field <b>Disconnect</b>

<dd>
<p>A pointer to a minidriver-supplied <a href="stream.avstrminipindisconnect">AVStrMiniPinDisconnect</a> callback routine. Optional. Can be <b>NULL</b>.</p>
</dd>

### -field <b>Clock</b>

<dd>
<p>A pointer to a <a href="..\ks\ns-ks--ksclock-dispatch.md">KSCLOCK_DISPATCH</a> structure. Specify this member for a pin that exposes a clock. Optional. Can be <b>NULL</b>.</p>
</dd>

### -field <b>Allocator</b>

<dd>
<p>A pointer to a <a href="..\ks\ns-ks--ksallocator-dispatch.md">KSALLOCATOR_DISPATCH</a> structure. Specify this member for a pin that is capable of performing kernel-level allocation. Optional. Can be <b>NULL</b>.</p>
</dd>
</dl>

## -remarks
<p>Any of the callback pointers can be <b>NULL</b>, indicating that the minidriver does not require to receive notification for this particular dispatch.</p>

<p>If the minidriver needs to determine whether it has been signaled to go to a specific state (for example KSSTATE_RUN), comparing the value of the <b>DeviceState</b> member of <a href="..\ks\ns-ks--kspin.md">KSPIN</a> to <b>KSSTATE_RUN</b> is not a reliable method of doing this. <b>DeviceState</b> refers to the state to which the pin has been signaled to go, not the pipe. To perform the above reliably, instead create a variable in the <b>SetDeviceState</b> callback of this structure and then check this variable to make the determination.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and in Microsoft DirectX 8.0 and later versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\ns-ks--ksclock-dispatch.md">KSCLOCK_DISPATCH</a>
</dt>
<dt>
<a href="..\ks\ns-ks--ksallocator-dispatch.md">KSALLOCATOR_DISPATCH</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kscompletependingrequest.md">KsCompletePendingRequest</a>
</dt>
<dt>
<a href="..\ks\ns-ks--kspin.md">KSPIN</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSPIN_DISPATCH structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

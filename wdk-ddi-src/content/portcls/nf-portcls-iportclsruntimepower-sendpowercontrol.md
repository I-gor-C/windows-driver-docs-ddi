---
UID: NF.portcls.IPortClsRuntimePower.SendPowerControl
title: IPortClsRuntimePower::SendPowerControl
author: windows-driver-content
description: The port class driver (PortCls) uses the SendPowerControl method to send power control codes to the audio adapter.
old-location: audio\iportclsruntimepower_sendpowercontrol.htm
old-project: audio
ms.assetid: 04B8EE71-59F9-4DE4-AD36-846632D3EBB4
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IPortClsRuntimePower, SendPowerControl, IPortClsRuntimePower::SendPowerControl
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 7
req.target-min-winversvr: Windows Server 2003
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPortClsRuntimePower.SendPowerControl
req.alt-loc: Portcls.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL.
req.iface: IPortClsRuntimePower
---

# IPortClsRuntimePower::SendPowerControl method



## -description
<p>The port class driver (PortCls) uses the <code>SendPowerControl</code>  method to send power control codes to the audio adapter.</p>


## -syntax

````
NTSTATUS SendPowerControl(
  [in]            PDEVICE_OBJECT DeviceObject,
  [in]            LPCGUID        PowerControlCode,
  [in, optional]  PVOID          InBuffer,
  [in]            SIZE_T         InBufferSize,
  [out, optional] PVOID          OutBuffer,
  [in]            SIZE_T         OutBufferSize,
  [out, optional] PSIZE_T        BytesReturned
);
````


## -parameters
<dl>

### -param <i>DeviceObject</i> [in]

<dd>
<p>The device object.</p>
</dd>

### -param <i>PowerControlCode</i> [in]

<dd>
<p>The power control code to be sent to the audio adapter.</p>
</dd>

### -param <i>InBuffer</i> [in, optional]

<dd>
<p>The input buffer.</p>
</dd>

### -param <i>InBufferSize</i> [in]

<dd>
<p>The size of the input buffer.</p>
</dd>

### -param <i>OutBuffer</i> [out, optional]

<dd>
<p>The output buffer.</p>
</dd>

### -param <i>OutBufferSize</i> [in]

<dd>
<p>The size of the output buffer.</p>
</dd>

### -param <i>BytesReturned</i> [out, optional]

<dd>
<p>The number of bytes returned.</p>
</dd>
</dl>

## -returns
<p>The <code>SendPowerControl</code> method returns STATUS_SUCCESS, if the call is successful. Otherwise, it returns the appropriate error code.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 7</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2003</p>
</td>
</tr>
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
<dt>Portcls.h</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\portcls\nn-portcls-iportclsruntimepower.md">IPortClsRuntimePower</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortClsRuntimePower::SendPowerControl method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

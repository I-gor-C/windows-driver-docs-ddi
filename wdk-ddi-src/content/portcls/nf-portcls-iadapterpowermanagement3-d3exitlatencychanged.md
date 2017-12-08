---
UID: NF.portcls.IAdapterPowerManagement3.D3ExitLatencyChanged
title: IAdapterPowerManagement3::D3ExitLatencyChanged
author: windows-driver-content
description: PortCls calls the D3ExitLatencyChanged method while the device is in sleep (D3) power state, to provide a new exit latency value.
old-location: audio\iadapterpowermanagement3_d3exitlatencychanged.htm
old-project: audio
ms.assetid: B62920AB-39B2-4A04-AFB9-9C935A273F9A
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IAdapterPowerManagement3, D3ExitLatencyChanged, IAdapterPowerManagement3::D3ExitLatencyChanged
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: 
req.target-type: Universal
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IAdapterPowerManagement3.D3ExitLatencyChanged
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
req.irql: 
req.iface: IAdapterPowerManagement3
---

# IAdapterPowerManagement3::D3ExitLatencyChanged method



## -description
<p>PortCls calls the D3ExitLatencyChanged method while the device is in sleep (D3) power state, to provide a new exit latency value.</p>


## -syntax

````
NTSTATUS D3ExitLatencyChanged(
  [in] PC_EXIT_LATENCY NewD3ExitLatency
);
````


## -parameters
<dl>

### -param NewD3ExitLatency [in]

<dd>
<p>The  <a href="..\portcls\ne-portcls--pc-exit-latency.md">PC_EXIT_LATENCY</a> enumerated value that Portcls has determined for the device.</p>
</dd>
</dl>

## -returns
<p>This method returns an NTSTATUS value.</p>

## -remarks
<p> The D3ExitLatencyChanged method is only called when the device is the D3 power state. When Portcls wakes the device into D0, it does so via <a href="audio.iadapterpowermanagement3_powerchangestate3">PowerChangeState3</a>, and the device must be able to exit its sleep state within the latency period indicated by <i>NewD3ExitLatency</i>. Waking the audio adapter in this manner allows the driver to use the most appropriate method to adjust the power state of the audio adapter within the time-frame indicated  by the <i>NewD3ExitLatency</i> value.</p>

<p>The following table shows the possible values for <i>NewD3ExitLatency</i>.
  <table>
<tr>
<th>Exit Latency</th>
<th>Meaning</th>
</tr>
<tr>
<td>PcExitLatencyInstant </td>
<td>The driver must wake the audio adapter instantly with no latency. </td>
</tr>
<tr>
<td>PcExitLatencyFast </td>
<td>The driver must wake the audio adapter  within 10 milliseconds.</td>
</tr>
<tr>
<td>PcExitLatencyResponsive</td>
<td>The driver must wake the audio adapter  within 200 milliseconds.</td>
</tr>
</table>
<p> </p>
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
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
<a href="..\portcls\nn-portcls-iadapterpowermanagement3.md">IAdapterPowerManagement3</a>
</dt>
<dt>
<a href="..\portcls\ne-portcls--pc-exit-latency.md">PC_EXIT_LATENCY</a>
</dt>
<dt>
<a href="audio.iadapterpowermanagement3_powerchangestate3">PowerChangeState3</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IAdapterPowerManagement3::D3ExitLatencyChanged method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

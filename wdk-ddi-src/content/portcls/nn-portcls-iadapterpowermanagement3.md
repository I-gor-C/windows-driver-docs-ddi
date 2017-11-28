---
UID: NN.portcls.IAdapterPowerManagement3
title: IAdapterPowerManagement3
author: windows-driver-content
description: The IAdapterPowerManagement3 interface inherits from IUnknown, and it is used for receiving power management messages.
old-location: audio\iadapterpowermanagement3.htm
old-project: audio
ms.assetid: 5F0729DB-C991-4745-9550-9D25D6836A1F
ms.author: windowsdriverdev
ms.date: 11/21/2017
ms.keywords: PcUnregisterIoTimeout
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 8
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IAdapterPowerManagement3
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# IAdapterPowerManagement3 interface



## -description
<p>The IAdapterPowerManagement3 interface inherits from <b>IUnknown</b>, and it is used for receiving power management messages.</p>
<p>To register this interface with PortCls, the adapter driver must call  <a href="https://msdn.microsoft.com/library/windows/hardware/ff537724">PcRegisterAdapterPowerManagement</a>.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IAdapterPowerManagement3</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IAdapterPowerManagement3</b> also has these types of members:</p>

<p>The <b>IAdapterPowerManagement3</b> interface has these methods.</p>

<p>PortCls calls the D3ExitLatencyChanged method while the device is in sleep (D3) power state, to provide a new exit latency value.</p>

<p>PortCls calls the PowerChangeState3 method to request a change to the new power state. This request is passed on to the adapter driver.</p>

<p> </p>

## -members
<p>The <b>IAdapterPowerManagement3</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/jj200331">D3ExitLatencyChanged</a>
</td>
<td align="left" width="63%">
<p>PortCls calls the D3ExitLatencyChanged method while the device is in sleep (D3) power state, to provide a new exit latency value.</p>
</td>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="https://msdn.microsoft.com/library/windows/hardware/jj200332">PowerChangeState3</a>
</td>
<td align="left" width="63%">
<p>PortCls calls the PowerChangeState3 method to request a change to the new power state. This request is passed on to the adapter driver.</p>
</td>
</tr>
</table><p>PortCls calls the D3ExitLatencyChanged method while the device is in sleep (D3) power state, to provide a new exit latency value.</p>

<p>PortCls calls the PowerChangeState3 method to request a change to the new power state. This request is passed on to the adapter driver.</p>

<p> </p>

## -remarks


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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff536486">IAdapterPowerManagement2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff537724">PcRegisterAdapterPowerManagement</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IAdapterPowerManagement3 interface%20 RELEASE:%20(11/21/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

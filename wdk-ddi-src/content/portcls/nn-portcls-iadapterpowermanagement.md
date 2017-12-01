---
UID: NN.portcls.IAdapterPowerManagement
title: IAdapterPowerManagement
author: windows-driver-content
description: The IAdapterPowerManagement interface is used to manage the power state of an audio adapter.
old-location: audio\iadapterpowermanagement.htm
old-project: audio
ms.assetid: 20c898fd-a782-4d73-bf1b-a25db4440632
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: PcUnregisterIoTimeout
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: portcls.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IAdapterPowerManagement
req.alt-loc: portcls.h
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

# IAdapterPowerManagement interface



## -description
<p>The <code>IAdapterPowerManagement</code> interface is used to manage the power state of an audio adapter. This interface is implemented by the adapter driver, which exposes the interface to the PortCls system driver. <code>IAdapterPowerManagement</code> inherits from the <b>IUnknown</b> interface.</p>
<p>The operating system manages power in a WDM audio adapter primarily through the <code>IAdapterPowerManagement</code> interface that the adapter driver registers with PortCls during the device-startup phase of device initialization (see <a href="https://msdn.microsoft.com/library/windows/hardware/ff563849">Starting a Device</a>). The adapter driver registers its <code>IAdapterPowerManagement</code> interface by calling the PortCls function <a href="..\portcls\nf-portcls-pcregisteradapterpowermanagement.md">PcRegisterAdapterPowerManagement</a>. This function receives an <b>IUnknown</b> object from the adapter driver and determines whether the object supports the <code>IAdapterPowerManagement</code> interface by calling <b>QueryInterface</b> on this object with REFIID <b>IID_IAdapterPowerManagement</b>.</p>
<p>For more information, see <a href="NULL">Implementing IAdapterPowerManagement</a>.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IAdapterPowerManagement</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface but does not have additional members.</p>

## -remarks


## -requirements
<table>
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
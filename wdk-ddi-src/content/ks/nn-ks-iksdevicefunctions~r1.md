---
UID: NN.ks.IKsDeviceFunctions~r1
title: IKsDeviceFunctions
author: windows-driver-content
description: The IKsDeviceFunctions interface is a COM-style interface implemented on AVStream devices. This interface is available in Windows Server 2003 SP1 and later versions of Windows.
old-location: stream\iksdevicefunctions.htm
old-project: stream
ms.assetid: d29e7b39-5fcf-4543-9363-6f8ac6a9c7dc
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsWriteFile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: interface
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IKsDeviceFunctions
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

# IKsDeviceFunctions interface



## -description
<p>The IKsDeviceFunctions interface is a COM-style interface implemented on AVStream devices. This interface is available in Windows Server 2003 SP1 and later versions of Windows.</p>


## -inheritance
<p>The <b xmlns:loc="http://microsoft.com/wdcml/l10n">IKsDeviceFunctions</b> interface inherits from the <a href="com.iunknown" xmlns:loc="http://microsoft.com/wdcml/l10n"><b>IUnknown</b></a> interface. <b>IKsDeviceFunctions</b> also has these types of members:</p>

<p>The <b>IKsDeviceFunctions</b> interface has these methods.</p>

<p>Registers a DMA adapter object with AVStream. All drivers compiled for Win64 should use this method instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561687">KsDeviceRegisterAdapterObject</a>.</p>

<p> </p>

## -members
<p>The <b>IKsDeviceFunctions</b> interface has these methods.</p><table class="members" id="memberListMethods">
<tr>
<th align="left" width="37%">Method</th>
<th align="left" width="63%">Description</th>
</tr>
<tr data="declared;">
<td align="left" width="37%">
<a href="stream.iksdevicefunctions_registeradapterobjectex">RegisterAdapterObjectEx</a>
</td>
<td align="left" width="63%">
<p>Registers a DMA adapter object with AVStream. All drivers compiled for Win64 should use this method instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561687">KsDeviceRegisterAdapterObject</a>.</p>
</td>
</tr>
</table><p>Registers a DMA adapter object with AVStream. All drivers compiled for Win64 should use this method instead of <a href="https://msdn.microsoft.com/library/windows/hardware/ff561687">KsDeviceRegisterAdapterObject</a>.</p>

<p> </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>
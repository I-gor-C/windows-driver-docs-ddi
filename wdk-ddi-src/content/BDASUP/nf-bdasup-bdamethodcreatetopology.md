---
UID: NF.bdasup.BdaMethodCreateTopology
title: BdaMethodCreateTopology
author: windows-driver-content
description: The BdaMethodCreateTopology function creates a template topology between two pins of a filter.
old-location: stream\bdamethodcreatetopology.htm
ms.assetid: 1f0e8fdc-ae3d-4f5e-b047-b3b7bf73d389
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: bdasup.h
req.include-header: Bdasup.h
req.target-type: Desktop
req.target-min-winverclnt: Available on Microsoft Windows XP and later operating systems. This routine is available on the Windows 2000 platform only if Microsoft DirectX 9.0 and later is installed on that platform.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: BdaMethodCreateTopology
req.alt-loc: Bdasup.lib,Bdasup.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Bdasup.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: BdaMethodCreateTopology
req.iface: 
---

# BdaMethodCreateTopology function



## -description
<p>The <b>BdaMethodCreateTopology</b> function creates a template topology between two pins of a filter. </p>


## -syntax

````
NTSTATUS BdaMethodCreateTopology(
  _In_ PIRP      Irp,
  _In_ PKSMETHOD pKSMethod,
       PVOID     pvIgnored
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>Points to the IRP for the request to create topology. The BDA minidriver receives this IRP with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563413">KSMETHOD_BDA_CREATE_TOPOLOGY</a> request.</p>
</dd>

### -param <i>pKSMethod</i> [in]

<dd>
<p>Points to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563398">KSMETHOD</a> structure that describes the method and request type of a method request.</p>
</dd>

### -param <i>pvIgnored</i> [optional]

<dd>
<p>Points to a buffer that is ignored. </p>
</dd>
</dl>

## -returns
<p>Returns STATUS_SUCCESS or an appropriate error code. </p>

## -remarks
<p>A BDA minidriver calls the <b>BdaMethodCreateTopology</b> function to create the template topology between two filter pins after the minidriver receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563413">KSMETHOD_BDA_CREATE_TOPOLOGY</a> request of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563404">KSMETHODSETID_BdaDeviceConfiguration</a> method set from the network provider. Most BDA minidrivers can define dispatch and filter-automation tables so that those minidrivers dispatch the <b>BdaMethodCreateTopology</b> function directly. Some BDA minidrivers must intercept this request, using an internal method (<a href="https://msdn.microsoft.com/library/windows/hardware/ff567191">KStrMethodHandler</a>), rather than dispatch it directly. These mindrivers must obtain a pointer to the BDA filter from the passed IRP before calling <b>BdaMethodCreateTopology</b> so that they can use the filter to keep track of associated pins. These mindrivers can then send instructions to the hardware when connecting particular pin types. See <a href="NULL">Defining Automation Tables</a> and <a href="NULL">Configuring a BDA Filter</a> for more information. </p>

<p>If a BDA minidriver must create the template topology between two filter pins without relying on the network provider, the BDA minidriver should call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556448">BdaCreateTopology</a> function.</p>

<p>A BDA minidriver calls the <b>BdaMethodCreateTopology</b> function to create the template topology between two filter pins after the minidriver receives a <a href="https://msdn.microsoft.com/library/windows/hardware/ff563413">KSMETHOD_BDA_CREATE_TOPOLOGY</a> request of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff563404">KSMETHODSETID_BdaDeviceConfiguration</a> method set from the network provider. Most BDA minidrivers can define dispatch and filter-automation tables so that those minidrivers dispatch the <b>BdaMethodCreateTopology</b> function directly. Some BDA minidrivers must intercept this request, using an internal method (<a href="https://msdn.microsoft.com/library/windows/hardware/ff567191">KStrMethodHandler</a>), rather than dispatch it directly. These mindrivers must obtain a pointer to the BDA filter from the passed IRP before calling <b>BdaMethodCreateTopology</b> so that they can use the filter to keep track of associated pins. These mindrivers can then send instructions to the hardware when connecting particular pin types. See <a href="NULL">Defining Automation Tables</a> and <a href="NULL">Configuring a BDA Filter</a> for more information. </p>

<p>If a BDA minidriver must create the template topology between two filter pins without relying on the network provider, the BDA minidriver should call the <a href="https://msdn.microsoft.com/library/windows/hardware/ff556448">BdaCreateTopology</a> function.</p>

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
<p>Available on Microsoft Windows XP and later operating systems. This routine is available on the Windows 2000 platform only if Microsoft DirectX 9.0 and later is installed on that platform.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Bdasup.h (include Bdasup.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Bdasup.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff556448">BdaCreateTopology</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563398">KSMETHOD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563413">KSMETHOD_BDA_CREATE_TOPOLOGY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563404">KSMETHODSETID_BdaDeviceConfiguration</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567191">KStrMethodHandler</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20BdaMethodCreateTopology function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

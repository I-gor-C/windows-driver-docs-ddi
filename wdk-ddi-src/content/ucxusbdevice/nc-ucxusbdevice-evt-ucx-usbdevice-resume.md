---
UID: NC.ucxusbdevice.EVT_UCX_USBDEVICE_RESUME
title: EVT_UCX_USBDEVICE_RESUME
author: windows-driver-content
description: UCX invokes this callback function to resume a device from suspend state.
old-location: buses\evt_ucx_usbdevice_resume.htm
old-project: usbref
ms.assetid: 876D9754-B3AA-42C5-8BDD-60CFD4F78951
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: STREAM_INFO, STREAM_INFO, *PSTREAM_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ucxusbdevice.h
req.include-header: Ucxclass.h
req.target-type: Windows
req.target-min-winverclnt: Windows 10, version 1709
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 1.0
req.umdf-ver: 2.0
req.alt-api: *PFN_UCX_USBDEVICE_RESUME
req.alt-loc: ucxusbdevice.h
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
req.product: Windows 10 or later.
---

# EVT_UCX_USBDEVICE_RESUME callback



## -description
<p>UCX invokes this callback function to resume a device from suspend state.</p>


## -prototype

````
EVT_UCX_USBDEVICE_RESUME EvtUcxDeviceResume;

void EvtUcxDeviceResume(
  _In_ UCXCONTROLLER UcxController,
  _In_ UCXUSBDEVICE  UcxUsbDevice
)
{ ... }

typedef EVT_UCX_USBDEVICE_RESUME *PFN_UCX_USBDEVICE_RESUME;
````


## -parameters
<dl>

### -param <i>UcxController</i> [in]

<dd>
<p> A handle to the UCX controller that the client driver received in a previous call to  the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188033">UcxControllerCreate</a> method.</p>
</dd>

### -param <i>UcxUsbDevice</i> [in]

<dd>
<p>A handle to a UCX object that represents the USB device that the client driver received in a previous call to the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188052">UcxUsbDeviceCreate</a> method.</p>
</dd>
</dl>

## -returns
<p>This callback function does not return a value.</p>

## -remarks
<p>The UCX client driver registers its implementation with the USB host controller extension (UCX) by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188052">UcxUsbDeviceCreate</a> method.</p>

<p>The UCX client driver registers its implementation with the USB host controller extension (UCX) by calling the <a href="https://msdn.microsoft.com/library/windows/hardware/mt188052">UcxUsbDeviceCreate</a> method.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10, version 1709</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2016</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum KMDF version</p>
</th>
<td width="70%">
<p>1.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum UMDF version</p>
</th>
<td width="70%">
<p>2.0</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ucxusbdevice.h (include Ucxclass.h)</dt>
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
---
UID: NF.sti.IStiDevice.Initialize
title: IStiDevice::Initialize
author: windows-driver-content
description: The IStiDevice::Initialize method initializes an instance of the COM object that defines the IStiDevice interface. This method is for internal use only.
old-location: image\istidevice_initialize.htm
old-project: image
ms.assetid: 3cd6ece6-2c8e-4072-8ac5-d1e90c9392db
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IStiDevice, Initialize, IStiDevice::Initialize
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: sti.h
req.include-header: Sti.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IStiDevice.Initialize
req.alt-loc: sti.h
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
req.iface: IStiDevice
req.product: Windows 10 or later.
---

# IStiDevice::Initialize method



## -description
<p>The <b>IStiDevice::Initialize</b> method initializes an instance of the COM object that defines the <b>IStiDevice</b> interface. <i>This method is for internal use only</i>.</p>


## -syntax

````
HRESULT Initialize(
  [in] HINSTANCE hinst,
  [in] LPCWSTR   pwszDeviceName,
       DWORD     dwVersion,
       DWORD     dwMode
);
````


## -parameters
<dl>

### -param <i>hinst</i> [in]

<dd>
<p>Caller-supplied instance handle of the calling process. This handle is obtained by calling <b>GetModuleName</b>(NULL).</p>
</dd>

### -param <i>pwszDeviceName</i> [in]

<dd>
<p>Caller-supplied pointer to a string representing an internal device name, obtained by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543790">IStillImage::GetSTILaunchInformation</a>.</p>
</dd>

### -param <i>dwVersion</i> 

<dd>
<p>Caller-supplied STI version number. This value must be STI_VERSION, defined in <i>Sti.h</i>.</p>
</dd>

### -param <i>dwMode</i> 

<dd>
<p>Caller-supplied constant value indicating the <a href="NULL">Transfer Modes</a> in which the device is to be used. The following values are valid.</p>
<table>
<tr>
<th>Mode</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>STI_DEVICE_CREATE_BOTH</p>
</td>
<td>
<p>The device is being opened for both obtaining status and transferring data.</p>
</td>
</tr>
<tr>
<td>
<p>STI_DEVICE_CREATE_DATA</p>
</td>
<td>
<p>The device is being opened only for data transfers.</p>
</td>
</tr>
<tr>
<td>
<p>STI_DEVICE_CREATE_STATUS</p>
</td>
<td>
<p>The device is being opened only for obtaining status information.</p>
</td>
</tr>
</table>
<p> </p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>The <b>IStiDevice::Initialize</b> method initializes the COM object instance that was created by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543778">IStillImage::CreateDevice</a>.</p>

<p>Because <b>IStiDevice::Initialize</b> is called by <b>IStillImage::CreateDevice</b>, clients of the <b>IStiDevice</b> interface do not typically call this method directly.</p>

<p>The <b>IStiDevice::Initialize</b> method initializes the COM object instance that was created by calling <a href="https://msdn.microsoft.com/library/windows/hardware/ff543778">IStillImage::CreateDevice</a>.</p>

<p>Because <b>IStiDevice::Initialize</b> is called by <b>IStillImage::CreateDevice</b>, clients of the <b>IStiDevice</b> interface do not typically call this method directly.</p>

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
<dt>Sti.h (include Sti.h)</dt>
</dl>
</td>
</tr>
</table>
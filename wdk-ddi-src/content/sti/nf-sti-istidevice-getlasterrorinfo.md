---
UID: NF.sti.IStiDevice.GetLastErrorInfo
title: IStiDevice::GetLastErrorInfo
author: windows-driver-content
description: The IStiDevice::GetLastErrorInfo method returns information about the last known error associated with a still image device.
old-location: image\istidevice_getlasterrorinfo.htm
ms.assetid: de2f8897-c75f-4c37-aecb-f36d0f9933f9
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: image
req.header: sti.h
req.include-header: Sti.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IStiDevice.GetLastErrorInfo
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
ms.keywords: IStiDevice, GetLastErrorInfo, IStiDevice::GetLastErrorInfo
req.iface: IStiDevice
req.product: Windows 10 or later.
---

# IStiDevice::GetLastErrorInfo method



## -description
<p>The <b>IStiDevice::GetLastErrorInfo</b> method returns information about the last known error associated with a still image device.</p>


## -syntax

````
HRESULT GetLastErrorInfo(
  [out] STI_ERROR_INFO *pLastErrorInf
);
````


## -parameters
<dl>

### -param <i>pLastErrorInf</i> [out]

<dd>
<p>Caller-supplied pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff548396">STI_ERROR_INFO</a> structure to receive error information.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>The <b>IStiDevice::GetLastErrorInfo</b> method returns information about the most recent error by filling in the caller-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff548396">STI_ERROR_INFO</a> structure. The method calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff543820">IStiUSD::GetLastErrorInfo</a>, which is exported by vendor-supplied minidrivers.</p>

<p>Before calling <b>IStiDevice::GetLastErrorInfo</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543778">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.</p>

<p>The <b>IStiDevice::GetLastErrorInfo</b> method returns information about the most recent error by filling in the caller-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff548396">STI_ERROR_INFO</a> structure. The method calls <a href="https://msdn.microsoft.com/library/windows/hardware/ff543820">IStiUSD::GetLastErrorInfo</a>, which is exported by vendor-supplied minidrivers.</p>

<p>Before calling <b>IStiDevice::GetLastErrorInfo</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="https://msdn.microsoft.com/library/windows/hardware/ff543778">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.</p>

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
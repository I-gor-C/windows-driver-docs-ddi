---
UID: NF.sti.IStiDevice.GetLastErrorInfo
title: IStiDevice::GetLastErrorInfo method
author: windows-driver-content
description: The IStiDevice::GetLastErrorInfo method returns information about the last known error associated with a still image device.
old-location: image\istidevice_getlasterrorinfo.htm
old-project: Image
ms.assetid: de2f8897-c75f-4c37-aecb-f36d0f9933f9
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: IStiDevice, IStiDevice::GetLastErrorInfo, GetLastErrorInfo
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: method
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
req.product: Windows 10 or later.
---

# IStiDevice::GetLastErrorInfo method



## -description
The <b>IStiDevice::GetLastErrorInfo</b> method returns information about the last known error associated with a still image device.



## -syntax

````
HRESULT GetLastErrorInfo(
  [out] STI_ERROR_INFO *pLastErrorInf
);
````


## -parameters

### -param pLastErrorInf [out]

Caller-supplied pointer to an <a href="image.sti_error_info">STI_ERROR_INFO</a> structure to receive error information.


## -returns
If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.


## -remarks
The <b>IStiDevice::GetLastErrorInfo</b> method returns information about the most recent error by filling in the caller-supplied <a href="image.sti_error_info">STI_ERROR_INFO</a> structure. The method calls <a href="image.istiusd_getlasterrorinfo">IStiUSD::GetLastErrorInfo</a>, which is exported by vendor-supplied minidrivers.

Before calling <b>IStiDevice::GetLastErrorInfo</b>, clients of the <b>IStiDevice</b> COM interface must call <a href="image.istillimage_createdevice">IStillImage::CreateDevice</a> to obtain an <b>IStiDevice</b> interface pointer, which provides access to a specified device.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Sti.h (include Sti.h)</dt>
</dl>
</td>
</tr>
</table>
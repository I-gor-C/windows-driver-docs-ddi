---
UID: NF.stiusd.IStiDeviceControl.GetMyDevicePortName
title: IStiDeviceControl::GetMyDevicePortName
author: windows-driver-content
description: The IStiDeviceControl::GetMyDevicePortName method allows a user-mode still image minidriver to obtain a device's port name.
old-location: image\istidevicecontrol_getmydeviceportname.htm
old-project: image
ms.assetid: f400ab05-aea9-4154-a725-5b23a6dc06b6
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: IStiDeviceControl, GetMyDevicePortName, IStiDeviceControl::GetMyDevicePortName
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: stiusd.h
req.include-header: Stiusd.h
req.target-type: Desktop
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IStiDeviceControl.GetMyDevicePortName
req.alt-loc: stiusd.h
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
req.iface: IStiDeviceControl
req.product: Windows 10 or later.
---

# IStiDeviceControl::GetMyDevicePortName method



## -description
<p>The <b>IStiDeviceControl::GetMyDevicePortName</b> method allows a user-mode still image minidriver to obtain a device's port name.</p>


## -syntax

````
HRESULT GetMyDevicePortName(
   LPWSTR lpszDevicePath,
   DWORD  cwDevicePathSize
);
````


## -parameters
<dl>

### -param lpszDevicePath 

<dd>
<p>Caller-supplied pointer to a buffer to receive the device's port name.</p>
</dd>

### -param cwDevicePathSize 

<dd>
<p>Caller-supplied number of characters (of type TCHAR) in the buffer pointed to by <i>lpszDevicePath</i>.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method returns S_OK. Otherwise, it returns one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>The path name that a still image minidriver receives by calling <b>IStiDeviceControl::GetMyDevicePortName</b> can be used as an input argument to <a href="fs.createfile">CreateFile</a> (described in the Microsoft Windows SDK documentation).</p>

<p>A still image minidriver receives an <b>IStiDeviceControl</b> interface pointer as an input argument to its <a href="image.istiusd_initialize">IStiUSD::Initialize</a> method.</p>

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
<dt>Stiusd.h (include Stiusd.h)</dt>
</dl>
</td>
</tr>
</table>
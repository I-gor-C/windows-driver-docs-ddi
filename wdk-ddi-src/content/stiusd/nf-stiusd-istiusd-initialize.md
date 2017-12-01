---
UID: NF.stiusd.IStiUSD.Initialize
title: IStiUSD::Initialize
author: windows-driver-content
description: A still image minidriver's IStiUSD::Initialize method initializes an instance of the COM object that defines the IStiUSD interface.
old-location: image\istiusd_initialize.htm
old-project: image
ms.assetid: a2aa0ce6-f63b-4df4-b1c4-a23e80cdcd6c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: IStiUSD, Initialize, IStiUSD::Initialize
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
req.alt-api: IStiUSD.Initialize
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
req.iface: IStiUSD
req.product: Windows 10 or later.
---

# IStiUSD::Initialize method



## -description
<p>A still image minidriver's <b>IStiUSD::Initialize</b> method initializes an instance of the COM object that defines the <b>IStiUSD</b> interface.</p>


## -syntax

````
HRESULT Initialize(
   PSTIDEVICECONTROL pDcb,
   DWORD             dwStiVersion,
   HKEY              hParametersKey
);
````


## -parameters
<dl>

### -param <i>pDcb</i> 

<dd>
<p>Caller-supplied pointer to the <a href="NULL">IStiDeviceControl COM Interface</a>.</p>
</dd>

### -param <i>dwStiVersion</i> 

<dd>
<p>Caller-supplied STI version number. This value is defined by STI_VERSION in <i>Sti.h</i>.</p>
</dd>

### -param <i>hParametersKey</i> 

<dd>
<p>Caller-supplied handle to the registry key under which device-specific information is to be stored.</p>
</dd>
</dl>

## -returns
<p>If the operation succeeds, the method should return S_OK. Otherwise, it should return one of the STIERR-prefixed error codes defined in <i>stierr.h</i>.</p>

## -remarks
<p>The <b>IStiUSD::Initialize</b> method, which is exported by still image minidrivers, is the first <b>IStiUSD</b> method called after a minidriver has been loaded. The method must initialize the driver and device.</p>

<p>The method should store the received <a href="NULL">IStiDeviceControl COM Interface</a> pointer, and it should call that interface's <a href="image.istidevicecontrol_addref">IStiDeviceControl::AddRef</a> method.</p>

<p>For devices connected to dedicated ports (such as SCSI devices), the method typically creates a read/write path to the device by calling <a href="fs.createfile">CreateFile</a> (described in the Microsoft Windows SDK documentation), using a device port name obtained by calling <a href="image.istidevicecontrol_getmydeviceportname">IStiDeviceControl::GetMyDevicePortName</a>.</p>

<p>For devices on shared ports (such as serial port devices), opening the port in the <b>IStiUSD::Initialize</b> method is not recommended, because access to other devices on the port will be locked out. For such devices, it is better to call <a href="fs.createfile">CreateFile</a> from within the <a href="image.istiusd_lockdevice">IStiUSD::LockDevice</a> method.</p>

<p> If the device being opened is one for which multiple calls to <a href="fs.createfile">CreateFile</a> are not allowed (such as devices connected to a serial port), the driver typically does not call <b>CreateFile</b> unless the caller has opened the device for data transfers, as illustrated in the following <b>CodeExample</b>.</p>

<p>The <b>IStiUSD::Initialize</b> method should validate the received STI version number and return an error if the received version does not match the driver's version.</p>

<p>The following example opens a device port only if a call to <a href="image.istidevicecontrol_getmydeviceopenmode">IStiDeviceControl::GetMyDeviceOpenMode</a> indicates an application has opened the device for data transfers. Such code might be used for a device that cannot support multiple <a href="fs.createfile">CreateFile</a> calls, such as a serial port device.</p>

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
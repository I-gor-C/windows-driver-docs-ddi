---
UID: NF.ks.KsPersistDeviceProfile
title: KsPersistDeviceProfile
author: windows-driver-content
description: The KsPersistDeviceProfile API commits the profile information to the persistent store.
old-location: stream\kspersistdeviceprofile.htm
old-project: stream
ms.assetid: 4EC3E99B-C73C-4EAC-9EBD-BB45ABFCE8EC
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsPersistDeviceProfile
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ksmedia.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsPersistDeviceProfile
req.alt-loc: ks.lib,ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: 
req.iface: 
---

# KsPersistDeviceProfile function



## -description
<p>The <b>KsPersistDeviceProfile</b> API commits the profile information to the persistent store.</p>


## -syntax

````
 __drv_maxIRQL(PASSIVE_LEVEL) KSDDKAPI NTSTATUS NTAPI KsPersistDeviceProfile(
  _In_ PKSFILTERFACTORY FilterFactory
);
````


## -parameters
<dl>

### -param <i>FilterFactory</i> [in]

<dd>
<p>This is the <a href="..\ks\ns-ks--ksfilterfactory.md">KSFILTERFACTORY</a> that was used to initialize the profile store in <a href="..\ks\nf-ks-ksinitializedeviceprofile.md">KsInitializeDeviceProfile</a>.</p>
</dd>
</dl>

## -returns
<p>If <b>KsPersistDeviceProfile</b> is called without first initializing the profile store with <b>KsInitializeDeviceProfile</b> the call to <b>KsPersistDeviceProfile</b> will fail with <b>STATUS_INVALID_DEVICE_REQUEST</b>.
Furthermore, this API may also fail with <b>STATUS_INSUFFICIENT_RESOURCE</b> if the page pool is exhausted when profile information is being persisted.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ksmedia.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
</table>
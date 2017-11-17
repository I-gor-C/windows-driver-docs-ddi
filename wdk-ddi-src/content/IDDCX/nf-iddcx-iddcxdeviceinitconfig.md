---
UID: NF.iddcx.IddCxDeviceInitConfig
title: IddCxDeviceInitConfig
author: windows-driver-content
description: Creates a WDFDEVICE initialization structure to allow indirect displays to be used.
old-location: display\iddcxdeviceinitconfig.htm
ms.assetid: 4789e848-bb95-43e1-9768-8f94a475f9c8
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: display
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IddCxDeviceInitConfig
req.alt-loc: iddcx.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: _Must_inspect_result_
ms.keywords: IddCxDeviceInitConfig
req.iface: 
---

# IddCxDeviceInitConfig function



## -description
<p>

                Creates a WDFDEVICE initialization structure to allow indirect displays to be used.</p>


## -syntax

````
NTSTATUS IddCxDeviceInitConfig(
         PWDFDEVICE_INIT       DeviceInit,
   const IDD_CX_CLIENT_CONFIG* Config
);
````


## -parameters
<dl>

### -param <i>DeviceInit</i> 

<dd>
<p>The information about the device that is being initialized. </p>
</dd>

### -param <i>Config</i> 

<dd>
<p>The information required about the configuration of the client.</p>
</dd>
</dl>

## -returns
<p>
(NTSTATUS) The method returns STATUS_SUCCESS if the operation succeeds. Otherwise, this method may return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.
                    </p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 10</p>
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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>_Must_inspect_result_</p>
</td>
</tr>
</table>
---
UID: NF.iddcx.IddCxMonitorQueryHardwareCursor
title: IddCxMonitorQueryHardwareCursor
author: windows-driver-content
description: An OS callback function the driver calls when it wants obtain the updated cursor information. The driver normally only calls this when the event that signals cursor update has triggered.
old-location: display\iddcxmonitorqueryhardwarecursor.htm
old-project: display
ms.assetid: e954b7e7-9e4a-47ae-9b0f-8c7e051cc00e
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IddCxMonitorQueryHardwareCursor
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: Windows 10
req.target-min-winversvr: Windows Server 2016
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IddCxMonitorQueryHardwareCursor
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
req.iface: 
---

# IddCxMonitorQueryHardwareCursor function



## -description
<p>

                 An OS callback function the driver calls when it wants obtain the updated cursor information. The driver normally only calls this when the event that signals cursor update has triggered</p>


## -syntax

````
NTSTATUS IddCxMonitorQueryHardwareCursor(
  _In_        IDDCX_MONITOR             MonitorObject,
  _In_  const IDARG_IN_QUERY_HWCURSOR*  pInArgs,
  _Out_       IDARG_OUT_QUERY_HWCURSOR* pOutArgs
);
````


## -parameters
<dl>

### -param <i>MonitorObject</i> [in]

<dd>
<p>This is the OS context handle for this monitor returned by the <a href="https://msdn.microsoft.com/library/windows/hardware/mt761920">IddCxMonitorArrival</a> call</p>
</dd>

### -param <i>pInArgs</i> [in]

<dd>
<p>Input arguments of the function</p>
</dd>

### -param <i>pOutArgs</i> [out]

<dd>
<p>Output arguments of the function</p>
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
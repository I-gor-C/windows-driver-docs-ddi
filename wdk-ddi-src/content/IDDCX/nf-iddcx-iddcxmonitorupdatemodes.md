---
UID: NF.iddcx.IddCxMonitorUpdateModes
title: IddCxMonitorUpdateModes
author: windows-driver-content
description: An OS callback function the driver calls to update the mode list.
old-location: display\iddcxmonitorupdatemodes.htm
ms.assetid: 0f05931a-2327-454a-9ba7-da02cb2f13d9
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
req.alt-api: IddCxMonitorUpdateModes
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
ms.keywords: IddCxMonitorUpdateModes
req.iface: 
---

# IddCxMonitorUpdateModes function



## -description
<p>

                An OS callback function the driver calls to update the mode list</p>


## -syntax

````
NTSTATUS IddCxMonitorUpdateModes(
  _In_       IDDCX_MONITOR         MonitorObject,
  _In_ const IDARG_IN_UPDATEMODES* pInArgs
);
````


## -parameters
<dl>

### -param <i>MonitorObject</i> [in]

<dd>
<p>The monitor object being updated</p>
</dd>

### -param <i>pInArgs</i> [in]

<dd>
<p>Input arguments of function </p>
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
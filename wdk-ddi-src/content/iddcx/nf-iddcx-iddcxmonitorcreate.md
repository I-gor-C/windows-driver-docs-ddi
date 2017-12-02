---
UID: NF.iddcx.IddCxMonitorCreate
title: IddCxMonitorCreate
author: windows-driver-content
description: An OS callback function the driver calls to create a monitor object that can later be used for arrival.
old-location: display\iddcxmonitorcreate.htm
old-project: display
ms.assetid: 2e089827-dd50-43cb-9e1a-34c439780831
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IddCxMonitorCreate
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
req.alt-api: IddCxMonitorCreate
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
req.irql: 
req.iface: 
---

# IddCxMonitorCreate function



## -description
<p>An OS callback function the driver calls to create a monitor object that can later be used for arrival.

                </p>


## -syntax

````
NTSTATUS IddCxMonitorCreate(
  _In_        IDDCX_ADAPTER            AdapterObject,
  _In_  const IDARG_IN_MONITORCREATE*  pInArgs,
  _Out_       IDARG_OUT_MONITORCREATE* pOutArgs
);
````


## -parameters
<dl>

### -param AdapterObject [in]

<dd>
<p>The adapter object that is hosting the newly arrived monitor</p>
</dd>

### -param pInArgs [in]

<dd>
<p>Input arguments to the function</p>
</dd>

### -param pOutArgs [out]

<dd>
<p>Output arguments to the function</p>
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
<p></p>
</td>
</tr>
</table>
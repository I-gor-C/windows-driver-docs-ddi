---
UID: NF.iddcx.IddCxAdapterUpdateMaxDisplayPipelineRate
title: IddCxAdapterUpdateMaxDisplayPipelineRate
author: windows-driver-content
description: An OS callback function the driver calls to report that the max display pipeline rate has changed.
old-location: display\iddcxadapterupdatemaxdisplaypipelinerate.htm
old-project: display
ms.assetid: 5d8e6b87-6cfd-48ec-ac38-a75cb94cf5ac
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IddCxAdapterUpdateMaxDisplayPipelineRate
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
req.alt-api: IddCxAdapterUpdateMaxDisplayPipelineRate
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

# IddCxAdapterUpdateMaxDisplayPipelineRate function



## -description
<p>

                An OS callback function the driver calls to report that the max display pipeline rate has changed</p>


## -syntax

````
NTSTATUS IddCxAdapterUpdateMaxDisplayPipelineRate(
  _In_       IDDCX_ADAPTER                    hOsAdapterContext,
  _In_ const IDARG_IN_MAXDISPLAYPIPELINERATE* pInArgs
);
````


## -parameters
<dl>

### -param <i>hOsAdapterContext</i> [in]

<dd>
<p>This is the OS context handle for this adapter returned by the <b>IddCxStart</b> call</p>
</dd>

### -param <i>pInArgs</i> [in]

<dd>
<p>Input arguments to the function</p>
</dd>
</dl>

## -returns
<p>
(NTSTATUS) The method returns S_OK if the operation succeeds. Otherwise, this method may return an appropriate <a href="https://msdn.microsoft.com/7792201b-63bb-4db5-803d-2af02893d505">NTSTATUS</a> error code.
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
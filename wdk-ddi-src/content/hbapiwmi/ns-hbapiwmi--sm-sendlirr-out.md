---
UID: NS.hbapiwmi._SM_SendLIRR_OUT
title: SM_SendLIRR_OUT
author: windows-driver-content
description: The SM_SendLIRR_OUT structure is used to receive output parameters from the SM_SendLIRR method.
old-location: storage\sm_sendlirr_out.htm
old-project: storage
ms.assetid: 68e6ab20-b8a2-4a72-bb38-28fe4345e638
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SM_SendLIRR_OUT, SM_SendLIRR_OUT, *PSM_SendLIRR_OUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SM_SendLIRR_OUT
req.alt-loc: hbapiwmi.h
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

# SM_SendLIRR_OUT structure



## -description
<p>The SM_SendLIRR_OUT structure is used to receive output parameters from the SM_SendLIRR method.</p>


## -syntax

````
typedef struct _SM_SendLIRR_OUT {
  ULONG HBAStatus;
  ULONG TotalRespBufferSize;
  ULONG OutRespBufferSize;
  UCHAR RespBuffer[1];
} SM_SendLIRR_OUT, *PSM_SendLIRR_OUT;
````


## -struct-fields
<dl>

### -field <b>HBAStatus</b>

<dd>
<p>The status of the operation. For a list of allowed values and their descriptions, see <a href="storage.hba_status">HBA_STATUS</a>.</p>
</dd>

### -field <b>TotalRespBufferSize</b>

<dd>
<p>The size, in bytes, of the results common transport (CT) command.</p>
</dd>

### -field <b>OutRespBufferSize</b>

<dd>
<p>The size, in bytes, of the data that was actually retrieved.</p>
</dd>

### -field <b>RespBuffer</b>

<dd>
<p>The results of the common transport command.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SM_SendRNID_OUT structure in <i>Hbapiwmi.h</i> when it compiles the MS_SM_FabricAndDomainManagementMethod WMI class.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hbapiwmi.h (include Hbapiwmi.h)</dt>
</dl>
</td>
</tr>
</table>
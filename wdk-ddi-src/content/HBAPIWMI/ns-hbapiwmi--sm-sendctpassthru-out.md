---
UID: NS.hbapiwmi._SM_SendCTPassThru_OUT
title: SM_SendCTPassThru_OUT
author: windows-driver-content
description: The SM_SendCTPassThru_OUT structure is used to receive output parameters from the SM_SendCTPassThru method.
old-location: storage\sm_sendctpassthru_out.htm
ms.assetid: df1869d1-83ed-4574-85c2-89fb2b78d177
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: Storage
req.header: hbapiwmi.h
req.include-header: Hbapiwmi.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: SM_SendCTPassThru_OUT
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
ms.keywords: SM_SendCTPassThru_OUT, SM_SendCTPassThru_OUT, *PSM_SendCTPassThru_OUT
req.iface: 
---

# SM_SendCTPassThru_OUT structure



## -description
<p>The SM_SendCTPassThru_OUT structure is used to receive output parameters from the SM_SendCTPassThru method.</p>


## -syntax

````
typedef struct _SM_SendCTPassThru_OUT {
  ULONG HBAStatus;
  ULONG TotalRespBufferSize;
  ULONG OutRespBufferSize;
  UCHAR RespBuffer[1];
} SM_SendCTPassThru_OUT, *PSM_SendCTPassThru_OUT;
````


## -struct-fields
<dl>

### -field <b>HBAStatus</b>

<dd>
<p>The status of the operation. For a list of allowed values and their descriptions, see <a href="https://msdn.microsoft.com/library/windows/hardware/ff557233">HBA_STATUS</a>.</p>
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
<p>The WMI tool suite generates a declaration of the SM_SendCTPassThru_OUT structure in <i>Hbapiwmi.h</i> when it compiles the MS_SM_FabricAndDomainManagementMethod WMI class.</p>

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
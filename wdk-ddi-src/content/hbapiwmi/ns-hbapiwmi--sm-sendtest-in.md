---
UID: NS.hbapiwmi._SM_SendTEST_IN
title: SM_SendTEST_IN
author: windows-driver-content
description: The SM_SendTEST_IN structure is used to provide input parameters to the SM_SendTEST method.
old-location: storage\sm_sendtest_in.htm
old-project: storage
ms.assetid: 5bb0620e-b271-4af6-b528-b904910b8a6c
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SM_SendTEST_IN, SM_SendTEST_IN, *PSM_SendTEST_IN
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
req.alt-api: SM_SendTEST_IN
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

# SM_SendTEST_IN structure



## -description
<p>The SM_SendTEST_IN structure is used to provide input parameters to the SM_SendTEST method.</p>


## -syntax

````
typedef struct _SM_SendTEST_IN {
  UCHAR HbaPortWWN[8];
  UCHAR DestWWN[8];
  ULONG DestFCID;
  ULONG ReqBufferSize;
  UCHAR ReqBuffer[1];
} SM_SendTEST_IN, *PSM_SendTEST_IN;
````


## -struct-fields
<dl>

### -field HbaPortWWN

<dd>
<p>The local HBA port worldwide name (WWN).</p>
</dd>

### -field DestWWN

<dd>
<p>The remote HBA port worldwide name (WWN) to which the command will be sent.</p>
</dd>

### -field DestFCID

<dd>
<p>The address identifier of the remote port.</p>
</dd>

### -field ReqBufferSize

<dd>
<p>The request buffer size.</p>
</dd>

### -field ReqBuffer

<dd>
<p>The request buffer data.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SM_SendTEST_IN structure in <i>Hbapiwmi.h</i> when it compiles the MS_SM_FabricAndDomainManagementMethod WMI class.</p>

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
---
UID: NS.hbapiwmi._SM_SendRNID_IN
title: SM_SendRNID_IN
author: windows-driver-content
description: The SM_SendRNID_IN structure is used to provide input parameters to the SM_SendRNID method.
old-location: storage\sm_sendrnid_in.htm
ms.assetid: 7d94fc94-bfc6-4666-a321-71a0643f3140
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
req.alt-api: SM_SendRNID_IN
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
ms.keywords: SM_SendRNID_IN, SM_SendRNID_IN, *PSM_SendRNID_IN
req.iface: 
---

# SM_SendRNID_IN structure



## -description
<p>The SM_SendRNID_IN structure is used to provide input parameters to the SM_SendRNID method.</p>


## -syntax

````
typedef struct _SM_SendRNID_IN {
  UCHAR HbaPortWWN[8];
  UCHAR DestWWN[8];
  ULONG DestFCID;
  ULONG NodeIdDataFormat;
  ULONG InRespBufferMaxSize;
} SM_SendRNID_IN, *PSM_SendRNID_IN;
````


## -struct-fields
<dl>

### -field <b>HbaPortWWN</b>

<dd>
<p>The worldwide name (WWN) of the local port.</p>
</dd>

### -field <b>DestWWN</b>

<dd>
<p>The worldwide name (WWN) of the destination port.</p>
</dd>

### -field <b>DestFCID</b>

<dd>
<p>The address identifier of the destination port.</p>
</dd>

### -field <b>NodeIdDataFormat</b>

<dd>
<p>The node identification data format.</p>
</dd>

### -field <b>InRespBufferMaxSize</b>

<dd>
<p>The maximum response buffer size.</p>
</dd>
</dl>

## -remarks
<p>The WMI tool suite generates a declaration of the SM_SendRNID_IN structure in <i>Hbapiwmi.h</i> when it compiles the MS_SM_FabricAndDomainManagementMethod WMI class.</p>

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
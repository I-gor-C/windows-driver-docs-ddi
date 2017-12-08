---
UID: NS.dxva._DXVA_ConfigAlphaLoad
title: DXVA_ConfigAlphaLoad
author: windows-driver-content
description: The DXVA_ConfigAlphaLoad structure is sent by the host decoder to the accelerator to set the configuration for alpha-blend, texture-loading operations.
old-location: display\dxva_configalphaload.htm
old-project: display
ms.assetid: 0754c362-57b8-40e8-a050-c9dded5180c1
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXVA_ConfigAlphaLoad, DXVA_ConfigAlphaLoad, *LPDXVA_ConfigAlphaLoad
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: dxva.h
req.include-header: Dxva.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXVA_ConfigAlphaLoad
req.alt-loc: dxva.h
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

# DXVA_ConfigAlphaLoad structure



## -description
<p>The DXVA_ConfigAlphaLoad structure is sent by the host decoder to the accelerator to set the configuration for alpha-blend, texture-loading operations.</p>


## -syntax

````
typedef struct _DXVA_ConfigAlphaLoad {
  DXVA_ConfigQueryOrReplyFunc dwFunction;
  DWORD                       dwReservedBits[3];
  BYTE                        bConfigDataType;
} DXVA_ConfigAlphaLoad, *LPDXVA_ConfigAlphaLoad;
````


## -struct-fields
<dl>

### -field dwFunction

<dd>
<p>Indicates the type of query or response when using probing and locking commands. The most significant 24 bits of <b>dwFunction</b> is the <a href="https://msdn.microsoft.com/bfb1a98e-b9f0-4baa-b486-b2ff33a8bac5">DXVA_ConfigQueryOrReplyFlag</a> variable.</p>
<p>The least significant 4 bits of the <i>DXVA_ConfigQueryOrReplyFlag</i> variable contains status indicators for the query or response being performed.</p>
<p>The least significant 8 bits of <b>dwFunction</b> is the <a href="https://msdn.microsoft.com/6db9fa71-7bc2-4eb6-afcb-b16df48f7e8b">bDXVA_Func variable</a> that, in this case, is equal to 2.</p>
</dd>

### -field dwReservedBits

<dd>
<p>Reserved bits used for packing and alignment. These bits are zero.</p>
</dd>

### -field bConfigDataType

<dd>
<p>Specifies the type of alpha-blend data to be used. This member can be set to one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Description</th>
</tr>
<tr>
<td>
<p>0</p>
</td>
<td>
<p>16-entry AYUV palette with <a href="wdkgloss.i#wdkgloss.ia44#wdkgloss.ia44"><i>IA44</i></a> alpha-blending surface.</p>
</td>
</tr>
<tr>
<td>
<p>1</p>
</td>
<td>
<p>16-entry AYUV palette with <a href="wdkgloss.a#wdkgloss.ai44#wdkgloss.ai44"><i>AI44</i></a> alpha-blending surface.</p>
</td>
</tr>
<tr>
<td>
<p>2</p>
</td>
<td>
<p>16-entry AYUV palette with DPXD, Highlight, and DCCMD data.</p>
</td>
</tr>
<tr>
<td>
<p>3</p>
</td>
<td>
<p>AYUV graphic surface.</p>
</td>
</tr>
</table>
<p> </p>
<p>The preferred values for an accelerator to support for <b>bConfigDataType</b> are 1 and 3.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Dxva.h (include Dxva.h)</dt>
</dl>
</td>
</tr>
</table>
---
UID: NS.ndischimney._OFFLOAD_STATE_HEADER
title: OFFLOAD_STATE_HEADER
author: windows-driver-content
description: The OFFLOAD_STATE_HEADER structure serves as a header in an offload state structure.
old-location: netvista\offload_state_header.htm
old-project: netvista
ms.assetid: 9becc611-ede9-4285-b2d7-c53747d098a9
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: OFFLOAD_STATE_HEADER, OFFLOAD_STATE_HEADER, *POFFLOAD_STATE_HEADER
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: OFFLOAD_STATE_HEADER
req.alt-loc: ndischimney.h
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

# OFFLOAD_STATE_HEADER structure



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>The OFFLOAD_STATE_HEADER structure serves as a header in an offload state structure.</p>


## -syntax

````
typedef struct _OFFLOAD_STATE_HEADER {
  ULONG Length;
  ULONG RecognizedOptions;
} OFFLOAD_STATE_HEADER, *POFFLOAD_STATE_HEADER;
````


## -struct-fields
<dl>

### -field Length

<dd>
<p>The total size, in bytes, of the offload state structure that includes the OFFLOAD_STATE_HEADER
     member. This size includes the size of the OFFLOAD_STATE_HEADER member and the other members of the
     offload state structure.</p>
</dd>

### -field RecognizedOptions

<dd>
<p>Reserved.</p>
</dd>
</dl>

## -remarks
<p>The following offload state structures include an OFFLOAD_STATE_HEADER structure:</p>

<p>
<a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-const.md">
       NEIGHBOR_OFFLOAD_STATE_CONST</a>
</p>

<p>
<a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-cached.md">
       NEIGHBOR_OFFLOAD_STATE_CACHED</a>
</p>

<p>
<a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-delegated.md">
       NEIGHBOR_OFFLOAD_STATE_DELEGATED</a>
</p>

<p>
<a href="..\ndischimney\ns-ndischimney--path-offload-state-const.md">PATH_OFFLOAD_STATE_CONST</a>
</p>

<p>
<a href="..\ndischimney\ns-ndischimney--path-offload-state-cached.md">PATH_OFFLOAD_STATE_CACHED</a>
</p>

<p>
<a href="..\ndischimney\ns-ndischimney--path-offload-state-delegated.md">
       PATH_OFFLOAD_STATE_DELEGATED</a>
</p>

<p>
<a href="..\ndischimney\ns-ndischimney--tcp-offload-state-const.md">TCP_OFFLOAD_STATE_CONST</a>
</p>

<p>
<a href="..\ndischimney\ns-ndischimney--tcp-offload-state-cached.md">TCP_OFFLOAD_STATE_CACHED</a>
</p>

<p>
<a href="..\ndischimney\ns-ndischimney--tcp-offload-state-delegated.md">TCP_OFFLOAD_STATE_DELEGATED</a>
</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndischimney.h (include Ndischimney.h)</dt>
</dl>
</td>
</tr>
</table>
---
UID: NS.ndischimney._OFFLOAD_STATE_HEADER
title: OFFLOAD_STATE_HEADER
author: windows-driver-content
description: The OFFLOAD_STATE_HEADER structure serves as a header in an offload state structure.
old-location: netvista\offload_state_header.htm
ms.assetid: 9becc611-ede9-4285-b2d7-c53747d098a9
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
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
ms.keywords: OFFLOAD_STATE_HEADER, OFFLOAD_STATE_HEADER, *POFFLOAD_STATE_HEADER
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

### -field <b>Length</b>

<dd>
<p>The total size, in bytes, of the offload state structure that includes the OFFLOAD_STATE_HEADER
     member. This size includes the size of the OFFLOAD_STATE_HEADER member and the other members of the
     offload state structure.</p>
</dd>

### -field <b>RecognizedOptions</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>

## -remarks
<p>The following offload state structures include an OFFLOAD_STATE_HEADER structure:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/1c79a3d6-c365-4740-a2e0-94333b70d8cc">
       NEIGHBOR_OFFLOAD_STATE_CONST</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/5dedffa8-9745-4668-8646-0e896942b9c8">
       NEIGHBOR_OFFLOAD_STATE_CACHED</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/94a35d0f-3585-45d0-bba8-0b4a8ebbe883">
       NEIGHBOR_OFFLOAD_STATE_DELEGATED</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569984">PATH_OFFLOAD_STATE_CONST</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569983">PATH_OFFLOAD_STATE_CACHED</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/3a1603ec-639f-4899-8889-3c7ed2cfe375">
       PATH_OFFLOAD_STATE_DELEGATED</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570938">TCP_OFFLOAD_STATE_CONST</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570937">TCP_OFFLOAD_STATE_CACHED</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570939">TCP_OFFLOAD_STATE_DELEGATED</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/1c79a3d6-c365-4740-a2e0-94333b70d8cc">
       NEIGHBOR_OFFLOAD_STATE_CONST</a>
</p>

<p>
<a href="https://msdn.microsoft.com/5dedffa8-9745-4668-8646-0e896942b9c8">
       NEIGHBOR_OFFLOAD_STATE_CACHED</a>
</p>

<p>
<a href="https://msdn.microsoft.com/94a35d0f-3585-45d0-bba8-0b4a8ebbe883">
       NEIGHBOR_OFFLOAD_STATE_DELEGATED</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569984">PATH_OFFLOAD_STATE_CONST</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569983">PATH_OFFLOAD_STATE_CACHED</a>
</p>

<p>
<a href="https://msdn.microsoft.com/3a1603ec-639f-4899-8889-3c7ed2cfe375">
       PATH_OFFLOAD_STATE_DELEGATED</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570938">TCP_OFFLOAD_STATE_CONST</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570937">TCP_OFFLOAD_STATE_CACHED</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff570939">TCP_OFFLOAD_STATE_DELEGATED</a>
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
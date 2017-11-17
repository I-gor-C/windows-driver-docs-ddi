---
UID: NE.ks.KSPROPERTY_STREAMALLOCATOR
title: KSPROPERTY_STREAMALLOCATOR
author: windows-driver-content
description: TBD.
old-location: stream\ksproperty_streamallocator.htm
ms.assetid: 4731864F-01B3-42CB-A1D4-C82FDD1DCBBE
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSPROPERTY_STREAMALLOCATOR
req.alt-loc: Ks.h
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
ms.keywords: MIDL_IKeywordDetectorOemAdapter_0003, KEYWORDSELECTOR
req.iface: IKeywordDetectorOemAdapter
---

# KSPROPERTY_STREAMALLOCATOR enumeration



## -description
<p>TBD</p>


## -syntax

````
typedef enum  { 
  KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE,
  KSPROPERTY_STREAMALLOCATOR_STATUS
} KSPROPERTY_STREAMALLOCATOR;
````


## -enum-fields
<dl>

### -field <a id="KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE"></a><a id="ksproperty_streamallocator_functiontable"></a><b>KSPROPERTY_STREAMALLOCATOR_FUNCTIONTABLE</b>

<dd>
<p>Specify to retrieve the function table of the allocator.</p>
</dd>

### -field <a id="KSPROPERTY_STREAMALLOCATOR_STATUS"></a><a id="ksproperty_streamallocator_status"></a><b>KSPROPERTY_STREAMALLOCATOR_STATUS</b>

<dd>
<p>Specify to retrieve the current status of the specified allocator.</p>
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
<dt>Ks.h</dt>
</dl>
</td>
</tr>
</table>
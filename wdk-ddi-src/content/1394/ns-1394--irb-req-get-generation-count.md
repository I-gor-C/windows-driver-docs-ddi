---
UID: NS.1394._IRB_REQ_GET_GENERATION_COUNT
title: IRB_REQ_GET_GENERATION_COUNT
author: windows-driver-content
description: This structure contains the fields necessary for the 1394 bus driver to carry out a GetGenerationCount request.
old-location: ieee\irb_req_get_generation_count.htm
old-project: IEEE
ms.assetid: C744C48E-476A-46F8-97BE-B3484E6FEF27
ms.author: windowsdriverdev
ms.date: 10/23/2017
ms.keywords: IRB_REQ_GET_GENERATION_COUNT, IRB_REQ_GET_GENERATION_COUNT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: 1394.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IRB_REQ_GET_GENERATION_COUNT
req.alt-loc: 1394.h
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
---

# IRB_REQ_GET_GENERATION_COUNT structure



## -description
<p>This structure contains the fields necessary for the 1394 bus driver to carry out a GetGenerationCount request. </p>


## -syntax

````
typedef struct _IRB_REQ_GET_GENERATION_COUNT {
  ULONG GenerationCount;
} IRB_REQ_GET_GENERATION_COUNT;
````


## -struct-fields
<dl>

### -field <b>GenerationCount</b>

<dd>
<p>Specifies the current generation count.</p>
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
<dt>1394.h</dt>
</dl>
</td>
</tr>
</table>
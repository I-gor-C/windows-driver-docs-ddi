---
UID: NS.iddcx.IDARG_IN_COMMITMODES~r1
title: IDARG_IN_COMMITMODES
author: windows-driver-content
description: Gives information about the paths that need to be committed.
old-location: display\idarg_in_commitmodes.htm
old-project: display
ms.assetid: 242b7573-409a-4fdc-8ebf-596b8e6d41c7
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: IDARG_IN_COMMITMODES,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: iddcx.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDARG_IN_COMMITMODES
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

# IDARG_IN_COMMITMODES structure



## -description
<p>Gives information about the paths that need to be committed.
             </p>


## -syntax

````
typedef struct IDARG_IN_COMMITMODES {
  UINT                                PathCount;
  _Field_size_(PathCount) IDDCX_PATH* pPaths;
} IDARG_IN_COMMITMODES, *IDARG_IN_COMMITMODES;
````


## -struct-fields
<dl>

### -field <b>PathCount</b>

<dd>
<p>
                     [in] The number of paths in the <b>pPaths</b> array
                 </p>
</dd>

### -field <b>pPaths</b>

<dd>
<p>
                     [in] A pointer to the array of paths that need to be committed.
                 </p>
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
<dt>Iddcx.h</dt>
</dl>
</td>
</tr>
</table>
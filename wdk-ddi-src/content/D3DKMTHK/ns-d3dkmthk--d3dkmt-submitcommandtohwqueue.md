---
UID: NS.d3dkmthk._D3DKMT_SUBMITCOMMANDTOHWQUEUE
title: D3DKMT_SUBMITCOMMANDTOHWQUEUE
author: windows-driver-content
description: A structure that holds information to submit a command to the hardware queue.
old-location: display\d3dkmt_submitcommandtohwqueue.htm
ms.assetid: 3807BD27-FAE4-4E12-A825-A9FAFB7A6ACA
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dkmthk.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DKMT_SUBMITCOMMANDTOHWQUEUE
req.alt-loc: d3dkmthk.h
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
ms.keywords: D3DKMT_SUBMITCOMMANDTOHWQUEUE, D3DKMT_SUBMITCOMMANDTOHWQUEUE
req.iface: 
---

# D3DKMT_SUBMITCOMMANDTOHWQUEUE structure



## -description
<p>A structure that holds information to submit a command to the hardware queue.</p>


## -syntax

````
typedef struct _D3DKMT_SUBMITCOMMANDTOHWQUEUE {
  D3DKMT_HANDLE          hHwQueue;
  UINT64                 HwQueueProgressFenceId;
  D3DGPU_VIRTUAL_ADDRESS  CommandBuffer;
  UINT                   CommandLength;
  UINT                   PrivateDriverDataSize;
  VOID                   *pPrivateDriverData;
  UINT                   NumPrimaries;
  D3DKMT_HANDLE CONST    *WrittenPrimaries;
} D3DKMT_SUBMITCOMMANDTOHWQUEUE;
````


## -struct-fields
<dl>

### -field <b>hHwQueue</b>

<dd>
<p>Context queue to submit the command to.
</p>
</dd>

### -field <b>HwQueueProgressFenceId</b>

<dd>
<p>Hardware queue progress fence value that will be signaled once the command is finished.</p>
</dd>

### -field <b> CommandBuffer</b>

<dd>
<p>GPU VA of the command buffer to be executed on the GPU.
</p>
</dd>

### -field <b>CommandLength</b>

<dd>
<p>Length in bytes of the command buffer.

</p>
</dd>

### -field <b>PrivateDriverDataSize</b>

<dd>
<p>Size of private driver data in bytes.

</p>
</dd>

### -field <b>pPrivateDriverData</b>

<dd>
<p>Pointer to the private driver data.
</p>
</dd>

### -field <b>NumPrimaries</b>

<dd>
<p>The number of primaries written by this command buffer.
</p>
</dd>

### -field <b>WrittenPrimaries</b>

<dd>
<p>The array of primaries written by this command buffer.
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
<dt>D3dkmthk.h</dt>
</dl>
</td>
</tr>
</table>
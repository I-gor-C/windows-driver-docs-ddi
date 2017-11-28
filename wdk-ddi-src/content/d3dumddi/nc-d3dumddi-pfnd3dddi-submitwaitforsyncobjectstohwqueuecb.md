---
UID: NC.d3dumddi.PFND3DDDI_SUBMITWAITFORSYNCOBJECTSTOHWQUEUECB
title: PFND3DDDI_SUBMITWAITFORSYNCOBJECTSTOHWQUEUECB
author: windows-driver-content
description: A callback to submit a wait command to the hardware queue.
old-location: display\pfnd3dddi_submitwaitforsyncobjectstohwqueuecb.htm
old-project: display
ms.assetid: 4FD92529-0F47-46FC-9567-D8C0A5D76728
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: d3dumddi.h
req.include-header: 
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: PFND3DDDI_SUBMITWAITFORSYNCOBJECTSTOHWQUEUECB
req.alt-loc: d3dumddi.h
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

# PFND3DDDI_SUBMITWAITFORSYNCOBJECTSTOHWQUEUECB callback



## -description
<p>A callback to submit a wait command to the hardware queue.</p>


## -prototype

````
_Check_return_ HRESULT APIENTRY CALLBACK PFND3DDDI_SUBMITWAITFORSYNCOBJECTSTOHWQUEUECB(
  _In_ HANDLE                                            hDevice,
  _In_ D3DDDICB_SUBMITWAITFORSYNCOBJECTSTOHWQUEUE *const submitWaitForSyncObjectsToHwQueue
);
````


## -parameters
<dl>

### -param <i>hDevice</i> [in]

<dd>
<p>A handle to the device.</p>
</dd>

### -param <i>submitWaitForSyncObjectsToHwQueue</i> [in]

<dd>
<p>A pointer to the structure holding information on submitting a wait command to the hardware queue.</p>
</dd>
</dl>

## -returns
<dl>
<dt><b>S_OK</b></dt>
</dl><p>The call was successfully completed.</p>

<p> </p>

<p>This function might also return other HRESULT values.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h</dt>
</dl>
</td>
</tr>
</table>
---
UID: NS.d3dukmdt.DXGK_MIRACAST_CHUNK_INFO
title: DXGK_MIRACAST_CHUNK_INFO
author: windows-driver-content
description: Contains info about a specified wireless display (Miracast) encode chunk.
old-location: display\dxgk_miracast_chunk_info.htm
old-project: display
ms.assetid: 4A5413AD-A2EB-4772-89BF-867C30E0CD10
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: DXGK_MIRACAST_CHUNK_INFO, DXGK_MIRACAST_CHUNK_INFO
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dukmdt.h
req.include-header: D3dukmdt.h, D3dkmddi.h
req.target-type: Windows
req.target-min-winverclnt: Windows 8.1
req.target-min-winversvr: Windows Server 2012 R2
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: DXGK_MIRACAST_CHUNK_INFO
req.alt-loc: D3dukmdt.h
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

# DXGK_MIRACAST_CHUNK_INFO structure



## -description
<p>Contains info about a specified wireless display (Miracast) encode chunk.</p>


## -syntax

````
typedef struct {
  DXGK_MIRACAST_CHUNK_TYPE ChunkType;
  MIRACAST_CHUNK_ID        ChunkId;
  UINT                     ProcessingTime;
  UINT                     EncodeRate;
} DXGK_MIRACAST_CHUNK_INFO;
````


## -struct-fields
<dl>

### -field <b>ChunkType</b>

<dd>
<p>The type of chunk that is to be processed, specified as a <a href="https://msdn.microsoft.com/library/windows/hardware/dn322057">DXGK_MIRACAST_CHUNK_TYPE</a> enumeration value.</p>
</dd>

### -field <b>ChunkId</b>

<dd>
<p>The identifier for this chunk, of type <a href="https://msdn.microsoft.com/library/windows/hardware/dn322055">DXGK_MIRACAST_CHUNK_ID</a>.</p>
</dd>

### -field <b>ProcessingTime</b>

<dd>
<p>The time, in microseconds, that it took to process this chunk.</p>
</dd>

### -field <b>EncodeRate</b>

<dd>
<p>The encode bit rate, in kilobits per second, that the display miniport driver reported for this chunk.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>Windows 8.1</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012 R2</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dukmdt.h (include D3dukmdt.h or D3dkmddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn322055">DXGK_MIRACAST_CHUNK_ID</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn322057">DXGK_MIRACAST_CHUNK_TYPE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20DXGK_MIRACAST_CHUNK_INFO structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

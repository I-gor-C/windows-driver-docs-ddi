---
UID: NS.d3d9types._D3DDEVINFO_VCACHE
title: D3DDEVINFO_VCACHE
author: windows-driver-content
description: DirectX 8.1 and later versions only. The D3DDEVINFO_VCACHE structure describes vertex-cache information of a device.
old-location: display\d3ddevinfo_vcache.htm
ms.assetid: 3c20b757-c27c-446c-a138-066fc57ec1bc
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d9types.h
req.include-header: D3d9types.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDEVINFO_VCACHE
req.alt-loc: d3d9types.h
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
ms.keywords: D3DDEVINFO_VCACHE, D3DDEVINFO_VCACHE, *LPD3DDEVINFO_VCACHE
req.iface: 
---

# D3DDEVINFO_VCACHE structure



## -description
<p>
   DirectX 8.1 and later versions only.
   </p>
<p>The D3DDEVINFO_VCACHE structure describes vertex-cache information of a device.</p>


## -syntax

````
typedef struct _D3DDEVINFO_VCACHE {
  DWORD Pattern;
  DWORD OptMethod;
  DWORD CacheSize;
  DWORD MagicNumber;
} D3DDEVINFO_VCACHE, *LPD3DDEVINFO_VCACHE;
````


## -struct-fields
<dl>

### -field <b>Pattern</b>

<dd>
<p>Specifies the bit pattern. The driver must specify the bit pattern as the CACH four-character code (FOURCC) value. The driver can use the MAKEFOURCC macro as follows to specify the FOURCC value as CACH:</p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>MAKEFOURCC('C', 'A', 'C', 'H');</pre>
</td>
</tr>
</table></span></div>
</dd>

### -field <b>OptMethod</b>

<dd>
<p>Specifies the method of mesh optimization. The driver can use one of the following values to specify the mesh optimization that it uses: </p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DXMESHOPT_STRIPREORDER (0)</p>
</td>
<td>
<p>Longest strips optimization</p>
</td>
</tr>
<tr>
<td>
<p>D3DXMESHOPT_VCACHE (1)</p>
</td>
<td>
<p>Vertex-cache based optimization</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>CacheSize</b>

<dd>
<p>Specifies the effective size, in entries, for which the driver optimizes the vertex cache. The actual cache size is not required to be the size specified in <b>CacheSize</b> because in most cases the actual cache size turns out to be larger. The driver only specifies an optimized size in <b>CacheSize</b> if it also specifies D3DXMESHOPT_VCACHE in the <b>OptMethod</b> member.</p>
</dd>

### -field <b>MagicNumber</b>

<dd>
<p>Specifies the number that should be used as part of a trial-and-error procedure when determining when to restart the strips list. This number can be set from 1 to the value in the <b>CacheSize</b> member. Typically, the best values are near <b>CacheSize</b>/2. </p>
</dd>
</dl>

## -remarks
<p><b>DirectX 8.1 versions only.</b> The Direct3D runtime calls a driver's <a href="https://msdn.microsoft.com/6e1b0bce-1ac5-46e7-ae25-b0d3ce8580a0">D3dGetDriverState</a> function to obtain vertex-cache information from the driver. In this <b>D3dGetDriverState</b> call, the runtime specifies the D3DDEVINFOID_VCACHE flag in the <b>dwFlags</b> member of the DD_GETDRIVERSTATEDATA structure that the runtime passes. The driver specifies vertex-cache information in a D3DDEVINFO_VCACHE structure and returns it at the <b>lpdwStates</b> member of DD_GETDRIVERSTATEDATA.</p>

<p><b>DirectX 9.0 and later versions only.</b> The Direct3D runtime specifies D3DDP2OP_CREATEQUERY and D3DDP2OP_ISSUEQUERY commands in calls to the driver's <a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a> callback to create driver-side resources for the query and then to asynchronously query the driver for vertex-cache information. In the call with the D3DDP2OP_CREATEQUERY command, the runtime specifies the D3DQUERYTYPE_VCACHE query type in the <b>QueryType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545469">D3DHAL_DP2CREATEQUERY</a> structure. </p>

<p>When the driver completes a vertex-cache query, the driver sets the total size of the response buffer in the dwErrorOffset member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff545957">D3DHAL_DRAWPRIMITIVES2DATA</a> structure and sets the <b>ddrval</b> member of D3DHAL_DRAWPRIMITIVES2DATA to D3D_OK for successful completion. The driver also overwrites the incoming command buffer with the outgoing response buffer. This response buffer contains a <a href="https://msdn.microsoft.com/library/windows/hardware/ff545714">D3DHAL_DP2RESPONSEQUERY</a> structure that identifies a response for the vertex-cache query. This D3DHAL_DP2RESPONSEQUERY is followed by the vertex-cache data in the D3DDEVINFO_VCACHE structure. </p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3d9types.h (include D3d9types.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>D3DDP2OP_CREATEQUERY</dt>
<dt>D3DDP2OP_ISSUEQUERY</dt>
<dt>
<a href="https://msdn.microsoft.com/6128ff7a-0d2c-48df-8b5e-cab33c5a74f5">D3dDrawPrimitives2</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/6e1b0bce-1ac5-46e7-ae25-b0d3ce8580a0">D3dGetDriverState</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545469">D3DHAL_DP2CREATEQUERY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545714">D3DHAL_DP2RESPONSEQUERY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff545957">D3DHAL_DRAWPRIMITIVES2DATA</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDEVINFO_VCACHE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NS.d3dumddi._D3DDDIDEVINFO_VCACHE
title: D3DDDIDEVINFO_VCACHE
author: windows-driver-content
description: The D3DDDIDEVINFO_VCACHE structure describes the vertex-cache information of a device.
old-location: display\d3dddidevinfo_vcache.htm
ms.assetid: 06635207-39fd-4ef9-b388-25513f8194fe
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIDEVINFO_VCACHE
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
ms.keywords: D3DDDIDEVINFO_VCACHE, D3DDDIDEVINFO_VCACHE
req.iface: 
---

# D3DDDIDEVINFO_VCACHE structure



## -description
<p>The D3DDDIDEVINFO_VCACHE structure describes the vertex-cache information of a device.</p>


## -syntax

````
typedef struct _D3DDDIDEVINFO_VCACHE {
  UINT Pattern;
  UINT OptMethod;
  UINT CacheSize;
  UINT MagicNumber;
} D3DDDIDEVINFO_VCACHE;
````


## -struct-fields
<dl>

### -field <b>Pattern</b>

<dd>
<p>[out] The bit pattern. The driver must specify the bit pattern as a CACH four-character code (FOURCC) value. The driver can use the following MAKEFOURCC macro to specify the FOURCC value as CACH:</p>
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
<p>[out] The method of mesh optimization. The driver can use one of the following values to specify the mesh optimization that it uses.</p>
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
<p>Vertex-cache-based optimization</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>CacheSize</b>

<dd>
<p>[out] The effective size, in entries, that the driver optimizes the vertex cache for. The actual cache size is not required to be the size that is specified in <b>CacheSize</b> because the actual cache size is larger in most situations. The driver specifies an optimized size in <b>CacheSize</b> only if it also specifies D3DXMESHOPT_VCACHE in the <b>OptMethod</b> member.</p>
</dd>

### -field <b>MagicNumber</b>

<dd>
<p>[out] The number that should be used as part of a trial-and-error procedure when determining when to restart the strips list. This number can be from 1 to the value that is specified in the <b>CacheSize</b> member. Typically, the best values are near <b>CacheSize</b>/2. The driver specifies a number in <b>MagicNumber</b> only if it also specifies D3DXMESHOPT_VCACHE in the <b>OptMethod</b> member. </p>
</dd>
</dl>

## -remarks
<p><b>Direct3D runtime version 9.0 and later.</b> The Microsoft Direct3D runtime calls the driver's <a href="https://msdn.microsoft.com/ac63b77b-2704-4d5b-bf1d-9d85e8a1e336">CreateQuery</a> function to create driver-side resources for the vertex-cache query. In this <b>CreateQuery</b> call, the runtime specifies the D3DDDIQUERYTYPE_VCACHE query type in the <b>QueryType</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff542958">D3DDDIARG_CREATEQUERY</a> structure. The driver should allocate a D3DDDIDEVINFO_VCACHE structure. The runtime then calls the driver's <a href="https://msdn.microsoft.com/e31b2b6a-3721-472a-8044-6516a8419ad3">IssueQuery</a> function to process the vertex-cache query. The driver should insert a graphics processing unit (GPU) instruction to write the vertex-cache data to an allocation. To retrieve the vertex-cache information from the driver, the runtime calls the driver's <a href="https://msdn.microsoft.com/64daec14-8e16-4df3-bb0c-27760223b86c">GetQueryData</a> function. In this <b>GetQueryData</b> call, the driver should lock the allocation and return the vertex-cache data at the <b>pData</b> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff543182">D3DDDIARG_GETQUERYDATA</a> structure that is pointed to by the <i>pData</i> parameter.</p>

<p><b>Direct3D runtime version 8.1 only.</b> The Direct3D runtime calls the driver's <a href="https://msdn.microsoft.com/library/windows/hardware/hh451309">GetInfo</a> function to obtain vertex-cache information from the driver. In this <b>GetInfo</b> call, the runtime passes the D3DDDIDEVINFOID_VCACHE flag in the <i>DevInfoID</i> parameter. The driver specifies vertex-cache information in a D3DDDIDEVINFO_VCACHE structure and returns it at the <i>pDevInfoStruct</i> parameter.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Windows Vista and later versions of the Windows operating systems.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>D3dumddi.h (include D3dumddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/ac63b77b-2704-4d5b-bf1d-9d85e8a1e336">CreateQuery</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff542958">D3DDDIARG_CREATEQUERY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff543182">D3DDDIARG_GETQUERYDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451309">GetInfo</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/64daec14-8e16-4df3-bb0c-27760223b86c">GetQueryData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/e31b2b6a-3721-472a-8044-6516a8419ad3">IssueQuery</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIDEVINFO_VCACHE structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

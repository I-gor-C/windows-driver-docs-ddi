---
UID: NS.d3dumddi._D3DDDIARG_CREATEQUERY
title: D3DDDIARG_CREATEQUERY
author: windows-driver-content
description: The D3DDDIARG_CREATEQUERY structure identifies a query to create.
old-location: display\d3dddiarg_createquery.htm
old-project: display
ms.assetid: f80224c6-9046-4471-b6c6-eb14f02fc51f
ms.author: windowsdriverdev
ms.date: 11/14/2017
ms.keywords: D3DDDIARG_CREATEQUERY, D3DDDIARG_CREATEQUERY
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: d3dumddi.h
req.include-header: D3dumddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3DDDIARG_CREATEQUERY
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

# D3DDDIARG_CREATEQUERY structure



## -description
<p>The D3DDDIARG_CREATEQUERY structure identifies a query to create. </p>


## -syntax

````
typedef struct _D3DDDIARG_CREATEQUERY {
  D3DDDIQUERYTYPE QueryType;
  HANDLE          hQuery;
} D3DDDIARG_CREATEQUERY;
````


## -struct-fields
<dl>

### -field <b>QueryType</b>

<dd>
<p>[in] A D3DDDIQUERYTYPE-typed value that indicates the query type to create resources for. This member can be one of the following values.</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td>
<p>D3DDDIQUERYTYPE_VCACHE</p>
</td>
<td>
<p>Query at issue end for driver hints about data layout for vertex caching. This query is processed through a call to the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-issuequery.md">IssueQuery</a> function in which the <b>End</b> bit-field flag is set in the <b>Flags</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-issuequery.md">D3DDDIARG_ISSUEQUERY</a> structure.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDIQUERYTYPE_EVENT</p>
</td>
<td>
<p>Query at issue end for asynchronous events that have occurred.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDIQUERYTYPE_OCCLUSION</p>
</td>
<td>
<p>Query for the number of pixels that pass z-testing. These pixels are for primitives that are drawn between an issue begin and an issue end. </p>
<p>This query is processed between calls to the driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-issuequery.md">IssueQuery</a> function in which first the <b>Begin</b> bit-field flag is set in the <b>Flags</b> member of the <a href="..\d3dumddi\ns-d3dumddi--d3dddiarg-issuequery.md">D3DDDIARG_ISSUEQUERY</a> structure and next the <b>End</b> bit-field flag is set.</p>
<p>This query enables an application to check the occlusion result against 0. A value of 0 is "fully occluded," which means the pixels are not visible from the current camera position.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDIQUERYTYPE_TIMESTAMP</p>
</td>
<td>
<p>Query at issue end for the 64-bit timestamp.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDIQUERYTYPE_TIMESTAMPDISJOINT</p>
</td>
<td>
<p>This query is used to notify an application whether the counter frequency has changed from the value that is returned from the D3DQUERYTYPE_TIMESTAMP query.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDIQUERYTYPE_TIMESTAMPFREQ</p>
</td>
<td>
<p>This query result is <b>TRUE</b> if the values from D3DQUERYTYPE_TIMESTAMP queries cannot be guaranteed to be continuous throughout the duration of the D3DQUERYTYPE_TIMESTAMPDISJOINT query. Otherwise, the query result is <b>FALSE</b>.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDIQUERYTYPE_PIPELINETIMINGS</p>
</td>
<td>
<p>Query for the percent of processing time spent on pipeline data.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDIQUERYTYPE_INTERFACETIMINGS</p>
</td>
<td>
<p>Query for the percent of processing time spent on data in the driver.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDIQUERYTYPE_VERTEXTIMINGS</p>
</td>
<td>
<p>Query for the percent of processing time spent on vertex shader data.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDIQUERYTYPE_PIXELTIMINGS</p>
</td>
<td>
<p>Query for the percent of processing time spent on pixel shader data.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDIQUERYTYPE_BANDWIDTHTIMINGS</p>
</td>
<td>
<p>Query for throughput measurements for help in understanding the performance of an application.</p>
</td>
</tr>
<tr>
<td>
<p>D3DDDIQUERYTYPE_CACHEUTILIZATION</p>
</td>
<td>
<p>Query for the cache hit-rate performance for textures and indexed vertices.</p>
</td>
</tr>
<tr>
<td>
<p>
  
  
  
     D3DDDIQUERYTYPE_COUNTER_DEVICE_DEPENDENT</p>
</td>
<td>
<p>Query for device-dependent counters.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>hQuery</b>

<dd>
<p>[out] A handle to the query. The user-mode display driver's <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createquery.md">CreateQuery</a> function returns this handle to the Microsoft Direct3D runtime. </p>
</dd>
</dl>

## -remarks
<p>The Direct3D runtime uses the handle that is specified by the <b>hQuery</b> member when the runtime calls:</p>

<p>The <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-issuequery.md">IssueQuery</a> function to process a query.</p>

<p>The <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getquerydata.md">GetQueryData</a> function to retrieve information about the query.</p>

<p>The <a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroyquery.md">DestroyQuery</a> function to destroy the handle.</p>

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
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-createquery.md">CreateQuery</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-destroyquery.md">DestroyQuery</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-getquerydata.md">GetQueryData</a>
</dt>
<dt>
<a href="..\d3dumddi\nc-d3dumddi-pfnd3dddi-issuequery.md">IssueQuery</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3DDDIARG_CREATEQUERY structure%20 RELEASE:%20(11/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

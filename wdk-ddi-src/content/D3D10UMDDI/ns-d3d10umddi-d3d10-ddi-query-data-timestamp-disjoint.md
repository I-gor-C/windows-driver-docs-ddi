---
UID: NS.d3d10umddi.D3D10_DDI_QUERY_DATA_TIMESTAMP_DISJOINT
title: D3D10_DDI_QUERY_DATA_TIMESTAMP_DISJOINT
author: windows-driver-content
description: The D3D10_DDI_QUERY_DATA_TIMESTAMP_DISJOINT structure describes timestamp-disjoint information that is used in a call to the CreateQuery(D3D10) function to create a D3D10DDI_QUERY_TIMESTAMPDISJOINT query type and in a call to the QueryGetData function to return information about the query.
old-location: display\d3d10_ddi_query_data_timestamp_disjoint.htm
ms.assetid: 1dd7e73d-b804-4018-8c72-732bd68dd8d2
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: display
req.header: d3d10umddi.h
req.include-header: D3d10umddi.h
req.target-type: Windows
req.target-min-winverclnt: Available in Windows Vista and later versions of the Windows operating systems.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: D3D10_DDI_QUERY_DATA_TIMESTAMP_DISJOINT
req.alt-loc: d3d10umddi.h
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
ms.keywords: D3D10_DDI_QUERY_DATA_TIMESTAMP_DISJOINT, D3D10_DDI_QUERY_DATA_TIMESTAMP_DISJOINT
req.iface: 
---

# D3D10_DDI_QUERY_DATA_TIMESTAMP_DISJOINT structure



## -description
<p>The D3D10_DDI_QUERY_DATA_TIMESTAMP_DISJOINT structure describes timestamp-disjoint information that is used in a call to the <a href="https://msdn.microsoft.com/abe6a82f-1613-4c74-9e81-01939db74bfd">CreateQuery(D3D10)</a> function to create a D3D10DDI_QUERY_TIMESTAMPDISJOINT query type and in a call to the <a href="https://msdn.microsoft.com/78ee9813-e23e-4d46-acc4-f2fa88559b03">QueryGetData</a> function to return information about the query. </p>


## -syntax

````
typedef struct D3D10_DDI_QUERY_DATA_TIMESTAMP_DISJOINT {
  UINT64 Frequency;
  BOOL   Disjoint;
} D3D10_DDI_QUERY_DATA_TIMESTAMP_DISJOINT;
````


## -struct-fields
<dl>

### -field <b>Frequency</b>

<dd>
<p>The frequency, in Hz, of the timestamp clock. </p>
</dd>

### -field <b>Disjoint</b>

<dd>
<p>A BOOL value that indicates whether something caused the timestamp counter to become discontinuous or disjoint. This value is <b>TRUE</b> if the values from TIMESTAMP queries cannot be guaranteed to be continuous throughout the duration of the D3D10DDI_QUERY_TIMESTAMPDISJOINT query. Otherwise, this value should be <b>FALSE</b>. </p>
</dd>
</dl>

## -remarks
<p>The driver associates a D3D10_DDI_QUERY_DATA_TIMESTAMP_DISJOINT structure with the D3D10DDI_QUERY_TIMESTAMPDISJOINT query type value from the <a href="https://msdn.microsoft.com/library/windows/hardware/ff541850">D3D10DDI_QUERY</a> enumeration.</p>

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
<dt>D3d10umddi.h (include D3d10umddi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/abe6a82f-1613-4c74-9e81-01939db74bfd">CreateQuery(D3D10)</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541850">D3D10DDI_QUERY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/78ee9813-e23e-4d46-acc4-f2fa88559b03">QueryGetData</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [display\display]:%20D3D10_DDI_QUERY_DATA_TIMESTAMP_DISJOINT structure%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

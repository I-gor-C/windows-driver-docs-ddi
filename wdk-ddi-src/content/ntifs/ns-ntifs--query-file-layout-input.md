---
UID: NS.ntifs._QUERY_FILE_LAYOUT_INPUT
title: QUERY_FILE_LAYOUT_INPUT
author: windows-driver-content
description: The QUERY_FILE_LAYOUT_INPUT structure selects which file layout entries are returned from a FSCTL_QUERY_FILE_LAYOUT request.
old-location: ifsk\query_file_layout_input.htm
old-project: ifsk
ms.assetid: 7404BFC3-8942-4927-9F5B-9FA860F9F95F
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: QUERY_FILE_LAYOUT_INPUT, QUERY_FILE_LAYOUT_INPUT, *PQUERY_FILE_LAYOUT_INPUT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntifs.h
req.include-header: Ntifs.h
req.target-type: Windows
req.target-min-winverclnt: Available starting in Windows 8.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: QUERY_FILE_LAYOUT_INPUT
req.alt-loc: Ntifs.h
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

# QUERY_FILE_LAYOUT_INPUT structure



## -description
<p>The <b>QUERY_FILE_LAYOUT_INPUT</b> structure selects which file layout entries are returned from a <a href="ifsk.fsctl_query_file_layout">FSCTL_QUERY_FILE_LAYOUT</a> request.</p>


## -syntax

````
typedef struct _QUERY_FILE_LAYOUT_INPUT {
  ULONG                         NumberOfPairs;
  ULONG                         Flags;
  QUERY_FILE_LAYOUT_FILTER_TYPE FilterType;
  ULONG                         Reserved;
  union {
    CLUSTER_RANGE        ClusterRanges[1];
    FILE_REFERENCE_RANGE FileReferenceRanges[1];
  } Filter;
} QUERY_FILE_LAYOUT_INPUT, *PQUERY_FILE_LAYOUT_INPUT;
````


## -struct-fields
<dl>

### -field NumberOfPairs

<dd>
<p>The number of filter ranges present in the <b>Filter</b> array.</p>
</dd>

### -field Flags

<dd>
<p>Indicates which file layout entries are included in the query results. <b>Flags</b> is set to a valid combination of these values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="QUERY_FILE_LAYOUT_INCLUDE_EXTENTS"></a><a id="query_file_layout_include_extents"></a><dl>

### -field QUERY_FILE_LAYOUT_INCLUDE_EXTENTS

</dl>
</td>
<td width="60%">
<p>Stream extent entries are included in the query results. To use this flag, the <b>QUERY_FILE_LAYOUT_INCLUDE_STREAMS</b> flag must also be set.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="QUERY_FILE_LAYOUT_INCLUDE_EXTRA_INFO"></a><a id="query_file_layout_include_extra_info"></a><dl>

### -field QUERY_FILE_LAYOUT_INCLUDE_EXTRA_INFO

</dl>
</td>
<td width="60%">
<p>Extra file information name entries are included in the query results.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="QUERY_FILE_LAYOUT_INCLUDE_NAMES"></a><a id="query_file_layout_include_names"></a><dl>

### -field QUERY_FILE_LAYOUT_INCLUDE_NAMES

</dl>
</td>
<td width="60%">
<p>File name entries are included in the query results.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="QUERY_FILE_LAYOUT_INCLUDE_STREAMS"></a><a id="query_file_layout_include_streams"></a><dl>

### -field QUERY_FILE_LAYOUT_INCLUDE_STREAMS

</dl>
</td>
<td width="60%">
<p>File stream entries are included in the query results.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="QUERY_FILE_LAYOUT_RESTART"></a><a id="query_file_layout_restart"></a><dl>

### -field QUERY_FILE_LAYOUT_RESTART

</dl>
</td>
<td width="60%">
<p>Reset the file  layout entry iterator to the beginning of the volume.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="QUERY_FILE_LAYOUT_INCLUDE_STREAMS_WITH_NO_CLUSTERS_ALLOCATED"></a><a id="query_file_layout_include_streams_with_no_clusters_allocated"></a><dl>

### -field QUERY_FILE_LAYOUT_INCLUDE_STREAMS_WITH_NO_CLUSTERS_ALLOCATED

</dl>
</td>
<td width="60%">
<p>Include entries for resident streams and unallocated attributes. To use this flag, the <b>QUERY_FILE_LAYOUT_INCLUDE_STREAMS</b> flag must also be set.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field FilterType

<dd>
<p>Specifies a filtering method to restrict returned layout information. May be one of these values:</p>
<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
<td width="40%"><a id="QUERY_FILE_LAYOUT_FILTER_TYPE_NONE"></a><a id="query_file_layout_filter_type_none"></a><dl>

### -field QUERY_FILE_LAYOUT_FILTER_TYPE_NONE

</dl>
</td>
<td width="60%">
<p>Perform no filtering and return all information. When using this type, <i>NumberOfPairs</i> must be 0.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="QUERY_FILE_LAYOUT_FILTER_TYPE_CLUSTERS"></a><a id="query_file_layout_filter_type_clusters"></a><dl>

### -field QUERY_FILE_LAYOUT_FILTER_TYPE_CLUSTERS

</dl>
</td>
<td width="60%">
<p>Restrict filter layout information to the ranges in <b>Filter.ClusterRanges</b>.</p>
</td>
</tr>
<tr>
<td width="40%"><a id="QUERY_FILE_LAYOUT_FILTER_TYPE_FILEID"></a><a id="query_file_layout_filter_type_fileid"></a><dl>

### -field QUERY_FILE_LAYOUT_FILTER_TYPE_FILEID

</dl>
</td>
<td width="60%">
<p>Restrict filter layout information to the ranges in <b>Filter.FileReferenceRanges</b>.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field Reserved

<dd>
<p>Reserved for system use.</p>
</dd>

### -field Filter

<dd>
<p>An array of filter structures used to select specific layout information. These contain either cluster or file reference ranges. The array length is specified by the <b>NumberOfPairs</b> member. Each range must be distinct and cannot overlap with any other range.</p>
<p>This member is ignored if <b>QUERY_FILE_LAYOUT_FILTER_TYPE_NONE</b> is specified in <b>FilterType</b>.</p>
<dl>

### -field ClusterRanges

<dd>
<p>Specifies a set of cluster ranges to filter layout information. The range structure has the following format.</p>
<p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _CLUSTER_RANGE {
    LARGE_INTEGER    StartingCluster;
    LARGE_INTEGER    ClusterCount;
} CLUSTER_RANGE, *PCLUSTER_RANGE;</pre>
</td>
</tr>
</table></span></div>
</p>
</dd>

### -field FileReferenceRanges

<dd>
<p>Specifies a set of file reference ranges to filter layout information. The range structure has the following format.</p>
<p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _FILE_REFERENCE_RANGE {
    LARGE_INTEGER    StartingFileReference;
    LARGE_INTEGER    EndingReferenceNumber;
} FILE_REFERENCE_RANGE, *PFILE_REFERENCE_RANGE;</pre>
</td>
</tr>
</table></span></div>
</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The <b>QUERY_FILE_LAYOUT_RESTART</b> flag is set on the first <a href="ifsk.fsctl_query_file_layout">FSCTL_QUERY_FILE_LAYOUT</a> request. If filter ranges are included in the request, they are cached when <b>QUERY_FILE_LAYOUT_RESTART</b> is set. Further requests will return layout file entries until the end of the volume or until filter ranges are exhausted.</p>

<p>If <b>QUERY_FILE_LAYOUT_RESTART</b> is set again for the same volume, the file layout position is reset to the beginning of the volume. Additionally, the filter ranges are re-cached and their  evaluation order is reset to the first range. </p>

<p>The file layout entries are returned in the output buffer following a <a href="..\ntifs\ns-ntifs--query-file-layout-output.md">QUERY_FILE_LAYOUT_OUTPUT</a> structure.</p>

<p>When <b>FilterType</b> is <b>QUERY_FILE_LAYOUT_FILTER_TYPE_CLUSTERS</b>, the <b>ClusterRanges</b> member of the <b>Filter</b> union is used for range filtering. Otherwise, if <b>FilterType</b> is <b>QUERY_FILE_LAYOUT_FILTER_TYPE_FILEID</b>, the <b>FileReferenceRanges</b> member is used for range filtering.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available starting in Windows 8.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntifs.h (include Ntifs.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="ifsk.fsctl_query_file_layout">FSCTL_QUERY_FILE_LAYOUT</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs--query-file-layout-output.md">QUERY_FILE_LAYOUT_OUTPUT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20QUERY_FILE_LAYOUT_INPUT structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

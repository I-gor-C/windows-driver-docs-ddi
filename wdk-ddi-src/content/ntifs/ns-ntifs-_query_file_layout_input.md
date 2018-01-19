---
UID : NS:ntifs._QUERY_FILE_LAYOUT_INPUT
title : _QUERY_FILE_LAYOUT_INPUT
author : windows-driver-content
description : The QUERY_FILE_LAYOUT_INPUT structure selects which file layout entries are returned from a FSCTL_QUERY_FILE_LAYOUT request.
old-location : ifsk\query_file_layout_input.htm
old-project : ifsk
ms.assetid : 7404BFC3-8942-4927-9F5B-9FA860F9F95F
ms.author : windowsdriverdev
ms.date : 1/9/2018
ms.keywords : _QUERY_FILE_LAYOUT_INPUT, QUERY_FILE_LAYOUT_INPUT, *PQUERY_FILE_LAYOUT_INPUT
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ntifs.h
req.include-header : Ntifs.h
req.target-type : Windows
req.target-min-winverclnt : Available starting in Windows 8.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.alt-api : QUERY_FILE_LAYOUT_INPUT
req.alt-loc : Ntifs.h
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
req.typenames : QUERY_FILE_LAYOUT_INPUT, *PQUERY_FILE_LAYOUT_INPUT
---

# _QUERY_FILE_LAYOUT_INPUT structure
The <b>QUERY_FILE_LAYOUT_INPUT</b> structure selects which file layout entries are returned from a <a href="https://msdn.microsoft.com/library/windows/hardware/hh451133">FSCTL_QUERY_FILE_LAYOUT</a> request.

## Syntax
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

## Members

        
            `Filter`

            An array of filter structures used to select specific layout information. These contain either cluster or file reference ranges. The array length is specified by the <b>NumberOfPairs</b> member. Each range must be distinct and cannot overlap with any other range.

This member is ignored if <b>QUERY_FILE_LAYOUT_FILTER_TYPE_NONE</b> is specified in <b>FilterType</b>.
        
            `FilterType`

            Specifies a filtering method to restrict returned layout information. May be one of these values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `Flags`

            Indicates which file layout entries are included in the query results. <b>Flags</b> is set to a valid combination of these values:

<table>
<tr>
<th>Value</th>
<th>Meaning</th>
</tr>
<tr>
        
            `NumberOfPairs`

            The number of filter ranges present in the <b>Filter</b> array.
        
            `Reserved`

            Reserved for system use.

    ## Remarks
        The <b>QUERY_FILE_LAYOUT_RESTART</b> flag is set on the first <a href="https://msdn.microsoft.com/library/windows/hardware/hh451133">FSCTL_QUERY_FILE_LAYOUT</a> request. If filter ranges are included in the request, they are cached when <b>QUERY_FILE_LAYOUT_RESTART</b> is set. Further requests will return layout file entries until the end of the volume or until filter ranges are exhausted.

If <b>QUERY_FILE_LAYOUT_RESTART</b> is set again for the same volume, the file layout position is reset to the beginning of the volume. Additionally, the filter ranges are re-cached and their  evaluation order is reset to the first range. 

The file layout entries are returned in the output buffer following a <a href="..\ntifs\ns-ntifs-_query_file_layout_output.md">QUERY_FILE_LAYOUT_OUTPUT</a> structure.

When <b>FilterType</b> is <b>QUERY_FILE_LAYOUT_FILTER_TYPE_CLUSTERS</b>, the <b>ClusterRanges</b> member of the <b>Filter</b> union is used for range filtering. Otherwise, if <b>FilterType</b> is <b>QUERY_FILE_LAYOUT_FILTER_TYPE_FILEID</b>, the <b>FileReferenceRanges</b> member is used for range filtering.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ntifs.h (include Ntifs.h) |

    ## See Also

        <dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh451133">FSCTL_QUERY_FILE_LAYOUT</a>
</dt>
<dt>
<a href="..\ntifs\ns-ntifs-_query_file_layout_output.md">QUERY_FILE_LAYOUT_OUTPUT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [ifsk\ifsk]:%20QUERY_FILE_LAYOUT_INPUT structure%20 RELEASE:%20(1/9/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
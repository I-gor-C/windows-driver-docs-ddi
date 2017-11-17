---
UID: NS.ndis._NDIS_ENUM_FILTERS
title: NDIS_ENUM_FILTERS
author: windows-driver-content
description: The NDIS_ENUM_FILTERS structure is returned from the call to the NdisEnumerateFilterModules function to provide filter information for a filter stack.
old-location: netvista\ndis_enum_filters.htm
ms.assetid: 0f57e226-dd60-4e62-8622-bfab5c66f537
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: struct
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_ENUM_FILTERS
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
ms.keywords: NDIS_ENUM_FILTERS, NDIS_ENUM_FILTERS, *PNDIS_ENUM_FILTERS
req.iface: 
---

# NDIS_ENUM_FILTERS structure



## -description
<p>The NDIS_ENUM_FILTERS structure is returned from the call to the 
  <a href="https://msdn.microsoft.com/cab7609e-cf87-46f6-af23-891e19ef1b80">
  NdisEnumerateFilterModules</a> function to provide filter information for a filter stack.</p>


## -syntax

````
typedef struct _NDIS_ENUM_FILTERS {
  NDIS_OBJECT_HEADER    Header;
  ULONG                 Flags;
  ULONG                 NumberOfFilters;
  ULONG                 OffsetFirstFilter;
  NDIS_FILTER_INTERFACE Filter[1];
} NDIS_ENUM_FILTERS, *PNDIS_ENUM_FILTERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     filter enumeration structure. The driver sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT, the 
     <b>Revision</b> member to NDIS_ENUM_FILTERS_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_ENUM_FILTERS_REVISION_1.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>NumberOfFilters</b>

<dd>
<p>The number of filter information structures that are included in the array in the 
     <b>Filter</b> member.</p>
</dd>

### -field <b>OffsetFirstFilter</b>

<dd>
<p>The offset, in bytes, to the first member of array at the 
     <b>Filter</b> member from the beginning of the NDIS_ENUM_FILTERS structure.</p>
</dd>

### -field <b>Filter</b>

<dd>
<p>An array that contains zero or more 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff565532">NDIS_FILTER_INTERFACE</a> structures that
     the call returns.</p>
</dd>
</dl>

## -remarks
<p>The 
    <a href="https://msdn.microsoft.com/cab7609e-cf87-46f6-af23-891e19ef1b80">
    NdisEnumerateFilterModules</a> function returns an NDIS_ENUM_FILTERS structure and the 
    <b>Filter</b> member of that structure contains an array of 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff565532">NDIS_FILTER_INTERFACE</a> structures. The
    array contains one NDIS_FILTER_INTERFACE structure for each NDIS 5.1 or earlier filter intermediate
    driver or NDIS 6.0 or later NDIS filter module that is in the driver stack.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.0 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff565532">NDIS_FILTER_INTERFACE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561758">NdisEnumerateFilterModules</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_ENUM_FILTERS structure%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

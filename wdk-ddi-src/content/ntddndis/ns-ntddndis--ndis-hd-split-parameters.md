---
UID: NS.ntddndis._NDIS_HD_SPLIT_PARAMETERS
title: NDIS_HD_SPLIT_PARAMETERS
author: windows-driver-content
description: The NDIS_HD_SPLIT_PARAMETERS structure defines the current header-data split settings of a miniport adapter.
old-location: netvista\ndis_hd_split_parameters.htm
old-project: netvista
ms.assetid: 1cc76765-871e-4cd0-b927-b0b4d3d746b4
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NDIS_HD_SPLIT_PARAMETERS, NDIS_HD_SPLIT_PARAMETERS, *PNDIS_HD_SPLIT_PARAMETERS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ntddndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.1 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_HD_SPLIT_PARAMETERS
req.alt-loc: ntddndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NDIS_HD_SPLIT_PARAMETERS structure



## -description
<p>The NDIS_HD_SPLIT_PARAMETERS structure defines the current header-data split settings of a miniport
  adapter.</p>


## -syntax

````
typedef struct _NDIS_HD_SPLIT_PARAMETERS {
  NDIS_OBJECT_HEADER Header;
  ULONG              HDSplitCombineFlags;
} NDIS_HD_SPLIT_PARAMETERS, *PNDIS_HD_SPLIT_PARAMETERS;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
     provider characteristics structure (NDIS_HD_SPLIT_PARAMETERS). The driver sets the 
     <b>Type</b> member of the structure that 
     <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT, the 
     <b>Revision</b> member to NDIS_ HD_SPLIT_PARAMETERS_REVISION_1, and the 
     <b>Size</b> member to NDIS_SIZEOF_HD_SPLIT_PARAMETERS_REVISION_1.</p>
</dd>

### -field <b>HDSplitCombineFlags</b>

<dd>
<p>A set of flags that specify the current header-data split settings of a miniport adapter. A
     protocol driver or user-mode application can specify a bitwise OR of the following flags:
     </p>
<p></p>
<dl>

### -field <a id="NDIS_HD_SPLIT_COMBINE_ALL_HEADERS"></a><a id="ndis_hd_split_combine_all_headers"></a>NDIS_HD_SPLIT_COMBINE_ALL_HEADERS

<dd>
<p>The miniport adapter should combine split frames. If header-data split is enabled in the
       hardware, the miniport driver should combine the header and data before indicating the frame to
       NDIS.</p>
</dd>
</dl>
</dd>
</dl>

## -remarks
<p>The NDIS_HD_SPLIT_PARAMETERS structure is used in the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569587">OID_GEN_HD_SPLIT_PARAMETERS</a> OID set
    request to specify the current header-data split settings of a miniport adapter.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.1 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569587">OID_GEN_HD_SPLIT_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_HD_SPLIT_PARAMETERS structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

---
UID: NE.ntddstor._STORAGE_PROTOCOL_UFS_DATA_TYPE
title: STORAGE_PROTOCOL_UFS_DATA_TYPE
author: windows-driver-content
description: The UFS (Universal Flash Storage) data type. Describes the type of UFS specific data that's to be queried during an IOCTL_STORAGE_QUERY_PROPERTY request.
old-location: storage\storage_protocol_ufs_data_type.htm
ms.assetid: A4324FAD-A925-4D65-9697-9CC2878DBE0B
ms.author: windowsdriverdev
ms.date: 10/24/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: Storage
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_PROTOCOL_UFS_DATA_TYPE
req.alt-loc: Ntddstor.h
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
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
req.iface: 
---

# STORAGE_PROTOCOL_UFS_DATA_TYPE enumeration



## -description
<p>The UFS (Universal Flash Storage) data type. Describes the type of UFS specific data that's to be queried during an <a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a> request.</p>


## -syntax

````
typedef enum _STORAGE_PROTOCOL_UFS_DATA_TYPE { 
  UfsDataTypeUnknown              = 0,
      UfsDataTypeQueryDescriptor,
          UfsDataTypeMax
} STORAGE_PROTOCOL_UFS_DATA_TYPE;
````


## -enum-fields
<dl>

### -field <a id="UfsDataTypeUnknown"></a><a id="ufsdatatypeunknown"></a><a id="UFSDATATYPEUNKNOWN"></a><b>UfsDataTypeUnknown</b>

<dd>
<p>Unknown data type.</p>
</dd>

### -field <a id="____UfsDataTypeQueryDescriptor"></a><a id="____ufsdatatypequerydescriptor"></a><a id="____UFSDATATYPEQUERYDESCRIPTOR"></a><b>    UfsDataTypeQueryDescriptor</b>

<dd>
<p>Query Descriptor data type. Retrieved by command UfsSrbQueryProtocolQueryDescriptor.</p>
</dd>

### -field <a id="________UfsDataTypeMax"></a><a id="________ufsdatatypemax"></a><a id="________UFSDATATYPEMAX"></a><b>        UfsDataTypeMax</b>

<dd>
<p>Max size of data type.</p>
</dd>
</dl>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ntddstor.h (include Ntddstor.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/dn931815">STORAGE_PROTOCOL_DATA_DESCRIPTOR</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [Storage\storage]:%20STORAGE_PROTOCOL_UFS_DATA_TYPE enumeration%20 RELEASE:%20(10/24/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

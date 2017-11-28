---
UID: NE.ntddstor._STORAGE_QUERY_TYPE
title: STORAGE_QUERY_TYPE
author: windows-driver-content
description: The STORAGE_QUERY_TYPE enumeration is used in conjunction with the IOCTL_STORAGE_QUERY_PROPERTY request to retrieve the properties of a storage device or adapter.
old-location: storage\storage_query_type.htm
old-project: storage
ms.assetid: 3f346a09-071e-4512-bf77-994d277cef4d
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: SERIALPERF_STATS, SERIALPERF_STATS, *PSERIALPERF_STATS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: enum
req.header: ntddstor.h
req.include-header: Ntddstor.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: STORAGE_QUERY_TYPE
req.alt-loc: ntddstor.h
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

# STORAGE_QUERY_TYPE enumeration



## -description
<p>The STORAGE_QUERY_TYPE enumeration is used in conjunction with the <a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a> request to retrieve the properties of a storage device or adapter.</p>


## -syntax

````
typedef enum _STORAGE_QUERY_TYPE { 
  PropertyStandardQuery    = 0,
  PropertyExistsQuery,
  PropertyMaskQuery,
  PropertyQueryMaxDefined
} STORAGE_QUERY_TYPE, *PSTORAGE_QUERY_TYPE;
````


## -enum-fields
<dl>

### -field <a id="PropertyStandardQuery"></a><a id="propertystandardquery"></a><a id="PROPERTYSTANDARDQUERY"></a><b>PropertyStandardQuery</b>

<dd>
<p>Instructs the port driver to report a device descriptor, an adapter descriptor or a unique hardware device ID (DUID).</p>
</dd>

### -field <a id="PropertyExistsQuery"></a><a id="propertyexistsquery"></a><a id="PROPERTYEXISTSQUERY"></a><b>PropertyExistsQuery</b>

<dd>
<p>Instructs the port driver to report whether the descriptor is supported.</p>
</dd>

### -field <a id="PropertyMaskQuery"></a><a id="propertymaskquery"></a><a id="PROPERTYMASKQUERY"></a><b>PropertyMaskQuery</b>

<dd>
<p>Not currently supported. Do not use.</p>
</dd>

### -field <a id="PropertyQueryMaxDefined"></a><a id="propertyquerymaxdefined"></a><a id="PROPERTYQUERYMAXDEFINED"></a><b>PropertyQueryMaxDefined</b>

<dd>
<p>Specifies the upper limit of the list of query types. This is used to validate the query type.</p>
</dd>
</dl>

## -remarks
<p>Caller specifies the type of query by choosing one of the enumeration values.</p>

<p>Caller defines the exact nature of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a> request by specifying the query type together with the property ID. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff566997">STORAGE_PROPERTY_QUERY</a> for an explanation of how these two values are combined to define the query. </p>

<p>Caller specifies the type of query by choosing one of the enumeration values.</p>

<p>Caller defines the exact nature of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a> request by specifying the query type together with the property ID. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff566997">STORAGE_PROPERTY_QUERY</a> for an explanation of how these two values are combined to define the query. </p>

<p>Caller specifies the type of query by choosing one of the enumeration values.</p>

<p>Caller defines the exact nature of an <a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a> request by specifying the query type together with the property ID. See <a href="https://msdn.microsoft.com/library/windows/hardware/ff566997">STORAGE_PROPERTY_QUERY</a> for an explanation of how these two values are combined to define the query. </p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560590">IOCTL_STORAGE_QUERY_PROPERTY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566997">STORAGE_PROPERTY_QUERY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566996">STORAGE_PROPERTY_ID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20STORAGE_QUERY_TYPE enumeration%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>

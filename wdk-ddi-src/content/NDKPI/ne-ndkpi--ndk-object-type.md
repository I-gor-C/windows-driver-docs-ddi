---
UID: NE.ndkpi._NDK_OBJECT_TYPE
title: NDK_OBJECT_TYPE
author: windows-driver-content
description: The NDK_OBJECT_TYPE enumeration defines types of Network Direct Kernel (NDK) objects.
old-location: netvista\ndk_object_type.htm
ms.assetid: 8CB39DF6-00DA-4480-A44E-62CAF1DB35CE
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: enum
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndkpi.h
req.include-header: Ndkpi.h
req.target-type: Windows
req.target-min-winverclnt: None supported,Supported in NDIS 6.30 and later.
req.target-min-winversvr: Windows Server 2012
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDK_OBJECT_TYPE
req.alt-loc: ndkpi.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: <=DISPATCH_LEVEL
ms.keywords: NDIS_WWAN_VISIBLE_PROVIDERS, NDIS_WWAN_VISIBLE_PROVIDERS, *PNDIS_WWAN_VISIBLE_PROVIDERS
req.iface: 
---

# NDK_OBJECT_TYPE enumeration



## -description
<p>The <b>NDK_OBJECT_TYPE</b> enumeration defines  types of Network Direct Kernel (NDK) objects.</p>


## -syntax

````
typedef enum _NDK_OBJECT_TYPE { 
  NdkObjectTypeUndefined       = 0,
  NdkObjectTypeAdapter         = 1,
  NdkObjectTypeQp              = 2,
  NdkObjectTypeCq              = 3,
  NdkObjectTypeMr              = 4,
  NdkObjectTypeMw              = 5,
  NdkObjectTypePd              = 6,
  NdkObjectTypeSharedEndpoint  = 7,
  NdkObjectTypeConnector       = 8,
  NdkObjectTypeListener        = 9,
  NdkObjectTypeSrq             = 10,
  NdkObjectTypeMax             = 11
} NDK_OBJECT_TYPE;
````


## -enum-fields
<dl>

### -field <a id="NdkObjectTypeUndefined"></a><a id="ndkobjecttypeundefined"></a><a id="NDKOBJECTTYPEUNDEFINED"></a><b>NdkObjectTypeUndefined</b>

<dd>
<p>Specifies  an undefined NDK  object.</p>
</dd>

### -field <a id="NdkObjectTypeAdapter"></a><a id="ndkobjecttypeadapter"></a><a id="NDKOBJECTTYPEADAPTER"></a><b>NdkObjectTypeAdapter</b>

<dd>
<p>Specifies an NDK adapter object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439848">NDK_ADAPTER</a>).</p>
</dd>

### -field <a id="NdkObjectTypeQp"></a><a id="ndkobjecttypeqp"></a><a id="NDKOBJECTTYPEQP"></a><b>NdkObjectTypeQp</b>

<dd>
<p>Specifies an NDK queue pair (QP) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439933">NDK_QP</a>).</p>
</dd>

### -field <a id="NdkObjectTypeCq"></a><a id="ndkobjecttypecq"></a><a id="NDKOBJECTTYPECQ"></a><b>NdkObjectTypeCq</b>

<dd>
<p>Specifies an NDK completion queue (CQ) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439854">NDK_CQ</a>).</p>
</dd>

### -field <a id="NdkObjectTypeMr"></a><a id="ndkobjecttypemr"></a><a id="NDKOBJECTTYPEMR"></a><b>NdkObjectTypeMr</b>

<dd>
<p>Specifies an NDK memory region (MR) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439922">NDK_MR</a>).</p>
</dd>

### -field <a id="NdkObjectTypeMw"></a><a id="ndkobjecttypemw"></a><a id="NDKOBJECTTYPEMW"></a><b>NdkObjectTypeMw</b>

<dd>
<p>Specifies an NDK memory window (MW) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439926">NDK_MW</a>).</p>
</dd>

### -field <a id="NdkObjectTypePd"></a><a id="ndkobjecttypepd"></a><a id="NDKOBJECTTYPEPD"></a><b>NdkObjectTypePd</b>

<dd>
<p>Specifies an NDK protection domain (PD) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439931">NDK_PD</a>).</p>
</dd>

### -field <a id="NdkObjectTypeSharedEndpoint"></a><a id="ndkobjecttypesharedendpoint"></a><a id="NDKOBJECTTYPESHAREDENDPOINT"></a><b>NdkObjectTypeSharedEndpoint</b>

<dd>
<p>Specifies an NDK shared endpoint object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439937">NDK_SHARED_ENDPOINT</a>).</p>
</dd>

### -field <a id="NdkObjectTypeConnector"></a><a id="ndkobjecttypeconnector"></a><a id="NDKOBJECTTYPECONNECTOR"></a><b>NdkObjectTypeConnector</b>

<dd>
<p>Specifies an NDK connector object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439852">NDK_CONNECTOR</a>).</p>
</dd>

### -field <a id="NdkObjectTypeListener"></a><a id="ndkobjecttypelistener"></a><a id="NDKOBJECTTYPELISTENER"></a><b>NdkObjectTypeListener</b>

<dd>
<p>Specifies an NDK listener object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439918">NDK_LISTENER</a>).</p>
</dd>

### -field <a id="NdkObjectTypeSrq"></a><a id="ndkobjecttypesrq"></a><a id="NDKOBJECTTYPESRQ"></a><b>NdkObjectTypeSrq</b>

<dd>
<p>Specifies an NDK shared receive queue (SRQ) object (<a href="https://msdn.microsoft.com/library/windows/hardware/hh439939">NDK_SRQ</a>).</p>
</dd>

### -field <a id="NdkObjectTypeMax"></a><a id="ndkobjecttypemax"></a><a id="NDKOBJECTTYPEMAX"></a><b>NdkObjectTypeMax</b>

<dd>
<p>The maximum value for this enumeration. This value might change in future versions of the header files and binaries. 

</p>
</dd>
</dl>

## -remarks
<p>NDK objects include an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439928">NDK_OBJECT_HEADER</a> structure that packages the object type,  version, and other information.</p>

<p>NDK objects include an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439928">NDK_OBJECT_HEADER</a> structure that packages the object type,  version, and other information.</p>

<p>NDK objects include an <a href="https://msdn.microsoft.com/library/windows/hardware/hh439928">NDK_OBJECT_HEADER</a> structure that packages the object type,  version, and other information.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Minimum supported client</p>
</th>
<td width="70%">
<p>None supported</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Minimum supported server</p>
</th>
<td width="70%">
<p>Windows Server 2012</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.30 and later.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndkpi.h (include Ndkpi.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439848">NDK_ADAPTER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439852">NDK_CONNECTOR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439854">NDK_CQ</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439918">NDK_LISTENER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439922">NDK_MR</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439926">NDK_MW</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439928">NDK_OBJECT_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439931">NDK_PD</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439933">NDK_QP</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439937">NDK_SHARED_ENDPOINT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh439939">NDK_SRQ</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDK_OBJECT_TYPE enumeration%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
